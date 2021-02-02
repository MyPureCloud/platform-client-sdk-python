---
title: Platform API Client SDK - Python
---

[![PyPI version](https://badge.fury.io/py/PureCloudPlatformClientV2.svg)](https://badge.fury.io/py/PureCloudPlatformClientV2)
[![Release Notes Badge](https://developer.mypurecloud.com/images/sdk-release-notes.png)](https://github.com/MyPureCloud/platform-client-sdk-python/blob/master/releaseNotes.md)

Documentation can be found at [https://developer.mypurecloud.com/api/rest/client-libraries/python/](https://developer.mypurecloud.com/api/rest/client-libraries/python/)

## Install Using pip

```{"language":"python"}
pip install PureCloudPlatformClientV2
```

Package info can be found at [https://pypi.python.org/pypi/PureCloudPlatformClientV2](https://pypi.python.org/pypi/PureCloudPlatformClientV2)

## Using the Library

### Referencing the Library

Import the package in the python script:

```{"language":"python"}
import PureCloudPlatformClientV2
```

### Authenticating

#### Client Credentials Grant

**Use when...**

* The app is authenticating as a non-human (e.g. a service, scheduled task, or other non-UI application)

For headless and non-user applications, the [Client Credentials Grant](http://developer.mypurecloud.com/api/rest/authorization/use-client-credentials.html) 

```{"language":"python"}
apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token("7de3af06-c0b3-4f9b-af45-72f4a14037cc", "qLh-825gtjPrIY2kcWKAkmlaSgi6Z1Ws2BAyixWbTrs")
authApi = PureCloudPlatformClientV2.AuthorizationApi(apiclient)
print(authApi.get_authorization_permissions())
```

#### OAuth2 SAML2 Bearer Grant

**Use when...**

* The app is authenticating as a human user, the [OAuth2 SAML2 Bearer](https://developer.mypurecloud.com/api/rest/authorization/use-saml2-bearer.html)

```{"language":"python"}
apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_saml2bearer_token("565c3091-4107-4675-b606-b1fead2d15a4", "9pal483eSr_vCZf0qQomFK298I8htjBZo49FI_lLZQ8", orgName ,encodedsamlassertion)
usersApi = PureCloudPlatformClientV2.UsersApi(apiclient)
print(usersApi.get_users_me())

```

### Authorization Code Grant

* The app is authenticating as a human, the [Authorization Code Grant](https://developer.mypurecloud.com/api/rest/authorization/use-authorization-code.html)
* The app is served via a web server
* There is server-side code that will be making API requests

```{"language":"python"}
apiclient, auth_token_info = apiclient.get_code_authorization_token("565c3091-4107-4675-b606-b1fead2d15a4",
                                                                    "9pal483eSr_vCZf0qQomFK298I8htjBZo49FI_lLZQ8",
                                                                    "fjaXJaIG7Y-gFhgwvxvNZLj-dcqhWS_pm_n-_1MziN8",
                                                                    "https://redirect-uri.com/oauth/callback")
usersApi = PureCloudPlatformClientV2.UsersApi(apiclient)
```

By default the SDK will use the refresh token to request a new access token transparently when it expires. If multiple threads are running 1 thread will request a new token, other threads will wait a maximum of 10 seconds for the token refresh to complete, this time can be overriden with the _refresh_token_wait_time_ field of the _Configuration_ object.  
If you wish to implement the refresh logic, set _should_refresh_access_token_ to false and store the refresh token from the auth response. The expires_in value can be used to proactively request a new one before it expires:

```{"language":"python"}
refresh_token = auth_token_info["refresh_token"]
expires_in = auth_token_info["expires_in"]
PureCloudPlatformClientV2.configuration.should_refresh_access_token = False
```

When the access token expires refresh it using the refresh_code_authorization_token method using the same clientId and clientSecret as used to request it.

```{"language":"python"}
apiclient, auth_token_info = apiclient.refresh_code_authorization_token("565c3091-4107-4675-b606-b1fead2d15a4",
                                                                        "9pal483eSr_vCZf0qQomFK298I8htjBZo49FI_lLZQ8",
                                                                        refresh_token)
```

### Setting the Environment

If connecting to a Genesys Cloud environment other than mypurecloud.com (e.g. mypurecloud.ie), set the new base path before constructing any API classes. The new base path should be the base path to the Platform API for your environment.

```{"language":"python"}
region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_east_1
PureCloudPlatformClientV2.configuration.host = region.get_api_host()
```

### Connect to a Proxy Server

If connecting to a proxy server, set the the address of your proxy server as follows:

```{"language":"python"}
PureCloudPlatformClientV2.configuration.proxy = 'YOUR_PROXY_URL'
```

If your proxy server requires authentication, set the username and password as follows:

```{"language":"python"}
PureCloudPlatformClientV2.configuration.proxy_username = 'YOUR_PROXY_USERNAME'
PureCloudPlatformClientV2.configuration.proxy_password = 'YOUR_PROXY_PASSWORD'
```

The Python SDK uses `urllib3.ProxyManager` to make requests when `proxy` is given.

### Making Requests

There are two steps to making requests:

1. Instantiate one of the API classes in the ININ.PureCloudApi.Api namespace
2. Call the methods on the API object

Example of getting the authenticated user's information:

```{"language":"python"}
usersApi = PureCloudPlatformClientV2.UsersApi()
print(usersApi.get_users_me())
```

### Transform response object to JSON

You can use `to_json()` method on the model to get a raw JSON string of the model.

```{"language":"python"}
print(usersApi.get_users_me().to_json())
```

## SDK Source Code Generation

The SDK is automatically regenerated and published from the API's definition after each API release. For more information on the build process, see the [platform-client-sdk-common](https://github.com/MyPureCloud/platform-client-sdk-common) project.


## Versioning

The SDK's version is incremented according to the [Semantic Versioning Specification](https://semver.org/). The decision to increment version numbers is determined by [diffing the Platform API's swagger](https://github.com/purecloudlabs/platform-client-sdk-common/blob/master/modules/swaggerDiff.js) for automated builds, and optionally forcing a version bump when a build is triggered manually (e.g. releasing a bugfix).


## Support

This package is intended to be forwards compatible with v2 of Genesys Cloud's Platform API. While the general policy for the API is not to introduce breaking changes, there are certain additions and changes to the API that cause breaking changes for the SDK, often due to the way the API is expressed in its swagger definition. Because of this, the SDK can have a major version bump while the API remains at major version 2. While the SDK is intended to be forward compatible, patches will only be released to the latest version. For these reasons, it is strongly recommended that all applications using this SDK are kept up to date and use the latest version of the SDK.

For any issues, questions, or suggestions for the SDK, visit the [Genesys Cloud Developer Forum](https://developer.mypurecloud.com/forum/).
