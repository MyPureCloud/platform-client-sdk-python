# Platform API Client SDK - Python

[![PyPI version](https://badge.fury.io/py/PureCloudPlatformClientV2.svg)](https://badge.fury.io/py/PureCloudPlatformClientV2)
[![Release Notes Badge](https://developer-content.genesys.cloud/images/sdk-release-notes.png)](https://github.com/MyPureCloud/platform-client-sdk-python/blob/master/releaseNotes.md)

Documentation can be found at https://mypurecloud.github.io/platform-client-sdk-python/

Documentation version PureCloudPlatformClientV2 229.0.0

## Preview APIs

**Warning:** Preview APIs are included in this SDK. These resources are subject to both breaking and non-breaking changes at any time without notice. This includes, but is not limited to, changing resource names, paths, contracts, documentation, and removing resources entirely. For a full list of the preview APIs see [here](https://developer.genesys.cloud/platform/preview-apis)

## Install Using pip

```bash
pip install PureCloudPlatformClientV2
```

**Note**: For Windows users, the [maximum path length limitation](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd) must be removed prior to installing to avoid a `No such file or directory error`

Package info can be found at [https://pypi.python.org/pypi/PureCloudPlatformClientV2](https://pypi.python.org/pypi/PureCloudPlatformClientV2)

## Using the Library

### Referencing the Library

Import the package in the python script:

```python
import PureCloudPlatformClientV2
```

### Authenticating

#### Client Credentials Grant

**Use when...**

* The app is authenticating as a non-human (e.g. a service, scheduled task, or other non-UI application)

For headless and non-user applications, the [Client Credentials Grant](https://developer.genesys.cloud/authorization/platform-auth/use-client-credentials) 

```python
apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(os.environ['GENESYS_CLOUD_CLIENT_ID'],
                                                                                          os.environ['GENESYS_CLOUD_CLIENT_SECRET'])
authApi = PureCloudPlatformClientV2.AuthorizationApi(apiclient)
print(authApi.get_authorization_permissions())
```

#### OAuth2 SAML2 Bearer Grant

**Use when...**

* The app is authenticating as a human user, the [OAuth2 SAML2 Bearer](https://developer.genesys.cloud/authorization/platform-auth/use-saml2-bearer)

```python
apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_saml2bearer_token(os.environ['GENESYS_CLOUD_SAML2BEARER_CLIENT_ID'],
                                                                                   os.environ['GENESYS_CLOUD_SAML2BEARER_CLIENT_SECRET'],
                                                                                   orgName,
                                                                                   encodedsamlassertion)
usersApi = PureCloudPlatformClientV2.UsersApi(apiclient)
print(usersApi.get_users_me())

```

### Authorization Code Grant

* The app is authenticating as a human, the [Authorization Code Grant](https://developer.genesys.cloud/authorization/platform-auth/use-authorization-code)
* The app is served via a web server
* There is server-side code that will be making API requests

```python
apiclient, auth_token_info = apiclient.get_code_authorization_token(os.environ['GENESYS_CLOUD_CODEAUTH_CLIENT_ID'],
                                                                    os.environ['GENESYS_CLOUD_CODEAUTH_CLIENT_SECRET'],
                                                                    auth_code,
                                                                    "https://redirect-uri.com/oauth/callback")
usersApi = PureCloudPlatformClientV2.UsersApi(apiclient)
```

By default, the SDK will use the refresh token to request a new access token transparently when it expires. If multiple threads are running, 1 thread will request a new token. Other threads will wait a maximum of 10 seconds for the token refresh to complete This time can be overridden with the _refresh_token_wait_time_ field of the _Configuration_ object. If you wish to implement the refresh logic, set _should_refresh_access_token_ to false and store the refresh token from the auth response. The expires_in value can be used to proactively request a new one before it expires:

```python
refresh_token = auth_token_info["refresh_token"]
expires_in = auth_token_info["expires_in"]
PureCloudPlatformClientV2.configuration.should_refresh_access_token = False
```

When the access token expires, refresh it using the refresh_code_authorization_token method using the same clientId and clientSecret as used to request it.

```python
apiclient, auth_token_info = apiclient.refresh_code_authorization_token(os.environ['GENESYS_CLOUD_CODEAUTH_CLIENT_ID'],
                                                                        os.environ['GENESYS_CLOUD_CODEAUTH_CLIENT_SECRET'],
                                                                        refresh_token)
```

### PKCE Grant

* The app is authenticating as a human, the [PKCE Grant](https://developer.genesys.cloud/authorization/platform-auth/use-pkce)
* The app is served via a web server
* There is server-side code that will be making API requests

```python
apiclient, auth_token_info = apiclient.get_pkce_token(os.environ['GENESYS_CLOUD_CODEAUTH_CLIENT_ID'],
                                                                    code_verifier,
                                                                    auth_code,
                                                                    "https://redirect-uri.com/oauth/callback")
usersApi = PureCloudPlatformClientV2.UsersApi(apiclient)
```

The SDK provides methods to generate a PKCE Code Verifier and to compute PKCE Code Challenge.

```python
code_verifier = PureCloudPlatformClientV2.api_client.ApiClient().generate_pkce_code_verifier(128)
code_challenge = PureCloudPlatformClientV2.api_client.ApiClient().compute_pkce_code_challenge(code_verifier)
```

### Setting the Environment

If connecting to a Genesys Cloud environment other than mypurecloud.com (e.g. mypurecloud.ie), set the new base path before constructing any API classes. The new base path should be the base path to the Platform API for your environment.

```python
region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_east_1
PureCloudPlatformClientV2.configuration.host = region.get_api_host()
```

#### Setting the gateway

The Genesys Cloud Login and API URL path can be overridden if necessary (i.e. if the Genesys Cloud requests must be sent through to an intermediate API gateway or equivalent).

This can be achieved setting the gateway on the `ApiClient` instance with *set_gateway*. You can use *None* as parameter's value for default configuration (e.g. "https" for protocol, -1 for port, ...).

```python
apiClient = PureCloudPlatformClientV2.api_client.ApiClient()
apiClient.set_gateway("mygateway.mydomain.myextension", "https", 1443, "myadditionalpathforlogin", "myadditionalpathforapi")
apiClient.get_client_credentials_token(os.environ['GENESYS_CLOUD_CLIENT_ID'],
                                        os.environ['GENESYS_CLOUD_CLIENT_SECRET'])
```

or setting as default for all clients

```python
gateway_configuration = PureCloudPlatformClientV2.GatewayConfiguration()
gateway_configuration.host = "mygateway.mydomain.myextension";
gateway_configuration.protocol = "https";
gateway_configuration.port = 1443;
gateway_configuration.path_params_login = "myadditionalpathforlogin";
gateway_configuration.path_params_api = "myadditionalpathforapi";
...
PureCloudPlatformClientV2.configuration.gateway_configuration = gateway_configuration
```

* "host" is the address of your gateway.
* "protocol" is not mandatory. It will default to "https" if the parameter is not defined or empty.
* "port" is not mandatory. This parameter can be defined if a non default port is used and needs to be specified in the url (value must be greater or equal to 0). Set to -1 to use default port (default unspecified port).
* "path_params_login" and "path_params_api" are not mandatory. They will be appended to the gateway url path if these parameters are defined and non empty (for Login requests and for API requests).
* "username" and "password" are not used at this stage. This is for a possible future use.

With the configuration below, this would result in:

* Login requests to: "https://mygateway.mydomain.myextension:1443/myadditionalpathforlogin" (e.g. "https://mygateway.mydomain.myextension:1443/myadditionalpathforlogin/oauth/token")
* API requests to: "https://mygateway.mydomain.myextension:1443/myadditionalpathforapi" (e.g. "https://mygateway.mydomain.myextension:1443/myadditionalpathforlogin/api/v2/users/me")

### Connect to a Proxy Server

If connecting to a proxy server, set the the address of your proxy server as follows:

```python
PureCloudPlatformClientV2.configuration.proxy = 'YOUR_PROXY_URL'
```

If your proxy server requires authentication, set the username and password as follows:

```python
PureCloudPlatformClientV2.configuration.proxy_username = 'YOUR_PROXY_USERNAME'
PureCloudPlatformClientV2.configuration.proxy_password = 'YOUR_PROXY_PASSWORD'
```

The Python SDK uses `urllib3.ProxyManager` to make requests when `proxy` is provided with default http client implementation (refer to [Inject Custom HTTP Client](#inject-custom-http-client)).

#### SDK Logging

Logging of API requests and responses can be controlled by several parameters on the `configuration`'s `logging` instance.

`PureCloudPlatformClientV2.logger.LogLevel` values:

1. LTrace (HTTP Method, URL, Request Body, HTTP Status Code, Request Headers, Response Headers)
2. LDebug (HTTP Method, URL, Request Body, HTTP Status Code, Request Headers)
3. LError (HTTP Method, URL, Request Body, Response Body, HTTP Status Code, Request Headers, Response Headers)
4. LNone - default

`PureCloudPlatformClientV2.logger.LogFormat` values:

1. JSON
2. TEXT - default

By default, the request and response bodies are not logged because these can contain PII. Be mindful of this data if choosing to log it.  
To log to a file, provide a file path to the the `PureCloudPlatformClientV2.configuration.logger.log_file_path` property. SDK users are responsible for the rotation of the log file.

Example logging configuration:

```python
PureCloudPlatformClientV2.configuration.logger.log_level = PureCloudPlatformClientV2.logger.LogLevel.LError
PureCloudPlatformClientV2.configuration.logger.log_request_body = True
PureCloudPlatformClientV2.configuration.logger.log_response_body = True
PureCloudPlatformClientV2.configuration.logger.log_format = PureCloudPlatformClientV2.logger.LogFormat.TEXT
PureCloudPlatformClientV2.configuration.logger.log_to_console = False
PureCloudPlatformClientV2.configuration.logger.log_file_path = "/var/log/pythonsdk.log"
```

#### Configuration file

Several configuration parameters can be applied using a configuration file. There are two sources for this file:

1. The SDK will look for `%HOME%\.genesyscloudpython\config` or `%USERPROFILE%\.genesyscloudpython\config` if `%HOME%` is not set on Windows, or `$HOME/.genesyscloudpython/config` on Unix.
2. Set the `PureCloudPlatformClientV2.configuration.config_file_path` property to the path of your configuration file.

The SDK will take an event-driven approach to monitor for config file changes and will apply changes in near real-time, regardless of whether a config file was present at start-up. To disable this behavior, set `PureCloudPlatformClientV2.configuration.live_reload_config` to false.  
INI and JSON formats are supported. See below for examples of configuration values in both formats:

INI:

```ini
[logging]
log_level = trace
log_format = text
log_to_console = false
log_file_path = /var/log/pythonsdk.log
log_response_body = false
log_request_body = false
[reauthentication]
refresh_access_token = true
refresh_token_wait_max = 10
[general]
live_reload_config = true
host = https://api.mypurecloud.com
```

JSON:

```json
{
    "logging": {
        "log_level": "trace",
        "log_format": "text",
        "log_to_console": false,
        "log_file_path": "/var/log/pythonsdk.log",
        "log_response_body": false,
        "log_request_body": false
    },
    "reauthentication": {
        "refresh_access_token": true,
        "refresh_token_wait_max": 10
    },
    "general": {
        "live_reload_config": true,
        "host": "https://api.mypurecloud.com"
    }
}
```

The Genesys Cloud Login and API URL path can be overridden if necessary (i.e. if the Genesys Cloud requests must be sent through to an intermediate API gateway or equivalent).

This can be achieved defining a "gateway" configuration, in the INI or the JSON configuration file.

* "host" is the address of your gateway.
* "protocol" is not mandatory. It will default to "https" if the parameter is not defined or empty.
* "port" is not mandatory. This parameter can be defined if a non default port is used and needs to be specified in the url (value must be greater or equal to 0). Set to -1 to use default port (default unspecified port).
* "path_params_login" and "path_params_api" are not mandatory. They will be appended to the gateway url path if these parameters are defined and non empty (for Login requests and for API requests).
* "username" and "password" are not used at this stage. This is for a possible future use.

With the configuration below, this would result in:

* Login requests to: "https://mygateway.mydomain.myextension:1443/myadditionalpathforlogin" (e.g. "https://mygateway.mydomain.myextension:1443/myadditionalpathforlogin/oauth/token")
* API requests to: "https://mygateway.mydomain.myextension:1443/myadditionalpathforapi" (e.g. "https://mygateway.mydomain.myextension:1443/myadditionalpathforlogin/api/v2/users/me")

INI:

```ini
[logging]
log_level = trace
log_format = text
log_to_console = false
log_file_path = /var/log/pythonsdk.log
log_response_body = false
log_request_body = false
[reauthentication]
refresh_access_token = true
refresh_token_wait_max = 10
[general]
live_reload_config = true
host = https://api.mypurecloud.com
[gateway]
host = mygateway.mydomain.myextension
protocol = https
port = 1443
path_params_login = myadditionalpathforlogin
path_params_api = myadditionalpathforapi
username = username
password = password
```

JSON:

```json
{
    "logging": {
        "log_level": "trace",
        "log_format": "text",
        "log_to_console": false,
        "log_file_path": "/var/log/pythonsdk.log",
        "log_response_body": false,
        "log_request_body": false
    },
    "reauthentication": {
        "refresh_access_token": true,
        "refresh_token_wait_max": 10
    },
    "general": {
        "live_reload_config": true,
        "host": "https://api.mypurecloud.com"
    },
    "gateway": {
        "host": "mygateway.mydomain.myextension",
        "protocol": "https",
        "port": 1443,
        "path_params_login": "myadditionalpathforlogin",
        "path_params_api": "myadditionalpathforapi",
        "username": "username",
        "password": "password"
    }
}
```

### Making Requests

There are two steps to making requests:

1. Instantiate one of the API classes in the ININ.PureCloudApi.Api namespace
2. Call the methods on the API object

Example of getting the authenticated user's information:

```python
usersApi = PureCloudPlatformClientV2.UsersApi()
print(usersApi.get_users_me())
```

### Transform response object to JSON

You can use `to_json()` method on the model to get a raw JSON string of the model.

```python
print(usersApi.get_users_me().to_json())
```

### Force JSON Null value in API request body's attribute

Some methods require a body content (i.e. a model) as input parameter (*e.g. usersApi.post_users(body), usersApi.patch_user(userid, body)*).

When the method is invoked, the SDK will automatically serialize the model (the *body* input parameter) to a JSON content (the API request's body).  
*Note: With Python, `None` value is serialized into JSON `null`.*

Before issuing the request to Genesys Cloud, the SDK will **strip out** all attributes with a JSON `null` value (i.e. model properties with a value set to `None` are ignored).  
Except for a few cases, this is what is expected by the Genesys Cloud platform.

Indeed, there are couple of API endpoints, where JSON `null` value is used to reset a property.
e.g. with *PATCH /api/v2/taskmanagement/worktypes/{worktypeId}* (*patch_taskmanagement_worktype(worktype_id, body)*), *defaultQueueId* can be set to null in order to reset this worktype's property.

This is why we introduce a new singleton class - *ApiNullValue()* - which will allow overriding the SDK's default behavior.  
A model property set to `PureCloudPlatformClientV2.ApiNullValue()`, instead of `None`, will be kept and serialized to JSON as `null`.

```python
task_api = PureCloudPlatformClientV2.TaskManagementApi()
worktype_update = PureCloudPlatformClientV2.WorktypeUpdate()
worktype_update.name = 'abcd'
worktype_update.default_queue_id = PureCloudPlatformClientV2.ApiNullValue()
...
task_api.patch_taskmanagement_worktype(worktype_id, worktype_update)
```

### Managing updates in Platform API Enumerations

The Platform API Client SDKs (Java, Javascript/NodeJs, Python, Go, .Net, iOS/Swift) are automatically generated using the Platform API OpenAPI v2 definition.
The Platform API definition file is downloaded at the time of the SDK build and is used to generate operations (i.e. API methods) and definitions (i.e. classes for the different models, enumerations, ...) in the different SDK languages.

The Python Platform API Client SDK implements the following strategy to manage the introduction of new enumeration values in the Platform API (i.e. in a version of the SDK which doesn't include these changes):
* If an unknown enumeration value is received (i.e. a new enumeration value, introduced in Platform API, after the SDK version you are using was built), the SDK will map it to a `outdated_sdk_version` string value. This is to prevent errors during deserialization when an unknown enumeration value is received from Genesys Cloud.

## Inject Custom HTTP Client
By default, the SDK uses the urllib3 library as the default HTTP client. If you want to inject a new third-party/custom implementation of the client, you can set the HTTP client instance.

The CustomHttpClient should be a class that inherits from AbstractHttpClient defined in the SDK and implements the request method. Here's an example:

```python
from PureCloudPlatformClientV2 import AbstractHttpClient
import requests

class CustomHttpClient(AbstractHttpClient):
    def __init__(self):
        super().__init__()
        self._session = requests.Session()

    def request(self, options):
        return self._session.request(**options)

# Initialize the API client
api_client = PureCloudPlatformClientV2.api_client.ApiClient()

# Create and set custom HTTP client
http_client = CustomHttpClient()
api_client.set_http_client(http_client)
```

## Using MTLS authentication via a Gateway
With Python Client applications, if there is MTLS authentication that need to be set for a gateway server (i.e. if the Genesys Cloud requests must be sent through an intermediate API gateway or equivalent, with MTLS enabled), you can use set_mtls_certificates or set_mtls_contents to set the certificates.

An example using set_mtls_certificates to setup MTLS for gateway is shown below

```python
MTLS_CERT_DIR = "mtls-certs"
CA_CERT_FILENAME = "ca-chain.cert.pem"
CLIENT_CERT_FILENAME = "localhost.cert.pem"
CLIENT_KEY_FILENAME = "localhost.key.pem"
base_dir = os.path.dirname(__file__)
ca_cert_path = os.path.join(base_dir, MTLS_CERT_DIR, CA_CERT_FILENAME)
client_cert_path = os.path.join(base_dir, MTLS_CERT_DIR, CLIENT_CERT_FILENAME)
client_key_path = os.path.join(base_dir, MTLS_CERT_DIR, CLIENT_KEY_FILENAME)
PureCloudPlatformClientV2.configuration.set_mtls_certificates(client_cert_path, client_key_path, ca_cert_path)

apiclient_mtls = PureCloudPlatformClientV2.api_client.ApiClient()
apiclient_mtls.set_gateway(
    hostname="mygateway.mydomain.myextension",
    scheme="https",
    port=4027,
    login_path="login",
    api_path="api"
)
```


If you have content of the private keys and cert information instead of the the filepaths , you can directly set this information using set_mtls_contents

An example using set_mtls_contents to setup MTLS for gateway is shown below

```python
PureCloudPlatformClientV2.configuration.set_mtls_contents(client_cert_conts, client_key_conts, ca_cert_conts) # make sure that the content of the certificate and key have been feteched properly and supplied to set_mtls_contents() function.

apiclient_mtls = PureCloudPlatformClientV2.api_client.ApiClient()
apiclient_mtls.set_gateway(
    hostname="mygateway.mydomain.myextension",
    scheme="https",
    port=4027,
    login_path="login",
    api_path="api"
)
```



If you require a custom HTTP client to handle mTLS, you can utilize the set_http_client() method of the API client instance to integrate your own implementation. Remember that you will be responsible for configuring the mTLS settings within your custom HTTP client.

### Using Pre Commit and Post Commit Hooks

For any custom requirements like pre validations or post cleanups (for ex: OCSP and CRL validation), we can inject the prehook and posthook functions.
The SDK's default client will make sure the injected hook functions are executed.

```python
def pre_hook(http_request_options):
    try:
        print('Running PreHook: Certificate Validation Checks')

        // Custom validation logic here

        print('Certificate Validation Complete')
    except:
        raise Exception('Error in prehook validation')

apiclient = PureCloudPlatformClientV2.api_client.ApiClient()
http_client = apiclient.get_http_client()

http_client.set_pre_request_hook(pre_hook)
```


## SDK Source Code Generation

The SDK is automatically regenerated and published from the API's definition after each API release. For more information on the build process, see the [platform-client-sdk-common](https://github.com/MyPureCloud/platform-client-sdk-common) project.

## Versioning

The SDK's version is incremented according to the [Semantic Versioning Specification](https://semver.org/). The decision to increment version numbers is determined by [diffing the Platform API's swagger](https://github.com/purecloudlabs/platform-client-sdk-common/blob/master/modules/swaggerDiff.js) for automated builds, and optionally forcing a version bump when a build is triggered manually (e.g. releasing a bugfix).

## Support

This package is intended to be forwards compatible with v2 of Genesys Cloud's Platform API. While the general policy for the API is not to introduce breaking changes, there are certain additions and changes to the API that cause breaking changes for the SDK, often due to the way the API is expressed in its swagger definition. Because of this, the SDK can have a major version bump while the API remains at major version 2. While the SDK is intended to be forward compatible, patches will only be released to the latest version. For these reasons, it is strongly recommended that all applications using this SDK are kept up to date and use the latest version of the SDK.

For any issues, questions, or suggestions for the SDK, visit the [Genesys Cloud Developer Community](https://community.genesys.com/communities/community-home1/digestviewer?CommunityKey=a39cc4d6-857e-43cb-be7b-019581ab9f38).
