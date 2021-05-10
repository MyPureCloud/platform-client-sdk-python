import logging
import json
from datetime import datetime

class Logger(object):
    def __init__(self):
        # disable urllib3 logging
        logging.getLogger("urllib3").setLevel(logging.CRITICAL + 1)
        logging.getLogger("urllib3").propagate = False
        # disable watchdog logging   
        logging.getLogger("watchdog").setLevel(logging.CRITICAL + 1)
        logging.getLogger("watchdog").propagate = False

        # add trace log level
        logging.addLevelName(LogLevel.LTrace, 'TRACE')

        # private properties
        self._logger = logging.getLogger('PureCloudPlatformClientV2')
        self._file_handler = None
        self._console_handler = None

        # public properties
        self.log_file_path = None
        self.log_to_console = True
        self.log_format = LogFormat.TEXT
        self.log_level = LogLevel.LNone
        self.log_response_body = False
        self.log_request_body = False

        # configure file and console handlers
        self.set_log_outputs()

    def set_log_outputs(self):
        try:
            logger_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

            # remove handlers
            if self._file_handler is not None:
                self._logger.removeHandler(self._file_handler)
            if self._console_handler is not None:
                self._logger.removeHandler(self._console_handler)

            # add file handler
            if self.log_file_path is not None:
                try:
                    self._file_handler = logging.FileHandler(self.log_file_path)
                    if self.log_format == LogFormat.TEXT:
                        self._file_handler.setFormatter(logger_formatter)
                    self._logger.addHandler(self._file_handler)
                except:
                    None

            # add console handler
            if self.log_to_console:
                self._console_handler = logging.StreamHandler()
                if self.log_format == LogFormat.TEXT:
                    self._console_handler.setFormatter(logger_formatter)
                self._logger.addHandler(self._console_handler)
        except:
            None

    @property
    def log_level(self):
        return self.__log_level

    @log_level.setter
    def log_level(self, value):
        self.__log_level = value
        self._logger.setLevel(self.__log_level)

    @property
    def log_format(self):
        return self.__log_format

    @log_format.setter
    def log_format(self, value):
        self.__log_format = value
        self.set_log_outputs()

    @property
    def log_to_console(self):
        return self.__log_to_console

    @log_to_console.setter
    def log_to_console(self, value):
        self.__log_to_console = value
        self.set_log_outputs()

    @property
    def log_file_path(self):
        return self.__log_file_path

    @log_file_path.setter
    def log_file_path(self, value):
        self.__log_file_path = value
        self.set_log_outputs()

    def trace(self, method, url, request_body, status_code, request_headers, response_headers):
        now = datetime.now()
        log_statement = LogStatement(level="trace", date=now.strftime("%m-%d-%Y, %H:%M:%S"), method=method, url=url, request_body=request_body,
                                    status_code=status_code, request_headers=request_headers, response_headers=response_headers)
        self._logger.log(LogLevel.LTrace, log_statement.string(self.log_format, self.log_request_body, self.log_response_body))

    def debug(self, method, url, request_body, status_code, request_headers):
        now = datetime.now()
        log_statement = LogStatement(level="debug", date=now.strftime("%m-%d-%Y, %H:%M:%S"), method=method, url=url, request_body=request_body,
                                    status_code=status_code, request_headers=request_headers)
        self._logger.log(LogLevel.LDebug, log_statement.string(self.log_format, self.log_request_body, self.log_response_body))

    def error(self, method, url, request_body, status_code, request_headers, response_body, response_headers):
        now = datetime.now()
        log_statement = LogStatement("error", now.strftime("%m-%d-%Y, %H:%M:%S"), method, url, request_body, status_code, request_headers, response_body, response_headers)
        self._logger.log(LogLevel.LError, log_statement.string(self.log_format, self.log_request_body, self.log_response_body))

class LogFormat:
    TEXT = 1
    JSON = 2

    @staticmethod
    def from_string(value):
        try:
            return {
                'text': LogFormat.TEXT,
                'json': LogFormat.JSON,
            }[value.lower()]
        except:
            return LogFormat.TEXT

class LogLevel:
    LTrace = logging.DEBUG - 5
    LDebug = logging.DEBUG
    LError = logging.ERROR
    LNone = logging.CRITICAL + 1

    @staticmethod
    def from_string(value):
        try:
            return {
                'trace': LogLevel.LTrace,
                'debug': LogLevel.LDebug,
                'error': LogLevel.LError,
                'none': LogLevel.LNone,
            }[value.lower()]
        except:
            return LogLevel.LNone

class LogStatement(object):
    def __init__(self, level, date, method, url, request_body, status_code, request_headers, response_body=None, response_headers=None):
        self.level = level
        self.date = date
        self.method = method
        self.url = url
        self.request_body = request_body
        self.response_body = response_body
        self.status_code = status_code
        self.request_headers = request_headers
        if response_headers is not None:
            response_headers_dict = dict()
            # Convert from HTTPHeaderDict to dict
            for x, y in response_headers.items():
                response_headers_dict[x] = response_headers[x]
            self.response_headers = response_headers_dict
        else:
             self.response_headers = None
    
    def string(self, log_format, log_request_body, log_response_body):
        self.request_headers["Authorization"] = "[REDACTED]"

        if not log_request_body:
            self.request_body = None
        if not log_response_body:
            self.response_body = None

        if log_format == LogFormat.JSON:
            json_output = dict()
            for x, y in self.__dict__.items():
                if y is not None:
                    json_output[self._camel_case(x)] = self.__dict__[x]
            return json.dumps(json_output, skipkeys=True)
        else:
            return """
=== REQUEST ==={}{}{}{}
=== RESPONSE ==={}{}{}{}""".format(self._format_value("URL", self.url),
           self._format_value("Method", self.method),
           self._format_value("Headers", self._format_headers(self.request_headers)),
           self._format_value("Body", self.request_body),

           self._format_value("Status", self.status_code),
           self._format_value("Headers", self._format_headers(self.response_headers)),
           self._format_value("CorrelationId", self._get_correlation_id(self.response_headers)),
           self._format_value("Body", self.response_body))
    
    def _camel_case(self, st):
        output = ''.join(x for x in st.title() if x.isalnum())
        return output[0].lower() + output[1:]

    def _get_correlation_id(self, headers):
        if headers is None:
            return ""
        try:
            return headers["ININ-Correlation-Id"]
        except KeyError:
            return ""

    def _format_value(self, name, value):
        if value == "" or value is None:
            return ""
        return "\n{}: {}".format(name, value)

    def _format_headers(self, headers):
        result = ""
        if headers is None:
            return result
        for x, y in headers.items():
            result += "\n\t{}: {}".format(x, y)
        return result
