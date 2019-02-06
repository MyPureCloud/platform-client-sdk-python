---
title: PureCloud API SDK - Python
---

[![PyPI version](https://badge.fury.io/py/PureCloudPlatformClientV2.svg)](https://badge.fury.io/py/PureCloudPlatformClientV2)

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

The Python SDK does not currently contain helper methods to complete an OAuth flow. The consuming applicaiton must complete an OAuth flow to get an access token outside the scope of the SDK. Once an access token is obtained, it should be set on the SDK via `PureCloudPlatformClientV2.configuration.access_token`. For more information about authenticating with OAuth, see the Developer Center article [Authorization](https://developer.mypurecloud.com/api/rest/authorization/index.html).

```{"language":"python"}
PureCloudPlatformClientV2.configuration.access_token = 'cuQbSAf1LU4CuIaSj1D6Gm399jmTr7zLTTc3KPSyCvEyJQIo9r648h3SH8oFzLPPKxE3Mvb166lq5NcjSBoGE5A'
```

### Setting the Environment

If connecting to a PureCloud environment other than mypurecloud.com (e.g. mypurecloud.ie), set the new base path before constructing any API classes. The new base path should be the base path to the Platform API for your environment.

```{"language":"python"}
PureCloudPlatformClientV2.configuration.host = 'https://api.mypurecloud.ie'
```

### Making Requests

There are two steps to making requests:

1. Instantiate one of the API classes in the ININ.PureCloudApi.Api namespace
2. Call the methods on the API object

Example of getting the authenticated user's information:

```{"language":"python"}
usersApi = PureCloudPlatformClientV2.UsersApi()
print usersApi.get_users_me()
```

## SDK Source Code Generation

The SDK is automatically regenerated and published from the API's definition after each API release. For more information on the build process, see the [platform-client-sdk-common](https://github.com/MyPureCloud/platform-client-sdk-common) project.


## Versioning

The SDK's version is incremented according to the [Semantic Versioning Specification](https://semver.org/). The decision to increment version numbers is determined by [diffing the Platform API's swagger](https://github.com/purecloudlabs/platform-client-sdk-common/blob/master/modules/swaggerDiff.js) for automated builds, and optionally forcing a version bump when a build is triggered manually (e.g. releasing a bugfix).


## Support

This package is intended to be forwards compatible with v2 of PureCloud's Platform API. While the general policy for the API is not to introduce breaking changes, there are certain additions and changes to the API that cause breaking changes for the SDK, often due to the way the API is expressed in its swagger definition. Because of this, the SDK can have a major version bump while the API remains at major version 2. While the SDK is intended to be forward compatible, patches will only be released to the latest version. For these reasons, it is strongly recommended that all applications using this SDK are kept up to date and use the latest version of the SDK.

For any issues, questions, or suggestions for the SDK, visit the [PureCloud Developer Forum](https://developer.mypurecloud.com/forum/).
