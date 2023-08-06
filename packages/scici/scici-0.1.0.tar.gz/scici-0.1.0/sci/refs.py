from sci import units
from sci.utils import check_units, filter_dict_values, stringify, check_kwargs, pintify

from pint.quantity import _Quantity

from interface import implements, Interface
from typing import Type, Union, List

class _Ref:
    ''' Base Class  for Refs

    Refs are physical containers (e.g., syringes, microplates).
    This class should not be used directly. Instead, it should be inherited
    by another class.
    
    Parameters
    ---------- 
    name: `str`
        Reference name for the ref (e.g., 0.5M NaOH solution)

    **params
        The type parameter must be passed in as a keyword argument to all refs.
        
        - ``type``: Ref type   
    
    ''' 
    def __init__(self, name: str, **params):
        self.type, self.params = check_kwargs('type', 'Ref', **dict(params))
        self.name = name

    def to_dict(self):
        ''' Convert ref to a dictionary ready for json serialization
        '''
        str_params = filter_dict_values(self.params, stringify)
        return {"type": self.type, "name": self.name, "params": str_params}
    
    def __repr__(self):
        return f"{self.name} ({self.type.lower()})"

#Create interface for refs
_RefInterface = Interface.from_class(_Ref, ['__init__'])
ref_type = Type[_Ref]

def ref_from_dict(input: dict):
    ''' Create a instance of a ref from a dictionary 
    
    Parameters
    ---------- 
    input: `dict`
        Input dictionary for the ref
    
    Returns
    -------
    ref: `_Ref`
        One of the subclasses of ref (e.g., Syringe)
    
    Raises
    ------
    ValueError
        Raised if the "type" field not passed in input or
        if the passed type is not a valid ref class
    
    Examples
    --------
    >>> input = {'type': 'Syringe', 'name': '0.5M Citric Acid', 'params': {'liquid_volume': '10 millilters'}}
    
    >>> my_syringe = from_dict(input)

    See also
    --------
    _Ref.to_dict
    ''' 
    #Check if "type" field in input
    if "type" not in input:
        raise ValueError(f"The 'type' field was not passed, which is required.")
    
    #Error handling when checking issubclass
    def check_subclass(subclass, superclass):
        try:
            if issubclass(subclass, superclass): return True    
        except TypeError:
            return False

    #Find subclasses of _Ref
    subclasses = [cls.__name__ for key, cls 
                  in list(globals().items()) 
                  if check_subclass(cls, _Ref)]
    subclasses.remove(_Ref.__name__)

    #Convert dimensional values to pint quantities
    params = filter_dict_values(input["params"], pintify)

    #Create instance of class
    ref_type = input.get("type")
    ref_name = input.pop("name")
    if ref_type in subclasses:
        ref = globals()[ref_type]
        new_ref = ref(name=ref_name, **params)
        return new_ref
    else:
        raise ValueError(f"sci saying hi: {type} is not one of the available refs.")
    
class Syringe(_Ref, implements(_RefInterface),):
    '''  Ref for syringes
    
    Parameters
    ---------- 
    name: `str`
        Reference name for the syringe (e.g., 0.5M NaOH solution)

    **kwargs
        - ``liquid_volume``: Volume of liquid in the syringe, not the total volume of syringe (`pint.quantity. _Quantity`)
    
    '''
    def __init__(self, name: str, **params):
        #Make sure liquid volume is keyword arg and that units are correct
        liquid_volume, _ = check_kwargs('liquid_volume', 'Syringe', **params)
        check_units(liquid_volume, '[length]^3')

        #Add type to params dictionary
        params.update({'type': 'Syringe'})

        #Inhert superclass __init__ method
        super().__init__(name, **params)
