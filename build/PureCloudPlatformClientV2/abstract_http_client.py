from abc import ABC, abstractmethod

class AbstractHttpClient(ABC):
    def __init__(self):
        self.timeout = 16000        
        self.https_agent = None #it is a http proxy agent will be used later

    def set_timeout(self, timeout):
        if not isinstance(timeout, (int, float)):
            raise ValueError("The 'timeout' property must be a number")
        self.timeout = timeout
    
    @abstractmethod
    def request(self, http_request_options):
        raise NotImplementedError("method must be implemented")
