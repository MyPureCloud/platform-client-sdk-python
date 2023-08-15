---
title: QualityApi
---

## PureCloudPlatformClientV2.QualityApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_quality_calibration**](QualityApi.html#delete_quality_calibration) | Delete a calibration by id.|
|[**delete_quality_conversation_evaluation**](QualityApi.html#delete_quality_conversation_evaluation) | Delete an evaluation|
|[**delete_quality_form**](QualityApi.html#delete_quality_form) | Delete an evaluation form.|
|[**delete_quality_forms_evaluation**](QualityApi.html#delete_quality_forms_evaluation) | Delete an evaluation form.|
|[**delete_quality_forms_survey**](QualityApi.html#delete_quality_forms_survey) | Delete a survey form.|
|[**get_analytics_evaluations_aggregates_job**](QualityApi.html#get_analytics_evaluations_aggregates_job) | Get status for async query for evaluation aggregates|
|[**get_analytics_evaluations_aggregates_job_results**](QualityApi.html#get_analytics_evaluations_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_surveys_aggregates_job**](QualityApi.html#get_analytics_surveys_aggregates_job) | Get status for async query for survey aggregates|
|[**get_analytics_surveys_aggregates_job_results**](QualityApi.html#get_analytics_surveys_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_quality_agents_activity**](QualityApi.html#get_quality_agents_activity) | Gets a list of Agent Activities|
|[**get_quality_calibration**](QualityApi.html#get_quality_calibration) | Get a calibration by id.  Requires either calibrator id or conversation id|
|[**get_quality_calibrations**](QualityApi.html#get_quality_calibrations) | Get the list of calibrations|
|[**get_quality_conversation_evaluation**](QualityApi.html#get_quality_conversation_evaluation) | Get an evaluation|
|[**get_quality_conversation_surveys**](QualityApi.html#get_quality_conversation_surveys) | Get the surveys for a conversation|
|[**get_quality_conversations_audits_query_transaction_id**](QualityApi.html#get_quality_conversations_audits_query_transaction_id) | Get status of audit query execution|
|[**get_quality_conversations_audits_query_transaction_id_results**](QualityApi.html#get_quality_conversations_audits_query_transaction_id_results) | Get results of audit query|
|[**get_quality_evaluations_query**](QualityApi.html#get_quality_evaluations_query) | Queries Evaluations and returns a paged list|
|[**get_quality_evaluators_activity**](QualityApi.html#get_quality_evaluators_activity) | Get an evaluator activity|
|[**get_quality_form**](QualityApi.html#get_quality_form) | Get an evaluation form|
|[**get_quality_form_versions**](QualityApi.html#get_quality_form_versions) | Gets all the revisions for a specific evaluation.|
|[**get_quality_forms**](QualityApi.html#get_quality_forms) | Get the list of evaluation forms|
|[**get_quality_forms_evaluation**](QualityApi.html#get_quality_forms_evaluation) | Get an evaluation form|
|[**get_quality_forms_evaluation_versions**](QualityApi.html#get_quality_forms_evaluation_versions) | Gets all the revisions for a specific evaluation.|
|[**get_quality_forms_evaluations**](QualityApi.html#get_quality_forms_evaluations) | Get the list of evaluation forms|
|[**get_quality_forms_evaluations_bulk_contexts**](QualityApi.html#get_quality_forms_evaluations_bulk_contexts) | Retrieve a list of the latest published evaluation form versions by context ids|
|[**get_quality_forms_survey**](QualityApi.html#get_quality_forms_survey) | Get a survey form|
|[**get_quality_forms_survey_versions**](QualityApi.html#get_quality_forms_survey_versions) | Gets all the revisions for a specific survey.|
|[**get_quality_forms_surveys**](QualityApi.html#get_quality_forms_surveys) | Get the list of survey forms|
|[**get_quality_forms_surveys_bulk**](QualityApi.html#get_quality_forms_surveys_bulk) | Retrieve a list of survey forms by their ids|
|[**get_quality_forms_surveys_bulk_contexts**](QualityApi.html#get_quality_forms_surveys_bulk_contexts) | Retrieve a list of the latest form versions by context ids|
|[**get_quality_publishedform**](QualityApi.html#get_quality_publishedform) | Get the published evaluation forms.|
|[**get_quality_publishedforms**](QualityApi.html#get_quality_publishedforms) | Get the published evaluation forms.|
|[**get_quality_publishedforms_evaluation**](QualityApi.html#get_quality_publishedforms_evaluation) | Get the most recent published version of an evaluation form.|
|[**get_quality_publishedforms_evaluations**](QualityApi.html#get_quality_publishedforms_evaluations) | Get the published evaluation forms.|
|[**get_quality_publishedforms_survey**](QualityApi.html#get_quality_publishedforms_survey) | Get the most recent published version of a survey form.|
|[**get_quality_publishedforms_surveys**](QualityApi.html#get_quality_publishedforms_surveys) | Get the published survey forms.|
|[**get_quality_survey**](QualityApi.html#get_quality_survey) | Get a survey for a conversation|
|[**get_quality_surveys_scorable**](QualityApi.html#get_quality_surveys_scorable) | Get a survey as an end-customer, for the purposes of scoring it.|
|[**patch_quality_forms_survey**](QualityApi.html#patch_quality_forms_survey) | Disable a particular version of a survey form and invalidates any invitations that have already been sent to customers using this version of the form.|
|[**post_analytics_evaluations_aggregates_jobs**](QualityApi.html#post_analytics_evaluations_aggregates_jobs) | Query for evaluation aggregates asynchronously|
|[**post_analytics_evaluations_aggregates_query**](QualityApi.html#post_analytics_evaluations_aggregates_query) | Query for evaluation aggregates|
|[**post_analytics_surveys_aggregates_jobs**](QualityApi.html#post_analytics_surveys_aggregates_jobs) | Query for survey aggregates asynchronously|
|[**post_analytics_surveys_aggregates_query**](QualityApi.html#post_analytics_surveys_aggregates_query) | Query for survey aggregates|
|[**post_quality_calibrations**](QualityApi.html#post_quality_calibrations) | Create a calibration|
|[**post_quality_conversation_evaluations**](QualityApi.html#post_quality_conversation_evaluations) | Create an evaluation|
|[**post_quality_conversations_audits_query**](QualityApi.html#post_quality_conversations_audits_query) | Create audit query execution|
|[**post_quality_evaluations_aggregates_query_me**](QualityApi.html#post_quality_evaluations_aggregates_query_me) | Query for evaluation aggregates for the current user|
|[**post_quality_evaluations_scoring**](QualityApi.html#post_quality_evaluations_scoring) | Score evaluation|
|[**post_quality_forms**](QualityApi.html#post_quality_forms) | Create an evaluation form.|
|[**post_quality_forms_evaluations**](QualityApi.html#post_quality_forms_evaluations) | Create an evaluation form.|
|[**post_quality_forms_surveys**](QualityApi.html#post_quality_forms_surveys) | Create a survey form.|
|[**post_quality_publishedforms**](QualityApi.html#post_quality_publishedforms) | Publish an evaluation form.|
|[**post_quality_publishedforms_evaluations**](QualityApi.html#post_quality_publishedforms_evaluations) | Publish an evaluation form.|
|[**post_quality_publishedforms_surveys**](QualityApi.html#post_quality_publishedforms_surveys) | Publish a survey form.|
|[**post_quality_surveys_scoring**](QualityApi.html#post_quality_surveys_scoring) | Score survey|
|[**put_quality_calibration**](QualityApi.html#put_quality_calibration) | Update a calibration to the specified calibration via PUT.  Editable fields include: evaluators, expertEvaluator, and scoringIndex|
|[**put_quality_conversation_evaluation**](QualityApi.html#put_quality_conversation_evaluation) | Update an evaluation|
|[**put_quality_form**](QualityApi.html#put_quality_form) | Update an evaluation form.|
|[**put_quality_forms_evaluation**](QualityApi.html#put_quality_forms_evaluation) | Update an evaluation form.|
|[**put_quality_forms_survey**](QualityApi.html#put_quality_forms_survey) | Update a survey form.|
|[**put_quality_surveys_scorable**](QualityApi.html#put_quality_surveys_scorable) | Update a survey as an end-customer, for the purposes of scoring it.|
{: class="table table-striped"}

<a name="delete_quality_calibration"></a>

## [**Calibration**](Calibration.html) delete_quality_calibration(calibration_id, calibrator_id)



Delete a calibration by id.

Wraps DELETE /api/v2/quality/calibrations/{calibrationId} 

Requires ANY permissions: 

* quality:calibration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
calibration_id = 'calibration_id_example' # str | Calibration ID
calibrator_id = 'calibrator_id_example' # str | calibratorId

try:
    # Delete a calibration by id.
    api_response = api_instance.delete_quality_calibration(calibration_id, calibrator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->delete_quality_calibration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **calibration_id** | **str**| Calibration ID |  |
| **calibrator_id** | **str**| calibratorId |  |
{: class="table table-striped"}

### Return type

[**Calibration**](Calibration.html)

<a name="delete_quality_conversation_evaluation"></a>

## [**EvaluationResponse**](EvaluationResponse.html) delete_quality_conversation_evaluation(conversation_id, evaluation_id, expand=expand)



Delete an evaluation

Wraps DELETE /api/v2/quality/conversations/{conversationId}/evaluations/{evaluationId} 

Requires ANY permissions: 

* quality:evaluation:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
conversation_id = 'conversation_id_example' # str | conversationId
evaluation_id = 'evaluation_id_example' # str | evaluationId
expand = 'expand_example' # str | evaluatorId, evaluationForm (optional)

try:
    # Delete an evaluation
    api_response = api_instance.delete_quality_conversation_evaluation(conversation_id, evaluation_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->delete_quality_conversation_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **evaluation_id** | **str**| evaluationId |  |
| **expand** | **str**| evaluatorId, evaluationForm | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationResponse**](EvaluationResponse.html)

<a name="delete_quality_form"></a>

##  delete_quality_form(form_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete an evaluation form.

Wraps DELETE /api/v2/quality/forms/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Delete an evaluation form.
    api_instance.delete_quality_form(form_id)
except ApiException as e:
    print("Exception when calling QualityApi->delete_quality_form: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_quality_forms_evaluation"></a>

##  delete_quality_forms_evaluation(form_id)



Delete an evaluation form.

Wraps DELETE /api/v2/quality/forms/evaluations/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Delete an evaluation form.
    api_instance.delete_quality_forms_evaluation(form_id)
except ApiException as e:
    print("Exception when calling QualityApi->delete_quality_forms_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_quality_forms_survey"></a>

##  delete_quality_forms_survey(form_id)



Delete a survey form.

Wraps DELETE /api/v2/quality/forms/surveys/{formId} 

Requires ALL permissions: 

* quality:surveyForm:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Delete a survey form.
    api_instance.delete_quality_forms_survey(form_id)
except ApiException as e:
    print("Exception when calling QualityApi->delete_quality_forms_survey: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_analytics_evaluations_aggregates_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_evaluations_aggregates_job(job_id)



Get status for async query for evaluation aggregates

get_analytics_evaluations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/evaluations/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for evaluation aggregates
    api_response = api_instance.get_analytics_evaluations_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_analytics_evaluations_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_evaluations_aggregates_job_results"></a>

## [**EvaluationAsyncAggregateQueryResponse**](EvaluationAsyncAggregateQueryResponse.html) get_analytics_evaluations_aggregates_job_results(job_id, cursor=cursor)



Fetch a page of results for an async aggregates query

get_analytics_evaluations_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/evaluations/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_evaluations_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_analytics_evaluations_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationAsyncAggregateQueryResponse**](EvaluationAsyncAggregateQueryResponse.html)

<a name="get_analytics_surveys_aggregates_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_surveys_aggregates_job(job_id)



Get status for async query for survey aggregates

get_analytics_surveys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/surveys/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for survey aggregates
    api_response = api_instance.get_analytics_surveys_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_analytics_surveys_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_surveys_aggregates_job_results"></a>

## [**SurveyAsyncAggregateQueryResponse**](SurveyAsyncAggregateQueryResponse.html) get_analytics_surveys_aggregates_job_results(job_id, cursor=cursor)



Fetch a page of results for an async aggregates query

get_analytics_surveys_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/surveys/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_surveys_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_analytics_surveys_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |
{: class="table table-striped"}

### Return type

[**SurveyAsyncAggregateQueryResponse**](SurveyAsyncAggregateQueryResponse.html)

<a name="get_quality_agents_activity"></a>

## [**AgentActivityEntityListing**](AgentActivityEntityListing.html) get_quality_agents_activity(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, start_time=start_time, end_time=end_time, agent_user_id=agent_user_id, evaluator_user_id=evaluator_user_id, name=name, group=group)



Gets a list of Agent Activities

Each item on the list shows one agent's evaluation activity comprised of the number of evaluations and the highest, average, and lowest standard and critical scores, as well as a sub list showing the number and average score of evaluations for each evaluator for that agent.  evaluatorUserId, startTime, and endTime are all filtering criteria. If specified, the only evaluations used to compile the agent activity response will be ones that match the filtering criteria. agentUserId, name, group, and agentTeamId are all agent selection criteria. criteria.  If one or more agent selection criteria are specified, then the returned activity will include users that match the criteria even if those users did not have any agent activity or evaluations that do not match any filtering criteria.  If no agent selection criteria are specified but an evaluatorUserId is, then the returned activity will be only for those agents that had evaluations where the evaluator is the evaluatorUserId.  If no agent selection criteria are specified and no evaluatorUserId is specified, then the returned activity will be for all users

Wraps GET /api/v2/quality/agents/activity 

Requires ANY permissions: 

* quality:evaluation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | Start time of agent activity based on assigned date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | End time of agent activity based on assigned date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)
agent_user_id = ['agent_user_id_example'] # list[str] | user id of agent requested (optional)
evaluator_user_id = 'evaluator_user_id_example' # str | user id of the evaluator (optional)
name = 'name_example' # str | name (optional)
group = 'group_example' # str | group id (optional)

try:
    # Gets a list of Agent Activities
    api_response = api_instance.get_quality_agents_activity(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, start_time=start_time, end_time=end_time, agent_user_id=agent_user_id, evaluator_user_id=evaluator_user_id, name=name, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_agents_activity: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **start_time** | **datetime**| Start time of agent activity based on assigned date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
| **end_time** | **datetime**| End time of agent activity based on assigned date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
| **agent_user_id** | [**list[str]**](str.html)| user id of agent requested | [optional]  |
| **evaluator_user_id** | **str**| user id of the evaluator | [optional]  |
| **name** | **str**| name | [optional]  |
| **group** | **str**| group id | [optional]  |
{: class="table table-striped"}

### Return type

[**AgentActivityEntityListing**](AgentActivityEntityListing.html)

<a name="get_quality_calibration"></a>

## [**Calibration**](Calibration.html) get_quality_calibration(calibration_id, calibrator_id=calibrator_id, conversation_id=conversation_id)



Get a calibration by id.  Requires either calibrator id or conversation id

Wraps GET /api/v2/quality/calibrations/{calibrationId} 

Requires ANY permissions: 

* quality:calibration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
calibration_id = 'calibration_id_example' # str | Calibration ID
calibrator_id = 'calibrator_id_example' # str | calibratorId (optional)
conversation_id = 'conversation_id_example' # str | conversationId (optional)

try:
    # Get a calibration by id.  Requires either calibrator id or conversation id
    api_response = api_instance.get_quality_calibration(calibration_id, calibrator_id=calibrator_id, conversation_id=conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_calibration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **calibration_id** | **str**| Calibration ID |  |
| **calibrator_id** | **str**| calibratorId | [optional]  |
| **conversation_id** | **str**| conversationId | [optional]  |
{: class="table table-striped"}

### Return type

[**Calibration**](Calibration.html)

<a name="get_quality_calibrations"></a>

## [**CalibrationEntityListing**](CalibrationEntityListing.html) get_quality_calibrations(calibrator_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, conversation_id=conversation_id, start_time=start_time, end_time=end_time)



Get the list of calibrations

Wraps GET /api/v2/quality/calibrations 

Requires ANY permissions: 

* quality:calibration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
calibrator_id = 'calibrator_id_example' # str | user id of calibrator
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
conversation_id = 'conversation_id_example' # str | conversation id (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | Beginning of the calibration query. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | end of the calibration query. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)

try:
    # Get the list of calibrations
    api_response = api_instance.get_quality_calibrations(calibrator_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, conversation_id=conversation_id, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_calibrations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **calibrator_id** | **str**| user id of calibrator |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **conversation_id** | **str**| conversation id | [optional]  |
| **start_time** | **datetime**| Beginning of the calibration query. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
| **end_time** | **datetime**| end of the calibration query. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
{: class="table table-striped"}

### Return type

[**CalibrationEntityListing**](CalibrationEntityListing.html)

<a name="get_quality_conversation_evaluation"></a>

## [**EvaluationResponse**](EvaluationResponse.html) get_quality_conversation_evaluation(conversation_id, evaluation_id, expand=expand)



Get an evaluation

Wraps GET /api/v2/quality/conversations/{conversationId}/evaluations/{evaluationId} 

Requires ANY permissions: 

* quality:evaluation:view
* quality:evaluation:assign
* quality:evaluation:release

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
conversation_id = 'conversation_id_example' # str | conversationId
evaluation_id = 'evaluation_id_example' # str | evaluationId
expand = 'expand_example' # str | agent, assignee, evaluator, evaluationForm (optional)

try:
    # Get an evaluation
    api_response = api_instance.get_quality_conversation_evaluation(conversation_id, evaluation_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_conversation_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **evaluation_id** | **str**| evaluationId |  |
| **expand** | **str**| agent, assignee, evaluator, evaluationForm | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationResponse**](EvaluationResponse.html)

<a name="get_quality_conversation_surveys"></a>

## [**list[Survey]**](Survey.html) get_quality_conversation_surveys(conversation_id)



Get the surveys for a conversation

Wraps GET /api/v2/quality/conversations/{conversationId}/surveys 

Requires ANY permissions: 

* quality:survey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get the surveys for a conversation
    api_response = api_instance.get_quality_conversation_surveys(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_conversation_surveys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**list[Survey]**](Survey.html)

<a name="get_quality_conversations_audits_query_transaction_id"></a>

## [**QualityAuditQueryExecutionStatusResponse**](QualityAuditQueryExecutionStatusResponse.html) get_quality_conversations_audits_query_transaction_id(transaction_id)



Get status of audit query execution

Wraps GET /api/v2/quality/conversations/audits/query/{transactionId} 

Requires ALL permissions: 

* audits:interactionDetails:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
transaction_id = 'transaction_id_example' # str | Transaction ID

try:
    # Get status of audit query execution
    api_response = api_instance.get_quality_conversations_audits_query_transaction_id(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_conversations_audits_query_transaction_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transaction_id** | **str**| Transaction ID |  |
{: class="table table-striped"}

### Return type

[**QualityAuditQueryExecutionStatusResponse**](QualityAuditQueryExecutionStatusResponse.html)

<a name="get_quality_conversations_audits_query_transaction_id_results"></a>

## [**QualityAuditQueryExecutionResultsResponse**](QualityAuditQueryExecutionResultsResponse.html) get_quality_conversations_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand)



Get results of audit query

Wraps GET /api/v2/quality/conversations/audits/query/{transactionId}/results 

Requires ALL permissions: 

* audits:interactionDetails:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
transaction_id = 'transaction_id_example' # str | Transaction ID
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 25 # int | Page size (optional) (default to 25)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get results of audit query
    api_response = api_instance.get_quality_conversations_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_conversations_audits_query_transaction_id_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transaction_id** | **str**| Transaction ID |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: user |
{: class="table table-striped"}

### Return type

[**QualityAuditQueryExecutionResultsResponse**](QualityAuditQueryExecutionResultsResponse.html)

<a name="get_quality_evaluations_query"></a>

## [**EvaluationEntityListing**](EvaluationEntityListing.html) get_quality_evaluations_query(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, conversation_id=conversation_id, agent_user_id=agent_user_id, evaluator_user_id=evaluator_user_id, assignee_user_id=assignee_user_id, queue_id=queue_id, start_time=start_time, end_time=end_time, evaluation_state=evaluation_state, is_released=is_released, agent_has_read=agent_has_read, expand_answer_total_scores=expand_answer_total_scores, maximum=maximum, sort_order=sort_order)



Queries Evaluations and returns a paged list

Query params must include one of conversationId, evaluatorUserId, agentUserId or assigneeUserId. When querying by agentUserId (and not conversationId or evaluatorUserId), the results are sorted by release date. Evaluations set to 'Never Release' are omitted in this case. When querying by evaluatorUserId or conversationId (including when combined with agentUserId), the results are sorted by assigned date.

Wraps GET /api/v2/quality/evaluations/query 

Requires ANY permissions: 

* quality:evaluation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | NOTE: Does not work when querying evaluations (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | NOTE: Does not work when querying evaluations (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
conversation_id = 'conversation_id_example' # str | conversationId specified (optional)
agent_user_id = 'agent_user_id_example' # str | user id of the agent (optional)
evaluator_user_id = 'evaluator_user_id_example' # str | evaluator user id (optional)
assignee_user_id = 'assignee_user_id_example' # str | assignee user id (optional)
queue_id = 'queue_id_example' # str | queue id (optional)
start_time = 'start_time_example' # str | start time of the evaluation query (optional)
end_time = 'end_time_example' # str | end time of the evaluation query (optional)
evaluation_state = ['evaluation_state_example'] # list[str] |  (optional)
is_released = True # bool | the evaluation has been released (optional)
agent_has_read = True # bool | agent has the evaluation (optional)
expand_answer_total_scores = True # bool | get the total scores for evaluations (optional)
maximum = 56 # int | the maximum number of results to return (optional)
sort_order = 'sort_order_example' # str | NOTE: Does not work when conversationId is supplied. (optional)

try:
    # Queries Evaluations and returns a paged list
    api_response = api_instance.get_quality_evaluations_query(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, conversation_id=conversation_id, agent_user_id=agent_user_id, evaluator_user_id=evaluator_user_id, assignee_user_id=assignee_user_id, queue_id=queue_id, start_time=start_time, end_time=end_time, evaluation_state=evaluation_state, is_released=is_released, agent_has_read=agent_has_read, expand_answer_total_scores=expand_answer_total_scores, maximum=maximum, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_evaluations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| NOTE: Does not work when querying evaluations | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| NOTE: Does not work when querying evaluations | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **conversation_id** | **str**| conversationId specified | [optional]  |
| **agent_user_id** | **str**| user id of the agent | [optional]  |
| **evaluator_user_id** | **str**| evaluator user id | [optional]  |
| **assignee_user_id** | **str**| assignee user id | [optional]  |
| **queue_id** | **str**| queue id | [optional]  |
| **start_time** | **str**| start time of the evaluation query | [optional]  |
| **end_time** | **str**| end time of the evaluation query | [optional]  |
| **evaluation_state** | [**list[str]**](str.html)|  | [optional]  |
| **is_released** | **bool**| the evaluation has been released | [optional]  |
| **agent_has_read** | **bool**| agent has the evaluation | [optional]  |
| **expand_answer_total_scores** | **bool**| get the total scores for evaluations | [optional]  |
| **maximum** | **int**| the maximum number of results to return | [optional]  |
| **sort_order** | **str**| NOTE: Does not work when conversationId is supplied. | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationEntityListing**](EvaluationEntityListing.html)

<a name="get_quality_evaluators_activity"></a>

## [**EvaluatorActivityEntityListing**](EvaluatorActivityEntityListing.html) get_quality_evaluators_activity(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, start_time=start_time, end_time=end_time, name=name, permission=permission, group=group)



Get an evaluator activity

Wraps GET /api/v2/quality/evaluators/activity 

Requires ANY permissions: 

* quality:evaluation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | The start time specified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | The end time specified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)
name = 'name_example' # str | Evaluator name (optional)
permission = ['permission_example'] # list[str] | permission strings (optional)
group = 'group_example' # str | group id (optional)

try:
    # Get an evaluator activity
    api_response = api_instance.get_quality_evaluators_activity(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, start_time=start_time, end_time=end_time, name=name, permission=permission, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_evaluators_activity: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **start_time** | **datetime**| The start time specified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
| **end_time** | **datetime**| The end time specified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
| **name** | **str**| Evaluator name | [optional]  |
| **permission** | [**list[str]**](str.html)| permission strings | [optional]  |
| **group** | **str**| group id | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluatorActivityEntityListing**](EvaluatorActivityEntityListing.html)

<a name="get_quality_form"></a>

## [**EvaluationForm**](EvaluationForm.html) get_quality_form(form_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get an evaluation form

Wraps GET /api/v2/quality/forms/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Get an evaluation form
    api_response = api_instance.get_quality_form(form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_form: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="get_quality_form_versions"></a>

## [**EvaluationFormEntityListing**](EvaluationFormEntityListing.html) get_quality_form_versions(form_id, page_size=page_size, page_number=page_number)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Gets all the revisions for a specific evaluation.

Wraps GET /api/v2/quality/forms/{formId}/versions 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Gets all the revisions for a specific evaluation.
    api_response = api_instance.get_quality_form_versions(form_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_form_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**EvaluationFormEntityListing**](EvaluationFormEntityListing.html)

<a name="get_quality_forms"></a>

## [**EvaluationFormEntityListing**](EvaluationFormEntityListing.html) get_quality_forms(page_size=page_size, page_number=page_number, sort_by=sort_by, next_page=next_page, previous_page=previous_page, expand=expand, name=name, sort_order=sort_order)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the list of evaluation forms

Wraps GET /api/v2/quality/forms 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
expand = 'expand_example' # str | If 'expand=publishHistory', then each unpublished evaluation form includes a listing of its published versions (optional)
name = 'name_example' # str | Name (optional)
sort_order = 'sort_order_example' # str | Order to sort results, either asc or desc (optional)

try:
    # Get the list of evaluation forms
    api_response = api_instance.get_quality_forms(page_size=page_size, page_number=page_number, sort_by=sort_by, next_page=next_page, previous_page=previous_page, expand=expand, name=name, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **expand** | **str**| If &#39;expand&#x3D;publishHistory&#39;, then each unpublished evaluation form includes a listing of its published versions | [optional] <br />**Values**: publishHistory |
| **name** | **str**| Name | [optional]  |
| **sort_order** | **str**| Order to sort results, either asc or desc | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationFormEntityListing**](EvaluationFormEntityListing.html)

<a name="get_quality_forms_evaluation"></a>

## [**EvaluationForm**](EvaluationForm.html) get_quality_forms_evaluation(form_id)



Get an evaluation form

Wraps GET /api/v2/quality/forms/evaluations/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Get an evaluation form
    api_response = api_instance.get_quality_forms_evaluation(form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="get_quality_forms_evaluation_versions"></a>

## [**EvaluationFormEntityListing**](EvaluationFormEntityListing.html) get_quality_forms_evaluation_versions(form_id, page_size=page_size, page_number=page_number, sort_order=sort_order)



Gets all the revisions for a specific evaluation.

Wraps GET /api/v2/quality/forms/evaluations/{formId}/versions 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')

try:
    # Gets all the revisions for a specific evaluation.
    api_response = api_instance.get_quality_forms_evaluation_versions(form_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_evaluation_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;] |
{: class="table table-striped"}

### Return type

[**EvaluationFormEntityListing**](EvaluationFormEntityListing.html)

<a name="get_quality_forms_evaluations"></a>

## [**EvaluationFormEntityListing**](EvaluationFormEntityListing.html) get_quality_forms_evaluations(page_size=page_size, page_number=page_number, sort_by=sort_by, next_page=next_page, previous_page=previous_page, expand=expand, name=name, sort_order=sort_order)



Get the list of evaluation forms

Wraps GET /api/v2/quality/forms/evaluations 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
expand = 'expand_example' # str | If 'expand=publishHistory', then each unpublished evaluation form includes a listing of its published versions (optional)
name = 'name_example' # str | Name (optional)
sort_order = 'sort_order_example' # str | Order to sort results, either asc or desc (optional)

try:
    # Get the list of evaluation forms
    api_response = api_instance.get_quality_forms_evaluations(page_size=page_size, page_number=page_number, sort_by=sort_by, next_page=next_page, previous_page=previous_page, expand=expand, name=name, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_evaluations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **expand** | **str**| If &#39;expand&#x3D;publishHistory&#39;, then each unpublished evaluation form includes a listing of its published versions | [optional] <br />**Values**: publishHistory |
| **name** | **str**| Name | [optional]  |
| **sort_order** | **str**| Order to sort results, either asc or desc | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationFormEntityListing**](EvaluationFormEntityListing.html)

<a name="get_quality_forms_evaluations_bulk_contexts"></a>

## [**list[EvaluationForm]**](EvaluationForm.html) get_quality_forms_evaluations_bulk_contexts(context_id)



Retrieve a list of the latest published evaluation form versions by context ids

Wraps GET /api/v2/quality/forms/evaluations/bulk/contexts 

Requires ALL permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
context_id = ['context_id_example'] # list[str] | A comma-delimited list of valid evaluation form context ids

try:
    # Retrieve a list of the latest published evaluation form versions by context ids
    api_response = api_instance.get_quality_forms_evaluations_bulk_contexts(context_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_evaluations_bulk_contexts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **context_id** | [**list[str]**](str.html)| A comma-delimited list of valid evaluation form context ids |  |
{: class="table table-striped"}

### Return type

[**list[EvaluationForm]**](EvaluationForm.html)

<a name="get_quality_forms_survey"></a>

## [**SurveyForm**](SurveyForm.html) get_quality_forms_survey(form_id)



Get a survey form

Wraps GET /api/v2/quality/forms/surveys/{formId} 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Get a survey form
    api_response = api_instance.get_quality_forms_survey(form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_survey: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

[**SurveyForm**](SurveyForm.html)

<a name="get_quality_forms_survey_versions"></a>

## [**SurveyFormEntityListing**](SurveyFormEntityListing.html) get_quality_forms_survey_versions(form_id, page_size=page_size, page_number=page_number)



Gets all the revisions for a specific survey.

Wraps GET /api/v2/quality/forms/surveys/{formId}/versions 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Gets all the revisions for a specific survey.
    api_response = api_instance.get_quality_forms_survey_versions(form_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_survey_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**SurveyFormEntityListing**](SurveyFormEntityListing.html)

<a name="get_quality_forms_surveys"></a>

## [**SurveyFormEntityListing**](SurveyFormEntityListing.html) get_quality_forms_surveys(page_size=page_size, page_number=page_number, sort_by=sort_by, next_page=next_page, previous_page=previous_page, expand=expand, name=name, sort_order=sort_order)



Get the list of survey forms

Wraps GET /api/v2/quality/forms/surveys 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
expand = 'expand_example' # str | If 'expand=publishHistory', then each unpublished evaluation form includes a listing of its published versions (optional)
name = 'name_example' # str | Name (optional)
sort_order = 'sort_order_example' # str | Order to sort results, either asc or desc (optional)

try:
    # Get the list of survey forms
    api_response = api_instance.get_quality_forms_surveys(page_size=page_size, page_number=page_number, sort_by=sort_by, next_page=next_page, previous_page=previous_page, expand=expand, name=name, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_surveys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **expand** | **str**| If &#39;expand&#x3D;publishHistory&#39;, then each unpublished evaluation form includes a listing of its published versions | [optional] <br />**Values**: publishHistory |
| **name** | **str**| Name | [optional]  |
| **sort_order** | **str**| Order to sort results, either asc or desc | [optional]  |
{: class="table table-striped"}

### Return type

[**SurveyFormEntityListing**](SurveyFormEntityListing.html)

<a name="get_quality_forms_surveys_bulk"></a>

## [**SurveyFormEntityListing**](SurveyFormEntityListing.html) get_quality_forms_surveys_bulk(id)



Retrieve a list of survey forms by their ids

Wraps GET /api/v2/quality/forms/surveys/bulk 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
id = ['id_example'] # list[str] | A comma-delimited list of valid survey form ids

try:
    # Retrieve a list of survey forms by their ids
    api_response = api_instance.get_quality_forms_surveys_bulk(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_surveys_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| A comma-delimited list of valid survey form ids |  |
{: class="table table-striped"}

### Return type

[**SurveyFormEntityListing**](SurveyFormEntityListing.html)

<a name="get_quality_forms_surveys_bulk_contexts"></a>

## [**list[SurveyForm]**](SurveyForm.html) get_quality_forms_surveys_bulk_contexts(context_id, published=published)



Retrieve a list of the latest form versions by context ids

Wraps GET /api/v2/quality/forms/surveys/bulk/contexts 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
context_id = ['context_id_example'] # list[str] | A comma-delimited list of valid survey form context ids. The maximum number of ids allowed in this list is 100.
published = True # bool | If true, the latest published version will be included. If false, only the unpublished version will be included. (optional) (default to True)

try:
    # Retrieve a list of the latest form versions by context ids
    api_response = api_instance.get_quality_forms_surveys_bulk_contexts(context_id, published=published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_forms_surveys_bulk_contexts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **context_id** | [**list[str]**](str.html)| A comma-delimited list of valid survey form context ids. The maximum number of ids allowed in this list is 100. |  |
| **published** | **bool**| If true, the latest published version will be included. If false, only the unpublished version will be included. | [optional] [default to True] |
{: class="table table-striped"}

### Return type

[**list[SurveyForm]**](SurveyForm.html)

<a name="get_quality_publishedform"></a>

## [**EvaluationForm**](EvaluationForm.html) get_quality_publishedform(form_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the published evaluation forms.

Wraps GET /api/v2/quality/publishedforms/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Get the published evaluation forms.
    api_response = api_instance.get_quality_publishedform(form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_publishedform: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="get_quality_publishedforms"></a>

## [**EvaluationFormEntityListing**](EvaluationFormEntityListing.html) get_quality_publishedforms(page_size=page_size, page_number=page_number, name=name, only_latest_per_context=only_latest_per_context)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the published evaluation forms.

Wraps GET /api/v2/quality/publishedforms 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
only_latest_per_context = False # bool | onlyLatestPerContext (optional) (default to False)

try:
    # Get the published evaluation forms.
    api_response = api_instance.get_quality_publishedforms(page_size=page_size, page_number=page_number, name=name, only_latest_per_context=only_latest_per_context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_publishedforms: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **only_latest_per_context** | **bool**| onlyLatestPerContext | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**EvaluationFormEntityListing**](EvaluationFormEntityListing.html)

<a name="get_quality_publishedforms_evaluation"></a>

## [**EvaluationForm**](EvaluationForm.html) get_quality_publishedforms_evaluation(form_id)



Get the most recent published version of an evaluation form.

Wraps GET /api/v2/quality/publishedforms/evaluations/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Get the most recent published version of an evaluation form.
    api_response = api_instance.get_quality_publishedforms_evaluation(form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_publishedforms_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="get_quality_publishedforms_evaluations"></a>

## [**EvaluationFormEntityListing**](EvaluationFormEntityListing.html) get_quality_publishedforms_evaluations(page_size=page_size, page_number=page_number, name=name, only_latest_per_context=only_latest_per_context)



Get the published evaluation forms.

Wraps GET /api/v2/quality/publishedforms/evaluations 

Requires ANY permissions: 

* quality:evaluationForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
only_latest_per_context = False # bool | onlyLatestPerContext (optional) (default to False)

try:
    # Get the published evaluation forms.
    api_response = api_instance.get_quality_publishedforms_evaluations(page_size=page_size, page_number=page_number, name=name, only_latest_per_context=only_latest_per_context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_publishedforms_evaluations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **only_latest_per_context** | **bool**| onlyLatestPerContext | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**EvaluationFormEntityListing**](EvaluationFormEntityListing.html)

<a name="get_quality_publishedforms_survey"></a>

## [**SurveyForm**](SurveyForm.html) get_quality_publishedforms_survey(form_id)



Get the most recent published version of a survey form.

Wraps GET /api/v2/quality/publishedforms/surveys/{formId} 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID

try:
    # Get the most recent published version of a survey form.
    api_response = api_instance.get_quality_publishedforms_survey(form_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_publishedforms_survey: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
{: class="table table-striped"}

### Return type

[**SurveyForm**](SurveyForm.html)

<a name="get_quality_publishedforms_surveys"></a>

## [**SurveyFormEntityListing**](SurveyFormEntityListing.html) get_quality_publishedforms_surveys(page_size=page_size, page_number=page_number, name=name, only_latest_enabled_per_context=only_latest_enabled_per_context)



Get the published survey forms.

Wraps GET /api/v2/quality/publishedforms/surveys 

Requires ALL permissions: 

* quality:surveyForm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
only_latest_enabled_per_context = False # bool | onlyLatestEnabledPerContext (optional) (default to False)

try:
    # Get the published survey forms.
    api_response = api_instance.get_quality_publishedforms_surveys(page_size=page_size, page_number=page_number, name=name, only_latest_enabled_per_context=only_latest_enabled_per_context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_publishedforms_surveys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **only_latest_enabled_per_context** | **bool**| onlyLatestEnabledPerContext | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**SurveyFormEntityListing**](SurveyFormEntityListing.html)

<a name="get_quality_survey"></a>

## [**Survey**](Survey.html) get_quality_survey(survey_id)



Get a survey for a conversation

Wraps GET /api/v2/quality/surveys/{surveyId} 

Requires ANY permissions: 

* quality:survey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
survey_id = 'survey_id_example' # str | surveyId

try:
    # Get a survey for a conversation
    api_response = api_instance.get_quality_survey(survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_survey: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **survey_id** | **str**| surveyId |  |
{: class="table table-striped"}

### Return type

[**Survey**](Survey.html)

<a name="get_quality_surveys_scorable"></a>

## [**ScorableSurvey**](ScorableSurvey.html) get_quality_surveys_scorable(customer_survey_url)



Get a survey as an end-customer, for the purposes of scoring it.

Wraps GET /api/v2/quality/surveys/scorable 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
customer_survey_url = 'customer_survey_url_example' # str | customerSurveyUrl

try:
    # Get a survey as an end-customer, for the purposes of scoring it.
    api_response = api_instance.get_quality_surveys_scorable(customer_survey_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->get_quality_surveys_scorable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_survey_url** | **str**| customerSurveyUrl |  |
{: class="table table-striped"}

### Return type

[**ScorableSurvey**](ScorableSurvey.html)

<a name="patch_quality_forms_survey"></a>

## [**SurveyForm**](SurveyForm.html) patch_quality_forms_survey(form_id, body)



Disable a particular version of a survey form and invalidates any invitations that have already been sent to customers using this version of the form.

Wraps PATCH /api/v2/quality/forms/surveys/{formId} 

Requires ALL permissions: 

* quality:surveyForm:disable

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
body = PureCloudPlatformClientV2.SurveyForm() # SurveyForm | Survey form

try:
    # Disable a particular version of a survey form and invalidates any invitations that have already been sent to customers using this version of the form.
    api_response = api_instance.patch_quality_forms_survey(form_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->patch_quality_forms_survey: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **body** | [**SurveyForm**](SurveyForm.html)| Survey form |  |
{: class="table table-striped"}

### Return type

[**SurveyForm**](SurveyForm.html)

<a name="post_analytics_evaluations_aggregates_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_evaluations_aggregates_jobs(body)



Query for evaluation aggregates asynchronously

post_analytics_evaluations_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/evaluations/aggregates/jobs 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.EvaluationAsyncAggregationQuery() # EvaluationAsyncAggregationQuery | query

try:
    # Query for evaluation aggregates asynchronously
    api_response = api_instance.post_analytics_evaluations_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_analytics_evaluations_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationAsyncAggregationQuery**](EvaluationAsyncAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_evaluations_aggregates_query"></a>

## [**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse.html) post_analytics_evaluations_aggregates_query(body)



Query for evaluation aggregates

Wraps POST /api/v2/analytics/evaluations/aggregates/query 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.EvaluationAggregationQuery() # EvaluationAggregationQuery | query

try:
    # Query for evaluation aggregates
    api_response = api_instance.post_analytics_evaluations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_analytics_evaluations_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationAggregationQuery**](EvaluationAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse.html)

<a name="post_analytics_surveys_aggregates_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_surveys_aggregates_jobs(body)



Query for survey aggregates asynchronously

post_analytics_surveys_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/surveys/aggregates/jobs 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.SurveyAsyncAggregationQuery() # SurveyAsyncAggregationQuery | query

try:
    # Query for survey aggregates asynchronously
    api_response = api_instance.post_analytics_surveys_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_analytics_surveys_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyAsyncAggregationQuery**](SurveyAsyncAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_surveys_aggregates_query"></a>

## [**SurveyAggregateQueryResponse**](SurveyAggregateQueryResponse.html) post_analytics_surveys_aggregates_query(body)



Query for survey aggregates

Wraps POST /api/v2/analytics/surveys/aggregates/query 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.SurveyAggregationQuery() # SurveyAggregationQuery | query

try:
    # Query for survey aggregates
    api_response = api_instance.post_analytics_surveys_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_analytics_surveys_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyAggregationQuery**](SurveyAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**SurveyAggregateQueryResponse**](SurveyAggregateQueryResponse.html)

<a name="post_quality_calibrations"></a>

## [**Calibration**](Calibration.html) post_quality_calibrations(body, expand=expand)



Create a calibration

Wraps POST /api/v2/quality/calibrations 

Requires ANY permissions: 

* quality:calibration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.CalibrationCreate() # CalibrationCreate | calibration
expand = 'expand_example' # str | calibratorId (optional)

try:
    # Create a calibration
    api_response = api_instance.post_quality_calibrations(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_calibrations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CalibrationCreate**](CalibrationCreate.html)| calibration |  |
| **expand** | **str**| calibratorId | [optional]  |
{: class="table table-striped"}

### Return type

[**Calibration**](Calibration.html)

<a name="post_quality_conversation_evaluations"></a>

## [**Evaluation**](Evaluation.html) post_quality_conversation_evaluations(conversation_id, body, expand=expand)



Create an evaluation

Wraps POST /api/v2/quality/conversations/{conversationId}/evaluations 

Requires ANY permissions: 

* quality:evaluation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Evaluation() # Evaluation | evaluation
expand = 'expand_example' # str | evaluatorId (optional)

try:
    # Create an evaluation
    api_response = api_instance.post_quality_conversation_evaluations(conversation_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_conversation_evaluations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Evaluation**](Evaluation.html)| evaluation |  |
| **expand** | **str**| evaluatorId | [optional]  |
{: class="table table-striped"}

### Return type

[**Evaluation**](Evaluation.html)

<a name="post_quality_conversations_audits_query"></a>

## [**QualityAuditQueryExecutionStatusResponse**](QualityAuditQueryExecutionStatusResponse.html) post_quality_conversations_audits_query(body)



Create audit query execution

Wraps POST /api/v2/quality/conversations/audits/query 

Requires ALL permissions: 

* audits:interactionDetails:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.QMAuditQueryRequest() # QMAuditQueryRequest | query

try:
    # Create audit query execution
    api_response = api_instance.post_quality_conversations_audits_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_conversations_audits_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**QMAuditQueryRequest**](QMAuditQueryRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**QualityAuditQueryExecutionStatusResponse**](QualityAuditQueryExecutionStatusResponse.html)

<a name="post_quality_evaluations_aggregates_query_me"></a>

## [**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse.html) post_quality_evaluations_aggregates_query_me(body)



Query for evaluation aggregates for the current user

Wraps POST /api/v2/quality/evaluations/aggregates/query/me 

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
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.EvaluationAggregationQueryMe() # EvaluationAggregationQueryMe | query

try:
    # Query for evaluation aggregates for the current user
    api_response = api_instance.post_quality_evaluations_aggregates_query_me(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_evaluations_aggregates_query_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationAggregationQueryMe**](EvaluationAggregationQueryMe.html)| query |  |
{: class="table table-striped"}

### Return type

[**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse.html)

<a name="post_quality_evaluations_scoring"></a>

## [**EvaluationScoringSet**](EvaluationScoringSet.html) post_quality_evaluations_scoring(body)



Score evaluation

Wraps POST /api/v2/quality/evaluations/scoring 

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
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.EvaluationFormAndScoringSet() # EvaluationFormAndScoringSet | evaluationAndScoringSet

try:
    # Score evaluation
    api_response = api_instance.post_quality_evaluations_scoring(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_evaluations_scoring: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationFormAndScoringSet**](EvaluationFormAndScoringSet.html)| evaluationAndScoringSet |  |
{: class="table table-striped"}

### Return type

[**EvaluationScoringSet**](EvaluationScoringSet.html)

<a name="post_quality_forms"></a>

## [**EvaluationForm**](EvaluationForm.html) post_quality_forms(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create an evaluation form.

Wraps POST /api/v2/quality/forms 

Requires ANY permissions: 

* quality:evaluationForm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.EvaluationForm() # EvaluationForm | Evaluation form

try:
    # Create an evaluation form.
    api_response = api_instance.post_quality_forms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_forms: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationForm**](EvaluationForm.html)| Evaluation form |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="post_quality_forms_evaluations"></a>

## [**EvaluationForm**](EvaluationForm.html) post_quality_forms_evaluations(body)



Create an evaluation form.

Wraps POST /api/v2/quality/forms/evaluations 

Requires ANY permissions: 

* quality:evaluationForm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.EvaluationForm() # EvaluationForm | Evaluation form

try:
    # Create an evaluation form.
    api_response = api_instance.post_quality_forms_evaluations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_forms_evaluations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationForm**](EvaluationForm.html)| Evaluation form |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="post_quality_forms_surveys"></a>

## [**SurveyForm**](SurveyForm.html) post_quality_forms_surveys(body)



Create a survey form.

Wraps POST /api/v2/quality/forms/surveys 

Requires ALL permissions: 

* quality:surveyForm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.SurveyForm() # SurveyForm | Survey form

try:
    # Create a survey form.
    api_response = api_instance.post_quality_forms_surveys(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_forms_surveys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyForm**](SurveyForm.html)| Survey form |  |
{: class="table table-striped"}

### Return type

[**SurveyForm**](SurveyForm.html)

<a name="post_quality_publishedforms"></a>

## [**EvaluationForm**](EvaluationForm.html) post_quality_publishedforms(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Publish an evaluation form.

Wraps POST /api/v2/quality/publishedforms 

Requires ANY permissions: 

* quality:evaluationForm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.PublishForm() # PublishForm | Publish request containing id of form to publish

try:
    # Publish an evaluation form.
    api_response = api_instance.post_quality_publishedforms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_publishedforms: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PublishForm**](PublishForm.html)| Publish request containing id of form to publish |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="post_quality_publishedforms_evaluations"></a>

## [**EvaluationForm**](EvaluationForm.html) post_quality_publishedforms_evaluations(body)



Publish an evaluation form.

Wraps POST /api/v2/quality/publishedforms/evaluations 

Requires ANY permissions: 

* quality:evaluationForm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.PublishForm() # PublishForm | Publish request containing id of form to publish

try:
    # Publish an evaluation form.
    api_response = api_instance.post_quality_publishedforms_evaluations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_publishedforms_evaluations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PublishForm**](PublishForm.html)| Publish request containing id of form to publish |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="post_quality_publishedforms_surveys"></a>

## [**SurveyForm**](SurveyForm.html) post_quality_publishedforms_surveys(body)



Publish a survey form.

Wraps POST /api/v2/quality/publishedforms/surveys 

Requires ALL permissions: 

* quality:surveyForm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.PublishForm() # PublishForm | Survey form

try:
    # Publish a survey form.
    api_response = api_instance.post_quality_publishedforms_surveys(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_publishedforms_surveys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PublishForm**](PublishForm.html)| Survey form |  |
{: class="table table-striped"}

### Return type

[**SurveyForm**](SurveyForm.html)

<a name="post_quality_surveys_scoring"></a>

## [**SurveyScoringSet**](SurveyScoringSet.html) post_quality_surveys_scoring(body)



Score survey

Wraps POST /api/v2/quality/surveys/scoring 

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
api_instance = PureCloudPlatformClientV2.QualityApi()
body = PureCloudPlatformClientV2.SurveyFormAndScoringSet() # SurveyFormAndScoringSet | surveyAndScoringSet

try:
    # Score survey
    api_response = api_instance.post_quality_surveys_scoring(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->post_quality_surveys_scoring: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyFormAndScoringSet**](SurveyFormAndScoringSet.html)| surveyAndScoringSet |  |
{: class="table table-striped"}

### Return type

[**SurveyScoringSet**](SurveyScoringSet.html)

<a name="put_quality_calibration"></a>

## [**Calibration**](Calibration.html) put_quality_calibration(calibration_id, body)



Update a calibration to the specified calibration via PUT.  Editable fields include: evaluators, expertEvaluator, and scoringIndex

Wraps PUT /api/v2/quality/calibrations/{calibrationId} 

Requires ANY permissions: 

* quality:calibration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
calibration_id = 'calibration_id_example' # str | Calibration ID
body = PureCloudPlatformClientV2.Calibration() # Calibration | Calibration

try:
    # Update a calibration to the specified calibration via PUT.  Editable fields include: evaluators, expertEvaluator, and scoringIndex
    api_response = api_instance.put_quality_calibration(calibration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->put_quality_calibration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **calibration_id** | **str**| Calibration ID |  |
| **body** | [**Calibration**](Calibration.html)| Calibration |  |
{: class="table table-striped"}

### Return type

[**Calibration**](Calibration.html)

<a name="put_quality_conversation_evaluation"></a>

## [**EvaluationResponse**](EvaluationResponse.html) put_quality_conversation_evaluation(conversation_id, evaluation_id, body, expand=expand)



Update an evaluation

The quality:evaluation:edit permission allows modification of most fields, while the quality:evaluation:editScore permission allows an evaluator to change just the question scores, and the quality:evaluation:editAgentSignoff permission allows an agent to change the agent comments and sign off on the evaluation.

Wraps PUT /api/v2/quality/conversations/{conversationId}/evaluations/{evaluationId} 

Requires ANY permissions: 

* quality:evaluation:edit
* quality:evaluation:editScore
* quality:evaluation:editAgentSignoff

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
conversation_id = 'conversation_id_example' # str | conversationId
evaluation_id = 'evaluation_id_example' # str | evaluationId
body = PureCloudPlatformClientV2.Evaluation() # Evaluation | evaluation
expand = 'expand_example' # str | evaluatorId, evaluationForm, assignee, evaluator (optional)

try:
    # Update an evaluation
    api_response = api_instance.put_quality_conversation_evaluation(conversation_id, evaluation_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->put_quality_conversation_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **evaluation_id** | **str**| evaluationId |  |
| **body** | [**Evaluation**](Evaluation.html)| evaluation |  |
| **expand** | **str**| evaluatorId, evaluationForm, assignee, evaluator | [optional]  |
{: class="table table-striped"}

### Return type

[**EvaluationResponse**](EvaluationResponse.html)

<a name="put_quality_form"></a>

## [**EvaluationForm**](EvaluationForm.html) put_quality_form(form_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update an evaluation form.

Wraps PUT /api/v2/quality/forms/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
body = PureCloudPlatformClientV2.EvaluationForm() # EvaluationForm | Evaluation form

try:
    # Update an evaluation form.
    api_response = api_instance.put_quality_form(form_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->put_quality_form: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **body** | [**EvaluationForm**](EvaluationForm.html)| Evaluation form |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="put_quality_forms_evaluation"></a>

## [**EvaluationForm**](EvaluationForm.html) put_quality_forms_evaluation(form_id, body)



Update an evaluation form.

Wraps PUT /api/v2/quality/forms/evaluations/{formId} 

Requires ANY permissions: 

* quality:evaluationForm:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
body = PureCloudPlatformClientV2.EvaluationForm() # EvaluationForm | Evaluation form

try:
    # Update an evaluation form.
    api_response = api_instance.put_quality_forms_evaluation(form_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->put_quality_forms_evaluation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **body** | [**EvaluationForm**](EvaluationForm.html)| Evaluation form |  |
{: class="table table-striped"}

### Return type

[**EvaluationForm**](EvaluationForm.html)

<a name="put_quality_forms_survey"></a>

## [**SurveyForm**](SurveyForm.html) put_quality_forms_survey(form_id, body)



Update a survey form.

Wraps PUT /api/v2/quality/forms/surveys/{formId} 

Requires ALL permissions: 

* quality:surveyForm:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
form_id = 'form_id_example' # str | Form ID
body = PureCloudPlatformClientV2.SurveyForm() # SurveyForm | Survey form

try:
    # Update a survey form.
    api_response = api_instance.put_quality_forms_survey(form_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->put_quality_forms_survey: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **form_id** | **str**| Form ID |  |
| **body** | [**SurveyForm**](SurveyForm.html)| Survey form |  |
{: class="table table-striped"}

### Return type

[**SurveyForm**](SurveyForm.html)

<a name="put_quality_surveys_scorable"></a>

## [**ScorableSurvey**](ScorableSurvey.html) put_quality_surveys_scorable(customer_survey_url, body)



Update a survey as an end-customer, for the purposes of scoring it.

Wraps PUT /api/v2/quality/surveys/scorable 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.QualityApi()
customer_survey_url = 'customer_survey_url_example' # str | customerSurveyUrl
body = PureCloudPlatformClientV2.ScorableSurvey() # ScorableSurvey | survey

try:
    # Update a survey as an end-customer, for the purposes of scoring it.
    api_response = api_instance.put_quality_surveys_scorable(customer_survey_url, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityApi->put_quality_surveys_scorable: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_survey_url** | **str**| customerSurveyUrl |  |
| **body** | [**ScorableSurvey**](ScorableSurvey.html)| survey |  |
{: class="table table-striped"}

### Return type

[**ScorableSurvey**](ScorableSurvey.html)

