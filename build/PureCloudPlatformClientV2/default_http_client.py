from .abstract_http_client import AbstractHttpClient
from .http_request_options import HttpRequestOptions
from .rest import RESTClientObject
from .configuration import Configuration

class DefaultHttpClient(AbstractHttpClient):
    def __init__(self, timeout=None, https_agent=None):
        super().__init__()
        if timeout is not None:
            self.set_timeout(timeout)
        
        Configuration().create_mtls_or_ssl_context()
        
        #This object "self.rest_client" handles all REST API communication (requests/responses).
        #Implementation: rest.py (templates/rest.mustache).
        self.rest_client = RESTClientObject()

    def request(self, http_request_options):
        if not isinstance(http_request_options, HttpRequestOptions):
            raise ValueError("httpRequestOptions must be an instance of HttpRequestOptions")
        
        if self.pre_hook and callable(self.pre_hook):
            http_request_options = self.pre_hook(http_request_options)

        config = self.to_rest_client_config(http_request_options)
        
        if config['method'] == "GET":
            response = self.rest_client.GET(config['url'],
                                        query_params=config['query_params'],
                                        headers=config['headers'])
        elif config['method'] == "HEAD":
            response = self.rest_client.HEAD(config['url'],
                                        query_params=config['query_params'],
                                        headers=config['headers'])
        elif config['method'] == "OPTIONS":
            response = self.rest_client.OPTIONS(config['url'],
                                            query_params=config['query_params'],
                                            headers=config['headers'],
                                            post_params=config['post_params'],
                                            body=config['body'])
        elif config['method'] == "POST":
            response = self.rest_client.POST(config['url'],
                                        query_params=config['query_params'],
                                        headers=config['headers'],
                                        post_params=config['post_params'],
                                        body=config['body'])
        elif config['method'] == "PUT":
            response = self.rest_client.PUT(config['url'],
                                        query_params=config['query_params'],
                                        headers=config['headers'],
                                        post_params=config['post_params'],
                                        body=config['body'])
        elif config['method'] == "PATCH":
            response = self.rest_client.PATCH(config['url'],
                                        query_params=config['query_params'],
                                        headers=config['headers'],
                                        post_params=config['post_params'],
                                        body=config['body'])
        elif config['method'] == "DELETE":
            response = self.rest_client.DELETE(config['url'],
                                        query_params=config['query_params'],
                                        headers=config['headers'],
                                        body=config['body'])
        else:
            raise ValueError(
                "http method must be `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD` or `TRACE`."
            )
        
        if self.post_hook and callable(self.post_hook):
            response = self.post_hook(response)

        return response
                    

    def to_rest_client_config(self, http_request_options):
        if not http_request_options.url or not http_request_options.method:
            raise ValueError("Mandatory fields 'url' and 'method' must be set before making a request")
        
        config = {
            "url": http_request_options.url,
            "method": http_request_options.method,
            "headers": http_request_options.headers or {},
            "query_params": http_request_options.query_params or {},
            "post_params": http_request_options.post_params or {},
            "body": http_request_options.body or None,
            "timeout": self.timeout if self.timeout else None,
        }
        return config
