from abc import ABC, abstractmethod

class AbstractHttpClient(ABC):
    def __init__(self):
        self.timeout = 16000        
        self.https_agent = None #it is a http proxy agent will be used later
        self.pre_hook = None
        self.post_hook = None

    def set_timeout(self, timeout):
        if not isinstance(timeout, (int, float)):
            raise ValueError("The 'timeout' property must be a number")
        self.timeout = timeout

    def set_pre_request_hook(self, hook):
        """
        Sets a pre-request hook that will be called before each request
        
        Args:
            hook: A function that takes an HTTP request and returns a modified HTTP request
        """
        if not callable(hook) or hook.__code__.co_argcount != 1:
            raise ValueError("preHook must be a function that accepts (http_request_options)")
        self.pre_hook = hook
    
    def set_post_request_hook(self, hook):
        """
        Sets a post-request hook that will be called after each request
        
        Args:
            hook: A function that takes an HTTP response and returns a modified HTTP response
        """
        if not callable(hook) or hook.__code__.co_argcount != 1:
            raise ValueError("postHook must be a function that accepts (RESTResponse)")
        self.post_hook = hook
    
    @abstractmethod
    def request(self, http_request_options):
        raise NotImplementedError("method must be implemented")
