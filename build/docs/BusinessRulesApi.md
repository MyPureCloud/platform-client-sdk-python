# BusinessRulesApi

## PureCloudPlatformClientV2.BusinessRulesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_businessrules_decisiontable**](#delete_businessrules_decisiontable) | Delete a decision table|
|[**delete_businessrules_decisiontable_version**](#delete_businessrules_decisiontable_version) | Delete a decision table version|
|[**delete_businessrules_decisiontable_version_row**](#delete_businessrules_decisiontable_version_row) | Delete a decision table row|
|[**delete_businessrules_schema**](#delete_businessrules_schema) | Delete a schema|
|[**get_businessrules_decisiontable**](#get_businessrules_decisiontable) | Get a decision table|
|[**get_businessrules_decisiontable_version**](#get_businessrules_decisiontable_version) | Get a decision table version|
|[**get_businessrules_decisiontable_version_row**](#get_businessrules_decisiontable_version_row) | Get a decision table row|
|[**get_businessrules_decisiontable_version_rows**](#get_businessrules_decisiontable_version_rows) | Get a list of decision table rows.|
|[**get_businessrules_decisiontable_versions**](#get_businessrules_decisiontable_versions) | Get a list of decision table versions|
|[**get_businessrules_decisiontables**](#get_businessrules_decisiontables) | Get a list of decision tables.|
|[**get_businessrules_decisiontables_search**](#get_businessrules_decisiontables_search) | Search for decision tables.|
|[**get_businessrules_schema**](#get_businessrules_schema) | Get a schema|
|[**get_businessrules_schemas**](#get_businessrules_schemas) | Get a list of schemas.|
|[**get_businessrules_schemas_coretype**](#get_businessrules_schemas_coretype) | Get a specific named core type.|
|[**get_businessrules_schemas_coretypes**](#get_businessrules_schemas_coretypes) | Get the core types from which all schemas are built.|
|[**patch_businessrules_decisiontable**](#patch_businessrules_decisiontable) | Update a decision table|
|[**patch_businessrules_decisiontable_version**](#patch_businessrules_decisiontable_version) | Update a decision table version|
|[**post_businessrules_decisiontable_execute**](#post_businessrules_decisiontable_execute) | Execute a published decision table|
|[**post_businessrules_decisiontable_version_copy**](#post_businessrules_decisiontable_version_copy) | Copy a decision table version|
|[**post_businessrules_decisiontable_version_execute**](#post_businessrules_decisiontable_version_execute) | Execute a decision table version|
|[**post_businessrules_decisiontable_version_rows**](#post_businessrules_decisiontable_version_rows) | Create a decision table row|
|[**post_businessrules_decisiontable_version_rows_search**](#post_businessrules_decisiontable_version_rows_search) | Search for decision table rows|
|[**post_businessrules_decisiontable_version_sync**](#post_businessrules_decisiontable_version_sync) | Update the Business Rules Schema to the latest version for a given decision table version|
|[**post_businessrules_decisiontable_versions**](#post_businessrules_decisiontable_versions) | Create a new decision table version|
|[**post_businessrules_decisiontables**](#post_businessrules_decisiontables) | Create a decision table|
|[**post_businessrules_schemas**](#post_businessrules_schemas) | Create a schema|
|[**put_businessrules_decisiontable_version_publish**](#put_businessrules_decisiontable_version_publish) | Publish a decision table version|
|[**put_businessrules_decisiontable_version_row**](#put_businessrules_decisiontable_version_row) | Full update a decision table row|
|[**put_businessrules_schema**](#put_businessrules_schema) | Update a schema|



## delete_businessrules_decisiontable

>  delete_businessrules_decisiontable(table_id, force_delete=force_delete)


Delete a decision table

Wraps DELETE /api/v2/businessrules/decisiontables/{tableId} 

Requires ANY permissions: 

* businessrules:decisionTable:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
force_delete = False # bool | Force delete decision table (under certain conditions) (optional) (default to False)

try:
    # Delete a decision table
    api_instance.delete_businessrules_decisiontable(table_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->delete_businessrules_decisiontable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **force_delete** | **bool**| Force delete decision table (under certain conditions) | [optional] [default to False] |

### Return type

void (empty response body)


## delete_businessrules_decisiontable_version

>  delete_businessrules_decisiontable_version(table_id, table_version)


Delete a decision table version

Wraps DELETE /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion} 

Requires ANY permissions: 

* businessrules:decisionTable:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version

try:
    # Delete a decision table version
    api_instance.delete_businessrules_decisiontable_version(table_id, table_version)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->delete_businessrules_decisiontable_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |

### Return type

void (empty response body)


## delete_businessrules_decisiontable_version_row

>  delete_businessrules_decisiontable_version_row(table_id, table_version, row_id)


Delete a decision table row

Wraps DELETE /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/rows/{rowId} 

Requires ALL permissions: 

* businessrules:decisionTableRow:delete
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
row_id = 'row_id_example' # str | Row ID

try:
    # Delete a decision table row
    api_instance.delete_businessrules_decisiontable_version_row(table_id, table_version, row_id)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->delete_businessrules_decisiontable_version_row: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **row_id** | **str**| Row ID |  |

### Return type

void (empty response body)


## delete_businessrules_schema

>  delete_businessrules_schema(schema_id)


Delete a schema

Wraps DELETE /api/v2/businessrules/schemas/{schemaId} 

Requires ANY permissions: 

* businessrules:businessRulesSchema:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Delete a schema
    api_instance.delete_businessrules_schema(schema_id)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->delete_businessrules_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

void (empty response body)


## get_businessrules_decisiontable

> [**DecisionTable**](DecisionTable) get_businessrules_decisiontable(table_id)


Get a decision table

Wraps GET /api/v2/businessrules/decisiontables/{tableId} 

Requires ANY permissions: 

* businessrules:decisionTable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID

try:
    # Get a decision table
    api_response = api_instance.get_businessrules_decisiontable(table_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |

### Return type

[**DecisionTable**](DecisionTable)


## get_businessrules_decisiontable_version

> [**DecisionTableVersion**](DecisionTableVersion) get_businessrules_decisiontable_version(table_id, table_version)


Get a decision table version

Wraps GET /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion} 

Requires ANY permissions: 

* businessrules:decisionTable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version

try:
    # Get a decision table version
    api_response = api_instance.get_businessrules_decisiontable_version(table_id, table_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontable_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## get_businessrules_decisiontable_version_row

> [**DecisionTableRow**](DecisionTableRow) get_businessrules_decisiontable_version_row(table_id, table_version, row_id)


Get a decision table row

Wraps GET /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/rows/{rowId} 

Requires ANY permissions: 

* businessrules:decisionTableRow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
row_id = 'row_id_example' # str | Row ID

try:
    # Get a decision table row
    api_response = api_instance.get_businessrules_decisiontable_version_row(table_id, table_version, row_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontable_version_row: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **row_id** | **str**| Row ID |  |

### Return type

[**DecisionTableRow**](DecisionTableRow)


## get_businessrules_decisiontable_version_rows

> [**DecisionTableRowListing**](DecisionTableRowListing) get_businessrules_decisiontable_version_rows(table_id, table_version, page_number=page_number, page_size=page_size)


Get a list of decision table rows.

Wraps GET /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/rows 

Requires ANY permissions: 

* businessrules:decisionTableRow:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
page_number = 'page_number_example' # str | Page number of the entities to return. Defaults to 1. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 100. Defaults to 25. (optional)

try:
    # Get a list of decision table rows.
    api_response = api_instance.get_businessrules_decisiontable_version_rows(table_id, table_version, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontable_version_rows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **page_number** | **str**| Page number of the entities to return. Defaults to 1. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. Defaults to 25. | [optional]  |

### Return type

[**DecisionTableRowListing**](DecisionTableRowListing)


## get_businessrules_decisiontable_versions

> [**DecisionTableVersionListing**](DecisionTableVersionListing) get_businessrules_decisiontable_versions(table_id, after=after, page_size=page_size)


Get a list of decision table versions

Wraps GET /api/v2/businessrules/decisiontables/{tableId}/versions 

Requires ANY permissions: 

* businessrules:decisionTable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 100. (optional)

try:
    # Get a list of decision table versions
    api_response = api_instance.get_businessrules_decisiontable_versions(table_id, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontable_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. | [optional]  |

### Return type

[**DecisionTableVersionListing**](DecisionTableVersionListing)


## get_businessrules_decisiontables

> [**DecisionTableListing**](DecisionTableListing) get_businessrules_decisiontables(after=after, page_size=page_size, division_ids=division_ids, name=name)


Get a list of decision tables.

Wraps GET /api/v2/businessrules/decisiontables 

Requires ANY permissions: 

* businessrules:decisionTable:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 100. (optional)
division_ids = ['division_ids_example'] # list[str] | One or more comma separated divisions to filters decision tables by. If nothing is provided, the decision tables associated with the list of divisions that the user has access to will be returned. (optional)
name = 'name_example' # str | Search for decision tables with a name that contains the given search string. Search is case insensitive and will match any table that contains this string in any part of the name. (optional)

try:
    # Get a list of decision tables.
    api_response = api_instance.get_businessrules_decisiontables(after=after, page_size=page_size, division_ids=division_ids, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontables: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. | [optional]  |
| **division_ids** | [**list[str]**](str)| One or more comma separated divisions to filters decision tables by. If nothing is provided, the decision tables associated with the list of divisions that the user has access to will be returned. | [optional]  |
| **name** | **str**| Search for decision tables with a name that contains the given search string. Search is case insensitive and will match any table that contains this string in any part of the name. | [optional]  |

### Return type

[**DecisionTableListing**](DecisionTableListing)


## get_businessrules_decisiontables_search

> [**DecisionTableListing**](DecisionTableListing) get_businessrules_decisiontables_search(after=after, page_size=page_size, schema_id=schema_id, name=name, with_published_version=with_published_version, expand=expand, ids=ids)


Search for decision tables.

Wraps GET /api/v2/businessrules/decisiontables/search 

Requires ANY permissions: 

* businessrules:decisionTable:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 100. (optional)
schema_id = 'schema_id_example' # str | Search for decision tables that use the schema with this ID. Cannot be combined with name search. Search results will not be paginated if used. (optional)
name = 'name_example' # str | Search for decision tables with a name that contains the given search string. Search is case insensitive and will match any table that contains this string in any part of the name. Cannot be combined with schema search. Search results will not be paginated if used. (optional)
with_published_version = True # bool | Filters results to only decision tables that have at least one version in Published status (optional)
expand = ['expand_example'] # list[str] | Fields to expand in response (optional)
ids = ['ids_example'] # list[str] | Decision table IDs to search for (optional)

try:
    # Search for decision tables.
    api_response = api_instance.get_businessrules_decisiontables_search(after=after, page_size=page_size, schema_id=schema_id, name=name, with_published_version=with_published_version, expand=expand, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_decisiontables_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. | [optional]  |
| **schema_id** | **str**| Search for decision tables that use the schema with this ID. Cannot be combined with name search. Search results will not be paginated if used. | [optional]  |
| **name** | **str**| Search for decision tables with a name that contains the given search string. Search is case insensitive and will match any table that contains this string in any part of the name. Cannot be combined with schema search. Search results will not be paginated if used. | [optional]  |
| **with_published_version** | **bool**| Filters results to only decision tables that have at least one version in Published status | [optional]  |
| **expand** | [**list[str]**](str)| Fields to expand in response | [optional] <br />**Values**: ExecutionInputSchema, ExecutionOutputSchema |
| **ids** | [**list[str]**](str)| Decision table IDs to search for | [optional]  |

### Return type

[**DecisionTableListing**](DecisionTableListing)


## get_businessrules_schema

> [**BusinessRulesDataSchema**](BusinessRulesDataSchema) get_businessrules_schema(schema_id)


Get a schema

Wraps GET /api/v2/businessrules/schemas/{schemaId} 

Requires ANY permissions: 

* businessrules:businessRulesSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get a schema
    api_response = api_instance.get_businessrules_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**BusinessRulesDataSchema**](BusinessRulesDataSchema)


## get_businessrules_schemas

> [**BusinessRulesDataSchemaListing**](BusinessRulesDataSchemaListing) get_businessrules_schemas()


Get a list of schemas.

Wraps GET /api/v2/businessrules/schemas 

Requires ANY permissions: 

* businessrules:businessRulesSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()

try:
    # Get a list of schemas.
    api_response = api_instance.get_businessrules_schemas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_schemas: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**BusinessRulesDataSchemaListing**](BusinessRulesDataSchemaListing)


## get_businessrules_schemas_coretype

> [**Coretype**](Coretype) get_businessrules_schemas_coretype(core_type_name)


Get a specific named core type.

Wraps GET /api/v2/businessrules/schemas/coretypes/{coreTypeName} 

Requires ANY permissions: 

* businessrules:businessRulesSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
core_type_name = 'core_type_name_example' # str | The core type's name

try:
    # Get a specific named core type.
    api_response = api_instance.get_businessrules_schemas_coretype(core_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_schemas_coretype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **core_type_name** | **str**| The core type&#39;s name |  |

### Return type

[**Coretype**](Coretype)


## get_businessrules_schemas_coretypes

> [**CoretypeListing**](CoretypeListing) get_businessrules_schemas_coretypes()


Get the core types from which all schemas are built.

Wraps GET /api/v2/businessrules/schemas/coretypes 

Requires ANY permissions: 

* businessrules:businessRulesSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()

try:
    # Get the core types from which all schemas are built.
    api_response = api_instance.get_businessrules_schemas_coretypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->get_businessrules_schemas_coretypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CoretypeListing**](CoretypeListing)


## patch_businessrules_decisiontable

> [**DecisionTable**](DecisionTable) patch_businessrules_decisiontable(table_id, body)


Update a decision table

Wraps PATCH /api/v2/businessrules/decisiontables/{tableId} 

Requires ALL permissions: 

* businessrules:decisionTable:edit
* businessrules:businessRulesSchema:view
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
body = PureCloudPlatformClientV2.UpdateDecisionTableRequest() # UpdateDecisionTableRequest | Decision Table

try:
    # Update a decision table
    api_response = api_instance.patch_businessrules_decisiontable(table_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->patch_businessrules_decisiontable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **body** | [**UpdateDecisionTableRequest**](UpdateDecisionTableRequest)| Decision Table |  |

### Return type

[**DecisionTable**](DecisionTable)


## patch_businessrules_decisiontable_version

> [**DecisionTableVersion**](DecisionTableVersion) patch_businessrules_decisiontable_version(table_id, table_version, body)


Update a decision table version

Wraps PATCH /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion} 

Requires ANY permissions: 

* businessrules:decisionTable:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
body = PureCloudPlatformClientV2.UpdateDecisionTableVersionRequest() # UpdateDecisionTableVersionRequest | Decision Table

try:
    # Update a decision table version
    api_response = api_instance.patch_businessrules_decisiontable_version(table_id, table_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->patch_businessrules_decisiontable_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **body** | [**UpdateDecisionTableVersionRequest**](UpdateDecisionTableVersionRequest)| Decision Table |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## post_businessrules_decisiontable_execute

> [**DecisionTableExecutionResponse**](DecisionTableExecutionResponse) post_businessrules_decisiontable_execute(table_id, body)


Execute a published decision table

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/execute 

Requires ANY permissions: 

* businessrules:decisionTable:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
body = PureCloudPlatformClientV2.DecisionTableExecutionRequest() # DecisionTableExecutionRequest | Decision Table

try:
    # Execute a published decision table
    api_response = api_instance.post_businessrules_decisiontable_execute(table_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_execute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **body** | [**DecisionTableExecutionRequest**](DecisionTableExecutionRequest)| Decision Table |  |

### Return type

[**DecisionTableExecutionResponse**](DecisionTableExecutionResponse)


## post_businessrules_decisiontable_version_copy

> [**DecisionTableVersion**](DecisionTableVersion) post_businessrules_decisiontable_version_copy(table_id, table_version, body)


Copy a decision table version

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/copy 

Requires ANY permissions: 

* businessrules:decisionTable:copy

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
body = PureCloudPlatformClientV2.CopyDecisionTableRequest() # CopyDecisionTableRequest | Decision Table

try:
    # Copy a decision table version
    api_response = api_instance.post_businessrules_decisiontable_version_copy(table_id, table_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_version_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **body** | [**CopyDecisionTableRequest**](CopyDecisionTableRequest)| Decision Table |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## post_businessrules_decisiontable_version_execute

> [**DecisionTableExecutionResponse**](DecisionTableExecutionResponse) post_businessrules_decisiontable_version_execute(table_id, table_version, body)


Execute a decision table version

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/execute 

Requires ANY permissions: 

* businessrules:decisionTable:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
body = PureCloudPlatformClientV2.DecisionTableExecutionRequest() # DecisionTableExecutionRequest | Decision Table

try:
    # Execute a decision table version
    api_response = api_instance.post_businessrules_decisiontable_version_execute(table_id, table_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_version_execute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **body** | [**DecisionTableExecutionRequest**](DecisionTableExecutionRequest)| Decision Table |  |

### Return type

[**DecisionTableExecutionResponse**](DecisionTableExecutionResponse)


## post_businessrules_decisiontable_version_rows

> [**DecisionTableRow**](DecisionTableRow) post_businessrules_decisiontable_version_rows(table_id, table_version, body)


Create a decision table row

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/rows 

Requires ALL permissions: 

* businessrules:decisionTableRow:add
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
body = PureCloudPlatformClientV2.CreateDecisionTableRowRequest() # CreateDecisionTableRowRequest | Create decision table row request

try:
    # Create a decision table row
    api_response = api_instance.post_businessrules_decisiontable_version_rows(table_id, table_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_version_rows: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **body** | [**CreateDecisionTableRowRequest**](CreateDecisionTableRowRequest)| Create decision table row request |  |

### Return type

[**DecisionTableRow**](DecisionTableRow)


## post_businessrules_decisiontable_version_rows_search

> [**DecisionTableRowListing**](DecisionTableRowListing) post_businessrules_decisiontable_version_rows_search(table_id, table_version, body, page_number=page_number, page_size=page_size)


Search for decision table rows

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/rows/search 

Requires ANY permissions: 

* businessrules:decisionTableRow:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
body = PureCloudPlatformClientV2.SearchDecisionTableRowsRequest() # SearchDecisionTableRowsRequest | Search decision table rows request
page_number = 'page_number_example' # str | Page number of the entities to return. Defaults to 1. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 100. Defaults to 25. (optional)

try:
    # Search for decision table rows
    api_response = api_instance.post_businessrules_decisiontable_version_rows_search(table_id, table_version, body, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_version_rows_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **body** | [**SearchDecisionTableRowsRequest**](SearchDecisionTableRowsRequest)| Search decision table rows request |  |
| **page_number** | **str**| Page number of the entities to return. Defaults to 1. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. Defaults to 25. | [optional]  |

### Return type

[**DecisionTableRowListing**](DecisionTableRowListing)


## post_businessrules_decisiontable_version_sync

> [**DecisionTableVersion**](DecisionTableVersion) post_businessrules_decisiontable_version_sync(table_id, table_version)


Update the Business Rules Schema to the latest version for a given decision table version

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/sync 

Requires ANY permissions: 

* businessrules:decisionTable:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version

try:
    # Update the Business Rules Schema to the latest version for a given decision table version
    api_response = api_instance.post_businessrules_decisiontable_version_sync(table_id, table_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_version_sync: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## post_businessrules_decisiontable_versions

> [**DecisionTableVersion**](DecisionTableVersion) post_businessrules_decisiontable_versions(table_id)


Create a new decision table version

Wraps POST /api/v2/businessrules/decisiontables/{tableId}/versions 

Requires ANY permissions: 

* businessrules:decisionTable:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID

try:
    # Create a new decision table version
    api_response = api_instance.post_businessrules_decisiontable_versions(table_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontable_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## post_businessrules_decisiontables

> [**DecisionTableVersion**](DecisionTableVersion) post_businessrules_decisiontables(body)


Create a decision table

Wraps POST /api/v2/businessrules/decisiontables 

Requires ALL permissions: 

* businessrules:decisionTable:add
* businessrules:businessRulesSchema:view
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
body = PureCloudPlatformClientV2.CreateDecisionTableRequest() # CreateDecisionTableRequest | Decision Table

try:
    # Create a decision table
    api_response = api_instance.post_businessrules_decisiontables(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_decisiontables: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateDecisionTableRequest**](CreateDecisionTableRequest)| Decision Table |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## post_businessrules_schemas

> [**BusinessRulesDataSchema**](BusinessRulesDataSchema) post_businessrules_schemas(body)


Create a schema

Wraps POST /api/v2/businessrules/schemas 

Requires ANY permissions: 

* businessrules:businessRulesSchema:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
body = PureCloudPlatformClientV2.BusinessRulesSchemaCreateRequest() # BusinessRulesSchemaCreateRequest | Business Rules Schema Create Request

try:
    # Create a schema
    api_response = api_instance.post_businessrules_schemas(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->post_businessrules_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BusinessRulesSchemaCreateRequest**](BusinessRulesSchemaCreateRequest)| Business Rules Schema Create Request |  |

### Return type

[**BusinessRulesDataSchema**](BusinessRulesDataSchema)


## put_businessrules_decisiontable_version_publish

> [**DecisionTableVersion**](DecisionTableVersion) put_businessrules_decisiontable_version_publish(table_id, table_version)


Publish a decision table version

Wraps PUT /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/publish 

Requires ANY permissions: 

* businessrules:decisionTable:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version

try:
    # Publish a decision table version
    api_response = api_instance.put_businessrules_decisiontable_version_publish(table_id, table_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->put_businessrules_decisiontable_version_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |

### Return type

[**DecisionTableVersion**](DecisionTableVersion)


## put_businessrules_decisiontable_version_row

> [**DecisionTableRow**](DecisionTableRow) put_businessrules_decisiontable_version_row(table_id, table_version, row_id, body)


Full update a decision table row

Wraps PUT /api/v2/businessrules/decisiontables/{tableId}/versions/{tableVersion}/rows/{rowId} 

Requires ALL permissions: 

* businessrules:decisionTableRow:edit
* routing:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
table_id = 'table_id_example' # str | Table ID
table_version = 56 # int | Table Version
row_id = 'row_id_example' # str | Row ID
body = PureCloudPlatformClientV2.PutDecisionTableRowRequest() # PutDecisionTableRowRequest | Full update decision table row request

try:
    # Full update a decision table row
    api_response = api_instance.put_businessrules_decisiontable_version_row(table_id, table_version, row_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->put_businessrules_decisiontable_version_row: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **table_id** | **str**| Table ID |  |
| **table_version** | **int**| Table Version |  |
| **row_id** | **str**| Row ID |  |
| **body** | [**PutDecisionTableRowRequest**](PutDecisionTableRowRequest)| Full update decision table row request |  |

### Return type

[**DecisionTableRow**](DecisionTableRow)


## put_businessrules_schema

> [**BusinessRulesDataSchema**](BusinessRulesDataSchema) put_businessrules_schema(schema_id, body)


Update a schema

Wraps PUT /api/v2/businessrules/schemas/{schemaId} 

Requires ANY permissions: 

* businessrules:businessRulesSchema:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BusinessRulesApi()
schema_id = 'schema_id_example' # str | Schema ID
body = PureCloudPlatformClientV2.BusinessRulesSchemaUpdateRequest() # BusinessRulesSchemaUpdateRequest | Business Rules Schema Update Request

try:
    # Update a schema
    api_response = api_instance.put_businessrules_schema(schema_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessRulesApi->put_businessrules_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **body** | [**BusinessRulesSchemaUpdateRequest**](BusinessRulesSchemaUpdateRequest)| Business Rules Schema Update Request |  |

### Return type

[**BusinessRulesDataSchema**](BusinessRulesDataSchema)


_PureCloudPlatformClientV2 241.0.0_
