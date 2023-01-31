import PrimePyAnsysPrimeServer as Prime

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.meshing.prime.internals.error_handling import (
    communicator_error_handler,
    error_code_handler,
)

global return_value
return_value = ""


class PrimeCommunicator(Communicator):
    def __init__(self):
        Prime.SetupForPyPrime_Beta(1)

    @error_code_handler
    @communicator_error_handler
    def serve(self, model, command, *args, **kwargs) -> dict:
        command = {"Command": command}
        if len(args) > 0:
            command.update({"ObjectID": args[0]})
        if kwargs is not None:
            if "args" in kwargs:
                command.update({"Args": kwargs["args"]})

        if config.is_optimizing_numpy_arrays():
            return json.loads(
                Prime.ServeJsonBinary(model._object_id, json.dumps(command)).AsBytes()
            )

        return json.loads(Prime.ServeJson(model._object_id, json.dumps(command)).Get())

    def initialize_params(self, model, param_name: str) -> dict:
        command = {
            "ParamName": param_name,
        }

        with config.numpy_array_optimization_disabled():
            res = json.loads(Prime.GetParamDefaultJson(model._object_id, json.dumps(command)).Get())

        return res

    def run_on_server(self, model, recipe: str) -> dict:
        exec(recipe, globals())
        output = '{"Results" : "' + str(return_value) + '"}'
        with config.numpy_array_optimization_disabled():
            result = json.loads(output)
        return result

    def close(self):
        pass
