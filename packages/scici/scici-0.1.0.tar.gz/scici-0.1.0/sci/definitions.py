
class StepDefinition:
    def __init__(self, description, inputs, instruments, outputs, step_fn):
        self.description = description
        self.inputs = inputs
        self.instruments = instruments
        self.outputs = outputs
        self.step_fn = step_fn

# class StepExecutionResult:
#     def __init__(self, success, step, result, )

class ProtcolExecutionResult:
    def __init__(self, results):
        self.results = results

    @property
    def success(self):
        return all([result.success for result in self.results])


