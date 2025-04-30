class HttpRequestOptions:
    
    def __init__(self, *, url, method, headers=None, query_params=None, post_params=None, body=None, timeout=16000):
        self.url = url
        self.method = method
        self.headers = headers if headers else {}
        self.query_params = query_params if query_params else {}
        self.post_params = post_params if post_params else {}
        self.body = body if body else None
        self.timeout = timeout

    #getters
    @property
    def url(self):
        return self._url
    
    @property
    def method(self):
        return self._method
    
    @property
    def headers(self):
        return self._headers
    
    @property
    def query_params(self):
        return self._query_params
    
    @property
    def post_params(self):
        return self._post_params
    
    @property
    def body(self):
        return self._body
    
    @property
    def timeout(self):
        return self._timeout
    
    #setters
    @url.setter
    def url(self, url):
        if not url:
            raise ValueError("The 'url' property is required")
        self._url = url
    
    @method.setter
    def method(self, method):
        valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD','TRACE']
        if not method or method.upper() not in valid_methods:
            raise ValueError("The 'method' property is invalid or missing")
        self._method = method.upper()

    @headers.setter
    def headers(self, headers):
        self._headers = headers

    @query_params.setter
    def query_params(self, query_params):
        self._query_params = query_params

    @post_params.setter
    def post_params(self, post_params):
        self._post_params = post_params

    @body.setter
    def body(self, body):
        self._body = body

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout
