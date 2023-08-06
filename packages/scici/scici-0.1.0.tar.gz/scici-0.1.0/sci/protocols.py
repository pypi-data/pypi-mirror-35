from sci.definitions import StepDefinition, ProtcolExecutionResult
from sci.errors import SciExecutionError
from sci.driver import DriverDB, start_driver

from whaaaaat import (style_from_dict, Token, prompt, 
                      default_style, Separator)

import re
from functools import wraps
from inspect import getargspec

class _Step:
    def __init__(self, description, inputs, instruments, outputs, **kwargs):
        self.description = description
        self.inputs = inputs
        self.instruments = instruments
        self.outputs = outputs


    def __call__(self, wrapped):
        return StepDefinition(
                description=self.description,
                inputs=self.inputs,
                instruments=self.instruments,
                outputs=self.outputs,
                step_fn=wrapped
        )

def step(*, description, inputs, instruments, outputs):
    return _Step(description=description, inputs=inputs, 
                 instruments=instruments, outputs=outputs)

def check_refs_unique(steps):
    pass

def find_unique_instruments(instruments):
    refs = []
    final_instruments = []

    def add_refs_as_json(instrument, ref_list, instrument_list):
        if type(instrument.refs) == str:
            if instrument.refs not in ref_list:
                ref_list.append(instrument.refs)
                instrument_list.append(instrument)
        else:
            for ref in instrument.refs:
                if ref.to_dict() not in ref_list:
                    ref_list.append(ref.to_dict())
                    instrument_list.append(instrument)
        return ref_list, instrument_list
    
    for instrument in instruments:
        refs, final_instruments = add_refs_as_json(instrument, refs, final_instruments)
    
    return final_instruments

class InstrumentResolutionDefintion:
    def __init__(self, 
                 instruments_needed,
                 instruments_available):
        self.instruments_needed = instruments_needed
        self.instruments_available = instruments_available

def find_available_instruments_types(available_instruments):
    available_tally = {}
    for db_instrument in available_instruments:
        try:
            available_tally[db_instrument.model.type] += 1
        except KeyError:
            available_tally[db_instrument.model.type] = 1
    return available_tally

def format_driver(index: int, instrument: dict):
    return f'{instrument.name} ({instrument.model.brand} {instrument.model.model} {instrument.model.type}, id: {str(index)})'

def resolve_instruments(instruments_by_step, db):
    '''Resolve whether needed instruments are available'''
    # Find unique instruments based on refs
    instruments_needed = [instrument for instruments in instruments_by_step for instrument in instruments]
    instruments_needed = find_unique_instruments(instruments_needed) #Could probably replace with a map
   
    #Determine the number of each type of instrument needed
    needed_instrument_types = {}
    for instrument in instruments_needed:
        try:
            needed_instrument_types[instrument.instrument_type()] += 1
        except KeyError:
            needed_instrument_types[instrument.instrument_type()] = 1
    
    #Determine the number of each type of instrument available 
    instruments_available = db.get_drivers() 
    available_instrument_types = find_available_instruments_types(instruments_available)

    #Determine if supply meets demand
    missing_instruments = []
    for instrument in instruments_needed:
        try:
            assert needed_instrument_types[instrument.instrument_type()] <= available_instrument_types[instrument.instrument_type()]
        except AssertionError:
            missing_instruments.append(instrument)

    #Tell user if supply ≠ demand
    if missing_instruments:
        for missing_instrument in missing_instruments:
            type = missing_instrument.instrument_type()
            print(f"Missing instrument(s) of type: {type}")
            print(f"\t Protocol needs {needed_instrument_types[type]} {type}s but {available_instrument_types[type]} are installed.")
            exit(1)

    #Return the instruments needed and available instruments
    return InstrumentResolutionDefintion(instruments_needed, instruments_available)

style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})

def _driver_setup(instruments_by_step, instrument_db):
    '''Sets up all the instrument    drivers needed for the protocol
    '''
    #Check that all refs in instruments are unique 
    check_refs_unique(instruments_by_step) #NotImplemented

    #Resolve whether needed instruments are available
    resolved_instruments = resolve_instruments(instruments_by_step,instrument_db)
    ri = resolved_instruments

    #Start drivers based on user selection
    print("  Instrument Selection")
    print("This is for pairing virtual instruments in the protocol to drivers that driver real world instruments. ")
    for instrument in ri.instruments_needed:
        #User prompt
        refs = "".join([repr(ref) + ", " for ref in instrument.refs])
        refs = refs.rstrip(", ")
        if len(instrument.refs) == 1:
            message = f"Which driver should be used for the {instrument.instrument_type()} with ref {refs}?"
        else:    
            message = f"Which driver should be used for the {instrument.instrument_type()} with refs {refs}?"

        #List available instruments as choices
        choices = [format_driver(i, available_instrument)
                   for i, available_instrument in enumerate(ri.instruments_available)
                   if available_instrument.model.type == instrument.instrument_type()]
        choices.append('Cancel and Exit.')

        question = [{
            'type': 'list',
            'name': 'instrument_select',
            'message': message,
            'choices': choices
        }]
        answer  = prompt(question, style=style)
        answer = answer['instrument_select']
        match = re.search(r'(?!id: )\d+', answer, re.M) #format_driver appends index as id
        if match:
            index = match.group()
            index = int(float(index))
        else:
            raise ValueError('Valid id not found in instrument selected')

        available_instrument = ri.instruments_available[index]
        start_driver(available_instrument)

    #Return grpc addresses
    return [[available_instrument.grpc_address for 
             instrument in instruments
             if instrument.instrument_type() == available_instrument.model.type] 
             for instruments in instruments_by_step] 
    
    return addresses

def _start_grpc_clients(grpc_addresses, steps):
    # instrument._start_grpc_client(grpc_addresses[i,j])
    [instrument[1]._start_grpc_client(grpc_addresses[i][j])
     for i, step in enumerate(steps) 
     for j, instrument in enumerate(step.instruments)]
    return steps

class Protocol:
    ''' 
    The Protocol class is the heart of sci protocols. 
    '''
    def __init__(self, name, description, steps, **kwargs):
        self.name = name
        self.description = description
        self.steps = steps
        filepath = kwargs.get('driver_db')
        self.db = DriverDB(filepath) if filepath else DriverDB()

    def __call__(self):
        #Set up instruments (drivers and clients)
        instruments_by_step = [[instrument_tuple[1] for instrument_tuple in step.instruments] 
                               for step in self.steps]
        grpc_addresses =  _driver_setup(instruments_by_step, self.db)
        self.steps = _start_grpc_clients(grpc_addresses, self.steps)
        
        #Execute protocol
        results = []
        for result in _execute_protocol_iterator(self.steps):
            results.append(result)

        return ProtcolExecutionResult(results)

def _execute_protocol_iterator(steps):
    for step in steps:
        try:
            result = _execute_step(step)

            #If step successful, do any output transforms/materializaitons
            #and yield the result
            # if result.success():
            #     _execute_output(result, step)
            #     yield result
            yield 'Success'

        except SciExecutionError:
            #Handle errors
            pass

def _compose_args(inputs, instruments):
    inputs = {input[0]:input[1] for input in inputs}
    inputs.update({instrument[0]:instrument[1] for instrument in instruments})
    return inputs

def _execute_step(step):
    new_args = _compose_args(step.inputs, step.instruments)
    return step.step_fn(*new_args) 

def _execute_output(result, step):
    return