# CaseManagementApi

## PureCloudPlatformClientV2.CaseManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_casemanagement_case**](#delete_casemanagement_case) | Delete a Case.|
|[**delete_casemanagement_case_comments_me_comment_id**](#delete_casemanagement_case_comments_me_comment_id) | Delete my Comment.|
|[**delete_casemanagement_caseplan**](#delete_casemanagement_caseplan) | Delete a Caseplan.|
|[**delete_casemanagement_caseplan_dataschema**](#delete_casemanagement_caseplan_dataschema) | Remove a data schema from a draft Caseplan.|
|[**get_casemanagement_case**](#get_casemanagement_case) | Get a Case.|
|[**get_casemanagement_case_association**](#get_casemanagement_case_association) | Get a Case Association.|
|[**get_casemanagement_case_associations**](#get_casemanagement_case_associations) | Get a list of Case associations for the Case.|
|[**get_casemanagement_case_comment**](#get_casemanagement_case_comment) | Get a Comment.|
|[**get_casemanagement_case_comments**](#get_casemanagement_case_comments) | Get comments for a Case.|
|[**get_casemanagement_case_stage**](#get_casemanagement_case_stage) | Get a Stage.|
|[**get_casemanagement_case_stage_step**](#get_casemanagement_case_stage_step) | Get a Step.|
|[**get_casemanagement_case_stage_steps**](#get_casemanagement_case_stage_steps) | Get a list of Steps.|
|[**get_casemanagement_case_stages**](#get_casemanagement_case_stages) | Get a list of Stages.|
|[**get_casemanagement_case_terminate_job**](#get_casemanagement_case_terminate_job) | Get a Terminate Job for a Case.|
|[**get_casemanagement_caseplan**](#get_casemanagement_caseplan) | Get a Caseplan.|
|[**get_casemanagement_caseplan_version**](#get_casemanagement_caseplan_version) | Get a Caseplan version.|
|[**get_casemanagement_caseplan_version_dataschemas**](#get_casemanagement_caseplan_version_dataschemas) | Get the data schemas for a Caseplan version.|
|[**get_casemanagement_caseplan_version_intakesettings**](#get_casemanagement_caseplan_version_intakesettings) | Get the intake settings for a Caseplan version.|
|[**get_casemanagement_caseplan_version_stageplan**](#get_casemanagement_caseplan_version_stageplan) | Get a Stageplan.|
|[**get_casemanagement_caseplan_version_stageplan_stepplan**](#get_casemanagement_caseplan_version_stageplan_stepplan) | Get a Stepplan.|
|[**get_casemanagement_caseplan_version_stageplan_stepplans**](#get_casemanagement_caseplan_version_stageplan_stepplans) | Get a list of Stepplans.|
|[**get_casemanagement_caseplan_version_stageplans**](#get_casemanagement_caseplan_version_stageplans) | Get a list of Stageplans.|
|[**get_casemanagement_caseplans**](#get_casemanagement_caseplans) | Get a list of Caseplans.|
|[**get_casemanagement_cases_externalcontact**](#get_casemanagement_cases_externalcontact) | Get a list of Cases for an External Contact.|
|[**get_casemanagement_cases_reference**](#get_casemanagement_cases_reference) | Get a Case by reference.|
|[**patch_casemanagement_case_datedue**](#patch_casemanagement_case_datedue) | Update the due date of a Case.|
|[**patch_casemanagement_case_priority**](#patch_casemanagement_case_priority) | Update priority of a Case.|
|[**patch_casemanagement_case_summary**](#patch_casemanagement_case_summary) | Update summary of a Case.|
|[**patch_casemanagement_caseplan**](#patch_casemanagement_caseplan) | Update the attributes of a Caseplan.|
|[**patch_casemanagement_caseplan_stageplan**](#patch_casemanagement_caseplan_stageplan) | Update the attributes of a Stageplan.|
|[**patch_casemanagement_caseplan_stageplan_stepplan**](#patch_casemanagement_caseplan_stageplan_stepplan) | Update the attributes of a Stepplan.|
|[**post_casemanagement_case_associations**](#post_casemanagement_case_associations) | Create a Case association.|
|[**post_casemanagement_case_comments**](#post_casemanagement_case_comments) | Add a comment to a Case.|
|[**post_casemanagement_case_terminate_jobs**](#post_casemanagement_case_terminate_jobs) | Create a Terminate Job for a Case.|
|[**post_casemanagement_caseplan_dataschemas**](#post_casemanagement_caseplan_dataschemas) | Add a data schema to a draft Caseplan.|
|[**post_casemanagement_caseplan_publish**](#post_casemanagement_caseplan_publish) | Publish Caseplan.|
|[**post_casemanagement_caseplan_versions**](#post_casemanagement_caseplan_versions) | Create Caseplan version.|
|[**post_casemanagement_caseplans**](#post_casemanagement_caseplans) | Create a Caseplan.|
|[**post_casemanagement_caseplans_query**](#post_casemanagement_caseplans_query) | Query for Caseplans.|
|[**post_casemanagement_cases**](#post_casemanagement_cases) | Create a Case.|
|[**post_casemanagement_cases_associations_query**](#post_casemanagement_cases_associations_query) | Query for Case associations by interaction.|
|[**put_casemanagement_caseplan_dataschema**](#put_casemanagement_caseplan_dataschema) | Update a data schema on a draft Caseplan.|
|[**put_casemanagement_caseplan_intakesettings**](#put_casemanagement_caseplan_intakesettings) | Update the intake settings for a Caseplan.|



## delete_casemanagement_case

> object** delete_casemanagement_case(case_id)


Delete a Case.

Wraps DELETE /api/v2/casemanagement/cases/{caseId} 

Requires ALL permissions: 

* caseManagement:case:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.

try:
    # Delete a Case.
    api_response = api_instance.delete_casemanagement_case(case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->delete_casemanagement_case: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |

### Return type

**object**


## delete_casemanagement_case_comments_me_comment_id

> object** delete_casemanagement_case_comments_me_comment_id(case_id, comment_id)


Delete my Comment.

Wraps DELETE /api/v2/casemanagement/cases/{caseId}/comments/me/{commentId} 

Requires ANY permissions: 

* caseManagement:commentSelf:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
comment_id = 'comment_id_example' # str | Comment identifier.

try:
    # Delete my Comment.
    api_response = api_instance.delete_casemanagement_case_comments_me_comment_id(case_id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->delete_casemanagement_case_comments_me_comment_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **comment_id** | **str**| Comment identifier. |  |

### Return type

**object**


## delete_casemanagement_caseplan

> object** delete_casemanagement_caseplan(caseplan_id)


Delete a Caseplan.

Wraps DELETE /api/v2/casemanagement/caseplans/{caseplanId} 

Requires ALL permissions: 

* caseManagement:caseplan:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.

try:
    # Delete a Caseplan.
    api_response = api_instance.delete_casemanagement_caseplan(caseplan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->delete_casemanagement_caseplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |

### Return type

**object**


## delete_casemanagement_caseplan_dataschema

> object** delete_casemanagement_caseplan_dataschema(caseplan_id, schema_key_name)


Remove a data schema from a draft Caseplan.

Wraps DELETE /api/v2/casemanagement/caseplans/{caseplanId}/dataschemas/{schemaKeyName} 

Requires ALL permissions: 

* caseManagement:caseplanDataSchemas:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
schema_key_name = 'schema_key_name_example' # str | Schema key (for example \"default\").

try:
    # Remove a data schema from a draft Caseplan.
    api_response = api_instance.delete_casemanagement_caseplan_dataschema(caseplan_id, schema_key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->delete_casemanagement_caseplan_dataschema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **schema_key_name** | **str**| Schema key (for example \&quot;default\&quot;). |  |

### Return type

**object**


## get_casemanagement_case

> [**Case**](Case) get_casemanagement_case(case_id, expands=expands)


Get a Case.

Wraps GET /api/v2/casemanagement/cases/{caseId} 

Requires ANY permissions: 

* caseManagement:case:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
expands = ['expands_example'] # list[str] | Attributes to expand. Comma-separated if more than one. (optional)

try:
    # Get a Case.
    api_response = api_instance.get_casemanagement_case(case_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **expands** | [**list[str]**](str)| Attributes to expand. Comma-separated if more than one. | [optional] <br />**Values**: caseplan, owner, modifiedBy, externalContact, customerIntent |

### Return type

[**Case**](Case)


## get_casemanagement_case_association

> [**CaseAssociation**](CaseAssociation) get_casemanagement_case_association(case_id, association_id)


Get a Case Association.

Wraps GET /api/v2/casemanagement/cases/{caseId}/associations/{associationId} 

Requires ANY permissions: 

* caseManagement:caseAssociation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
association_id = 'association_id_example' # str | Case association identifier.

try:
    # Get a Case Association.
    api_response = api_instance.get_casemanagement_case_association(case_id, association_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_association: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **association_id** | **str**| Case association identifier. |  |

### Return type

[**CaseAssociation**](CaseAssociation)


## get_casemanagement_case_associations

> [**CaseAssociationListing**](CaseAssociationListing) get_casemanagement_case_associations(case_id, before=before, after=after, page_size=page_size)


Get a list of Case associations for the Case.

Wraps GET /api/v2/casemanagement/cases/{caseId}/associations 

Requires ANY permissions: 

* caseManagement:caseAssociation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get a list of Case associations for the Case.
    api_response = api_instance.get_casemanagement_case_associations(case_id, before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_associations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**CaseAssociationListing**](CaseAssociationListing)


## get_casemanagement_case_comment

> [**Comment**](Comment) get_casemanagement_case_comment(case_id, comment_id)


Get a Comment.

Wraps GET /api/v2/casemanagement/cases/{caseId}/comments/{commentId} 

Requires ANY permissions: 

* caseManagement:comment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
comment_id = 'comment_id_example' # str | Comment identifier.

try:
    # Get a Comment.
    api_response = api_instance.get_casemanagement_case_comment(case_id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_comment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **comment_id** | **str**| Comment identifier. |  |

### Return type

[**Comment**](Comment)


## get_casemanagement_case_comments

> [**CommentListing**](CommentListing) get_casemanagement_case_comments(case_id, after=after, page_size=page_size, sort_order=sort_order)


Get comments for a Case.

Wraps GET /api/v2/casemanagement/cases/{caseId}/comments 

Requires ANY permissions: 

* caseManagement:comment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
after = 'after_example' # str | Cursor pointing to the end of the previously returned page of comments. (optional)
page_size = 56 # int | Number of comments to return. Maximum is 100. (optional)
sort_order = ''desc'' # str | Ascending or descending sort order. (optional) (default to 'desc')

try:
    # Get comments for a Case.
    api_response = api_instance.get_casemanagement_case_comments(case_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_comments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **after** | **str**| Cursor pointing to the end of the previously returned page of comments. | [optional]  |
| **page_size** | **int**| Number of comments to return. Maximum is 100. | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order. | [optional] [default to &#39;desc&#39;]<br />**Values**: asc, desc |

### Return type

[**CommentListing**](CommentListing)


## get_casemanagement_case_stage

> [**Stage**](Stage) get_casemanagement_case_stage(case_id, stage_id)


Get a Stage.

Wraps GET /api/v2/casemanagement/cases/{caseId}/stages/{stageId} 

Requires ANY permissions: 

* caseManagement:stage:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
stage_id = 'stage_id_example' # str | Stage identifier.

try:
    # Get a Stage.
    api_response = api_instance.get_casemanagement_case_stage(case_id, stage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_stage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **stage_id** | **str**| Stage identifier. |  |

### Return type

[**Stage**](Stage)


## get_casemanagement_case_stage_step

> [**Step**](Step) get_casemanagement_case_stage_step(case_id, stage_id, step_id)


Get a Step.

Wraps GET /api/v2/casemanagement/cases/{caseId}/stages/{stageId}/steps/{stepId} 

Requires ANY permissions: 

* caseManagement:step:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
stage_id = 'stage_id_example' # str | Stage identifier.
step_id = 'step_id_example' # str | Step identifier.

try:
    # Get a Step.
    api_response = api_instance.get_casemanagement_case_stage_step(case_id, stage_id, step_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_stage_step: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **stage_id** | **str**| Stage identifier. |  |
| **step_id** | **str**| Step identifier. |  |

### Return type

[**Step**](Step)


## get_casemanagement_case_stage_steps

> [**StepListing**](StepListing) get_casemanagement_case_stage_steps(case_id, stage_id, before=before, after=after, page_size=page_size)


Get a list of Steps.

Wraps GET /api/v2/casemanagement/cases/{caseId}/stages/{stageId}/steps 

Requires ANY permissions: 

* caseManagement:step:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
stage_id = 'stage_id_example' # str | Stage identifier.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get a list of Steps.
    api_response = api_instance.get_casemanagement_case_stage_steps(case_id, stage_id, before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_stage_steps: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **stage_id** | **str**| Stage identifier. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**StepListing**](StepListing)


## get_casemanagement_case_stages

> [**StageListing**](StageListing) get_casemanagement_case_stages(case_id, before=before, after=after, page_size=page_size)


Get a list of Stages.

Wraps GET /api/v2/casemanagement/cases/{caseId}/stages 

Requires ANY permissions: 

* caseManagement:stage:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get a list of Stages.
    api_response = api_instance.get_casemanagement_case_stages(case_id, before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_stages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**StageListing**](StageListing)


## get_casemanagement_case_terminate_job

> [**TerminateJob**](TerminateJob) get_casemanagement_case_terminate_job(case_id, job_id)


Get a Terminate Job for a Case.

Wraps GET /api/v2/casemanagement/cases/{caseId}/terminate/jobs/{jobId} 

Requires ANY permissions: 

* caseManagement:terminateJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
job_id = 'job_id_example' # str | Terminate Job identifier.

try:
    # Get a Terminate Job for a Case.
    api_response = api_instance.get_casemanagement_case_terminate_job(case_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_terminate_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **job_id** | **str**| Terminate Job identifier. |  |

### Return type

[**TerminateJob**](TerminateJob)


## get_casemanagement_caseplan

> [**Caseplan**](Caseplan) get_casemanagement_caseplan(caseplan_id)


Get a Caseplan.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId} 

Requires ANY permissions: 

* caseManagement:caseplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.

try:
    # Get a Caseplan.
    api_response = api_instance.get_casemanagement_caseplan(caseplan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |

### Return type

[**Caseplan**](Caseplan)


## get_casemanagement_caseplan_version

> [**Caseplan**](Caseplan) get_casemanagement_caseplan_version(caseplan_id, version_id)


Get a Caseplan version.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId} 

Requires ANY permissions: 

* caseManagement:caseplan:version

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.

try:
    # Get a Caseplan version.
    api_response = api_instance.get_casemanagement_caseplan_version(caseplan_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |

### Return type

[**Caseplan**](Caseplan)


## get_casemanagement_caseplan_version_dataschemas

> [**CaseplanDataSchemaListing**](CaseplanDataSchemaListing) get_casemanagement_caseplan_version_dataschemas(caseplan_id, version_id)


Get the data schemas for a Caseplan version.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId}/dataschemas 

Requires ANY permissions: 

* caseManagement:caseplanDataSchemas:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.

try:
    # Get the data schemas for a Caseplan version.
    api_response = api_instance.get_casemanagement_caseplan_version_dataschemas(caseplan_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_dataschemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |

### Return type

[**CaseplanDataSchemaListing**](CaseplanDataSchemaListing)


## get_casemanagement_caseplan_version_intakesettings

> [**IntakeSettingsListing**](IntakeSettingsListing) get_casemanagement_caseplan_version_intakesettings(caseplan_id, version_id)


Get the intake settings for a Caseplan version.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId}/intakesettings 

Requires ANY permissions: 

* caseManagement:caseplanIntakeSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.

try:
    # Get the intake settings for a Caseplan version.
    api_response = api_instance.get_casemanagement_caseplan_version_intakesettings(caseplan_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_intakesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |

### Return type

[**IntakeSettingsListing**](IntakeSettingsListing)


## get_casemanagement_caseplan_version_stageplan

> [**Stageplan**](Stageplan) get_casemanagement_caseplan_version_stageplan(caseplan_id, version_id, stageplan_id, expands=expands)


Get a Stageplan.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId}/stageplans/{stageplanId} 

Requires ANY permissions: 

* caseManagement:stageplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.
stageplan_id = 'stageplan_id_example' # str | Stageplan identifier.
expands = ['expands_example'] # list[str] | Fields to expand. (optional)

try:
    # Get a Stageplan.
    api_response = api_instance.get_casemanagement_caseplan_version_stageplan(caseplan_id, version_id, stageplan_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_stageplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |
| **stageplan_id** | **str**| Stageplan identifier. |  |
| **expands** | [**list[str]**](str)| Fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**Stageplan**](Stageplan)


## get_casemanagement_caseplan_version_stageplan_stepplan

> [**Stepplan**](Stepplan) get_casemanagement_caseplan_version_stageplan_stepplan(caseplan_id, version_id, stageplan_id, stepplan_id, expands=expands)


Get a Stepplan.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId}/stageplans/{stageplanId}/stepplans/{stepplanId} 

Requires ANY permissions: 

* caseManagement:stepplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.
stageplan_id = 'stageplan_id_example' # str | Stageplan identifier.
stepplan_id = 'stepplan_id_example' # str | Stepplan identifier.
expands = ['expands_example'] # list[str] | Fields to expand. (optional)

try:
    # Get a Stepplan.
    api_response = api_instance.get_casemanagement_caseplan_version_stageplan_stepplan(caseplan_id, version_id, stageplan_id, stepplan_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_stageplan_stepplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |
| **stageplan_id** | **str**| Stageplan identifier. |  |
| **stepplan_id** | **str**| Stepplan identifier. |  |
| **expands** | [**list[str]**](str)| Fields to expand. | [optional] <br />**Values**: stageplan, caseplan, worktype |

### Return type

[**Stepplan**](Stepplan)


## get_casemanagement_caseplan_version_stageplan_stepplans

> [**StepplanListing**](StepplanListing) get_casemanagement_caseplan_version_stageplan_stepplans(caseplan_id, version_id, stageplan_id, before=before, after=after, page_size=page_size, expands=expands)


Get a list of Stepplans.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId}/stageplans/{stageplanId}/stepplans 

Requires ANY permissions: 

* caseManagement:stepplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.
stageplan_id = 'stageplan_id_example' # str | Stageplan identifier.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
expands = ['expands_example'] # list[str] | Fields to expand. (optional)

try:
    # Get a list of Stepplans.
    api_response = api_instance.get_casemanagement_caseplan_version_stageplan_stepplans(caseplan_id, version_id, stageplan_id, before=before, after=after, page_size=page_size, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_stageplan_stepplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |
| **stageplan_id** | **str**| Stageplan identifier. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **expands** | [**list[str]**](str)| Fields to expand. | [optional] <br />**Values**: caseplan, stageplan, worktype |

### Return type

[**StepplanListing**](StepplanListing)


## get_casemanagement_caseplan_version_stageplans

> [**StageplanListing**](StageplanListing) get_casemanagement_caseplan_version_stageplans(caseplan_id, version_id, before=before, after=after, page_size=page_size, expands=expands)


Get a list of Stageplans.

Wraps GET /api/v2/casemanagement/caseplans/{caseplanId}/versions/{versionId}/stageplans 

Requires ANY permissions: 

* caseManagement:stageplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
version_id = 'version_id_example' # str | Caseplan version identifier.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
expands = ['expands_example'] # list[str] | Fields to expand. (optional)

try:
    # Get a list of Stageplans.
    api_response = api_instance.get_casemanagement_caseplan_version_stageplans(caseplan_id, version_id, before=before, after=after, page_size=page_size, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_stageplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **version_id** | **str**| Caseplan version identifier. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **expands** | [**list[str]**](str)| Fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**StageplanListing**](StageplanListing)


## get_casemanagement_caseplans

> [**CaseplanListing**](CaseplanListing) get_casemanagement_caseplans(after=after, page_size=page_size, customer_intent_id=customer_intent_id, division_ids=division_ids)


Get a list of Caseplans.

Wraps GET /api/v2/casemanagement/caseplans 

Requires ANY permissions: 

* caseManagement:caseplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
after = 'after_example' # str | Cursor that points to the end of the previously returned set of Caseplans. (optional)
page_size = 56 # int | Number of Caseplans to return. Maximum is 200. (optional)
customer_intent_id = 'customer_intent_id_example' # str | Filter by customer intent. (optional)
division_ids = 'division_ids_example' # str | Filter by divisions. (optional)

try:
    # Get a list of Caseplans.
    api_response = api_instance.get_casemanagement_caseplans(after=after, page_size=page_size, customer_intent_id=customer_intent_id, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **str**| Cursor that points to the end of the previously returned set of Caseplans. | [optional]  |
| **page_size** | **int**| Number of Caseplans to return. Maximum is 200. | [optional]  |
| **customer_intent_id** | **str**| Filter by customer intent. | [optional]  |
| **division_ids** | **str**| Filter by divisions. | [optional]  |

### Return type

[**CaseplanListing**](CaseplanListing)


## get_casemanagement_cases_externalcontact

> [**CaseListing**](CaseListing) get_casemanagement_cases_externalcontact(external_contact_id, after=after, page_size=page_size, division_ids=division_ids, expands=expands)


Get a list of Cases for an External Contact.

Wraps GET /api/v2/casemanagement/cases/externalcontacts/{externalContactId} 

Requires ANY permissions: 

* caseManagement:caseExternalContact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
external_contact_id = 'external_contact_id_example' # str | External contact identifier.
after = 'after_example' # str | Cursor pointing to the end of the previously returned page of Cases. (optional)
page_size = 56 # int | Number of Cases to return (maximum 200). (optional)
division_ids = 'division_ids_example' # str | Filter by divisions. (optional)
expands = ['expands_example'] # list[str] | Fields to expand. (optional)

try:
    # Get a list of Cases for an External Contact.
    api_response = api_instance.get_casemanagement_cases_externalcontact(external_contact_id, after=after, page_size=page_size, division_ids=division_ids, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_cases_externalcontact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_contact_id** | **str**| External contact identifier. |  |
| **after** | **str**| Cursor pointing to the end of the previously returned page of Cases. | [optional]  |
| **page_size** | **int**| Number of Cases to return (maximum 200). | [optional]  |
| **division_ids** | **str**| Filter by divisions. | [optional]  |
| **expands** | [**list[str]**](str)| Fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**CaseListing**](CaseListing)


## get_casemanagement_cases_reference

> [**Case**](Case) get_casemanagement_cases_reference(reference_id, expands=expands)


Get a Case by reference.

Wraps GET /api/v2/casemanagement/cases/references/{referenceId} 

Requires ANY permissions: 

* caseManagement:caseReference:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
reference_id = 'reference_id_example' # str | Case reference.
expands = ['expands_example'] # list[str] | Attributes to expand. Comma-separated if more than one. (optional)

try:
    # Get a Case by reference.
    api_response = api_instance.get_casemanagement_cases_reference(reference_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_cases_reference: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **reference_id** | **str**| Case reference. |  |
| **expands** | [**list[str]**](str)| Attributes to expand. Comma-separated if more than one. | [optional] <br />**Values**: caseplan, owner, modifiedBy, externalContact, customerIntent |

### Return type

[**Case**](Case)


## patch_casemanagement_case_datedue

> [**Case**](Case) patch_casemanagement_case_datedue(case_id, body)


Update the due date of a Case.

Wraps PATCH /api/v2/casemanagement/cases/{caseId}/datedue 

Requires ANY permissions: 

* caseManagement:caseDateDue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
body = PureCloudPlatformClientV2.CaseDateDueUpdate() # CaseDateDueUpdate | Due date update.

try:
    # Update the due date of a Case.
    api_response = api_instance.patch_casemanagement_case_datedue(case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_case_datedue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **body** | [**CaseDateDueUpdate**](CaseDateDueUpdate)| Due date update. |  |

### Return type

[**Case**](Case)


## patch_casemanagement_case_priority

> [**Case**](Case) patch_casemanagement_case_priority(case_id, body)


Update priority of a Case.

Wraps PATCH /api/v2/casemanagement/cases/{caseId}/priority 

Requires ANY permissions: 

* caseManagement:casePriority:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
body = PureCloudPlatformClientV2.CasePriorityUpdate() # CasePriorityUpdate | Priority update.

try:
    # Update priority of a Case.
    api_response = api_instance.patch_casemanagement_case_priority(case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_case_priority: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **body** | [**CasePriorityUpdate**](CasePriorityUpdate)| Priority update. |  |

### Return type

[**Case**](Case)


## patch_casemanagement_case_summary

> [**Case**](Case) patch_casemanagement_case_summary(case_id, body)


Update summary of a Case.

Wraps PATCH /api/v2/casemanagement/cases/{caseId}/summary 

Requires ANY permissions: 

* caseManagement:caseSummary:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
body = PureCloudPlatformClientV2.CaseSummaryUpdate() # CaseSummaryUpdate | Summary update.

try:
    # Update summary of a Case.
    api_response = api_instance.patch_casemanagement_case_summary(case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_case_summary: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **body** | [**CaseSummaryUpdate**](CaseSummaryUpdate)| Summary update. |  |

### Return type

[**Case**](Case)


## patch_casemanagement_caseplan

> [**Caseplan**](Caseplan) patch_casemanagement_caseplan(caseplan_id, body)


Update the attributes of a Caseplan.

Wraps PATCH /api/v2/casemanagement/caseplans/{caseplanId} 

Requires ALL permissions: 

* caseManagement:caseplan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
body = PureCloudPlatformClientV2.CaseplanUpdate() # CaseplanUpdate | Caseplan update.

try:
    # Update the attributes of a Caseplan.
    api_response = api_instance.patch_casemanagement_caseplan(caseplan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_caseplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **body** | [**CaseplanUpdate**](CaseplanUpdate)| Caseplan update. |  |

### Return type

[**Caseplan**](Caseplan)


## patch_casemanagement_caseplan_stageplan

> [**Stageplan**](Stageplan) patch_casemanagement_caseplan_stageplan(caseplan_id, stageplan_id, body)


Update the attributes of a Stageplan.

Wraps PATCH /api/v2/casemanagement/caseplans/{caseplanId}/stageplans/{stageplanId} 

Requires ANY permissions: 

* caseManagement:stageplan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
stageplan_id = 'stageplan_id_example' # str | Stageplan identifier.
body = PureCloudPlatformClientV2.StageplanUpdate() # StageplanUpdate | Stageplan update.

try:
    # Update the attributes of a Stageplan.
    api_response = api_instance.patch_casemanagement_caseplan_stageplan(caseplan_id, stageplan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_caseplan_stageplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **stageplan_id** | **str**| Stageplan identifier. |  |
| **body** | [**StageplanUpdate**](StageplanUpdate)| Stageplan update. |  |

### Return type

[**Stageplan**](Stageplan)


## patch_casemanagement_caseplan_stageplan_stepplan

> [**Stepplan**](Stepplan) patch_casemanagement_caseplan_stageplan_stepplan(caseplan_id, stageplan_id, stepplan_id, body)


Update the attributes of a Stepplan.

Wraps PATCH /api/v2/casemanagement/caseplans/{caseplanId}/stageplans/{stageplanId}/stepplans/{stepplanId} 

Requires ANY permissions: 

* caseManagement:stepplan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
stageplan_id = 'stageplan_id_example' # str | Stageplan identifier.
stepplan_id = 'stepplan_id_example' # str | Stepplan identifier.
body = PureCloudPlatformClientV2.StepplanUpdate() # StepplanUpdate | Stepplan update.

try:
    # Update the attributes of a Stepplan.
    api_response = api_instance.patch_casemanagement_caseplan_stageplan_stepplan(caseplan_id, stageplan_id, stepplan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_caseplan_stageplan_stepplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **stageplan_id** | **str**| Stageplan identifier. |  |
| **stepplan_id** | **str**| Stepplan identifier. |  |
| **body** | [**StepplanUpdate**](StepplanUpdate)| Stepplan update. |  |

### Return type

[**Stepplan**](Stepplan)


## post_casemanagement_case_associations

> [**CaseAssociation**](CaseAssociation) post_casemanagement_case_associations(case_id, body)


Create a Case association.

Wraps POST /api/v2/casemanagement/cases/{caseId}/associations 

Requires ANY permissions: 

* caseManagement:caseAssociation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
body = PureCloudPlatformClientV2.CaseAssociationCreate() # CaseAssociationCreate | Case association create request.

try:
    # Create a Case association.
    api_response = api_instance.post_casemanagement_case_associations(case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_case_associations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **body** | [**CaseAssociationCreate**](CaseAssociationCreate)| Case association create request. |  |

### Return type

[**CaseAssociation**](CaseAssociation)


## post_casemanagement_case_comments

> [**Comment**](Comment) post_casemanagement_case_comments(case_id, body)


Add a comment to a Case.

Wraps POST /api/v2/casemanagement/cases/{caseId}/comments 

Requires ANY permissions: 

* caseManagement:comment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.
body = PureCloudPlatformClientV2.CommentCreate() # CommentCreate | Comment create request.

try:
    # Add a comment to a Case.
    api_response = api_instance.post_casemanagement_case_comments(case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_case_comments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |
| **body** | [**CommentCreate**](CommentCreate)| Comment create request. |  |

### Return type

[**Comment**](Comment)


## post_casemanagement_case_terminate_jobs

> [**TerminateJob**](TerminateJob) post_casemanagement_case_terminate_jobs(case_id)


Create a Terminate Job for a Case.

Wraps POST /api/v2/casemanagement/cases/{caseId}/terminate/jobs 

Requires ANY permissions: 

* caseManagement:terminateJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
case_id = 'case_id_example' # str | Case identifier.

try:
    # Create a Terminate Job for a Case.
    api_response = api_instance.post_casemanagement_case_terminate_jobs(case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_case_terminate_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case identifier. |  |

### Return type

[**TerminateJob**](TerminateJob)


## post_casemanagement_caseplan_dataschemas

> [**CaseplanDataSchema**](CaseplanDataSchema) post_casemanagement_caseplan_dataschemas(caseplan_id, body)


Add a data schema to a draft Caseplan.

Wraps POST /api/v2/casemanagement/caseplans/{caseplanId}/dataschemas 

Requires ALL permissions: 

* caseManagement:caseplanDataSchemas:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
body = PureCloudPlatformClientV2.CaseplanDataSchemaRequest() # CaseplanDataSchemaRequest | Data schema reference.

try:
    # Add a data schema to a draft Caseplan.
    api_response = api_instance.post_casemanagement_caseplan_dataschemas(caseplan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_caseplan_dataschemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **body** | [**CaseplanDataSchemaRequest**](CaseplanDataSchemaRequest)| Data schema reference. |  |

### Return type

[**CaseplanDataSchema**](CaseplanDataSchema)


## post_casemanagement_caseplan_publish

> [**Caseplan**](Caseplan) post_casemanagement_caseplan_publish(caseplan_id)


Publish Caseplan.

Wraps POST /api/v2/casemanagement/caseplans/{caseplanId}/publish 

Requires ANY permissions: 

* caseManagement:caseplan:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.

try:
    # Publish Caseplan.
    api_response = api_instance.post_casemanagement_caseplan_publish(caseplan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_caseplan_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |

### Return type

[**Caseplan**](Caseplan)


## post_casemanagement_caseplan_versions

> [**Caseplan**](Caseplan) post_casemanagement_caseplan_versions(caseplan_id)


Create Caseplan version.

Wraps POST /api/v2/casemanagement/caseplans/{caseplanId}/versions 

Requires ALL permissions: 

* caseManagement:caseplan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.

try:
    # Create Caseplan version.
    api_response = api_instance.post_casemanagement_caseplan_versions(caseplan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_caseplan_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |

### Return type

[**Caseplan**](Caseplan)


## post_casemanagement_caseplans

> [**CaseplanCreateResponse**](CaseplanCreateResponse) post_casemanagement_caseplans(body)


Create a Caseplan.

Wraps POST /api/v2/casemanagement/caseplans 

Requires ANY permissions: 

* caseManagement:caseplan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
body = PureCloudPlatformClientV2.CaseplanCreate() # CaseplanCreate | Caseplan create request.

try:
    # Create a Caseplan.
    api_response = api_instance.post_casemanagement_caseplans(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_caseplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseplanCreate**](CaseplanCreate)| Caseplan create request. |  |

### Return type

[**CaseplanCreateResponse**](CaseplanCreateResponse)


## post_casemanagement_caseplans_query

> [**CaseplanQueryEntityListing**](CaseplanQueryEntityListing) post_casemanagement_caseplans_query(body)


Query for Caseplans.

This endpoint supports two filtering modes. The recommended approach uses 'filters' (generic filter model) and 'attributes' (field projection). During the migration period, the legacy fields 'name', 'nameSearchType', and 'divisionIds' remain available as an alternative.

Wraps POST /api/v2/casemanagement/caseplans/query 

Requires ANY permissions: 

* caseManagement:caseplan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
body = PureCloudPlatformClientV2.CaseplanQueryRequest() # CaseplanQueryRequest | Caseplan query request.

try:
    # Query for Caseplans.
    api_response = api_instance.post_casemanagement_caseplans_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_caseplans_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseplanQueryRequest**](CaseplanQueryRequest)| Caseplan query request. |  |

### Return type

[**CaseplanQueryEntityListing**](CaseplanQueryEntityListing)


## post_casemanagement_cases

> [**Case**](Case) post_casemanagement_cases(body)


Create a Case.

Wraps POST /api/v2/casemanagement/cases 

Requires ANY permissions: 

* caseManagement:case:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
body = PureCloudPlatformClientV2.CaseCreate() # CaseCreate | Case create request.

try:
    # Create a Case.
    api_response = api_instance.post_casemanagement_cases(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_cases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseCreate**](CaseCreate)| Case create request. |  |

### Return type

[**Case**](Case)


## post_casemanagement_cases_associations_query

> [**CaseAssociationQueryEntityListing**](CaseAssociationQueryEntityListing) post_casemanagement_cases_associations_query(body)


Query for Case associations by interaction.

Wraps POST /api/v2/casemanagement/cases/associations/query 

Requires ANY permissions: 

* caseManagement:caseAssociation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
body = PureCloudPlatformClientV2.CaseAssociationQuery() # CaseAssociationQuery | Case association query request.

try:
    # Query for Case associations by interaction.
    api_response = api_instance.post_casemanagement_cases_associations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_cases_associations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseAssociationQuery**](CaseAssociationQuery)| Case association query request. |  |

### Return type

[**CaseAssociationQueryEntityListing**](CaseAssociationQueryEntityListing)


## put_casemanagement_caseplan_dataschema

> [**CaseplanDataSchema**](CaseplanDataSchema) put_casemanagement_caseplan_dataschema(caseplan_id, schema_key_name, body)


Update a data schema on a draft Caseplan.

Wraps PUT /api/v2/casemanagement/caseplans/{caseplanId}/dataschemas/{schemaKeyName} 

Requires ALL permissions: 

* caseManagement:caseplanDataSchemas:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
schema_key_name = 'schema_key_name_example' # str | Schema key (for example \"default\").
body = PureCloudPlatformClientV2.CaseplanDataSchemaRequest() # CaseplanDataSchemaRequest | Data schema reference.

try:
    # Update a data schema on a draft Caseplan.
    api_response = api_instance.put_casemanagement_caseplan_dataschema(caseplan_id, schema_key_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->put_casemanagement_caseplan_dataschema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **schema_key_name** | **str**| Schema key (for example \&quot;default\&quot;). |  |
| **body** | [**CaseplanDataSchemaRequest**](CaseplanDataSchemaRequest)| Data schema reference. |  |

### Return type

[**CaseplanDataSchema**](CaseplanDataSchema)


## put_casemanagement_caseplan_intakesettings

> [**IntakeSettingsListing**](IntakeSettingsListing) put_casemanagement_caseplan_intakesettings(caseplan_id, body)


Update the intake settings for a Caseplan.

Wraps PUT /api/v2/casemanagement/caseplans/{caseplanId}/intakesettings 

Requires ANY permissions: 

* caseManagement:caseplanIntakeSettings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CaseManagementApi()
caseplan_id = 'caseplan_id_example' # str | Caseplan identifier.
body = PureCloudPlatformClientV2.IntakeSettingsUpdate() # IntakeSettingsUpdate | Intake settings update.

try:
    # Update the intake settings for a Caseplan.
    api_response = api_instance.put_casemanagement_caseplan_intakesettings(caseplan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->put_casemanagement_caseplan_intakesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan identifier. |  |
| **body** | [**IntakeSettingsUpdate**](IntakeSettingsUpdate)| Intake settings update. |  |

### Return type

[**IntakeSettingsListing**](IntakeSettingsListing)


_PureCloudPlatformClientV2 263.0.0_
