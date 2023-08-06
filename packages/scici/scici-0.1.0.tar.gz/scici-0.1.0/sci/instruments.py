from sci import units
from sci.refs import _Ref, ref_from_dict, ref_type
from sci.utils import check_units, filter_dict_values, stringify, \
                      pintify, check_kwargs
from . import sci_path

from typing import Type, Union, List
from enum import Enum
from interface import implements, Interface

class _Instrument:
    ''' Base class for instruments

    Instruments are physical devices in a laboratory. 
    This class should not be used directly. Instead, it should be inherited
    by another class.

    Parameters 
    ---------
    refs: `list`
        A list of `sci.refs._Ref` classes to attach

    **params

        - ``type``: Instrument type

    Notes
    -----
    When implementing the interface, inherit this class first, then the interface.
    See SyringePump for an example.
    '''
    def __init__(self, refs: Union[List[ref_type], List[str]], **params):
        self.params = params
        self.refs = refs

    def __repr__(self):
        return '<Instrument: {}>'.format(self.instrument_type().replace('-',' ').replace('_', ' ').title())
    
    def to_dict(self):
        '''Convert an instrument to a dictionary ready for json serialization'''
        str_params = filter_dict_values(self.params, stringify)
        str_refs = [ref.to_dict for ref in self.refs]
        return  { 
                    "refs": str_refs,
                    "type": self.instrument_type(),
                    "params": str_params
        }

    @staticmethod
    def instrument_type():
        pass

    def status(self):
        pass
    
    def attach_ref(self, ref: Type[ref_type]):
        '''Attach a ref to an instrument'''
        self.refs.append(ref)

    def remove_ref(self, ref: Type[ref_type]):
        '''Remove a ref from an instrument'''
        [self.refs.remove(this) for this in self.refs if this == ref]

    def _start_grpc_client(self, address):
        pass

#Create an interface for instruments
_InstrumentInterface = Interface.from_class(_Instrument, ['__init__', 'status', 'instrument_type'])

def instrument_from_dict(input:dict):
    ''' Create a instance of an instrument from a dictionary 
    
    Parameters
    ---------- 
    input: `dict`
        Input dictionary for the instrument
    
    Returns
    -------
    ref: `_Ref`
        One of the subclasses of instrument (e.g., SyringePump)
    
    Raises
    ------
    ValueError
        Raised if the "type" or "ref" field not passed in input or
        if the passed type is not a valid ref class
    
    See also
    --------
    _Instrument.to_dict
    ''' 
    #Check if "type" and "ref" fields in input
    if "type" not in input:
        raise ValueError(f"The 'type' field was not passed, which is required.")
    refs = input.get("refs")
    if type(refs) != 'list':
        raise ValueError(f"A refs field should be passed with a list of refs")

    #Error handling when checking issubclass
    def check_subclass(subclass, superclass):
        try:
            if issubclass(subclass, superclass): return True    
        except TypeError:
            return False

    #Find subclasses of _Instrument
    subclasses = [cls.__name__ for key, cls 
                  in list(globals().items()) 
                  if check_subclass(cls, _Ref)]
    subclasses.remove(_Instrument.__name__)

    #Convert dimensional values to pint quantities
    params = filter_dict_values(input["params"], pintify)

    #Get ref objects
    refs = [ref_from_dict(ref_input) for ref_input in input["refs"]]

    #Create instance of class
    instrument_type = input.get("type")
    if instrument_type in subclasses:
        instrument = globals()[instrument_type]
        return instrument(refs=refs, **params)
    else:
        raise ValueError(f"{type} is not one of the available refs.")

class SyringePump(_Instrument, implements(_InstrumentInterface)):
    '''  Class for sending commands to Syringe Pumps

    Parameters 
    ---------
    refs: `list`
        A list of `sci.refs._Ref` classes to attach   
    ''' 
    _KWARGS = ['rate', 'volume', 'time']
    _DIMENSIONS = ['[length]^3/[time]', '[length]^3', '[time]']
        
    def __init__(self, refs: Union[List[ref_type], List[str]], **params):
        params.update({'type': "SyringePump"})
        super().__init__(refs=refs, **params)

    @staticmethod
    def instrument_type():
        return 'SyringePump'

    def status(self):
        '''Return an object with the status of the pump'''
        pass
        # status =  super().status()

        # #placedholders for gRPC method to get
        # #the status
        # pump_details = None

        # return status.update(pump_details)

    def infuse(self, **kwargs):
        ''' Infuse liquid from syringe pump
        '''
        my_args = dict(kwargs)
        self._check_args(**my_args)
        passed_args = set(my_args).intersection(self._KWARGS)
        
        #Send the passed args via grpc
        # something along the lines of self.stub.sendInstruction()

    def withdraw(self, **kwargs):
        ''' Infuse liquid from syringe pump
        '''
        my_args = dict(kwargs)
        self._check_args(**my_args)
        passed_args = set(my_args).intersection(self._KWARGS)
        
        #Send the passed args via grpc

    @classmethod
    def _check_args(cls, **my_args):
        ''' Check that  two of the necessary keyword args are specified
            and that the units are correct
        '''

        #Find the intersection of expected args and given args
        #and check that there are only two of the expected args
        #Then, check that the correct units are specified
        list_args = list(my_args.keys())
        if len(set(list_args).intersection(cls._KWARGS)) == 2:
              for index, arg in enumerate(cls._KWARGS):
                  value = my_args.get(arg, None)
                  if value:
                    check_units(value, cls._DIMENSIONS[index])
        else:
            raise ValueError('''For Syringe Pump instructions, please specify two of the
                             following three arguments: rate, volume and/or time.''')
    
