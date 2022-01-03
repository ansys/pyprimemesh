from abc import abstractmethod

class Communicator(object):
    @abstractmethod
    def serve(self, *args, **kwargs) -> dict:
        pass

    @abstractmethod
    def initialize_params(self, param_name: str) -> dict:
        pass

    @abstractmethod
    def run_on_server(self, file_name: str) -> dict:
        pass
