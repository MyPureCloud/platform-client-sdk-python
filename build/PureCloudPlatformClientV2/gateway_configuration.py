
class GatewayConfiguration:

    def __init__(self, *, host=None, protocol=None, port=-1, path_params_login=None, path_params_api=None, username=None, password=None):
        self.host = host
        self.protocol = protocol
        self.port = port
        self.path_params_login = path_params_login
        self.path_params_api = path_params_api
        self.username = username
        self.password = password

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if not value:
            self._host = None
        else:
            self._host = value

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if not value:
            self._protocol = "https"
        else:
            self._protocol = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if value is None or value < 0:
            self._port = -1
        else:
            self._port = value

    @property
    def path_params_login(self):
        return self._path_params_login

    @path_params_login.setter
    def path_params_login(self, value):
        if not value:
            self._path_params_login = ""
        else:
            if value.endswith("/"):
                self._path_params_login = value[:-1]
            else:
                self._path_params_login = value

    @property
    def path_params_api(self):
        return self._path_params_api

    @path_params_api.setter
    def path_params_api(self, value):
        if not value:
            self._path_params_api = ""
        else:
            if value.endswith("/"):
                self._path_params_api = value[:-1]
            else:
                self._path_params_api = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            self._username = None
        else:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            self._password = None
        else:
            self._password = value
