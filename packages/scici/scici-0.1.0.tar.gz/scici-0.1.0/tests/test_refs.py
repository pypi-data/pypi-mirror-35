from sci.refs import _Ref, _RefInterface, Syringe, ref_from_dict
from sci import units
import pytest
from interface import implements


def test_todict():
    ''' Test converting a ref to a dictionary
    '''
    class ExampleRef(_Ref, implements(_RefInterface)):
        def __init__(self, name:str, **params):
            params.update({"type": "ExampleRef"})
            super().__init__(name=name, **params)

    params = {"a": 1, "b": 2}
    ex = ExampleRef("Test", **params)
    actual = ex.to_dict()
    expected = {
                 "type": "ExampleRef",
                 "name": "Test",
                 "params": params
    }
    assert actual == expected

@pytest.mark.parametrize('inputs', [('Syringe', {"liquid_volume": "10 milliliters"})])
def test_fromdict(inputs):
    ''' Test creating a syringe from a dictionry
    '''
    input = {
            "type": inputs[0],
            "name": "Test",
            "params": inputs[1]
    }

    test_ref = ref_from_dict(input=input)
    assert test_ref.type == inputs[0]
    assert test_ref.name == "Test"
    assert test_ref.params == inputs[1]


@pytest.mark.parametrize('name', ['Reagent', 'HC3^O2'])
@pytest.mark.parametrize('liquid_volume', [10 * units.milliliters, 100* units.microliters])
def test_syringe(name, liquid_volume):
    '''Test creating syringe and converting to dict'''
    s = Syringe(name, liquid_volume=liquid_volume)
    actual = s.to_dict()
    expected = {'name': name, 
              'type': 'Syringe', 
              'params': {'liquid_volume': str(liquid_volume)}
             }
    assert actual == expected
