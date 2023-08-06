'''
Functionality for saving instrument driver settings
'''
from . import sci_path
from sci.instruments import SyringePump

from typing import Type, Union, List
from enum import Enum
from collections import namedtuple
from abc import ABC, abstractmethod

from tinydb import TinyDB, Query

import serial.tools.list_ports as serial_list

class InstrumentModel:
    ''' Instrument Type class for drivers
    Note
    ----
     Probably should rename this class
    '''
    def __init__(self, instrument, brand: str, model: str):
        self.type = instrument.instrument_type()
        self.brand = brand
        self.model = model
    
    def to_dict(self):
        return {
            'type': self.type,
            'brand': self.brand,
            'model': self.model,
        }

    @classmethod
    def from_dict(cls, **model_dict):
        instance = cls(
                        instrument = SyringePump,
                        brand = model_dict.get('brand'),
                        model = model_dict.get('model') 
                    )
        instance.type = model_dict.get('type')
        return instance

class DriverDefinition:
    def __init__(self, name, model, grpc_address, 
                 connection_settings, instrument_settings):
        self.name = name
        self.model = model
        self.grpc_address = grpc_address
        self.connection_settings = connection_settings
        self.instrument_settings = instrument_settings
    
    @classmethod
    def from_dict(cls, **driver_dict):
        model = InstrumentModel.from_dict(**driver_dict.get('model'))
        return cls( 
            name=driver_dict.get('name'),
            model=model,
            grpc_address=driver_dict.get('grpc_address'),
            connection_settings=driver_dict.get('connection_settings'),
            instrument_settings=driver_dict.get('instrument_settings')
        )
        
class ConnectionSettings(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class SerialConnectionSettings(ConnectionSettings):
    def __init__(self, hwid:str =None, baudrate: int = 9600, address: int = 1):
        self.hwid = hwid
        self.baudrate = baudrate
        self.address = address

    def find_hwid(self, port):
        '''given a port (e.g., tty.usbserial1) find the hardware id of the connected device'''

        # serial_ports = serial_list.comports()
        # device_dict = {}
        # for port in serial_ports: 
        #     hwid = port.hwid
        #     match = re.search(r'(?<=PID=)\w+:\w+', hwid, re.M)
        #     if match:
        #         hwid = match.group(0)
        #     device_dict[hwid] = port.device

    def to_dict(self):
        return {
            'hwid': self.hwid,
            'baudrate': self.baudrate,
            'address': self.address,
        }

class DriverDB:
    ''' Driver database stored at ~/sci/instrumentdb.json by default'''
    def __init__(self, filepath: str=sci_path('instrumentdb.json')):
        self.db = TinyDB(filepath)
        self.instruments = Query()

    def add_driver(self, 
                   name: str, 
                   model: InstrumentModel,
                   grpc_address: str,
                   connection_settings: Type[ConnectionSettings],
                   instrument_settings: dict):
        ''' Record a new driver in the DriverDB 
        
        Parameters
        ---------- 
        name: `str`
            Name of the instrument being controlled by the driver (must be unique in the DriverDB)            
        model: `InstrumentModel`
            Class representing the type, model and brand of instrument being controlled by the driver.
        connection_settings: `ConnectionSettings`
            Any class of type connection setting (e.g. SerialConnectionSettings)
        instrument_settings: dict
            Serializable dictionary of instrument parameters
        
        Raises
        ------
        ValueError
            Raised if a unique name is not passed  
        ''' 
        if self.db.contains(self.instruments.name == name):
            raise ValueError(f'Instrument of name {name} already exists in the database. Please choose a unique name.')
        update = {
            'name': name,
            'model': model.to_dict(),
            'grpc_address': grpc_address,
            'connection_settings': connection_settings.to_dict(),
            'instrument_settings': instrument_settings,
        }
        self.db.insert(update)

    def get_drivers(self, instrument_type=None):       
        ''' Get drivers from DriverDB
        
        Parameters
        ---------- 
        name: `str`
            Reference name for the instrument
        instrument_type: optional
            Filter for the type of instrument.  This should be a instrument from ``sci.instruments``.
        '''  
        if instrument_type:
            results = self.db.search(self.instruments.model.type ==instrument_type.instrument_type())
            if results:
                return [DriverDefinition.from_dict(**result) for result in results]
            else:
                return [{'no_instrument': instrument_type.instrument_type()}]
        else:
            results = self.db.all()
            return [DriverDefinition.from_dict(**result) for result in results]
        
    def remove_driver(self, name):
        '''Remove of driver from the DriverDB'''
        self.db.remove(self.instruments.name == name)

     
def start_driver(instrument, **kwargs):
    pass