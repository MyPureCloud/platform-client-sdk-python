# CaseManagementApi

## PureCloudPlatformClientV2.CaseManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_casemanagement_case**](#delete_casemanagement_case) | Delete a Case.|
|[**delete_casemanagement_caseplan**](#delete_casemanagement_caseplan) | Delete a Caseplan.|
|[**get_casemanagement_case**](#get_casemanagement_case) | Get a Case.|
|[**get_casemanagement_case_association**](#get_casemanagement_case_association) | Get a Case Association.|
|[**get_casemanagement_case_associations**](#get_casemanagement_case_associations) | Get a list of case associations for a provided case.|
|[**get_casemanagement_case_stage**](#get_casemanagement_case_stage) | Get a Stage.|
|[**get_casemanagement_case_stage_step**](#get_casemanagement_case_stage_step) | Get a Step.|
|[**get_casemanagement_case_stage_steps**](#get_casemanagement_case_stage_steps) | Get a list of Steps.|
|[**get_casemanagement_case_stages**](#get_casemanagement_case_stages) | Get a list of Stages.|
|[**get_casemanagement_case_terminate_job**](#get_casemanagement_case_terminate_job) | Get a Terminate Job for a Case.|
|[**get_casemanagement_caseplan**](#get_casemanagement_caseplan) | Get a Caseplan.|
|[**get_casemanagement_caseplan_version**](#get_casemanagement_caseplan_version) | Get a Caseplan version.|
|[**get_casemanagement_caseplan_version_dataschemas**](#get_casemanagement_caseplan_version_dataschemas) | Get the dataSchemas for a caseplan version.|
|[**get_casemanagement_caseplan_version_intakesettings**](#get_casemanagement_caseplan_version_intakesettings) | Get the intake settings for a Caseplan version.|
|[**get_casemanagement_caseplan_version_stageplan**](#get_casemanagement_caseplan_version_stageplan) | Get a Stageplan.|
|[**get_casemanagement_caseplan_version_stageplan_stepplan**](#get_casemanagement_caseplan_version_stageplan_stepplan) | Get a Stepplan.|
|[**get_casemanagement_caseplan_version_stageplan_stepplans**](#get_casemanagement_caseplan_version_stageplan_stepplans) | Get a list of Stepplans.|
|[**get_casemanagement_caseplan_version_stageplans**](#get_casemanagement_caseplan_version_stageplans) | Get a list of Stageplans.|
|[**get_casemanagement_caseplans**](#get_casemanagement_caseplans) | Get a list of Caseplans.|
|[**get_casemanagement_cases_externalcontact**](#get_casemanagement_cases_externalcontact) | Get a list of cases for provided external contact id.|
|[**get_casemanagement_cases_reference**](#get_casemanagement_cases_reference) | Get a Case by reference.|
|[**patch_casemanagement_case_datedue**](#patch_casemanagement_case_datedue) | Update date due of a Case.|
|[**patch_casemanagement_case_priority**](#patch_casemanagement_case_priority) | Update priority of a Case.|
|[**patch_casemanagement_case_summary**](#patch_casemanagement_case_summary) | Update summary of a Case.|
|[**patch_casemanagement_caseplan**](#patch_casemanagement_caseplan) | Update the attributes of a Caseplan.|
|[**patch_casemanagement_caseplan_stageplan**](#patch_casemanagement_caseplan_stageplan) | Update the attributes of a Stageplan.|
|[**patch_casemanagement_caseplan_stageplan_stepplan**](#patch_casemanagement_caseplan_stageplan_stepplan) | Update the attributes of a Stepplan.|
|[**post_casemanagement_case_associations**](#post_casemanagement_case_associations) | Create a case association.|
|[**post_casemanagement_case_terminate_jobs**](#post_casemanagement_case_terminate_jobs) | Create a Terminate Job for a Case.|
|[**post_casemanagement_caseplan_publish**](#post_casemanagement_caseplan_publish) | Publish Caseplan.|
|[**post_casemanagement_caseplan_versions**](#post_casemanagement_caseplan_versions) | Create Caseplan version.|
|[**post_casemanagement_caseplans**](#post_casemanagement_caseplans) | Create a Caseplan.|
|[**post_casemanagement_caseplans_query**](#post_casemanagement_caseplans_query) | Query for caseplans|
|[**post_casemanagement_cases**](#post_casemanagement_cases) | Create a Case.|
|[**post_casemanagement_cases_associations_query**](#post_casemanagement_cases_associations_query) | Query for case associations|
|[**put_casemanagement_caseplan_intakesettings**](#put_casemanagement_caseplan_intakesettings) | Update the intake settings for a Caseplan.|



## delete_casemanagement_case

> object** delete_casemanagement_case(case_id)


Delete a Case.

delete_casemanagement_case is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID

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
| **case_id** | **str**| Case ID |  |

### Return type

**object**


## delete_casemanagement_caseplan

> object** delete_casemanagement_caseplan(caseplan_id)


Delete a Caseplan.

delete_casemanagement_caseplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID

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
| **caseplan_id** | **str**| Caseplan ID |  |

### Return type

**object**


## get_casemanagement_case

> [**Case**](Case) get_casemanagement_case(case_id, expands=expands)


Get a Case.

get_casemanagement_case is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
expands = 'expands_example' # str | Which fields to expand. (optional)

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
| **case_id** | **str**| Case ID |  |
| **expands** | **str**| Which fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**Case**](Case)


## get_casemanagement_case_association

> [**CaseAssociation**](CaseAssociation) get_casemanagement_case_association(case_id, association_id)


Get a Case Association.

get_casemanagement_case_association is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
association_id = 'association_id_example' # str | Case Association ID

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
| **case_id** | **str**| Case ID |  |
| **association_id** | **str**| Case Association ID |  |

### Return type

[**CaseAssociation**](CaseAssociation)


## get_casemanagement_case_associations

> [**CaseAssociationListing**](CaseAssociationListing) get_casemanagement_case_associations(case_id, before=before, after=after, page_size=page_size)


Get a list of case associations for a provided case.

get_casemanagement_case_associations is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get a list of case associations for a provided case.
    api_response = api_instance.get_casemanagement_case_associations(case_id, before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_case_associations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case ID. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**CaseAssociationListing**](CaseAssociationListing)


## get_casemanagement_case_stage

> [**Stage**](Stage) get_casemanagement_case_stage(case_id, stage_id)


Get a Stage.

get_casemanagement_case_stage is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
stage_id = 'stage_id_example' # str | Stage ID

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
| **case_id** | **str**| Case ID |  |
| **stage_id** | **str**| Stage ID |  |

### Return type

[**Stage**](Stage)


## get_casemanagement_case_stage_step

> [**Step**](Step) get_casemanagement_case_stage_step(case_id, stage_id, step_id)


Get a Step.

get_casemanagement_case_stage_step is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
stage_id = 'stage_id_example' # str | Stage ID
step_id = 'step_id_example' # str | Step ID

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
| **case_id** | **str**| Case ID |  |
| **stage_id** | **str**| Stage ID |  |
| **step_id** | **str**| Step ID |  |

### Return type

[**Step**](Step)


## get_casemanagement_case_stage_steps

> [**StepListing**](StepListing) get_casemanagement_case_stage_steps(case_id, stage_id, before=before, after=after, page_size=page_size)


Get a list of Steps.

get_casemanagement_case_stage_steps is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
stage_id = 'stage_id_example' # str | Stage ID
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
| **case_id** | **str**| Case ID |  |
| **stage_id** | **str**| Stage ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**StepListing**](StepListing)


## get_casemanagement_case_stages

> [**StageListing**](StageListing) get_casemanagement_case_stages(case_id, before=before, after=after, page_size=page_size)


Get a list of Stages.

get_casemanagement_case_stages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
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
| **case_id** | **str**| Case ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**StageListing**](StageListing)


## get_casemanagement_case_terminate_job

> [**TerminateJob**](TerminateJob) get_casemanagement_case_terminate_job(case_id, job_id)


Get a Terminate Job for a Case.

get_casemanagement_case_terminate_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
job_id = 'job_id_example' # str | Job ID

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
| **case_id** | **str**| Case ID |  |
| **job_id** | **str**| Job ID |  |

### Return type

[**TerminateJob**](TerminateJob)


## get_casemanagement_caseplan

> [**Caseplan**](Caseplan) get_casemanagement_caseplan(caseplan_id)


Get a Caseplan.

get_casemanagement_caseplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID

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
| **caseplan_id** | **str**| Caseplan ID |  |

### Return type

[**Caseplan**](Caseplan)


## get_casemanagement_caseplan_version

> [**Caseplan**](Caseplan) get_casemanagement_caseplan_version(caseplan_id, version_id)


Get a Caseplan version.

get_casemanagement_caseplan_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version of the caseplan

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version of the caseplan |  |

### Return type

[**Caseplan**](Caseplan)


## get_casemanagement_caseplan_version_dataschemas

> [**CaseplanDataSchemaListing**](CaseplanDataSchemaListing) get_casemanagement_caseplan_version_dataschemas(caseplan_id, version_id)


Get the dataSchemas for a caseplan version.

get_casemanagement_caseplan_version_dataschemas is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version of the caseplan

try:
    # Get the dataSchemas for a caseplan version.
    api_response = api_instance.get_casemanagement_caseplan_version_dataschemas(caseplan_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_caseplan_version_dataschemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version of the caseplan |  |

### Return type

[**CaseplanDataSchemaListing**](CaseplanDataSchemaListing)


## get_casemanagement_caseplan_version_intakesettings

> [**IntakeSettingsListing**](IntakeSettingsListing) get_casemanagement_caseplan_version_intakesettings(caseplan_id, version_id)


Get the intake settings for a Caseplan version.

get_casemanagement_caseplan_version_intakesettings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version of the caseplan

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version of the caseplan |  |

### Return type

[**IntakeSettingsListing**](IntakeSettingsListing)


## get_casemanagement_caseplan_version_stageplan

> [**Stageplan**](Stageplan) get_casemanagement_caseplan_version_stageplan(caseplan_id, version_id, stageplan_id, expands=expands)


Get a Stageplan.

get_casemanagement_caseplan_version_stageplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version ID
stageplan_id = 'stageplan_id_example' # str | Stageplan ID
expands = ['expands_example'] # list[str] | Which fields to expand. (optional)

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version ID |  |
| **stageplan_id** | **str**| Stageplan ID |  |
| **expands** | [**list[str]**](str)| Which fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**Stageplan**](Stageplan)


## get_casemanagement_caseplan_version_stageplan_stepplan

> [**Stepplan**](Stepplan) get_casemanagement_caseplan_version_stageplan_stepplan(caseplan_id, version_id, stageplan_id, stepplan_id, expands=expands)


Get a Stepplan.

get_casemanagement_caseplan_version_stageplan_stepplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version ID
stageplan_id = 'stageplan_id_example' # str | Stageplan ID
stepplan_id = 'stepplan_id_example' # str | Stepplan ID
expands = ['expands_example'] # list[str] | Which fields to expand. (optional)

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version ID |  |
| **stageplan_id** | **str**| Stageplan ID |  |
| **stepplan_id** | **str**| Stepplan ID |  |
| **expands** | [**list[str]**](str)| Which fields to expand. | [optional] <br />**Values**: stageplan, caseplan, worktype |

### Return type

[**Stepplan**](Stepplan)


## get_casemanagement_caseplan_version_stageplan_stepplans

> [**StepplanListing**](StepplanListing) get_casemanagement_caseplan_version_stageplan_stepplans(caseplan_id, version_id, stageplan_id, before=before, after=after, page_size=page_size, expands=expands)


Get a list of Stepplans.

get_casemanagement_caseplan_version_stageplan_stepplans is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version ID
stageplan_id = 'stageplan_id_example' # str | Stageplan ID
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
expands = ['expands_example'] # list[str] | Which fields to expand. (optional)

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version ID |  |
| **stageplan_id** | **str**| Stageplan ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **expands** | [**list[str]**](str)| Which fields to expand. | [optional] <br />**Values**: caseplan, stageplan, worktype |

### Return type

[**StepplanListing**](StepplanListing)


## get_casemanagement_caseplan_version_stageplans

> [**StageplanListing**](StageplanListing) get_casemanagement_caseplan_version_stageplans(caseplan_id, version_id, before=before, after=after, page_size=page_size, expands=expands)


Get a list of Stageplans.

get_casemanagement_caseplan_version_stageplans is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
version_id = 'version_id_example' # str | Version ID
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
expands = ['expands_example'] # list[str] | Which fields to expand. (optional)

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **version_id** | **str**| Version ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **expands** | [**list[str]**](str)| Which fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**StageplanListing**](StageplanListing)


## get_casemanagement_caseplans

> [**CaseplanListing**](CaseplanListing) get_casemanagement_caseplans(after=after, page_size=page_size, customer_intent_id=customer_intent_id, division_ids=division_ids)


Get a list of Caseplans.

get_casemanagement_caseplans is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
after = 'after_example' # str | The cursor that points to the end of the set of caseplans that has been returned. (optional)
page_size = 56 # int | Number of caseplans to return. Maximum of 200. (optional)
customer_intent_id = 'customer_intent_id_example' # str | Filter by Customer Intent. (optional)
division_ids = 'division_ids_example' # str | Filter by Divisions. (optional)

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
| **after** | **str**| The cursor that points to the end of the set of caseplans that has been returned. | [optional]  |
| **page_size** | **int**| Number of caseplans to return. Maximum of 200. | [optional]  |
| **customer_intent_id** | **str**| Filter by Customer Intent. | [optional]  |
| **division_ids** | **str**| Filter by Divisions. | [optional]  |

### Return type

[**CaseplanListing**](CaseplanListing)


## get_casemanagement_cases_externalcontact

> [**CaseListing**](CaseListing) get_casemanagement_cases_externalcontact(external_contact_id, after=after, page_size=page_size, division_ids=division_ids, expands=expands)


Get a list of cases for provided external contact id.

get_casemanagement_cases_externalcontact is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
external_contact_id = 'external_contact_id_example' # str | External Contact ID
after = 'after_example' # str | The cursor that points to the end of the set of cases that has been returned. (optional)
page_size = 56 # int | Number of cases to return. Maximum of 200. (optional)
division_ids = 'division_ids_example' # str | Filter by Divisions (optional)
expands = ['expands_example'] # list[str] | Which fields to expand. (optional)

try:
    # Get a list of cases for provided external contact id.
    api_response = api_instance.get_casemanagement_cases_externalcontact(external_contact_id, after=after, page_size=page_size, division_ids=division_ids, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->get_casemanagement_cases_externalcontact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_contact_id** | **str**| External Contact ID |  |
| **after** | **str**| The cursor that points to the end of the set of cases that has been returned. | [optional]  |
| **page_size** | **int**| Number of cases to return. Maximum of 200. | [optional]  |
| **division_ids** | **str**| Filter by Divisions | [optional]  |
| **expands** | [**list[str]**](str)| Which fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**CaseListing**](CaseListing)


## get_casemanagement_cases_reference

> [**Case**](Case) get_casemanagement_cases_reference(reference_id, expands=expands)


Get a Case by reference.

get_casemanagement_cases_reference is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
reference_id = 'reference_id_example' # str | Reference
expands = 'expands_example' # str | Which fields to expand. (optional)

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
| **reference_id** | **str**| Reference |  |
| **expands** | **str**| Which fields to expand. | [optional] <br />**Values**: caseplan |

### Return type

[**Case**](Case)


## patch_casemanagement_case_datedue

> [**Case**](Case) patch_casemanagement_case_datedue(case_id, body)


Update date due of a Case.

patch_casemanagement_case_datedue is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
body = PureCloudPlatformClientV2.CaseDateDueUpdate() # CaseDateDueUpdate | Date due

try:
    # Update date due of a Case.
    api_response = api_instance.patch_casemanagement_case_datedue(case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->patch_casemanagement_case_datedue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case ID |  |
| **body** | [**CaseDateDueUpdate**](CaseDateDueUpdate)| Date due |  |

### Return type

[**Case**](Case)


## patch_casemanagement_case_priority

> [**Case**](Case) patch_casemanagement_case_priority(case_id, body)


Update priority of a Case.

patch_casemanagement_case_priority is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
body = PureCloudPlatformClientV2.CasePriorityUpdate() # CasePriorityUpdate | Priority

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
| **case_id** | **str**| Case ID |  |
| **body** | [**CasePriorityUpdate**](CasePriorityUpdate)| Priority |  |

### Return type

[**Case**](Case)


## patch_casemanagement_case_summary

> [**Case**](Case) patch_casemanagement_case_summary(case_id, body)


Update summary of a Case.

patch_casemanagement_case_summary is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID
body = PureCloudPlatformClientV2.CaseSummaryUpdate() # CaseSummaryUpdate | Summary

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
| **case_id** | **str**| Case ID |  |
| **body** | [**CaseSummaryUpdate**](CaseSummaryUpdate)| Summary |  |

### Return type

[**Case**](Case)


## patch_casemanagement_caseplan

> [**Caseplan**](Caseplan) patch_casemanagement_caseplan(caseplan_id, body)


Update the attributes of a Caseplan.

patch_casemanagement_caseplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
body = PureCloudPlatformClientV2.CaseplanUpdate() # CaseplanUpdate | Caseplan

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **body** | [**CaseplanUpdate**](CaseplanUpdate)| Caseplan |  |

### Return type

[**Caseplan**](Caseplan)


## patch_casemanagement_caseplan_stageplan

> [**Stageplan**](Stageplan) patch_casemanagement_caseplan_stageplan(caseplan_id, stageplan_id, body)


Update the attributes of a Stageplan.

patch_casemanagement_caseplan_stageplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
stageplan_id = 'stageplan_id_example' # str | Stageplan ID
body = PureCloudPlatformClientV2.StageplanUpdate() # StageplanUpdate | Stageplan

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **stageplan_id** | **str**| Stageplan ID |  |
| **body** | [**StageplanUpdate**](StageplanUpdate)| Stageplan |  |

### Return type

[**Stageplan**](Stageplan)


## patch_casemanagement_caseplan_stageplan_stepplan

> [**Stepplan**](Stepplan) patch_casemanagement_caseplan_stageplan_stepplan(caseplan_id, stageplan_id, stepplan_id, body)


Update the attributes of a Stepplan.

patch_casemanagement_caseplan_stageplan_stepplan is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
stageplan_id = 'stageplan_id_example' # str | Stageplan ID
stepplan_id = 'stepplan_id_example' # str | Stepplan ID
body = PureCloudPlatformClientV2.StepplanUpdate() # StepplanUpdate | Stepplan

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **stageplan_id** | **str**| Stageplan ID |  |
| **stepplan_id** | **str**| Stepplan ID |  |
| **body** | [**StepplanUpdate**](StepplanUpdate)| Stepplan |  |

### Return type

[**Stepplan**](Stepplan)


## post_casemanagement_case_associations

> [**CaseAssociation**](CaseAssociation) post_casemanagement_case_associations(case_id, body=body)


Create a case association.

post_casemanagement_case_associations is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID.
body = PureCloudPlatformClientV2.CaseAssociationCreate() # CaseAssociationCreate | Case Association (optional)

try:
    # Create a case association.
    api_response = api_instance.post_casemanagement_case_associations(case_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_case_associations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **case_id** | **str**| Case ID. |  |
| **body** | [**CaseAssociationCreate**](CaseAssociationCreate)| Case Association | [optional]  |

### Return type

[**CaseAssociation**](CaseAssociation)


## post_casemanagement_case_terminate_jobs

> [**TerminateJob**](TerminateJob) post_casemanagement_case_terminate_jobs(case_id)


Create a Terminate Job for a Case.

post_casemanagement_case_terminate_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
case_id = 'case_id_example' # str | Case ID

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
| **case_id** | **str**| Case ID |  |

### Return type

[**TerminateJob**](TerminateJob)


## post_casemanagement_caseplan_publish

> [**Caseplan**](Caseplan) post_casemanagement_caseplan_publish(caseplan_id)


Publish Caseplan.

post_casemanagement_caseplan_publish is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID

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
| **caseplan_id** | **str**| Caseplan ID |  |

### Return type

[**Caseplan**](Caseplan)


## post_casemanagement_caseplan_versions

> [**Caseplan**](Caseplan) post_casemanagement_caseplan_versions(caseplan_id)


Create Caseplan version.

post_casemanagement_caseplan_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID

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
| **caseplan_id** | **str**| Caseplan ID |  |

### Return type

[**Caseplan**](Caseplan)


## post_casemanagement_caseplans

> [**CaseplanCreateResponse**](CaseplanCreateResponse) post_casemanagement_caseplans(body)


Create a Caseplan.

post_casemanagement_caseplans is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
body = PureCloudPlatformClientV2.CaseplanCreate() # CaseplanCreate | Caseplan

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
| **body** | [**CaseplanCreate**](CaseplanCreate)| Caseplan |  |

### Return type

[**CaseplanCreateResponse**](CaseplanCreateResponse)


## post_casemanagement_caseplans_query

> [**CaseplanQueryEntityListing**](CaseplanQueryEntityListing) post_casemanagement_caseplans_query(body)


Query for caseplans

post_casemanagement_caseplans_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
body = PureCloudPlatformClientV2.CaseplanQueryRequest() # CaseplanQueryRequest | CaseplanQueryRequest

try:
    # Query for caseplans
    api_response = api_instance.post_casemanagement_caseplans_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_caseplans_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseplanQueryRequest**](CaseplanQueryRequest)| CaseplanQueryRequest |  |

### Return type

[**CaseplanQueryEntityListing**](CaseplanQueryEntityListing)


## post_casemanagement_cases

> [**Case**](Case) post_casemanagement_cases(body)


Create a Case.

post_casemanagement_cases is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
body = PureCloudPlatformClientV2.CaseCreate() # CaseCreate | Case

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
| **body** | [**CaseCreate**](CaseCreate)| Case |  |

### Return type

[**Case**](Case)


## post_casemanagement_cases_associations_query

> [**CaseAssociationQueryEntityListing**](CaseAssociationQueryEntityListing) post_casemanagement_cases_associations_query(body=body)


Query for case associations

post_casemanagement_cases_associations_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
body = PureCloudPlatformClientV2.CaseAssociationQuery() # CaseAssociationQuery | Case Association (optional)

try:
    # Query for case associations
    api_response = api_instance.post_casemanagement_cases_associations_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseManagementApi->post_casemanagement_cases_associations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseAssociationQuery**](CaseAssociationQuery)| Case Association | [optional]  |

### Return type

[**CaseAssociationQueryEntityListing**](CaseAssociationQueryEntityListing)


## put_casemanagement_caseplan_intakesettings

> [**IntakeSettingsListing**](IntakeSettingsListing) put_casemanagement_caseplan_intakesettings(caseplan_id, body)


Update the intake settings for a Caseplan.

put_casemanagement_caseplan_intakesettings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
caseplan_id = 'caseplan_id_example' # str | Caseplan ID
body = PureCloudPlatformClientV2.IntakeSettingsUpdate() # IntakeSettingsUpdate | Intake Settings

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
| **caseplan_id** | **str**| Caseplan ID |  |
| **body** | [**IntakeSettingsUpdate**](IntakeSettingsUpdate)| Intake Settings |  |

### Return type

[**IntakeSettingsListing**](IntakeSettingsListing)


_PureCloudPlatformClientV2 257.0.0_
