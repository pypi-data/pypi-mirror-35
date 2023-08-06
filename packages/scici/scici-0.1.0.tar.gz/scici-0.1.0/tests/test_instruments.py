from sci.instruments import _Instrument, _InstrumentInterface, SyringePump
from sci.refs import _Ref, _RefInterface, ref_type, Syringe
from sci import units

from interface import implements
from typing import List, Type, Union
import pytest

def test_todict():
    ''' Test converting an instrument to a dictionary
    '''
    class ExampleRef(_Ref, implements(_RefInterface)):
        def __init__(self, name:str, **params):
            params.update({"type": "ExampleRef"})
            super().__init__(name=name, **params)

    params = {"a": 1, "b": 2}
    ref = ExampleRef(name="Test")

    class ExampleInstrument(_Instrument, implements(_InstrumentInterface),):
        def __init__(self, refs: Union[List[ref_type], List[str]], **params):
            super().__init__(refs=refs, **params)

        @staticmethod
        def instrument_type():
            return 'ExampleInstrument'

        def status(self):
            pass
            
    params = {"a": 1, "b": 2}
    ex = ExampleInstrument([ref], **params)
    actual = ex.to_dict()
    expected = {
                 "type": "ExampleInstrument",
                 "refs": [ref],
                 "params": params
    }
    assert actual["type"] == expected["type"]
    #Not sure how to test refs yet
    assert actual["params"] == expected["params"]

@pytest.fixture
def sp():
    syringe = Syringe('0.5M NaOH', liquid_volume=10 * units.milliliters)
    return SyringePump(refs=[syringe])

@pytest.mark.parametrize('rate', [100.0 * units.microliters/ units.minute])
@pytest.mark.parametrize('volume', [1.0 * units.milliliter])
@pytest.mark.parametrize('time', [1.0 * units.seconds, 5.0 * units.minutes])
def test_sp_infuse(sp, rate, volume, time):
    ''' Test that syringe pump infusing works properly'''
    #Rate and volume together
    sp.infuse(rate=rate, volume=volume)
    #Rate and time together
    sp.infuse(rate=rate, time=time)
    #Volmue and time together
    sp.infuse(volume=volume, time=time)
    #Passing all three should raise an ValueError
    with pytest.raises(ValueError):
        sp.infuse(rate=rate, volume=volume, time=time)
    

@pytest.mark.parametrize('rate', [100.0 * units.microliters/ units.minute])
@pytest.mark.parametrize('volume', [1.0 * units.milliliter])
@pytest.mark.parametrize('time', [1.0 * units.seconds, 5.0 * units.minutes])
def test_sp_withdraw(sp, rate, volume, time):
    ''' Test that syringe pump withdrawing works properly'''
    #Rate and volume together
    sp.withdraw(rate=rate, volume=volume)
    #Rate and time together
    sp.withdraw(rate=rate, time=time)
    #Volmue and time together
    sp.withdraw(volume=volume, time=time)
    #Passing all three should raise an ValueError
    with pytest.raises(ValueError):
        sp.withdraw(rate=rate, volume=volume, time=time)
