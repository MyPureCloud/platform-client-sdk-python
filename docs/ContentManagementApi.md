# ContentManagementApi

## PureCloudPlatformClientV2.ContentManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_contentmanagement_document**](#delete_contentmanagement_document) | Delete a document.|
|[**delete_contentmanagement_share**](#delete_contentmanagement_share) | Deletes an existing share.|
|[**delete_contentmanagement_status_status_id**](#delete_contentmanagement_status_status_id) | Cancel the command for this status|
|[**delete_contentmanagement_workspace**](#delete_contentmanagement_workspace) | Delete a workspace|
|[**delete_contentmanagement_workspace_member**](#delete_contentmanagement_workspace_member) | Delete a member from a workspace|
|[**delete_contentmanagement_workspace_tagvalue**](#delete_contentmanagement_workspace_tagvalue) | Delete workspace tag|
|[**get_contentmanagement_document**](#get_contentmanagement_document) | Get a document.|
|[**get_contentmanagement_document_content**](#get_contentmanagement_document_content) | Download a document.|
|[**get_contentmanagement_documents**](#get_contentmanagement_documents) | Get a list of documents.|
|[**get_contentmanagement_query**](#get_contentmanagement_query) | Query content|
|[**get_contentmanagement_securityprofile**](#get_contentmanagement_securityprofile) | Get a Security Profile|
|[**get_contentmanagement_securityprofiles**](#get_contentmanagement_securityprofiles) | Get a List of Security Profiles|
|[**get_contentmanagement_share**](#get_contentmanagement_share) | Retrieve details about an existing share.|
|[**get_contentmanagement_shared_shared_id**](#get_contentmanagement_shared_shared_id) | Get shared documents. Securely download a shared document.|
|[**get_contentmanagement_shares**](#get_contentmanagement_shares) | Gets a list of shares.  You must specify at least one filter (e.g. entityId).|
|[**get_contentmanagement_status**](#get_contentmanagement_status) | Get a list of statuses for pending operations|
|[**get_contentmanagement_status_status_id**](#get_contentmanagement_status_status_id) | Get a status.|
|[**get_contentmanagement_usage**](#get_contentmanagement_usage) | Get usage details.|
|[**get_contentmanagement_workspace**](#get_contentmanagement_workspace) | Get a workspace.|
|[**get_contentmanagement_workspace_documents**](#get_contentmanagement_workspace_documents) | Get a list of documents.|
|[**get_contentmanagement_workspace_member**](#get_contentmanagement_workspace_member) | Get a workspace member|
|[**get_contentmanagement_workspace_members**](#get_contentmanagement_workspace_members) | Get a list workspace members|
|[**get_contentmanagement_workspace_tagvalue**](#get_contentmanagement_workspace_tagvalue) | Get a workspace tag|
|[**get_contentmanagement_workspace_tagvalues**](#get_contentmanagement_workspace_tagvalues) | Get a list of workspace tags|
|[**get_contentmanagement_workspaces**](#get_contentmanagement_workspaces) | Get a list of workspaces.|
|[**post_contentmanagement_document**](#post_contentmanagement_document) | Update a document.|
|[**post_contentmanagement_document_content**](#post_contentmanagement_document_content) | Replace the contents of a document.|
|[**post_contentmanagement_documents**](#post_contentmanagement_documents) | Add a document.|
|[**post_contentmanagement_query**](#post_contentmanagement_query) | Query content|
|[**post_contentmanagement_shares**](#post_contentmanagement_shares) | Creates a new share or updates an existing share if the entity has already been shared|
|[**post_contentmanagement_workspace_tagvalues**](#post_contentmanagement_workspace_tagvalues) | Create a workspace tag|
|[**post_contentmanagement_workspace_tagvalues_query**](#post_contentmanagement_workspace_tagvalues_query) | Perform a prefix query on tags in the workspace|
|[**post_contentmanagement_workspaces**](#post_contentmanagement_workspaces) | Create a group workspace|
|[**put_contentmanagement_workspace**](#put_contentmanagement_workspace) | Update a workspace|
|[**put_contentmanagement_workspace_member**](#put_contentmanagement_workspace_member) | Add a member to a workspace|
|[**put_contentmanagement_workspace_tagvalue**](#put_contentmanagement_workspace_tagvalue) | Update a workspace tag. Will update all documents with the new tag value.|



## delete_contentmanagement_document

>  delete_contentmanagement_document(document_id, override=override)


Delete a document.

Wraps DELETE /api/v2/contentmanagement/documents/{documentId} 

Requires ANY permissions: 

* content_management_user

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
document_id = 'document_id_example' # str | Document ID
override = True # bool | Override any lock on the document (optional)

try:
    # Delete a document.
    api_instance.delete_contentmanagement_document(document_id, override=override)
except ApiException as e:
    print("Exception when calling ContentManagementApi->delete_contentmanagement_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **override** | **bool**| Override any lock on the document | [optional]  |

### Return type

void (empty response body)


## delete_contentmanagement_share

>  delete_contentmanagement_share(share_id)


Deletes an existing share.

This revokes sharing rights specified in the share record

Wraps DELETE /api/v2/contentmanagement/shares/{shareId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
share_id = 'share_id_example' # str | Share ID

try:
    # Deletes an existing share.
    api_instance.delete_contentmanagement_share(share_id)
except ApiException as e:
    print("Exception when calling ContentManagementApi->delete_contentmanagement_share: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **share_id** | **str**| Share ID |  |

### Return type

void (empty response body)


## delete_contentmanagement_status_status_id

>  delete_contentmanagement_status_status_id(status_id)


Cancel the command for this status

Wraps DELETE /api/v2/contentmanagement/status/{statusId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
status_id = 'status_id_example' # str | Status ID

try:
    # Cancel the command for this status
    api_instance.delete_contentmanagement_status_status_id(status_id)
except ApiException as e:
    print("Exception when calling ContentManagementApi->delete_contentmanagement_status_status_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **status_id** | **str**| Status ID |  |

### Return type

void (empty response body)


## delete_contentmanagement_workspace

>  delete_contentmanagement_workspace(workspace_id, move_children_to_workspace_id=move_children_to_workspace_id)


Delete a workspace

Wraps DELETE /api/v2/contentmanagement/workspaces/{workspaceId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
move_children_to_workspace_id = 'move_children_to_workspace_id_example' # str | New location for objects in deleted workspace. (optional)

try:
    # Delete a workspace
    api_instance.delete_contentmanagement_workspace(workspace_id, move_children_to_workspace_id=move_children_to_workspace_id)
except ApiException as e:
    print("Exception when calling ContentManagementApi->delete_contentmanagement_workspace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **move_children_to_workspace_id** | **str**| New location for objects in deleted workspace. | [optional]  |

### Return type

void (empty response body)


## delete_contentmanagement_workspace_member

>  delete_contentmanagement_workspace_member(workspace_id, member_id)


Delete a member from a workspace

Wraps DELETE /api/v2/contentmanagement/workspaces/{workspaceId}/members/{memberId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
member_id = 'member_id_example' # str | Member ID

try:
    # Delete a member from a workspace
    api_instance.delete_contentmanagement_workspace_member(workspace_id, member_id)
except ApiException as e:
    print("Exception when calling ContentManagementApi->delete_contentmanagement_workspace_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **member_id** | **str**| Member ID |  |

### Return type

void (empty response body)


## delete_contentmanagement_workspace_tagvalue

>  delete_contentmanagement_workspace_tagvalue(workspace_id, tag_id)


Delete workspace tag

Delete a tag from a workspace. Will remove this tag from all documents.

Wraps DELETE /api/v2/contentmanagement/workspaces/{workspaceId}/tagvalues/{tagId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
tag_id = 'tag_id_example' # str | Tag ID

try:
    # Delete workspace tag
    api_instance.delete_contentmanagement_workspace_tagvalue(workspace_id, tag_id)
except ApiException as e:
    print("Exception when calling ContentManagementApi->delete_contentmanagement_workspace_tagvalue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **tag_id** | **str**| Tag ID |  |

### Return type

void (empty response body)


## get_contentmanagement_document

> [**Document**](Document) get_contentmanagement_document(document_id, expand=expand)


Get a document.

Wraps GET /api/v2/contentmanagement/documents/{documentId} 

Requires ANY permissions: 

* content_management_user

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
document_id = 'document_id_example' # str | Document ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a document.
    api_response = api_instance.get_contentmanagement_document(document_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: lockInfo, acl, workspace |

### Return type

[**Document**](Document)


## get_contentmanagement_document_content

> [**DownloadResponse**](DownloadResponse) get_contentmanagement_document_content(document_id, disposition=disposition, content_type=content_type)


Download a document.

Wraps GET /api/v2/contentmanagement/documents/{documentId}/content 

Requires ANY permissions: 

* content_management_user

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
document_id = 'document_id_example' # str | Document ID
disposition = 'disposition_example' # str | Request how the content will be downloaded: a file attachment or inline. Default is attachment. (optional)
content_type = 'content_type_example' # str | The requested format for the specified document. If supported, the document will be returned in that format. Example contentType=audio/wav (optional)

try:
    # Download a document.
    api_response = api_instance.get_contentmanagement_document_content(document_id, disposition=disposition, content_type=content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_document_content: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **disposition** | **str**| Request how the content will be downloaded: a file attachment or inline. Default is attachment. | [optional] <br />**Values**: attachment, inline |
| **content_type** | **str**| The requested format for the specified document. If supported, the document will be returned in that format. Example contentType&#x3D;audio/wav | [optional]  |

### Return type

[**DownloadResponse**](DownloadResponse)


## get_contentmanagement_documents

> [**DocumentEntityListing**](DocumentEntityListing) get_contentmanagement_documents(workspace_id, name=name, expand=expand, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get a list of documents.

Wraps GET /api/v2/contentmanagement/documents 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
name = 'name_example' # str | Name (optional)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'sort_by_example' # str | name or dateCreated (optional)
sort_order = ''ascending'' # str | ascending or descending (optional) (default to 'ascending')

try:
    # Get a list of documents.
    api_response = api_instance.get_contentmanagement_documents(workspace_id, name=name, expand=expand, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **name** | **str**| Name | [optional]  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: acl, workspace |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| name or dateCreated | [optional]  |
| **sort_order** | **str**| ascending or descending | [optional] [default to &#39;ascending&#39;] |

### Return type

[**DocumentEntityListing**](DocumentEntityListing)


## get_contentmanagement_query

> [**QueryResults**](QueryResults) get_contentmanagement_query(query_phrase, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, expand=expand)


Query content

Wraps GET /api/v2/contentmanagement/query 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
query_phrase = 'query_phrase_example' # str | Phrase tokens are ANDed together over all searchable fields
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''name'' # str | name or dateCreated (optional) (default to 'name')
sort_order = ''ascending'' # str | ascending or descending (optional) (default to 'ascending')
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Query content
    api_response = api_instance.get_contentmanagement_query(query_phrase, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **query_phrase** | **str**| Phrase tokens are ANDed together over all searchable fields |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| name or dateCreated | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| ascending or descending | [optional] [default to &#39;ascending&#39;] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: acl, workspace |

### Return type

[**QueryResults**](QueryResults)


## get_contentmanagement_securityprofile

> [**SecurityProfile**](SecurityProfile) get_contentmanagement_securityprofile(security_profile_id)


Get a Security Profile

Wraps GET /api/v2/contentmanagement/securityprofiles/{securityProfileId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
security_profile_id = 'security_profile_id_example' # str | Security Profile Id

try:
    # Get a Security Profile
    api_response = api_instance.get_contentmanagement_securityprofile(security_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_securityprofile: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **security_profile_id** | **str**| Security Profile Id |  |

### Return type

[**SecurityProfile**](SecurityProfile)


## get_contentmanagement_securityprofiles

> [**SecurityProfileEntityListing**](SecurityProfileEntityListing) get_contentmanagement_securityprofiles()


Get a List of Security Profiles

Wraps GET /api/v2/contentmanagement/securityprofiles 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()

try:
    # Get a List of Security Profiles
    api_response = api_instance.get_contentmanagement_securityprofiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_securityprofiles: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SecurityProfileEntityListing**](SecurityProfileEntityListing)


## get_contentmanagement_share

> [**Share**](Share) get_contentmanagement_share(share_id, expand=expand)


Retrieve details about an existing share.

Wraps GET /api/v2/contentmanagement/shares/{shareId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
share_id = 'share_id_example' # str | Share ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Retrieve details about an existing share.
    api_response = api_instance.get_contentmanagement_share(share_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_share: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **share_id** | **str**| Share ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: member |

### Return type

[**Share**](Share)


## get_contentmanagement_shared_shared_id

> [**SharedResponse**](SharedResponse) get_contentmanagement_shared_shared_id(shared_id, disposition=disposition, content_type=content_type, expand=expand)


Get shared documents. Securely download a shared document.

This method requires the download sharing URI obtained in the get document response (downloadSharingUri). Documents may be shared between users in the same workspace. Documents may also be shared between any user by creating a content management share.

Wraps GET /api/v2/contentmanagement/shared/{sharedId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
shared_id = 'shared_id_example' # str | Shared ID
disposition = ''attachment'' # str | Request how the share content will be downloaded: attached as a file or inline. Default is attachment. (optional) (default to 'attachment')
content_type = 'content_type_example' # str | The requested format for the specified document. If supported, the document will be returned in that format. Example contentType=audio/wav (optional)
expand = 'expand_example' # str | Expand some document fields (optional)

try:
    # Get shared documents. Securely download a shared document.
    api_response = api_instance.get_contentmanagement_shared_shared_id(shared_id, disposition=disposition, content_type=content_type, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_shared_shared_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **shared_id** | **str**| Shared ID |  |
| **disposition** | **str**| Request how the share content will be downloaded: attached as a file or inline. Default is attachment. | [optional] [default to &#39;attachment&#39;]<br />**Values**: attachment, inline, none |
| **content_type** | **str**| The requested format for the specified document. If supported, the document will be returned in that format. Example contentType&#x3D;audio/wav | [optional]  |
| **expand** | **str**| Expand some document fields | [optional] <br />**Values**: document.acl |

### Return type

[**SharedResponse**](SharedResponse)


## get_contentmanagement_shares

> [**ShareEntityListing**](ShareEntityListing) get_contentmanagement_shares(entity_id=entity_id, expand=expand, page_size=page_size, page_number=page_number)


Gets a list of shares.  You must specify at least one filter (e.g. entityId).

Failing to specify a filter will return 400.

Wraps GET /api/v2/contentmanagement/shares 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
entity_id = 'entity_id_example' # str | Filters the shares returned to only the entity specified by the value of this parameter. (optional)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Gets a list of shares.  You must specify at least one filter (e.g. entityId).
    api_response = api_instance.get_contentmanagement_shares(entity_id=entity_id, expand=expand, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_shares: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **entity_id** | **str**| Filters the shares returned to only the entity specified by the value of this parameter. | [optional]  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: member |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**ShareEntityListing**](ShareEntityListing)


## get_contentmanagement_status

> [**CommandStatusEntityListing**](CommandStatusEntityListing) get_contentmanagement_status(page_size=page_size, page_number=page_number)


Get a list of statuses for pending operations

Wraps GET /api/v2/contentmanagement/status 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of statuses for pending operations
    api_response = api_instance.get_contentmanagement_status(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**CommandStatusEntityListing**](CommandStatusEntityListing)


## get_contentmanagement_status_status_id

> [**CommandStatus**](CommandStatus) get_contentmanagement_status_status_id(status_id)


Get a status.

Wraps GET /api/v2/contentmanagement/status/{statusId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
status_id = 'status_id_example' # str | Status ID

try:
    # Get a status.
    api_response = api_instance.get_contentmanagement_status_status_id(status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_status_status_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **status_id** | **str**| Status ID |  |

### Return type

[**CommandStatus**](CommandStatus)


## get_contentmanagement_usage

> [**Usage**](Usage) get_contentmanagement_usage()


Get usage details.

Wraps GET /api/v2/contentmanagement/usage 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()

try:
    # Get usage details.
    api_response = api_instance.get_contentmanagement_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_usage: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**Usage**](Usage)


## get_contentmanagement_workspace

> [**Workspace**](Workspace) get_contentmanagement_workspace(workspace_id, expand=expand)


Get a workspace.

Wraps GET /api/v2/contentmanagement/workspaces/{workspaceId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a workspace.
    api_response = api_instance.get_contentmanagement_workspace(workspace_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: summary, acl |

### Return type

[**Workspace**](Workspace)


## get_contentmanagement_workspace_documents

> [**DocumentEntityListing**](DocumentEntityListing) get_contentmanagement_workspace_documents(workspace_id, expand=expand, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)


Get a list of documents.

Wraps GET /api/v2/contentmanagement/workspaces/{workspaceId}/documents 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'sort_by_example' # str | name or dateCreated (optional)
sort_order = ''ascending'' # str | ascending or descending (optional) (default to 'ascending')

try:
    # Get a list of documents.
    api_response = api_instance.get_contentmanagement_workspace_documents(workspace_id, expand=expand, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspace_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: acl, workspace |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| name or dateCreated | [optional]  |
| **sort_order** | **str**| ascending or descending | [optional] [default to &#39;ascending&#39;] |

### Return type

[**DocumentEntityListing**](DocumentEntityListing)


## get_contentmanagement_workspace_member

> [**WorkspaceMember**](WorkspaceMember) get_contentmanagement_workspace_member(workspace_id, member_id, expand=expand)


Get a workspace member

Wraps GET /api/v2/contentmanagement/workspaces/{workspaceId}/members/{memberId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
member_id = 'member_id_example' # str | Member ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a workspace member
    api_response = api_instance.get_contentmanagement_workspace_member(workspace_id, member_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspace_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **member_id** | **str**| Member ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: member |

### Return type

[**WorkspaceMember**](WorkspaceMember)


## get_contentmanagement_workspace_members

> [**WorkspaceMemberEntityListing**](WorkspaceMemberEntityListing) get_contentmanagement_workspace_members(workspace_id, page_size=page_size, page_number=page_number, expand=expand)


Get a list workspace members

Wraps GET /api/v2/contentmanagement/workspaces/{workspaceId}/members 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a list workspace members
    api_response = api_instance.get_contentmanagement_workspace_members(workspace_id, page_size=page_size, page_number=page_number, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspace_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: member |

### Return type

[**WorkspaceMemberEntityListing**](WorkspaceMemberEntityListing)


## get_contentmanagement_workspace_tagvalue

> [**TagValue**](TagValue) get_contentmanagement_workspace_tagvalue(workspace_id, tag_id, expand=expand)


Get a workspace tag

Wraps GET /api/v2/contentmanagement/workspaces/{workspaceId}/tagvalues/{tagId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
tag_id = 'tag_id_example' # str | Tag ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a workspace tag
    api_response = api_instance.get_contentmanagement_workspace_tagvalue(workspace_id, tag_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspace_tagvalue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **tag_id** | **str**| Tag ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: acl |

### Return type

[**TagValue**](TagValue)


## get_contentmanagement_workspace_tagvalues

> [**TagValueEntityListing**](TagValueEntityListing) get_contentmanagement_workspace_tagvalues(workspace_id, value=value, page_size=page_size, page_number=page_number, expand=expand)


Get a list of workspace tags

Wraps GET /api/v2/contentmanagement/workspaces/{workspaceId}/tagvalues 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
value = 'value_example' # str | filter the list of tags returned (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a list of workspace tags
    api_response = api_instance.get_contentmanagement_workspace_tagvalues(workspace_id, value=value, page_size=page_size, page_number=page_number, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspace_tagvalues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **value** | **str**| filter the list of tags returned | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: acl |

### Return type

[**TagValueEntityListing**](TagValueEntityListing)


## get_contentmanagement_workspaces

> [**WorkspaceEntityListing**](WorkspaceEntityListing) get_contentmanagement_workspaces(page_size=page_size, page_number=page_number, access=access, expand=expand)


Get a list of workspaces.

Specifying 'content' access will return all workspaces the user has document access to, while 'admin' access will return all group workspaces the user has administrative rights to.

Wraps GET /api/v2/contentmanagement/workspaces 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
access = ['access_example'] # list[str] | Requested access level. (optional)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a list of workspaces.
    api_response = api_instance.get_contentmanagement_workspaces(page_size=page_size, page_number=page_number, access=access, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->get_contentmanagement_workspaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **access** | [**list[str]**](str)| Requested access level. | [optional] <br />**Values**: content, admin, document:create, document:viewContent, document:viewMetadata, document:download, document:delete, document:update, document:share, document:shareView, document:email, document:print, document:auditView, document:replace, document:tag, tag:create, tag:view, tag:update, tag:apply, tag:remove, tag:delete |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: summary, acl |

### Return type

[**WorkspaceEntityListing**](WorkspaceEntityListing)


## post_contentmanagement_document

> [**Document**](Document) post_contentmanagement_document(document_id, body, expand=expand, override=override)


Update a document.

Wraps POST /api/v2/contentmanagement/documents/{documentId} 

Requires ANY permissions: 

* content_management_user

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
document_id = 'document_id_example' # str | Document ID
body = PureCloudPlatformClientV2.DocumentUpdate() # DocumentUpdate | Document
expand = 'expand_example' # str | Expand some document fields (optional)
override = True # bool | Override any lock on the document (optional)

try:
    # Update a document.
    api_response = api_instance.post_contentmanagement_document(document_id, body, expand=expand, override=override)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **body** | [**DocumentUpdate**](DocumentUpdate)| Document |  |
| **expand** | **str**| Expand some document fields | [optional] <br />**Values**: acl |
| **override** | **bool**| Override any lock on the document | [optional]  |

### Return type

[**Document**](Document)


## post_contentmanagement_document_content

> [**ReplaceResponse**](ReplaceResponse) post_contentmanagement_document_content(document_id, body, override=override)


Replace the contents of a document.

Wraps POST /api/v2/contentmanagement/documents/{documentId}/content 

Requires ANY permissions: 

* content_management_user

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
document_id = 'document_id_example' # str | Document ID
body = PureCloudPlatformClientV2.ReplaceRequest() # ReplaceRequest | Replace Request
override = True # bool | Override any lock on the document (optional)

try:
    # Replace the contents of a document.
    api_response = api_instance.post_contentmanagement_document_content(document_id, body, override=override)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_document_content: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **body** | [**ReplaceRequest**](ReplaceRequest)| Replace Request |  |
| **override** | **bool**| Override any lock on the document | [optional]  |

### Return type

[**ReplaceResponse**](ReplaceResponse)


## post_contentmanagement_documents

> [**Document**](Document) post_contentmanagement_documents(body, copy_source=copy_source, move_source=move_source, override=override)


Add a document.

Wraps POST /api/v2/contentmanagement/documents 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
body = PureCloudPlatformClientV2.DocumentUpload() # DocumentUpload | Document
copy_source = 'copy_source_example' # str | Copy a document within a workspace or to a new workspace. Provide a document ID as the copy source. (optional)
move_source = 'move_source_example' # str | Move a document to a new workspace. Provide a document ID as the move source. (optional)
override = True # bool | Override any lock on the source document (optional)

try:
    # Add a document.
    api_response = api_instance.post_contentmanagement_documents(body, copy_source=copy_source, move_source=move_source, override=override)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DocumentUpload**](DocumentUpload)| Document |  |
| **copy_source** | **str**| Copy a document within a workspace or to a new workspace. Provide a document ID as the copy source. | [optional]  |
| **move_source** | **str**| Move a document to a new workspace. Provide a document ID as the move source. | [optional]  |
| **override** | **bool**| Override any lock on the source document | [optional]  |

### Return type

[**Document**](Document)


## post_contentmanagement_query

> [**QueryResults**](QueryResults) post_contentmanagement_query(body, expand=expand)


Query content

Wraps POST /api/v2/contentmanagement/query 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
body = PureCloudPlatformClientV2.QueryRequest() # QueryRequest | Allows for a filtered query returning facet information
expand = 'expand_example' # str | Expand some document fields (optional)

try:
    # Query content
    api_response = api_instance.post_contentmanagement_query(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**QueryRequest**](QueryRequest)| Allows for a filtered query returning facet information |  |
| **expand** | **str**| Expand some document fields | [optional] <br />**Values**: acl, workspace |

### Return type

[**QueryResults**](QueryResults)


## post_contentmanagement_shares

> [**CreateShareResponse**](CreateShareResponse) post_contentmanagement_shares(body)


Creates a new share or updates an existing share if the entity has already been shared

Wraps POST /api/v2/contentmanagement/shares 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
body = PureCloudPlatformClientV2.CreateShareRequest() # CreateShareRequest | CreateShareRequest - entity id and type and a single member or list of members are required

try:
    # Creates a new share or updates an existing share if the entity has already been shared
    api_response = api_instance.post_contentmanagement_shares(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_shares: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateShareRequest**](CreateShareRequest)| CreateShareRequest - entity id and type and a single member or list of members are required |  |

### Return type

[**CreateShareResponse**](CreateShareResponse)


## post_contentmanagement_workspace_tagvalues

> [**TagValue**](TagValue) post_contentmanagement_workspace_tagvalues(workspace_id, body)


Create a workspace tag

Wraps POST /api/v2/contentmanagement/workspaces/{workspaceId}/tagvalues 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
body = PureCloudPlatformClientV2.TagValue() # TagValue | tag

try:
    # Create a workspace tag
    api_response = api_instance.post_contentmanagement_workspace_tagvalues(workspace_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_workspace_tagvalues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **body** | [**TagValue**](TagValue)| tag |  |

### Return type

[**TagValue**](TagValue)


## post_contentmanagement_workspace_tagvalues_query

> [**TagValueEntityListing**](TagValueEntityListing) post_contentmanagement_workspace_tagvalues_query(workspace_id, body, expand=expand)


Perform a prefix query on tags in the workspace

Wraps POST /api/v2/contentmanagement/workspaces/{workspaceId}/tagvalues/query 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
body = PureCloudPlatformClientV2.TagQueryRequest() # TagQueryRequest | query
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Perform a prefix query on tags in the workspace
    api_response = api_instance.post_contentmanagement_workspace_tagvalues_query(workspace_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_workspace_tagvalues_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **body** | [**TagQueryRequest**](TagQueryRequest)| query |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: acl |

### Return type

[**TagValueEntityListing**](TagValueEntityListing)


## post_contentmanagement_workspaces

> [**Workspace**](Workspace) post_contentmanagement_workspaces(body)


Create a group workspace

Wraps POST /api/v2/contentmanagement/workspaces 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
body = PureCloudPlatformClientV2.WorkspaceCreate() # WorkspaceCreate | Workspace

try:
    # Create a group workspace
    api_response = api_instance.post_contentmanagement_workspaces(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->post_contentmanagement_workspaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkspaceCreate**](WorkspaceCreate)| Workspace |  |

### Return type

[**Workspace**](Workspace)


## put_contentmanagement_workspace

> [**Workspace**](Workspace) put_contentmanagement_workspace(workspace_id, body)


Update a workspace

Wraps PUT /api/v2/contentmanagement/workspaces/{workspaceId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
body = PureCloudPlatformClientV2.Workspace() # Workspace | Workspace

try:
    # Update a workspace
    api_response = api_instance.put_contentmanagement_workspace(workspace_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->put_contentmanagement_workspace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **body** | [**Workspace**](Workspace)| Workspace |  |

### Return type

[**Workspace**](Workspace)


## put_contentmanagement_workspace_member

> [**WorkspaceMember**](WorkspaceMember) put_contentmanagement_workspace_member(workspace_id, member_id, body)


Add a member to a workspace

Wraps PUT /api/v2/contentmanagement/workspaces/{workspaceId}/members/{memberId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
member_id = 'member_id_example' # str | Member ID
body = PureCloudPlatformClientV2.WorkspaceMember() # WorkspaceMember | Workspace Member

try:
    # Add a member to a workspace
    api_response = api_instance.put_contentmanagement_workspace_member(workspace_id, member_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->put_contentmanagement_workspace_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **member_id** | **str**| Member ID |  |
| **body** | [**WorkspaceMember**](WorkspaceMember)| Workspace Member |  |

### Return type

[**WorkspaceMember**](WorkspaceMember)


## put_contentmanagement_workspace_tagvalue

> [**TagValue**](TagValue) put_contentmanagement_workspace_tagvalue(workspace_id, tag_id, body)


Update a workspace tag. Will update all documents with the new tag value.

Wraps PUT /api/v2/contentmanagement/workspaces/{workspaceId}/tagvalues/{tagId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ContentManagementApi()
workspace_id = 'workspace_id_example' # str | Workspace ID
tag_id = 'tag_id_example' # str | Tag ID
body = PureCloudPlatformClientV2.TagValue() # TagValue | Workspace

try:
    # Update a workspace tag. Will update all documents with the new tag value.
    api_response = api_instance.put_contentmanagement_workspace_tagvalue(workspace_id, tag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentManagementApi->put_contentmanagement_workspace_tagvalue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workspace_id** | **str**| Workspace ID |  |
| **tag_id** | **str**| Tag ID |  |
| **body** | [**TagValue**](TagValue)| Workspace |  |

### Return type

[**TagValue**](TagValue)


_PureCloudPlatformClientV2 233.0.0_
