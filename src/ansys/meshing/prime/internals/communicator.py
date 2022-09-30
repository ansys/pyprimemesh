from abc import abstractmethod


class Communicator(object):
    @abstractmethod
    def serve(self, model, command, *args, **kwargs) -> dict:
        pass

    @abstractmethod
    def initialize_params(self, model, param_name: str, *args) -> dict:
        pass

    @abstractmethod
    def run_on_server(self, model, recipe: str) -> dict:
        pass

    @abstractmethod
    def import_cad(self, model, file_name: str, *args) -> dict:
        pass

    @abstractmethod
    def close(self):
        pass
