# TaskManagementApi

## PureCloudPlatformClientV2.TaskManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_taskmanagement_workbin**](#delete_taskmanagement_workbin) | Delete a workbin|
|[**delete_taskmanagement_workitem**](#delete_taskmanagement_workitem) | Delete a workitem|
|[**delete_taskmanagement_workitems_bulk_add_job**](#delete_taskmanagement_workitems_bulk_add_job) | Delete a bulk add job|
|[**delete_taskmanagement_workitems_bulk_terminate_job**](#delete_taskmanagement_workitems_bulk_terminate_job) | Delete a Bulk job|
|[**delete_taskmanagement_workitems_schema**](#delete_taskmanagement_workitems_schema) | Delete a schema|
|[**delete_taskmanagement_worktype**](#delete_taskmanagement_worktype) | Delete a worktype|
|[**delete_taskmanagement_worktype_flows_datebased_rule**](#delete_taskmanagement_worktype_flows_datebased_rule) | Delete a date based rule|
|[**delete_taskmanagement_worktype_flows_onattributechange_rule**](#delete_taskmanagement_worktype_flows_onattributechange_rule) | Delete a rule|
|[**delete_taskmanagement_worktype_flows_oncreate_rule**](#delete_taskmanagement_worktype_flows_oncreate_rule) | Delete a rule|
|[**delete_taskmanagement_worktype_status**](#delete_taskmanagement_worktype_status) | Delete a status|
|[**get_taskmanagement_workbin**](#get_taskmanagement_workbin) | Get a workbin|
|[**get_taskmanagement_workbin_history**](#get_taskmanagement_workbin_history) | Get a listing of a workbin&#39;s attribute change history|
|[**get_taskmanagement_workbin_version**](#get_taskmanagement_workbin_version) | Get a version of a workbin|
|[**get_taskmanagement_workbin_versions**](#get_taskmanagement_workbin_versions) | Get all versions of a workbin|
|[**get_taskmanagement_workitem**](#get_taskmanagement_workitem) | Get a workitem|
|[**get_taskmanagement_workitem_history**](#get_taskmanagement_workitem_history) | Get a listing of a workitem&#39;s attribute change history|
|[**get_taskmanagement_workitem_user_wrapups**](#get_taskmanagement_workitem_user_wrapups) | Get all wrapup codes added for the given user for a workitem.|
|[**get_taskmanagement_workitem_version**](#get_taskmanagement_workitem_version) | Get a version of a workitem|
|[**get_taskmanagement_workitem_versions**](#get_taskmanagement_workitem_versions) | Get all versions of a workitem|
|[**get_taskmanagement_workitem_wrapups**](#get_taskmanagement_workitem_wrapups) | Get all wrapup codes added for all users for a workitem.|
|[**get_taskmanagement_workitems_bulk_add_job**](#get_taskmanagement_workitems_bulk_add_job) | Get the bulk add job associated with the job id.|
|[**get_taskmanagement_workitems_bulk_add_job_results**](#get_taskmanagement_workitems_bulk_add_job_results) | Get bulk add job results.|
|[**get_taskmanagement_workitems_bulk_jobs_users_me**](#get_taskmanagement_workitems_bulk_jobs_users_me) | Get bulk jobs created by the currently logged in user.|
|[**get_taskmanagement_workitems_bulk_terminate_job**](#get_taskmanagement_workitems_bulk_terminate_job) | Get the bulk job associated with the job id.|
|[**get_taskmanagement_workitems_bulk_terminate_job_results**](#get_taskmanagement_workitems_bulk_terminate_job_results) | Get bulk terminate job results.|
|[**get_taskmanagement_workitems_query_job**](#get_taskmanagement_workitems_query_job) | Get the workitem query job associated with the job id.|
|[**get_taskmanagement_workitems_query_job_results**](#get_taskmanagement_workitems_query_job_results) | Get results from for workitem query job |
|[**get_taskmanagement_workitems_schema**](#get_taskmanagement_workitems_schema) | Get a schema|
|[**get_taskmanagement_workitems_schema_version**](#get_taskmanagement_workitems_schema_version) | Get a specific version of a schema|
|[**get_taskmanagement_workitems_schema_versions**](#get_taskmanagement_workitems_schema_versions) | Get all versions of a schema|
|[**get_taskmanagement_workitems_schemas**](#get_taskmanagement_workitems_schemas) | Get a list of schemas.|
|[**get_taskmanagement_workitems_schemas_coretype**](#get_taskmanagement_workitems_schemas_coretype) | Get a specific named core type.|
|[**get_taskmanagement_workitems_schemas_coretypes**](#get_taskmanagement_workitems_schemas_coretypes) | Get the core types from which all schemas are built.|
|[**get_taskmanagement_workitems_schemas_limits**](#get_taskmanagement_workitems_schemas_limits) | Get quantitative limits on schemas|
|[**get_taskmanagement_worktype**](#get_taskmanagement_worktype) | Get a worktype|
|[**get_taskmanagement_worktype_flows_datebased_rule**](#get_taskmanagement_worktype_flows_datebased_rule) | Get a date based rule|
|[**get_taskmanagement_worktype_flows_datebased_rules**](#get_taskmanagement_worktype_flows_datebased_rules) | Get all date based rules for a worktype|
|[**get_taskmanagement_worktype_flows_onattributechange_rule**](#get_taskmanagement_worktype_flows_onattributechange_rule) | Get an attribute change rule|
|[**get_taskmanagement_worktype_flows_onattributechange_rules**](#get_taskmanagement_worktype_flows_onattributechange_rules) | Get all attribute-change rules for a worktype|
|[**get_taskmanagement_worktype_flows_oncreate_rule**](#get_taskmanagement_worktype_flows_oncreate_rule) | Get an on-create rule|
|[**get_taskmanagement_worktype_flows_oncreate_rules**](#get_taskmanagement_worktype_flows_oncreate_rules) | Get all on-create rules for a worktype|
|[**get_taskmanagement_worktype_history**](#get_taskmanagement_worktype_history) | Get a listing of a worktype&#39;s attribute change history|
|[**get_taskmanagement_worktype_status**](#get_taskmanagement_worktype_status) | Get a status|
|[**get_taskmanagement_worktype_statuses**](#get_taskmanagement_worktype_statuses) | Get list of statuses for this worktype.|
|[**get_taskmanagement_worktype_version**](#get_taskmanagement_worktype_version) | Get a version of a worktype|
|[**get_taskmanagement_worktype_versions**](#get_taskmanagement_worktype_versions) | Get all versions of a worktype|
|[**patch_taskmanagement_workbin**](#patch_taskmanagement_workbin) | Update the attributes of a workbin|
|[**patch_taskmanagement_workitem**](#patch_taskmanagement_workitem) | Update the attributes of a workitem|
|[**patch_taskmanagement_workitem_assignment**](#patch_taskmanagement_workitem_assignment) | Attempts to manually assign a specified workitem to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.|
|[**patch_taskmanagement_workitem_user_wrapups**](#patch_taskmanagement_workitem_user_wrapups) | Add/Remove a wrapup code for a given user in a workitem.|
|[**patch_taskmanagement_workitem_users_me_wrapups**](#patch_taskmanagement_workitem_users_me_wrapups) | Add/Remove a wrapup code for the current user in a workitem.|
|[**patch_taskmanagement_workitems_bulk_add_job**](#patch_taskmanagement_workitems_bulk_add_job) | Update workitem bulk add job.|
|[**patch_taskmanagement_workitems_bulk_terminate_job**](#patch_taskmanagement_workitems_bulk_terminate_job) | Update workitem bulk terminate job.|
|[**patch_taskmanagement_worktype**](#patch_taskmanagement_worktype) | Update the attributes of a worktype|
|[**patch_taskmanagement_worktype_flows_datebased_rule**](#patch_taskmanagement_worktype_flows_datebased_rule) | Update the attributes of a date based rule|
|[**patch_taskmanagement_worktype_flows_onattributechange_rule**](#patch_taskmanagement_worktype_flows_onattributechange_rule) | Update the attributes of a rule|
|[**patch_taskmanagement_worktype_flows_oncreate_rule**](#patch_taskmanagement_worktype_flows_oncreate_rule) | Update the attributes of a rule|
|[**patch_taskmanagement_worktype_status**](#patch_taskmanagement_worktype_status) | Update the attributes of a status|
|[**post_taskmanagement_workbins**](#post_taskmanagement_workbins) | Create a workbin|
|[**post_taskmanagement_workbins_query**](#post_taskmanagement_workbins_query) | Query for workbins|
|[**post_taskmanagement_workitem_acd_cancel**](#post_taskmanagement_workitem_acd_cancel) | Cancel the assignment process for a workitem that is currently queued for assignment through ACD.|
|[**post_taskmanagement_workitem_disconnect**](#post_taskmanagement_workitem_disconnect) | Disconnect the assignee of the workitem|
|[**post_taskmanagement_workitem_terminate**](#post_taskmanagement_workitem_terminate) | Terminate a workitem|
|[**post_taskmanagement_workitems**](#post_taskmanagement_workitems) | Create a workitem|
|[**post_taskmanagement_workitems_bulk_add_jobs**](#post_taskmanagement_workitems_bulk_add_jobs) | Create a workitem bulk add job.|
|[**post_taskmanagement_workitems_bulk_terminate_jobs**](#post_taskmanagement_workitems_bulk_terminate_jobs) | Create a workitem bulk terminate job.|
|[**post_taskmanagement_workitems_query**](#post_taskmanagement_workitems_query) | Query for workitems|
|[**post_taskmanagement_workitems_query_jobs**](#post_taskmanagement_workitems_query_jobs) | Create a workitem query job|
|[**post_taskmanagement_workitems_schemas**](#post_taskmanagement_workitems_schemas) | Create a schema|
|[**post_taskmanagement_worktype_flows_datebased_rules**](#post_taskmanagement_worktype_flows_datebased_rules) | Add a date based rule to a worktype|
|[**post_taskmanagement_worktype_flows_onattributechange_rules**](#post_taskmanagement_worktype_flows_onattributechange_rules) | Add an attribute-change rule to a worktype|
|[**post_taskmanagement_worktype_flows_oncreate_rules**](#post_taskmanagement_worktype_flows_oncreate_rules) | Add an on-create rule to a worktype|
|[**post_taskmanagement_worktype_statuses**](#post_taskmanagement_worktype_statuses) | Add a status to a worktype|
|[**post_taskmanagement_worktypes**](#post_taskmanagement_worktypes) | Create a worktype|
|[**post_taskmanagement_worktypes_query**](#post_taskmanagement_worktypes_query) | Query for worktypes|
|[**put_taskmanagement_workitems_schema**](#put_taskmanagement_workitems_schema) | Update a schema|



## delete_taskmanagement_workbin

>  delete_taskmanagement_workbin(workbin_id)


Delete a workbin

Wraps DELETE /api/v2/taskmanagement/workbins/{workbinId} 

Requires ANY permissions: 

* workitems:workbin:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID

try:
    # Delete a workbin
    api_instance.delete_taskmanagement_workbin(workbin_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workbin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |

### Return type

void (empty response body)


## delete_taskmanagement_workitem

>  delete_taskmanagement_workitem(workitem_id)


Delete a workitem

Wraps DELETE /api/v2/taskmanagement/workitems/{workitemId} 

Requires ANY permissions: 

* workitems:workitem:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID

try:
    # Delete a workitem
    api_instance.delete_taskmanagement_workitem(workitem_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workitem: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |

### Return type

void (empty response body)


## delete_taskmanagement_workitems_bulk_add_job

>  delete_taskmanagement_workitems_bulk_add_job(bulk_job_id)


Delete a bulk add job

Wraps DELETE /api/v2/taskmanagement/workitems/bulk/add/jobs/{bulkJobId} 

Requires ANY permissions: 

* workitems:bulkAddJob:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id

try:
    # Delete a bulk add job
    api_instance.delete_taskmanagement_workitems_bulk_add_job(bulk_job_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workitems_bulk_add_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |

### Return type

void (empty response body)


## delete_taskmanagement_workitems_bulk_terminate_job

>  delete_taskmanagement_workitems_bulk_terminate_job(bulk_job_id)


Delete a Bulk job

Wraps DELETE /api/v2/taskmanagement/workitems/bulk/terminate/jobs/{bulkJobId} 

Requires ALL permissions: 

* workitems:bulkTerminateJob:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id

try:
    # Delete a Bulk job
    api_instance.delete_taskmanagement_workitems_bulk_terminate_job(bulk_job_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workitems_bulk_terminate_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |

### Return type

void (empty response body)


## delete_taskmanagement_workitems_schema

>  delete_taskmanagement_workitems_schema(schema_id)


Delete a schema

Wraps DELETE /api/v2/taskmanagement/workitems/schemas/{schemaId} 

Requires ANY permissions: 

* workitems:workitemSchema:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Delete a schema
    api_instance.delete_taskmanagement_workitems_schema(schema_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workitems_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

void (empty response body)


## delete_taskmanagement_worktype

>  delete_taskmanagement_worktype(worktype_id)


Delete a worktype

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId} 

Requires ANY permissions: 

* workitems:worktype:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id

try:
    # Delete a worktype
    api_instance.delete_taskmanagement_worktype(worktype_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |

### Return type

void (empty response body)


## delete_taskmanagement_worktype_flows_datebased_rule

>  delete_taskmanagement_worktype_flows_datebased_rule(worktype_id, rule_id)


Delete a date based rule

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId}/flows/datebased/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleDateBased:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId

try:
    # Delete a date based rule
    api_instance.delete_taskmanagement_worktype_flows_datebased_rule(worktype_id, rule_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype_flows_datebased_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |

### Return type

void (empty response body)


## delete_taskmanagement_worktype_flows_onattributechange_rule

>  delete_taskmanagement_worktype_flows_onattributechange_rule(worktype_id, rule_id)


Delete a rule

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId}/flows/onattributechange/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleOnAttributeChange:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId

try:
    # Delete a rule
    api_instance.delete_taskmanagement_worktype_flows_onattributechange_rule(worktype_id, rule_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype_flows_onattributechange_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |

### Return type

void (empty response body)


## delete_taskmanagement_worktype_flows_oncreate_rule

>  delete_taskmanagement_worktype_flows_oncreate_rule(worktype_id, rule_id)


Delete a rule

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId}/flows/oncreate/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleOnCreate:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId

try:
    # Delete a rule
    api_instance.delete_taskmanagement_worktype_flows_oncreate_rule(worktype_id, rule_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype_flows_oncreate_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |

### Return type

void (empty response body)


## delete_taskmanagement_worktype_status

>  delete_taskmanagement_worktype_status(worktype_id, status_id)


Delete a status

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId}/statuses/{statusId} 

Requires ANY permissions: 

* workitems:status:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
status_id = 'status_id_example' # str | Status id

try:
    # Delete a status
    api_instance.delete_taskmanagement_worktype_status(worktype_id, status_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **status_id** | **str**| Status id |  |

### Return type

void (empty response body)


## get_taskmanagement_workbin

> [**Workbin**](Workbin) get_taskmanagement_workbin(workbin_id)


Get a workbin

Wraps GET /api/v2/taskmanagement/workbins/{workbinId} 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID

try:
    # Get a workbin
    api_response = api_instance.get_taskmanagement_workbin(workbin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |

### Return type

[**Workbin**](Workbin)


## get_taskmanagement_workbin_history

> [**WorkbinChangeListing**](WorkbinChangeListing) get_taskmanagement_workbin_history(workbin_id, after=after, page_size=page_size, sort_order=sort_order)


Get a listing of a workbin's attribute change history

Wraps GET /api/v2/taskmanagement/workbins/{workbinId}/history 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get a listing of a workbin's attribute change history
    api_response = api_instance.get_taskmanagement_workbin_history(workbin_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorkbinChangeListing**](WorkbinChangeListing)


## get_taskmanagement_workbin_version

> [**WorkbinVersion**](WorkbinVersion) get_taskmanagement_workbin_version(workbin_id, entity_version)


Get a version of a workbin

Wraps GET /api/v2/taskmanagement/workbins/{workbinId}/versions/{entityVersion} 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
entity_version = 56 # int | Workbin version

try:
    # Get a version of a workbin
    api_response = api_instance.get_taskmanagement_workbin_version(workbin_id, entity_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **entity_version** | **int**| Workbin version |  |

### Return type

[**WorkbinVersion**](WorkbinVersion)


## get_taskmanagement_workbin_versions

> [**WorkbinVersionListing**](WorkbinVersionListing) get_taskmanagement_workbin_versions(workbin_id, after=after, page_size=page_size, sort_order=sort_order)


Get all versions of a workbin

Wraps GET /api/v2/taskmanagement/workbins/{workbinId}/versions 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all versions of a workbin
    api_response = api_instance.get_taskmanagement_workbin_versions(workbin_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorkbinVersionListing**](WorkbinVersionListing)


## get_taskmanagement_workitem

> [**Workitem**](Workitem) get_taskmanagement_workitem(workitem_id, expands=expands)


Get a workitem

Wraps GET /api/v2/taskmanagement/workitems/{workitemId} 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
expands = ['expands_example'] # list[str] | Which fields to expand. Comma separated if more than one. (optional)

try:
    # Get a workitem
    api_response = api_instance.get_taskmanagement_workitem(workitem_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **expands** | [**list[str]**](str)| Which fields to expand. Comma separated if more than one. | [optional] <br />**Values**: type, workbin, status, queue, assignee |

### Return type

[**Workitem**](Workitem)


## get_taskmanagement_workitem_history

> [**WorkitemChangeListing**](WorkitemChangeListing) get_taskmanagement_workitem_history(workitem_id, after=after, page_size=page_size, sort_order=sort_order)


Get a listing of a workitem's attribute change history

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/history 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get a listing of a workitem's attribute change history
    api_response = api_instance.get_taskmanagement_workitem_history(workitem_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorkitemChangeListing**](WorkitemChangeListing)


## get_taskmanagement_workitem_user_wrapups

> [**WorkitemWrapupEntityListing**](WorkitemWrapupEntityListing) get_taskmanagement_workitem_user_wrapups(workitem_id, user_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)


Get all wrapup codes added for the given user for a workitem.

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/users/{userId}/wrapups 

Requires ANY permissions: 

* workitems:wrapup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
user_id = 'user_id_example' # str | The ID of the user
expands = 'expands_example' # str | Which fields, if any, to expand. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all wrapup codes added for the given user for a workitem.
    api_response = api_instance.get_taskmanagement_workitem_user_wrapups(workitem_id, user_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_user_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **user_id** | **str**| The ID of the user |  |
| **expands** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: wrapupCode |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorkitemWrapupEntityListing**](WorkitemWrapupEntityListing)


## get_taskmanagement_workitem_version

> [**WorkitemVersion**](WorkitemVersion) get_taskmanagement_workitem_version(workitem_id, entity_version)


Get a version of a workitem

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/versions/{entityVersion} 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
entity_version = 56 # int | Workitem version

try:
    # Get a version of a workitem
    api_response = api_instance.get_taskmanagement_workitem_version(workitem_id, entity_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **entity_version** | **int**| Workitem version |  |

### Return type

[**WorkitemVersion**](WorkitemVersion)


## get_taskmanagement_workitem_versions

> [**WorkitemVersionListing**](WorkitemVersionListing) get_taskmanagement_workitem_versions(workitem_id, after=after, page_size=page_size, sort_order=sort_order)


Get all versions of a workitem

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/versions 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all versions of a workitem
    api_response = api_instance.get_taskmanagement_workitem_versions(workitem_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorkitemVersionListing**](WorkitemVersionListing)


## get_taskmanagement_workitem_wrapups

> [**WorkitemWrapupEntityListing**](WorkitemWrapupEntityListing) get_taskmanagement_workitem_wrapups(workitem_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)


Get all wrapup codes added for all users for a workitem.

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/wrapups 

Requires ANY permissions: 

* workitems:wrapup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
expands = 'expands_example' # str | Which fields, if any, to expand. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all wrapup codes added for all users for a workitem.
    api_response = api_instance.get_taskmanagement_workitem_wrapups(workitem_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **expands** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: wrapupCode |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorkitemWrapupEntityListing**](WorkitemWrapupEntityListing)


## get_taskmanagement_workitems_bulk_add_job

> [**BulkJob**](BulkJob) get_taskmanagement_workitems_bulk_add_job(bulk_job_id)


Get the bulk add job associated with the job id.

Wraps GET /api/v2/taskmanagement/workitems/bulk/add/jobs/{bulkJobId} 

Requires ANY permissions: 

* workitems:bulkAddJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id

try:
    # Get the bulk add job associated with the job id.
    api_response = api_instance.get_taskmanagement_workitems_bulk_add_job(bulk_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_bulk_add_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |

### Return type

[**BulkJob**](BulkJob)


## get_taskmanagement_workitems_bulk_add_job_results

> [**BulkJobAddResponse**](BulkJobAddResponse) get_taskmanagement_workitems_bulk_add_job_results(bulk_job_id)


Get bulk add job results.

Wraps GET /api/v2/taskmanagement/workitems/bulk/add/jobs/{bulkJobId}/results 

Requires ANY permissions: 

* workitems:bulkAddJobResults:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id

try:
    # Get bulk add job results.
    api_response = api_instance.get_taskmanagement_workitems_bulk_add_job_results(bulk_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_bulk_add_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |

### Return type

[**BulkJobAddResponse**](BulkJobAddResponse)


## get_taskmanagement_workitems_bulk_jobs_users_me

> [**BulkJobsListing**](BulkJobsListing) get_taskmanagement_workitems_bulk_jobs_users_me(after=after, page_size=page_size, sort_order=sort_order, action=action)


Get bulk jobs created by the currently logged in user.

Wraps GET /api/v2/taskmanagement/workitems/bulk/jobs/users/me 

Requires ANY permissions: 

* workitems:bulkJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')
action = 'action_example' # str | The bulk job action. (optional)

try:
    # Get bulk jobs created by the currently logged in user.
    api_response = api_instance.get_taskmanagement_workitems_bulk_jobs_users_me(after=after, page_size=page_size, sort_order=sort_order, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_bulk_jobs_users_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
| **action** | **str**| The bulk job action. | [optional] <br />**Values**: TerminateWorkitems, AddWorkitems |

### Return type

[**BulkJobsListing**](BulkJobsListing)


## get_taskmanagement_workitems_bulk_terminate_job

> [**BulkJob**](BulkJob) get_taskmanagement_workitems_bulk_terminate_job(bulk_job_id)


Get the bulk job associated with the job id.

Wraps GET /api/v2/taskmanagement/workitems/bulk/terminate/jobs/{bulkJobId} 

Requires ALL permissions: 

* workitems:bulkTerminateJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id

try:
    # Get the bulk job associated with the job id.
    api_response = api_instance.get_taskmanagement_workitems_bulk_terminate_job(bulk_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_bulk_terminate_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |

### Return type

[**BulkJob**](BulkJob)


## get_taskmanagement_workitems_bulk_terminate_job_results

> [**BulkJobTerminateResultsResponse**](BulkJobTerminateResultsResponse) get_taskmanagement_workitems_bulk_terminate_job_results(bulk_job_id)


Get bulk terminate job results.

Wraps GET /api/v2/taskmanagement/workitems/bulk/terminate/jobs/{bulkJobId}/results 

Requires ALL permissions: 

* workitems:bulkTerminateJobResults:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id

try:
    # Get bulk terminate job results.
    api_response = api_instance.get_taskmanagement_workitems_bulk_terminate_job_results(bulk_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_bulk_terminate_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |

### Return type

[**BulkJobTerminateResultsResponse**](BulkJobTerminateResultsResponse)


## get_taskmanagement_workitems_query_job

> [**WorkitemQueryJobResponse**](WorkitemQueryJobResponse) get_taskmanagement_workitems_query_job(job_id)


Get the workitem query job associated with the job id.

Wraps GET /api/v2/taskmanagement/workitems/query/jobs/{jobId} 

Requires ALL permissions: 

* workitems:queryJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get the workitem query job associated with the job id.
    api_response = api_instance.get_taskmanagement_workitems_query_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_query_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**WorkitemQueryJobResponse**](WorkitemQueryJobResponse)


## get_taskmanagement_workitems_query_job_results

> [**WorkitemPagedEntityListing**](WorkitemPagedEntityListing) get_taskmanagement_workitems_query_job_results(job_id)


Get results from for workitem query job 

Wraps GET /api/v2/taskmanagement/workitems/query/jobs/{jobId}/results 

Requires ALL permissions: 

* workitems:queryJobResults:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get results from for workitem query job 
    api_response = api_instance.get_taskmanagement_workitems_query_job_results(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_query_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**WorkitemPagedEntityListing**](WorkitemPagedEntityListing)


## get_taskmanagement_workitems_schema

> [**DataSchema**](DataSchema) get_taskmanagement_workitems_schema(schema_id)


Get a schema

Wraps GET /api/v2/taskmanagement/workitems/schemas/{schemaId} 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get a schema
    api_response = api_instance.get_taskmanagement_workitems_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**DataSchema**](DataSchema)


## get_taskmanagement_workitems_schema_version

> [**DataSchema**](DataSchema) get_taskmanagement_workitems_schema_version(schema_id, version_id)


Get a specific version of a schema

Wraps GET /api/v2/taskmanagement/workitems/schemas/{schemaId}/versions/{versionId} 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID
version_id = 'version_id_example' # str | Schema version

try:
    # Get a specific version of a schema
    api_response = api_instance.get_taskmanagement_workitems_schema_version(schema_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schema_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **version_id** | **str**| Schema version |  |

### Return type

[**DataSchema**](DataSchema)


## get_taskmanagement_workitems_schema_versions

> [**DataSchemaListing**](DataSchemaListing) get_taskmanagement_workitems_schema_versions(schema_id)


Get all versions of a schema

Wraps GET /api/v2/taskmanagement/workitems/schemas/{schemaId}/versions 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get all versions of a schema
    api_response = api_instance.get_taskmanagement_workitems_schema_versions(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schema_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**DataSchemaListing**](DataSchemaListing)


## get_taskmanagement_workitems_schemas

> [**DataSchemaListing**](DataSchemaListing) get_taskmanagement_workitems_schemas()


Get a list of schemas.

Wraps GET /api/v2/taskmanagement/workitems/schemas 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()

try:
    # Get a list of schemas.
    api_response = api_instance.get_taskmanagement_workitems_schemas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schemas: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataSchemaListing**](DataSchemaListing)


## get_taskmanagement_workitems_schemas_coretype

> [**Coretype**](Coretype) get_taskmanagement_workitems_schemas_coretype(core_type_name)


Get a specific named core type.

Wraps GET /api/v2/taskmanagement/workitems/schemas/coretypes/{coreTypeName} 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
core_type_name = 'core_type_name_example' # str | Name of the core type

try:
    # Get a specific named core type.
    api_response = api_instance.get_taskmanagement_workitems_schemas_coretype(core_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schemas_coretype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **core_type_name** | **str**| Name of the core type |  |

### Return type

[**Coretype**](Coretype)


## get_taskmanagement_workitems_schemas_coretypes

> [**CoretypeListing**](CoretypeListing) get_taskmanagement_workitems_schemas_coretypes()


Get the core types from which all schemas are built.

Wraps GET /api/v2/taskmanagement/workitems/schemas/coretypes 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()

try:
    # Get the core types from which all schemas are built.
    api_response = api_instance.get_taskmanagement_workitems_schemas_coretypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schemas_coretypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CoretypeListing**](CoretypeListing)


## get_taskmanagement_workitems_schemas_limits

> [**SchemaQuantityLimits**](SchemaQuantityLimits) get_taskmanagement_workitems_schemas_limits()


Get quantitative limits on schemas

Wraps GET /api/v2/taskmanagement/workitems/schemas/limits 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()

try:
    # Get quantitative limits on schemas
    api_response = api_instance.get_taskmanagement_workitems_schemas_limits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schemas_limits: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SchemaQuantityLimits**](SchemaQuantityLimits)


## get_taskmanagement_worktype

> [**Worktype**](Worktype) get_taskmanagement_worktype(worktype_id, expands=expands)


Get a worktype

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId} 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
expands = ['expands_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a worktype
    api_response = api_instance.get_taskmanagement_worktype(worktype_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **expands** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: defaultQueue, defaultSkills, defaultLanguage, schema, flow, defaultScript |

### Return type

[**Worktype**](Worktype)


## get_taskmanagement_worktype_flows_datebased_rule

> [**WorkitemDateBasedRule**](WorkitemDateBasedRule) get_taskmanagement_worktype_flows_datebased_rule(worktype_id, rule_id)


Get a date based rule

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/flows/datebased/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleDateBased:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId

try:
    # Get a date based rule
    api_response = api_instance.get_taskmanagement_worktype_flows_datebased_rule(worktype_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_flows_datebased_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |

### Return type

[**WorkitemDateBasedRule**](WorkitemDateBasedRule)


## get_taskmanagement_worktype_flows_datebased_rules

> [**WorkitemDateBasedRuleListing**](WorkitemDateBasedRuleListing) get_taskmanagement_worktype_flows_datebased_rules(worktype_id, after=after, page_size=page_size)


Get all date based rules for a worktype

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/flows/datebased/rules 

Requires ANY permissions: 

* workitems:flowRuleDateBased:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)

try:
    # Get all date based rules for a worktype
    api_response = api_instance.get_taskmanagement_worktype_flows_datebased_rules(worktype_id, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_flows_datebased_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |

### Return type

[**WorkitemDateBasedRuleListing**](WorkitemDateBasedRuleListing)


## get_taskmanagement_worktype_flows_onattributechange_rule

> [**WorkitemOnAttributeChangeRule**](WorkitemOnAttributeChangeRule) get_taskmanagement_worktype_flows_onattributechange_rule(worktype_id, rule_id)


Get an attribute change rule

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/flows/onattributechange/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleOnAttributeChange:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId

try:
    # Get an attribute change rule
    api_response = api_instance.get_taskmanagement_worktype_flows_onattributechange_rule(worktype_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_flows_onattributechange_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |

### Return type

[**WorkitemOnAttributeChangeRule**](WorkitemOnAttributeChangeRule)


## get_taskmanagement_worktype_flows_onattributechange_rules

> [**WorkitemOnAttributeChangeRuleListing**](WorkitemOnAttributeChangeRuleListing) get_taskmanagement_worktype_flows_onattributechange_rules(worktype_id, after=after, page_size=page_size)


Get all attribute-change rules for a worktype

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/flows/onattributechange/rules 

Requires ANY permissions: 

* workitems:flowRuleOnAttributeChange:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)

try:
    # Get all attribute-change rules for a worktype
    api_response = api_instance.get_taskmanagement_worktype_flows_onattributechange_rules(worktype_id, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_flows_onattributechange_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |

### Return type

[**WorkitemOnAttributeChangeRuleListing**](WorkitemOnAttributeChangeRuleListing)


## get_taskmanagement_worktype_flows_oncreate_rule

> [**WorkitemOnCreateRule**](WorkitemOnCreateRule) get_taskmanagement_worktype_flows_oncreate_rule(worktype_id, rule_id)


Get an on-create rule

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/flows/oncreate/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleOnCreate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId

try:
    # Get an on-create rule
    api_response = api_instance.get_taskmanagement_worktype_flows_oncreate_rule(worktype_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_flows_oncreate_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |

### Return type

[**WorkitemOnCreateRule**](WorkitemOnCreateRule)


## get_taskmanagement_worktype_flows_oncreate_rules

> [**WorkitemOnCreateRuleListing**](WorkitemOnCreateRuleListing) get_taskmanagement_worktype_flows_oncreate_rules(worktype_id, after=after, page_size=page_size)


Get all on-create rules for a worktype

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/flows/oncreate/rules 

Requires ANY permissions: 

* workitems:flowRuleOnCreate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)

try:
    # Get all on-create rules for a worktype
    api_response = api_instance.get_taskmanagement_worktype_flows_oncreate_rules(worktype_id, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_flows_oncreate_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |

### Return type

[**WorkitemOnCreateRuleListing**](WorkitemOnCreateRuleListing)


## get_taskmanagement_worktype_history

> [**WorktypeChangeListing**](WorktypeChangeListing) get_taskmanagement_worktype_history(worktype_id, after=after, page_size=page_size, sort_order=sort_order, fields=fields)


Get a listing of a worktype's attribute change history

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/history 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')
fields = ['fields_example'] # list[str] | Comma-separated list of fields. The response will contain only versions created as a result of changes to these fields. (optional)

try:
    # Get a listing of a worktype's attribute change history
    api_response = api_instance.get_taskmanagement_worktype_history(worktype_id, after=after, page_size=page_size, sort_order=sort_order, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
| **fields** | [**list[str]**](str)| Comma-separated list of fields. The response will contain only versions created as a result of changes to these fields. | [optional] <br />**Values**: name, serviceLevelTarget, defaultWorkbinId, defaultDueDurationSeconds, defaultExpirationSeconds, defaultPriority, defaultLanguageId, defaultSkillIds, defaultQueueId, assignmentEnabled, defaultStatusId, statuses |

### Return type

[**WorktypeChangeListing**](WorktypeChangeListing)


## get_taskmanagement_worktype_status

> [**WorkitemStatus**](WorkitemStatus) get_taskmanagement_worktype_status(worktype_id, status_id)


Get a status

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/statuses/{statusId} 

Requires ANY permissions: 

* workitems:status:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
status_id = 'status_id_example' # str | Status id

try:
    # Get a status
    api_response = api_instance.get_taskmanagement_worktype_status(worktype_id, status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **status_id** | **str**| Status id |  |

### Return type

[**WorkitemStatus**](WorkitemStatus)


## get_taskmanagement_worktype_statuses

> [**WorkitemStatusListing**](WorkitemStatusListing) get_taskmanagement_worktype_statuses(worktype_id)


Get list of statuses for this worktype.

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/statuses 

Requires ANY permissions: 

* workitems:status:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id

try:
    # Get list of statuses for this worktype.
    api_response = api_instance.get_taskmanagement_worktype_statuses(worktype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_statuses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |

### Return type

[**WorkitemStatusListing**](WorkitemStatusListing)


## get_taskmanagement_worktype_version

> [**WorktypeVersion**](WorktypeVersion) get_taskmanagement_worktype_version(worktype_id, entity_version)


Get a version of a worktype

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/versions/{entityVersion} 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
entity_version = 56 # int | Worktype version

try:
    # Get a version of a worktype
    api_response = api_instance.get_taskmanagement_worktype_version(worktype_id, entity_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **entity_version** | **int**| Worktype version |  |

### Return type

[**WorktypeVersion**](WorktypeVersion)


## get_taskmanagement_worktype_versions

> [**WorktypeVersionListing**](WorktypeVersionListing) get_taskmanagement_worktype_versions(worktype_id, after=after, page_size=page_size, sort_order=sort_order)


Get all versions of a worktype

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/versions 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all versions of a worktype
    api_response = api_instance.get_taskmanagement_worktype_versions(worktype_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**WorktypeVersionListing**](WorktypeVersionListing)


## patch_taskmanagement_workbin

> [**Workbin**](Workbin) patch_taskmanagement_workbin(workbin_id, body)


Update the attributes of a workbin

Wraps PATCH /api/v2/taskmanagement/workbins/{workbinId} 

Requires ANY permissions: 

* workitems:workbin:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
body = PureCloudPlatformClientV2.WorkbinUpdate() # WorkbinUpdate | Json with attributes and their new values: {\"description\":\"new description\", \"name\":\"new name\"}.

try:
    # Update the attributes of a workbin
    api_response = api_instance.patch_taskmanagement_workbin(workbin_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workbin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **body** | [**WorkbinUpdate**](WorkbinUpdate)| Json with attributes and their new values: {\&quot;description\&quot;:\&quot;new description\&quot;, \&quot;name\&quot;:\&quot;new name\&quot;}. |  |

### Return type

[**Workbin**](Workbin)


## patch_taskmanagement_workitem

> [**Workitem**](Workitem) patch_taskmanagement_workitem(workitem_id, body)


Update the attributes of a workitem

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId} 

Requires ANY permissions: 

* workitems:workitem:edit
* workitems:workitem:accept

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
body = PureCloudPlatformClientV2.WorkitemUpdate() # WorkitemUpdate | Workitem

try:
    # Update the attributes of a workitem
    api_response = api_instance.patch_taskmanagement_workitem(workitem_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **body** | [**WorkitemUpdate**](WorkitemUpdate)| Workitem |  |

### Return type

[**Workitem**](Workitem)


## patch_taskmanagement_workitem_assignment

>  patch_taskmanagement_workitem_assignment(workitem_id, body)


Attempts to manually assign a specified workitem to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId}/assignment 

Requires ANY permissions: 

* workitems:workitem:pull
* workitems:workitem:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
body = PureCloudPlatformClientV2.WorkitemManualAssign() # WorkitemManualAssign | Targeted user

try:
    # Attempts to manually assign a specified workitem to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.
    api_instance.patch_taskmanagement_workitem_assignment(workitem_id, body)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem_assignment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **body** | [**WorkitemManualAssign**](WorkitemManualAssign)| Targeted user |  |

### Return type

void (empty response body)


## patch_taskmanagement_workitem_user_wrapups

>  patch_taskmanagement_workitem_user_wrapups(workitem_id, user_id, body)


Add/Remove a wrapup code for a given user in a workitem.

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId}/users/{userId}/wrapups 

Requires ANY permissions: 

* workitems:wrapup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
user_id = 'user_id_example' # str | The ID of the user
body = PureCloudPlatformClientV2.WorkitemWrapupUpdate() # WorkitemWrapupUpdate | Request body to add/remove a wrapup code for a workitem

try:
    # Add/Remove a wrapup code for a given user in a workitem.
    api_instance.patch_taskmanagement_workitem_user_wrapups(workitem_id, user_id, body)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem_user_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **user_id** | **str**| The ID of the user |  |
| **body** | [**WorkitemWrapupUpdate**](WorkitemWrapupUpdate)| Request body to add/remove a wrapup code for a workitem |  |

### Return type

void (empty response body)


## patch_taskmanagement_workitem_users_me_wrapups

>  patch_taskmanagement_workitem_users_me_wrapups(workitem_id, body)


Add/Remove a wrapup code for the current user in a workitem.

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId}/users/me/wrapups 

Requires ANY permissions: 

* workitems:wrapupSelf:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
body = PureCloudPlatformClientV2.WorkitemWrapupUpdate() # WorkitemWrapupUpdate | Request body to add/remove the wrapup code for workitem

try:
    # Add/Remove a wrapup code for the current user in a workitem.
    api_instance.patch_taskmanagement_workitem_users_me_wrapups(workitem_id, body)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem_users_me_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **body** | [**WorkitemWrapupUpdate**](WorkitemWrapupUpdate)| Request body to add/remove the wrapup code for workitem |  |

### Return type

void (empty response body)


## patch_taskmanagement_workitems_bulk_add_job

> [**BulkJob**](BulkJob) patch_taskmanagement_workitems_bulk_add_job(bulk_job_id, body)


Update workitem bulk add job.

Wraps PATCH /api/v2/taskmanagement/workitems/bulk/add/jobs/{bulkJobId} 

Requires ANY permissions: 

* workitems:bulkAddJob:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id
body = PureCloudPlatformClientV2.BulkJobUpdate() # BulkJobUpdate | Bulk add job update request

try:
    # Update workitem bulk add job.
    api_response = api_instance.patch_taskmanagement_workitems_bulk_add_job(bulk_job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitems_bulk_add_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |
| **body** | [**BulkJobUpdate**](BulkJobUpdate)| Bulk add job update request |  |

### Return type

[**BulkJob**](BulkJob)


## patch_taskmanagement_workitems_bulk_terminate_job

> [**BulkJob**](BulkJob) patch_taskmanagement_workitems_bulk_terminate_job(bulk_job_id, body)


Update workitem bulk terminate job.

Wraps PATCH /api/v2/taskmanagement/workitems/bulk/terminate/jobs/{bulkJobId} 

Requires ALL permissions: 

* workitems:bulkTerminateJob:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
bulk_job_id = 'bulk_job_id_example' # str | Bulk job id
body = PureCloudPlatformClientV2.BulkJobUpdate() # BulkJobUpdate | Bulk job update request

try:
    # Update workitem bulk terminate job.
    api_response = api_instance.patch_taskmanagement_workitems_bulk_terminate_job(bulk_job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitems_bulk_terminate_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulk_job_id** | **str**| Bulk job id |  |
| **body** | [**BulkJobUpdate**](BulkJobUpdate)| Bulk job update request |  |

### Return type

[**BulkJob**](BulkJob)


## patch_taskmanagement_worktype

> [**Worktype**](Worktype) patch_taskmanagement_worktype(worktype_id, body)


Update the attributes of a worktype

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId} 

Requires ALL permissions: 

* workitems:worktype:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorktypeUpdate() # WorktypeUpdate | Worktype

try:
    # Update the attributes of a worktype
    api_response = api_instance.patch_taskmanagement_worktype(worktype_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorktypeUpdate**](WorktypeUpdate)| Worktype |  |

### Return type

[**Worktype**](Worktype)


## patch_taskmanagement_worktype_flows_datebased_rule

> [**WorkitemDateBasedRule**](WorkitemDateBasedRule) patch_taskmanagement_worktype_flows_datebased_rule(worktype_id, rule_id, body)


Update the attributes of a date based rule

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId}/flows/datebased/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleDateBased:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId
body = PureCloudPlatformClientV2.WorkitemDateBasedRuleUpdate() # WorkitemDateBasedRuleUpdate | Rule

try:
    # Update the attributes of a date based rule
    api_response = api_instance.patch_taskmanagement_worktype_flows_datebased_rule(worktype_id, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype_flows_datebased_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |
| **body** | [**WorkitemDateBasedRuleUpdate**](WorkitemDateBasedRuleUpdate)| Rule |  |

### Return type

[**WorkitemDateBasedRule**](WorkitemDateBasedRule)


## patch_taskmanagement_worktype_flows_onattributechange_rule

> [**WorkitemOnAttributeChangeRule**](WorkitemOnAttributeChangeRule) patch_taskmanagement_worktype_flows_onattributechange_rule(worktype_id, rule_id, body)


Update the attributes of a rule

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId}/flows/onattributechange/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleOnAttributeChange:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId
body = PureCloudPlatformClientV2.WorkitemOnAttributeChangeRuleUpdate() # WorkitemOnAttributeChangeRuleUpdate | Rule

try:
    # Update the attributes of a rule
    api_response = api_instance.patch_taskmanagement_worktype_flows_onattributechange_rule(worktype_id, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype_flows_onattributechange_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |
| **body** | [**WorkitemOnAttributeChangeRuleUpdate**](WorkitemOnAttributeChangeRuleUpdate)| Rule |  |

### Return type

[**WorkitemOnAttributeChangeRule**](WorkitemOnAttributeChangeRule)


## patch_taskmanagement_worktype_flows_oncreate_rule

> [**WorkitemOnCreateRule**](WorkitemOnCreateRule) patch_taskmanagement_worktype_flows_oncreate_rule(worktype_id, rule_id, body)


Update the attributes of a rule

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId}/flows/oncreate/rules/{ruleId} 

Requires ANY permissions: 

* workitems:flowRuleOnCreate:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
rule_id = 'rule_id_example' # str | ruleId
body = PureCloudPlatformClientV2.WorkitemOnCreateRuleUpdate() # WorkitemOnCreateRuleUpdate | Rule

try:
    # Update the attributes of a rule
    api_response = api_instance.patch_taskmanagement_worktype_flows_oncreate_rule(worktype_id, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype_flows_oncreate_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **rule_id** | **str**| ruleId |  |
| **body** | [**WorkitemOnCreateRuleUpdate**](WorkitemOnCreateRuleUpdate)| Rule |  |

### Return type

[**WorkitemOnCreateRule**](WorkitemOnCreateRule)


## patch_taskmanagement_worktype_status

> [**WorkitemStatus**](WorkitemStatus) patch_taskmanagement_worktype_status(worktype_id, status_id, body)


Update the attributes of a status

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId}/statuses/{statusId} 

Requires ANY permissions: 

* workitems:status:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
status_id = 'status_id_example' # str | Status id
body = PureCloudPlatformClientV2.WorkitemStatusUpdate() # WorkitemStatusUpdate | Status

try:
    # Update the attributes of a status
    api_response = api_instance.patch_taskmanagement_worktype_status(worktype_id, status_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **status_id** | **str**| Status id |  |
| **body** | [**WorkitemStatusUpdate**](WorkitemStatusUpdate)| Status |  |

### Return type

[**WorkitemStatus**](WorkitemStatus)


## post_taskmanagement_workbins

> [**Workbin**](Workbin) post_taskmanagement_workbins(body)


Create a workbin

Wraps POST /api/v2/taskmanagement/workbins 

Requires ANY permissions: 

* workitems:workbin:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkbinCreate() # WorkbinCreate | Workbin

try:
    # Create a workbin
    api_response = api_instance.post_taskmanagement_workbins(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workbins: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkbinCreate**](WorkbinCreate)| Workbin |  |

### Return type

[**Workbin**](Workbin)


## post_taskmanagement_workbins_query

> [**WorkbinQueryEntityListing**](WorkbinQueryEntityListing) post_taskmanagement_workbins_query(body)


Query for workbins

Wraps POST /api/v2/taskmanagement/workbins/query 

Requires ALL permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkbinQueryRequest() # WorkbinQueryRequest | QueryPostRequest

try:
    # Query for workbins
    api_response = api_instance.post_taskmanagement_workbins_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workbins_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkbinQueryRequest**](WorkbinQueryRequest)| QueryPostRequest |  |

### Return type

[**WorkbinQueryEntityListing**](WorkbinQueryEntityListing)


## post_taskmanagement_workitem_acd_cancel

> [**Workitem**](Workitem) post_taskmanagement_workitem_acd_cancel(workitem_id)


Cancel the assignment process for a workitem that is currently queued for assignment through ACD.

Wraps POST /api/v2/taskmanagement/workitems/{workitemId}/acd/cancel 

Requires ANY permissions: 

* workitems:workitem:cancelRouting

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID

try:
    # Cancel the assignment process for a workitem that is currently queued for assignment through ACD.
    api_response = api_instance.post_taskmanagement_workitem_acd_cancel(workitem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitem_acd_cancel: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |

### Return type

[**Workitem**](Workitem)


## post_taskmanagement_workitem_disconnect

> [**Workitem**](Workitem) post_taskmanagement_workitem_disconnect(workitem_id)


Disconnect the assignee of the workitem

Wraps POST /api/v2/taskmanagement/workitems/{workitemId}/disconnect 

Requires ANY permissions: 

* workitems:workitem:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID

try:
    # Disconnect the assignee of the workitem
    api_response = api_instance.post_taskmanagement_workitem_disconnect(workitem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitem_disconnect: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |

### Return type

[**Workitem**](Workitem)


## post_taskmanagement_workitem_terminate

> [**Workitem**](Workitem) post_taskmanagement_workitem_terminate(workitem_id, body=body)


Terminate a workitem

Wraps POST /api/v2/taskmanagement/workitems/{workitemId}/terminate 

Requires ANY permissions: 

* workitems:workitem:terminate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
body = PureCloudPlatformClientV2.WorkitemTerminate() # WorkitemTerminate | Terminated request (optional)

try:
    # Terminate a workitem
    api_response = api_instance.post_taskmanagement_workitem_terminate(workitem_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitem_terminate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **body** | [**WorkitemTerminate**](WorkitemTerminate)| Terminated request | [optional]  |

### Return type

[**Workitem**](Workitem)


## post_taskmanagement_workitems

> [**Workitem**](Workitem) post_taskmanagement_workitems(body)


Create a workitem

Wraps POST /api/v2/taskmanagement/workitems 

Requires ANY permissions: 

* workitems:workitem:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkitemCreate() # WorkitemCreate | Workitem

try:
    # Create a workitem
    api_response = api_instance.post_taskmanagement_workitems(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkitemCreate**](WorkitemCreate)| Workitem |  |

### Return type

[**Workitem**](Workitem)


## post_taskmanagement_workitems_bulk_add_jobs

> [**BulkJob**](BulkJob) post_taskmanagement_workitems_bulk_add_jobs(body)


Create a workitem bulk add job.

Wraps POST /api/v2/taskmanagement/workitems/bulk/add/jobs 

Requires ANY permissions: 

* workitems:bulkAddJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.BulkJobAddRequest() # BulkJobAddRequest | Bulk job definition.

try:
    # Create a workitem bulk add job.
    api_response = api_instance.post_taskmanagement_workitems_bulk_add_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_bulk_add_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkJobAddRequest**](BulkJobAddRequest)| Bulk job definition. |  |

### Return type

[**BulkJob**](BulkJob)


## post_taskmanagement_workitems_bulk_terminate_jobs

> [**BulkJob**](BulkJob) post_taskmanagement_workitems_bulk_terminate_jobs(body)


Create a workitem bulk terminate job.

Wraps POST /api/v2/taskmanagement/workitems/bulk/terminate/jobs 

Requires ALL permissions: 

* workitems:bulkTerminateJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.BulkJobTerminateRequest() # BulkJobTerminateRequest | Bulk job definition.

try:
    # Create a workitem bulk terminate job.
    api_response = api_instance.post_taskmanagement_workitems_bulk_terminate_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_bulk_terminate_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkJobTerminateRequest**](BulkJobTerminateRequest)| Bulk job definition. |  |

### Return type

[**BulkJob**](BulkJob)


## post_taskmanagement_workitems_query

> [**WorkitemPostQueryEntityListing**](WorkitemPostQueryEntityListing) post_taskmanagement_workitems_query(body)


Query for workitems

This query requires at least one EQ filter on the workbinId, assigneeId or typeId attributes.

post_taskmanagement_workitems_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems/query 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkitemQueryPostRequest() # WorkitemQueryPostRequest | WorkitemQueryPostRequest

try:
    # Query for workitems
    api_response = api_instance.post_taskmanagement_workitems_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkitemQueryPostRequest**](WorkitemQueryPostRequest)| WorkitemQueryPostRequest |  |

### Return type

[**WorkitemPostQueryEntityListing**](WorkitemPostQueryEntityListing)


## post_taskmanagement_workitems_query_jobs

> [**WorkitemQueryJobResponse**](WorkitemQueryJobResponse) post_taskmanagement_workitems_query_jobs(body)


Create a workitem query job

Wraps POST /api/v2/taskmanagement/workitems/query/jobs 

Requires ANY permissions: 

* workitems:queryJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkitemQueryJobCreate() # WorkitemQueryJobCreate | WorkitemQueryJobCreate

try:
    # Create a workitem query job
    api_response = api_instance.post_taskmanagement_workitems_query_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_query_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkitemQueryJobCreate**](WorkitemQueryJobCreate)| WorkitemQueryJobCreate |  |

### Return type

[**WorkitemQueryJobResponse**](WorkitemQueryJobResponse)


## post_taskmanagement_workitems_schemas

> [**DataSchema**](DataSchema) post_taskmanagement_workitems_schemas(body)


Create a schema

Wraps POST /api/v2/taskmanagement/workitems/schemas 

Requires ANY permissions: 

* workitems:workitemSchema:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Schema

try:
    # Create a schema
    api_response = api_instance.post_taskmanagement_workitems_schemas(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DataSchema**](DataSchema)| Schema |  |

### Return type

[**DataSchema**](DataSchema)


## post_taskmanagement_worktype_flows_datebased_rules

> [**WorkitemDateBasedRule**](WorkitemDateBasedRule) post_taskmanagement_worktype_flows_datebased_rules(worktype_id, body)


Add a date based rule to a worktype

Wraps POST /api/v2/taskmanagement/worktypes/{worktypeId}/flows/datebased/rules 

Requires ANY permissions: 

* workitems:flowRuleDateBased:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorkitemDateBasedRuleCreate() # WorkitemDateBasedRuleCreate | Rule

try:
    # Add a date based rule to a worktype
    api_response = api_instance.post_taskmanagement_worktype_flows_datebased_rules(worktype_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktype_flows_datebased_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorkitemDateBasedRuleCreate**](WorkitemDateBasedRuleCreate)| Rule |  |

### Return type

[**WorkitemDateBasedRule**](WorkitemDateBasedRule)


## post_taskmanagement_worktype_flows_onattributechange_rules

> [**WorkitemOnAttributeChangeRule**](WorkitemOnAttributeChangeRule) post_taskmanagement_worktype_flows_onattributechange_rules(worktype_id, body)


Add an attribute-change rule to a worktype

Wraps POST /api/v2/taskmanagement/worktypes/{worktypeId}/flows/onattributechange/rules 

Requires ANY permissions: 

* workitems:flowRuleOnAttributeChange:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorkitemOnAttributeChangeRuleCreate() # WorkitemOnAttributeChangeRuleCreate | Rule

try:
    # Add an attribute-change rule to a worktype
    api_response = api_instance.post_taskmanagement_worktype_flows_onattributechange_rules(worktype_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktype_flows_onattributechange_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorkitemOnAttributeChangeRuleCreate**](WorkitemOnAttributeChangeRuleCreate)| Rule |  |

### Return type

[**WorkitemOnAttributeChangeRule**](WorkitemOnAttributeChangeRule)


## post_taskmanagement_worktype_flows_oncreate_rules

> [**WorkitemOnCreateRule**](WorkitemOnCreateRule) post_taskmanagement_worktype_flows_oncreate_rules(worktype_id, body)


Add an on-create rule to a worktype

Wraps POST /api/v2/taskmanagement/worktypes/{worktypeId}/flows/oncreate/rules 

Requires ANY permissions: 

* workitems:flowRuleOnCreate:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorkitemOnCreateRuleCreate() # WorkitemOnCreateRuleCreate | Rule

try:
    # Add an on-create rule to a worktype
    api_response = api_instance.post_taskmanagement_worktype_flows_oncreate_rules(worktype_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktype_flows_oncreate_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorkitemOnCreateRuleCreate**](WorkitemOnCreateRuleCreate)| Rule |  |

### Return type

[**WorkitemOnCreateRule**](WorkitemOnCreateRule)


## post_taskmanagement_worktype_statuses

> [**WorkitemStatus**](WorkitemStatus) post_taskmanagement_worktype_statuses(worktype_id, body)


Add a status to a worktype

Wraps POST /api/v2/taskmanagement/worktypes/{worktypeId}/statuses 

Requires ANY permissions: 

* workitems:status:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorkitemStatusCreate() # WorkitemStatusCreate | Status

try:
    # Add a status to a worktype
    api_response = api_instance.post_taskmanagement_worktype_statuses(worktype_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktype_statuses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorkitemStatusCreate**](WorkitemStatusCreate)| Status |  |

### Return type

[**WorkitemStatus**](WorkitemStatus)


## post_taskmanagement_worktypes

> [**Worktype**](Worktype) post_taskmanagement_worktypes(body)


Create a worktype

Wraps POST /api/v2/taskmanagement/worktypes 

Requires ANY permissions: 

* workitems:worktype:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorktypeCreate() # WorktypeCreate | Worktype

try:
    # Create a worktype
    api_response = api_instance.post_taskmanagement_worktypes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktypes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorktypeCreate**](WorktypeCreate)| Worktype |  |

### Return type

[**Worktype**](Worktype)


## post_taskmanagement_worktypes_query

> [**WorktypeQueryEntityListing**](WorktypeQueryEntityListing) post_taskmanagement_worktypes_query(body)


Query for worktypes

Wraps POST /api/v2/taskmanagement/worktypes/query 

Requires ALL permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorktypeQueryRequest() # WorktypeQueryRequest | QueryPostRequest

try:
    # Query for worktypes
    api_response = api_instance.post_taskmanagement_worktypes_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktypes_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorktypeQueryRequest**](WorktypeQueryRequest)| QueryPostRequest |  |

### Return type

[**WorktypeQueryEntityListing**](WorktypeQueryEntityListing)


## put_taskmanagement_workitems_schema

> [**DataSchema**](DataSchema) put_taskmanagement_workitems_schema(schema_id, body)


Update a schema

Wraps PUT /api/v2/taskmanagement/workitems/schemas/{schemaId} 

Requires ANY permissions: 

* workitems:workitemSchema:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Data Schema

try:
    # Update a schema
    api_response = api_instance.put_taskmanagement_workitems_schema(schema_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->put_taskmanagement_workitems_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **body** | [**DataSchema**](DataSchema)| Data Schema |  |

### Return type

[**DataSchema**](DataSchema)


_PureCloudPlatformClientV2 243.0.0_
