import PrimePyPrimeServer as Prime
import json
from ansys.meshing.prime import relaxed_json
from ansys.meshing.prime.internals.error_handling import (
    communicator_error_handler,
    error_code_handler
)
from ansys.meshing.prime.internals.communicator import Communicator

global return_value
return_value = ""

class PrimeCommunicator(Communicator):
    @error_code_handler
    @communicator_error_handler
    def serve(self, command, *args, **kwargs) -> dict:
        command = { "Command" : command }
        binary = False
        if(len(args) > 0 ):
            command.update({ "ObjectID" : args[0]})
        if (kwargs is not None):
            command.update({ "Args" : kwargs["args"]})
            binary = kwargs.get("binary", False)

        if binary:
            return relaxed_json.loads(Prime.ServeJsonBinary(json.dumps(command)).AsBytes())

        return json.loads(Prime.ServeJson(json.dumps(command)).Get())

    def initialize_params(self, param_name: str, *args) -> dict:
        command = { "ParamName" : param_name }
        if(len(args) > 0 ):
            command.update({ "ModelID" : args[0]})
        return json.loads(Prime.GetParamDefaultJson(json.dumps(command)).Get())

    def run_on_server(self, recipe: str) -> dict:
        exec(recipe, globals())
        output = '{"Results" : "' + str(return_value) + '"}'
        return json.loads(output)
