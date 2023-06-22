---
title: GamificationApi
---

## PureCloudPlatformClientV2.GamificationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_employeeperformance_externalmetrics_definition**](GamificationApi.html#delete_employeeperformance_externalmetrics_definition) | Delete an External Metric Definition|
|[**get_employeeperformance_externalmetrics_definition**](GamificationApi.html#get_employeeperformance_externalmetrics_definition) | Get an External Metric Definition|
|[**get_employeeperformance_externalmetrics_definitions**](GamificationApi.html#get_employeeperformance_externalmetrics_definitions) | Get a list of External Metric Definitions of an organization, sorted by name in ascending order|
|[**get_gamification_insights**](GamificationApi.html#get_gamification_insights) | Get insights summary|
|[**get_gamification_insights_details**](GamificationApi.html#get_gamification_insights_details) | Get insights details for the current user|
|[**get_gamification_insights_groups_trends**](GamificationApi.html#get_gamification_insights_groups_trends) | Get insights overall trend for the current user|
|[**get_gamification_insights_groups_trends_all**](GamificationApi.html#get_gamification_insights_groups_trends_all) | Get insights overall trend|
|[**get_gamification_insights_members**](GamificationApi.html#get_gamification_insights_members) | Query users in a profile during a period of time|
|[**get_gamification_insights_trends**](GamificationApi.html#get_gamification_insights_trends) | Get insights user trend for the current user|
|[**get_gamification_insights_user_details**](GamificationApi.html#get_gamification_insights_user_details) | Get insights details for the user|
|[**get_gamification_insights_user_trends**](GamificationApi.html#get_gamification_insights_user_trends) | Get insights user trend for the user|
|[**get_gamification_leaderboard**](GamificationApi.html#get_gamification_leaderboard) | Leaderboard of the requesting user&#39;s division or performance profile|
|[**get_gamification_leaderboard_all**](GamificationApi.html#get_gamification_leaderboard_all) | Leaderboard by filter type|
|[**get_gamification_leaderboard_all_bestpoints**](GamificationApi.html#get_gamification_leaderboard_all_bestpoints) | Best Points by division or performance profile|
|[**get_gamification_leaderboard_bestpoints**](GamificationApi.html#get_gamification_leaderboard_bestpoints) | Best Points of the requesting user&#39;s current performance profile or division|
|[**get_gamification_metricdefinition**](GamificationApi.html#get_gamification_metricdefinition) | Metric definition by id|
|[**get_gamification_metricdefinitions**](GamificationApi.html#get_gamification_metricdefinitions) | All metric definitions|
|[**get_gamification_profile**](GamificationApi.html#get_gamification_profile) | Performance profile by id|
|[**get_gamification_profile_members**](GamificationApi.html#get_gamification_profile_members) | Members of a given performance profile|
|[**get_gamification_profile_metric**](GamificationApi.html#get_gamification_profile_metric) | Performance profile gamified metric by id|
|[**get_gamification_profile_metrics**](GamificationApi.html#get_gamification_profile_metrics) | All gamified metrics for a given performance profile|
|[**get_gamification_profile_metrics_objectivedetails**](GamificationApi.html#get_gamification_profile_metrics_objectivedetails) | All metrics for a given performance profile with objective details such as order and maxPoints|
|[**get_gamification_profiles**](GamificationApi.html#get_gamification_profiles) | All performance profiles|
|[**get_gamification_profiles_user**](GamificationApi.html#get_gamification_profiles_user) | Performance profile of a user|
|[**get_gamification_profiles_users_me**](GamificationApi.html#get_gamification_profiles_users_me) | Performance profile of the requesting user|
|[**get_gamification_scorecards**](GamificationApi.html#get_gamification_scorecards) | Workday performance metrics of the requesting user|
|[**get_gamification_scorecards_attendance**](GamificationApi.html#get_gamification_scorecards_attendance) | Attendance status metrics of the requesting user|
|[**get_gamification_scorecards_bestpoints**](GamificationApi.html#get_gamification_scorecards_bestpoints) | Best points of the requesting user|
|[**get_gamification_scorecards_points_alltime**](GamificationApi.html#get_gamification_scorecards_points_alltime) | All-time points of the requesting user|
|[**get_gamification_scorecards_points_average**](GamificationApi.html#get_gamification_scorecards_points_average) | Average points of the requesting user&#39;s division or performance profile|
|[**get_gamification_scorecards_points_trends**](GamificationApi.html#get_gamification_scorecards_points_trends) | Points trends of the requesting user|
|[**get_gamification_scorecards_profile_metric_user_values_trends**](GamificationApi.html#get_gamification_scorecards_profile_metric_user_values_trends) | Average performance values trends by metric of a user|
|[**get_gamification_scorecards_profile_metric_users_values_trends**](GamificationApi.html#get_gamification_scorecards_profile_metric_users_values_trends) | Average performance values trends by metric of a division or a performance profile|
|[**get_gamification_scorecards_profile_metric_values_trends**](GamificationApi.html#get_gamification_scorecards_profile_metric_values_trends) | Average performance values trends by metric of the requesting user|
|[**get_gamification_scorecards_user**](GamificationApi.html#get_gamification_scorecards_user) | Workday performance metrics for a user|
|[**get_gamification_scorecards_user_attendance**](GamificationApi.html#get_gamification_scorecards_user_attendance) | Attendance status metrics for a user|
|[**get_gamification_scorecards_user_bestpoints**](GamificationApi.html#get_gamification_scorecards_user_bestpoints) | Best points of a user|
|[**get_gamification_scorecards_user_points_alltime**](GamificationApi.html#get_gamification_scorecards_user_points_alltime) | All-time points for a user|
|[**get_gamification_scorecards_user_points_trends**](GamificationApi.html#get_gamification_scorecards_user_points_trends) | Points trend for a user|
|[**get_gamification_scorecards_user_values_trends**](GamificationApi.html#get_gamification_scorecards_user_values_trends) | Values trends of a user|
|[**get_gamification_scorecards_users_points_average**](GamificationApi.html#get_gamification_scorecards_users_points_average) | Workday average points by target group|
|[**get_gamification_scorecards_users_values_average**](GamificationApi.html#get_gamification_scorecards_users_values_average) | Workday average values by target group|
|[**get_gamification_scorecards_users_values_trends**](GamificationApi.html#get_gamification_scorecards_users_values_trends) | Values trend by target group|
|[**get_gamification_scorecards_values_average**](GamificationApi.html#get_gamification_scorecards_values_average) | Average values of the requesting user&#39;s division or performance profile|
|[**get_gamification_scorecards_values_trends**](GamificationApi.html#get_gamification_scorecards_values_trends) | Values trends of the requesting user or group|
|[**get_gamification_status**](GamificationApi.html#get_gamification_status) | Gamification activation status|
|[**get_gamification_template**](GamificationApi.html#get_gamification_template) | Objective template by id|
|[**get_gamification_templates**](GamificationApi.html#get_gamification_templates) | All objective templates|
|[**patch_employeeperformance_externalmetrics_definition**](GamificationApi.html#patch_employeeperformance_externalmetrics_definition) | Update External Metric Definition|
|[**post_employeeperformance_externalmetrics_data**](GamificationApi.html#post_employeeperformance_externalmetrics_data) | Write External Metric Data|
|[**post_employeeperformance_externalmetrics_definitions**](GamificationApi.html#post_employeeperformance_externalmetrics_definitions) | Create External Metric Definition|
|[**post_gamification_profile_activate**](GamificationApi.html#post_gamification_profile_activate) | Activate a performance profile|
|[**post_gamification_profile_deactivate**](GamificationApi.html#post_gamification_profile_deactivate) | Deactivate a performance profile|
|[**post_gamification_profile_members**](GamificationApi.html#post_gamification_profile_members) | Assign members to a given performance profile|
|[**post_gamification_profile_members_validate**](GamificationApi.html#post_gamification_profile_members_validate) | Validate member assignment|
|[**post_gamification_profile_metric_link**](GamificationApi.html#post_gamification_profile_metric_link) | Creates a linked metric|
|[**post_gamification_profile_metrics**](GamificationApi.html#post_gamification_profile_metrics) | Creates a gamified metric with a given metric definition and metric objective under in a performance profile|
|[**post_gamification_profiles**](GamificationApi.html#post_gamification_profiles) | Create a new custom performance profile|
|[**post_gamification_profiles_user_query**](GamificationApi.html#post_gamification_profiles_user_query) | Query performance profiles in date range for a user|
|[**post_gamification_profiles_users_me_query**](GamificationApi.html#post_gamification_profiles_users_me_query) | Query performance profiles in date range for the current user|
|[**put_gamification_profile**](GamificationApi.html#put_gamification_profile) | Updates a performance profile|
|[**put_gamification_profile_metric**](GamificationApi.html#put_gamification_profile_metric) | Updates a metric in performance profile|
|[**put_gamification_status**](GamificationApi.html#put_gamification_status) | Update gamification activation status|
{: class="table table-striped"}

<a name="delete_employeeperformance_externalmetrics_definition"></a>

##  delete_employeeperformance_externalmetrics_definition(metric_id)



Delete an External Metric Definition

Wraps DELETE /api/v2/employeeperformance/externalmetrics/definitions/{metricId} 

Requires ANY permissions: 

* employeePerformance:externalMetricDefinition:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
metric_id = 'metric_id_example' # str | Specifies the External Metric Definition ID

try:
    # Delete an External Metric Definition
    api_instance.delete_employeeperformance_externalmetrics_definition(metric_id)
except ApiException as e:
    print("Exception when calling GamificationApi->delete_employeeperformance_externalmetrics_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **metric_id** | **str**| Specifies the External Metric Definition ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_employeeperformance_externalmetrics_definition"></a>

## [**ExternalMetricDefinition**](ExternalMetricDefinition.html) get_employeeperformance_externalmetrics_definition(metric_id)



Get an External Metric Definition

Wraps GET /api/v2/employeeperformance/externalmetrics/definitions/{metricId} 

Requires ANY permissions: 

* employeePerformance:externalMetricDefinition:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
metric_id = 'metric_id_example' # str | Specifies the External Metric Definition ID

try:
    # Get an External Metric Definition
    api_response = api_instance.get_employeeperformance_externalmetrics_definition(metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_employeeperformance_externalmetrics_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **metric_id** | **str**| Specifies the External Metric Definition ID |  |
{: class="table table-striped"}

### Return type

[**ExternalMetricDefinition**](ExternalMetricDefinition.html)

<a name="get_employeeperformance_externalmetrics_definitions"></a>

## [**ExternalMetricDefinitionListing**](ExternalMetricDefinitionListing.html) get_employeeperformance_externalmetrics_definitions(page_size=page_size, page_number=page_number)



Get a list of External Metric Definitions of an organization, sorted by name in ascending order

Wraps GET /api/v2/employeeperformance/externalmetrics/definitions 

Requires ANY permissions: 

* employeePerformance:externalMetricDefinition:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of External Metric Definitions of an organization, sorted by name in ascending order
    api_response = api_instance.get_employeeperformance_externalmetrics_definitions(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_employeeperformance_externalmetrics_definitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**ExternalMetricDefinitionListing**](ExternalMetricDefinitionListing.html)

<a name="get_gamification_insights"></a>

## [**InsightsSummary**](InsightsSummary.html) get_gamification_insights(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday, page_size=page_size, page_number=page_number, sort_key=sort_key, sort_metric_id=sort_metric_id, sort_order=sort_order, user_ids=user_ids)



Get insights summary

Wraps GET /api/v2/gamification/insights 

Requires ANY permissions: 

* gamification:insights:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_key = 'sort_key_example' # str | Sort key (optional)
sort_metric_id = 'sort_metric_id_example' # str | Sort Metric Id (optional)
sort_order = ''asc'' # str | Sort order (optional) (default to 'asc')
user_ids = 'user_ids_example' # str | A list of up to 100 comma-separated user Ids (optional)

try:
    # Get insights summary
    api_response = api_instance.get_gamification_insights(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday, page_size=page_size, page_number=page_number, sort_key=sort_key, sort_metric_id=sort_metric_id, sort_order=sort_order, user_ids=user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Weekly, Monthly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_key** | **str**| Sort key | [optional] <br />**Values**: percentOfGoal, percentOfGoalChange, overallPercentOfGoal, overallPercentOfGoalChange, value, valueChange |
| **sort_metric_id** | **str**| Sort Metric Id | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **user_ids** | **str**| A list of up to 100 comma-separated user Ids | [optional]  |
{: class="table table-striped"}

### Return type

[**InsightsSummary**](InsightsSummary.html)

<a name="get_gamification_insights_details"></a>

## [**InsightsDetails**](InsightsDetails.html) get_gamification_insights_details(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday)



Get insights details for the current user

Wraps GET /api/v2/gamification/insights/details 

Requires ANY permissions: 

* gamification:insights:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get insights details for the current user
    api_response = api_instance.get_gamification_insights_details(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Weekly, Monthly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**InsightsDetails**](InsightsDetails.html)

<a name="get_gamification_insights_groups_trends"></a>

## [**InsightsTrend**](InsightsTrend.html) get_gamification_insights_groups_trends(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)



Get insights overall trend for the current user

Wraps GET /api/v2/gamification/insights/groups/trends 

Requires ANY permissions: 

* gamification:insights:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
comparative_period_end_workday = '2013-10-20' # date | The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_end_workday = '2013-10-20' # date | The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get insights overall trend for the current user
    api_response = api_instance.get_gamification_insights_groups_trends(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_groups_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Daily, Weekly, Monthly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **comparative_period_end_workday** | **date**| The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_end_workday** | **date**| The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**InsightsTrend**](InsightsTrend.html)

<a name="get_gamification_insights_groups_trends_all"></a>

## [**InsightsTrend**](InsightsTrend.html) get_gamification_insights_groups_trends_all(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)



Get insights overall trend

Wraps GET /api/v2/gamification/insights/groups/trends/all 

Requires ANY permissions: 

* gamification:insights:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
comparative_period_end_workday = '2013-10-20' # date | The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_end_workday = '2013-10-20' # date | The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get insights overall trend
    api_response = api_instance.get_gamification_insights_groups_trends_all(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_groups_trends_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Daily, Weekly, Monthly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **comparative_period_end_workday** | **date**| The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_end_workday** | **date**| The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**InsightsTrend**](InsightsTrend.html)

<a name="get_gamification_insights_members"></a>

## [**InsightsAgents**](InsightsAgents.html) get_gamification_insights_members(filter_type, filter_id, granularity, start_workday)



Query users in a profile during a period of time

Wraps GET /api/v2/gamification/insights/members 

Requires ANY permissions: 

* gamification:insights:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
start_workday = '2013-10-20' # date | The start work day. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Query users in a profile during a period of time
    api_response = api_instance.get_gamification_insights_members(filter_type, filter_id, granularity, start_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Weekly, Monthly |
| **start_workday** | **date**| The start work day. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**InsightsAgents**](InsightsAgents.html)

<a name="get_gamification_insights_trends"></a>

## [**UserInsightsTrend**](UserInsightsTrend.html) get_gamification_insights_trends(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)



Get insights user trend for the current user

Wraps GET /api/v2/gamification/insights/trends 

Requires ANY permissions: 

* gamification:insights:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
comparative_period_end_workday = '2013-10-20' # date | The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_end_workday = '2013-10-20' # date | The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get insights user trend for the current user
    api_response = api_instance.get_gamification_insights_trends(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Daily, Weekly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **comparative_period_end_workday** | **date**| The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_end_workday** | **date**| The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**UserInsightsTrend**](UserInsightsTrend.html)

<a name="get_gamification_insights_user_details"></a>

## [**InsightsDetails**](InsightsDetails.html) get_gamification_insights_user_details(user_id, filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday)



Get insights details for the user

Wraps GET /api/v2/gamification/insights/users/{userId}/details 

Requires ANY permissions: 

* gamification:insights:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | The ID of a user.
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get insights details for the user
    api_response = api_instance.get_gamification_insights_user_details(user_id, filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_user_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. |  |
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Weekly, Monthly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**InsightsDetails**](InsightsDetails.html)

<a name="get_gamification_insights_user_trends"></a>

## [**UserInsightsTrend**](UserInsightsTrend.html) get_gamification_insights_user_trends(user_id, filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)



Get insights user trend for the user

Wraps GET /api/v2/gamification/insights/users/{userId}/trends 

Requires ANY permissions: 

* gamification:insights:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | The ID of a user.
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
granularity = 'granularity_example' # str | Granularity
comparative_period_start_workday = '2013-10-20' # date | The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
comparative_period_end_workday = '2013-10-20' # date | The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_start_workday = '2013-10-20' # date | The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
primary_period_end_workday = '2013-10-20' # date | The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get insights user trend for the user
    api_response = api_instance.get_gamification_insights_user_trends(user_id, filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_user_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. |  |
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Daily, Weekly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **comparative_period_end_workday** | **date**| The end work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_end_workday** | **date**| The end work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**UserInsightsTrend**](UserInsightsTrend.html)

<a name="get_gamification_leaderboard"></a>

## [**Leaderboard**](Leaderboard.html) get_gamification_leaderboard(start_workday, end_workday, metric_id=metric_id)



Leaderboard of the requesting user's division or performance profile

Wraps GET /api/v2/gamification/leaderboard 

Requires ANY permissions: 

* gamification:leaderboard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
start_workday = '2013-10-20' # date | Start workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
metric_id = 'metric_id_example' # str | Metric Id for which the leaderboard is to be generated. The total points is used if nothing is given. (optional)

try:
    # Leaderboard of the requesting user's division or performance profile
    api_response = api_instance.get_gamification_leaderboard(start_workday, end_workday, metric_id=metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_leaderboard: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_workday** | **date**| Start workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **metric_id** | **str**| Metric Id for which the leaderboard is to be generated. The total points is used if nothing is given. | [optional]  |
{: class="table table-striped"}

### Return type

[**Leaderboard**](Leaderboard.html)

<a name="get_gamification_leaderboard_all"></a>

## [**Leaderboard**](Leaderboard.html) get_gamification_leaderboard_all(filter_type, filter_id, start_workday, end_workday, metric_id=metric_id)



Leaderboard by filter type

Wraps GET /api/v2/gamification/leaderboard/all 

Requires ANY permissions: 

* gamification:leaderboard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type. For example, division or performance profile Id
start_workday = '2013-10-20' # date | Start workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
metric_id = 'metric_id_example' # str | Metric Id for which the leaderboard is to be generated. The total points is used if nothing is given. (optional)

try:
    # Leaderboard by filter type
    api_response = api_instance.get_gamification_leaderboard_all(filter_type, filter_id, start_workday, end_workday, metric_id=metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_leaderboard_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. For example, division or performance profile Id |  |
| **start_workday** | **date**| Start workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday to retrieve for the leaderboard. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **metric_id** | **str**| Metric Id for which the leaderboard is to be generated. The total points is used if nothing is given. | [optional]  |
{: class="table table-striped"}

### Return type

[**Leaderboard**](Leaderboard.html)

<a name="get_gamification_leaderboard_all_bestpoints"></a>

## [**OverallBestPoints**](OverallBestPoints.html) get_gamification_leaderboard_all_bestpoints(filter_type, filter_id)



Best Points by division or performance profile

Wraps GET /api/v2/gamification/leaderboard/all/bestpoints 

Requires ANY permissions: 

* gamification:leaderboard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type. For example, division or performance profile Id

try:
    # Best Points by division or performance profile
    api_response = api_instance.get_gamification_leaderboard_all_bestpoints(filter_type, filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_leaderboard_all_bestpoints: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. For example, division or performance profile Id |  |
{: class="table table-striped"}

### Return type

[**OverallBestPoints**](OverallBestPoints.html)

<a name="get_gamification_leaderboard_bestpoints"></a>

## [**OverallBestPoints**](OverallBestPoints.html) get_gamification_leaderboard_bestpoints()



Best Points of the requesting user's current performance profile or division

Wraps GET /api/v2/gamification/leaderboard/bestpoints 

Requires ANY permissions: 

* gamification:leaderboard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()

try:
    # Best Points of the requesting user's current performance profile or division
    api_response = api_instance.get_gamification_leaderboard_bestpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_leaderboard_bestpoints: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**OverallBestPoints**](OverallBestPoints.html)

<a name="get_gamification_metricdefinition"></a>

## [**MetricDefinition**](MetricDefinition.html) get_gamification_metricdefinition(metric_definition_id)



Metric definition by id

Wraps GET /api/v2/gamification/metricdefinitions/{metricDefinitionId} 

Requires ANY permissions: 

* gamification:profile:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
metric_definition_id = 'metric_definition_id_example' # str | metric definition id

try:
    # Metric definition by id
    api_response = api_instance.get_gamification_metricdefinition(metric_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_metricdefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **metric_definition_id** | **str**| metric definition id |  |
{: class="table table-striped"}

### Return type

[**MetricDefinition**](MetricDefinition.html)

<a name="get_gamification_metricdefinitions"></a>

## [**GetMetricDefinitionsResponse**](GetMetricDefinitionsResponse.html) get_gamification_metricdefinitions()



All metric definitions

Retrieves the metric definitions and their corresponding default objectives used to create a gamified metric

Wraps GET /api/v2/gamification/metricdefinitions 

Requires ANY permissions: 

* gamification:profile:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()

try:
    # All metric definitions
    api_response = api_instance.get_gamification_metricdefinitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_metricdefinitions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**GetMetricDefinitionsResponse**](GetMetricDefinitionsResponse.html)

<a name="get_gamification_profile"></a>

## [**PerformanceProfile**](PerformanceProfile.html) get_gamification_profile(profile_id)



Performance profile by id

Wraps GET /api/v2/gamification/profiles/{profileId} 

Requires ANY permissions: 

* gamification:profile:view
* gamification:leaderboard:viewAll
* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId

try:
    # Performance profile by id
    api_response = api_instance.get_gamification_profile(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profile: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="get_gamification_profile_members"></a>

## [**MemberListing**](MemberListing.html) get_gamification_profile_members(profile_id)



Members of a given performance profile

Wraps GET /api/v2/gamification/profiles/{profileId}/members 

Requires ANY permissions: 

* gamification:profile:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Profile Id

try:
    # Members of a given performance profile
    api_response = api_instance.get_gamification_profile_members(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profile_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Profile Id |  |
{: class="table table-striped"}

### Return type

[**MemberListing**](MemberListing.html)

<a name="get_gamification_profile_metric"></a>

## [**Metric**](Metric.html) get_gamification_profile_metric(profile_id, metric_id, workday=workday)



Performance profile gamified metric by id

Wraps GET /api/v2/gamification/profiles/{profileId}/metrics/{metricId} 

Requires ANY permissions: 

* gamification:profile:view
* gamification:leaderboard:view
* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Performance Profile Id
metric_id = 'metric_id_example' # str | Metric Id
workday = '2013-10-20' # date | The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # Performance profile gamified metric by id
    api_response = api_instance.get_gamification_profile_metric(profile_id, metric_id, workday=workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profile_metric: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Performance Profile Id |  |
| **metric_id** | **str**| Metric Id |  |
| **workday** | **date**| The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
{: class="table table-striped"}

### Return type

[**Metric**](Metric.html)

<a name="get_gamification_profile_metrics"></a>

## [**GetMetricResponse**](GetMetricResponse.html) get_gamification_profile_metrics(profile_id, expand=expand, workday=workday, metric_ids=metric_ids)



All gamified metrics for a given performance profile

Wraps GET /api/v2/gamification/profiles/{profileId}/metrics 

Requires ANY permissions: 

* gamification:profile:view
* gamification:leaderboard:view
* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Performance Profile Id
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
workday = '2013-10-20' # date | The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
metric_ids = 'metric_ids_example' # str | List of metric ids to filter the response (Optional, comma-separated). (optional)

try:
    # All gamified metrics for a given performance profile
    api_response = api_instance.get_gamification_profile_metrics(profile_id, expand=expand, workday=workday, metric_ids=metric_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profile_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Performance Profile Id |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: objective |
| **workday** | **date**| The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **metric_ids** | **str**| List of metric ids to filter the response (Optional, comma-separated). | [optional]  |
{: class="table table-striped"}

### Return type

[**GetMetricResponse**](GetMetricResponse.html)

<a name="get_gamification_profile_metrics_objectivedetails"></a>

## [**GetMetricsResponse**](GetMetricsResponse.html) get_gamification_profile_metrics_objectivedetails(profile_id, workday=workday)



All metrics for a given performance profile with objective details such as order and maxPoints

Wraps GET /api/v2/gamification/profiles/{profileId}/metrics/objectivedetails 

Requires ANY permissions: 

* gamification:profile:view
* gamification:leaderboard:view
* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Performance Profile Id
workday = '2013-10-20' # date | The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # All metrics for a given performance profile with objective details such as order and maxPoints
    api_response = api_instance.get_gamification_profile_metrics_objectivedetails(profile_id, workday=workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profile_metrics_objectivedetails: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Performance Profile Id |  |
| **workday** | **date**| The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
{: class="table table-striped"}

### Return type

[**GetMetricsResponse**](GetMetricsResponse.html)

<a name="get_gamification_profiles"></a>

## [**GetProfilesResponse**](GetProfilesResponse.html) get_gamification_profiles()



All performance profiles

Wraps GET /api/v2/gamification/profiles 

Requires ANY permissions: 

* gamification:profile:view
* gamification:leaderboard:viewAll
* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()

try:
    # All performance profiles
    api_response = api_instance.get_gamification_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profiles: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**GetProfilesResponse**](GetProfilesResponse.html)

<a name="get_gamification_profiles_user"></a>

## [**PerformanceProfile**](PerformanceProfile.html) get_gamification_profiles_user(user_id, workday=workday)



Performance profile of a user

Wraps GET /api/v2/gamification/profiles/users/{userId} 

Requires ANY permissions: 

* gamification:profile:view
* gamification:scorecard:viewAll
* gamification:leaderboard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 
workday = '2013-10-20' # date | Target querying workday. If not provided, then queries the current performance profile. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # Performance profile of a user
    api_response = api_instance.get_gamification_profiles_user(user_id, workday=workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profiles_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **workday** | **date**| Target querying workday. If not provided, then queries the current performance profile. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="get_gamification_profiles_users_me"></a>

## [**PerformanceProfile**](PerformanceProfile.html) get_gamification_profiles_users_me(workday=workday)



Performance profile of the requesting user

Wraps GET /api/v2/gamification/profiles/users/me 

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
api_instance = PureCloudPlatformClientV2.GamificationApi()
workday = '2013-10-20' # date | Target querying workday. If not provided, then queries the current performance profile. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # Performance profile of the requesting user
    api_response = api_instance.get_gamification_profiles_users_me(workday=workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_profiles_users_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workday** | **date**| Target querying workday. If not provided, then queries the current performance profile. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="get_gamification_scorecards"></a>

## [**WorkdayMetricListing**](WorkdayMetricListing.html) get_gamification_scorecards(workday, expand=expand)



Workday performance metrics of the requesting user

Wraps GET /api/v2/gamification/scorecards 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
workday = '2013-10-20' # date | Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Workday performance metrics of the requesting user
    api_response = api_instance.get_gamification_scorecards(workday, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workday** | **date**| Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: objective |
{: class="table table-striped"}

### Return type

[**WorkdayMetricListing**](WorkdayMetricListing.html)

<a name="get_gamification_scorecards_attendance"></a>

## [**AttendanceStatusListing**](AttendanceStatusListing.html) get_gamification_scorecards_attendance(start_workday, end_workday)



Attendance status metrics of the requesting user

Wraps GET /api/v2/gamification/scorecards/attendance 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Attendance status metrics of the requesting user
    api_response = api_instance.get_gamification_scorecards_attendance(start_workday, end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_attendance: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**AttendanceStatusListing**](AttendanceStatusListing.html)

<a name="get_gamification_scorecards_bestpoints"></a>

## [**UserBestPoints**](UserBestPoints.html) get_gamification_scorecards_bestpoints()



Best points of the requesting user

Wraps GET /api/v2/gamification/scorecards/bestpoints 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()

try:
    # Best points of the requesting user
    api_response = api_instance.get_gamification_scorecards_bestpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_bestpoints: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**UserBestPoints**](UserBestPoints.html)

<a name="get_gamification_scorecards_points_alltime"></a>

## [**AllTimePoints**](AllTimePoints.html) get_gamification_scorecards_points_alltime(end_workday)



All-time points of the requesting user

Wraps GET /api/v2/gamification/scorecards/points/alltime 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # All-time points of the requesting user
    api_response = api_instance.get_gamification_scorecards_points_alltime(end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_points_alltime: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**AllTimePoints**](AllTimePoints.html)

<a name="get_gamification_scorecards_points_average"></a>

## [**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints.html) get_gamification_scorecards_points_average(workday)



Average points of the requesting user's division or performance profile

Wraps GET /api/v2/gamification/scorecards/points/average 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
workday = '2013-10-20' # date | The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Average points of the requesting user's division or performance profile
    api_response = api_instance.get_gamification_scorecards_points_average(workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_points_average: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workday** | **date**| The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints.html)

<a name="get_gamification_scorecards_points_trends"></a>

## [**WorkdayPointsTrend**](WorkdayPointsTrend.html) get_gamification_scorecards_points_trends(start_workday, end_workday, day_of_week=day_of_week)



Points trends of the requesting user

Wraps GET /api/v2/gamification/scorecards/points/trends 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
day_of_week = 'day_of_week_example' # str | Optional filter to specify which day of weeks to be included in the response (optional)

try:
    # Points trends of the requesting user
    api_response = api_instance.get_gamification_scorecards_points_trends(start_workday, end_workday, day_of_week=day_of_week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_points_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **day_of_week** | **str**| Optional filter to specify which day of weeks to be included in the response | [optional] <br />**Values**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday |
{: class="table table-striped"}

### Return type

[**WorkdayPointsTrend**](WorkdayPointsTrend.html)

<a name="get_gamification_scorecards_profile_metric_user_values_trends"></a>

## [**MetricValueTrendAverage**](MetricValueTrendAverage.html) get_gamification_scorecards_profile_metric_user_values_trends(profile_id, metric_id, user_id, start_workday, end_workday, reference_workday=reference_workday, time_zone=time_zone)



Average performance values trends by metric of a user

Wraps GET /api/v2/gamification/scorecards/profiles/{profileId}/metrics/{metricId}/users/{userId}/values/trends 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId
metric_id = 'metric_id_example' # str | metricId
user_id = 'user_id_example' # str | 
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
reference_workday = '2013-10-20' # date | Reference workday for the trend. Used to determine the associated metric definition. If not set, then the value of endWorkday is used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Average performance values trends by metric of a user
    api_response = api_instance.get_gamification_scorecards_profile_metric_user_values_trends(profile_id, metric_id, user_id, start_workday, end_workday, reference_workday=reference_workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_profile_metric_user_values_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
| **metric_id** | **str**| metricId |  |
| **user_id** | **str**|  |  |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **reference_workday** | **date**| Reference workday for the trend. Used to determine the associated metric definition. If not set, then the value of endWorkday is used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**MetricValueTrendAverage**](MetricValueTrendAverage.html)

<a name="get_gamification_scorecards_profile_metric_users_values_trends"></a>

## [**MetricValueTrendAverage**](MetricValueTrendAverage.html) get_gamification_scorecards_profile_metric_users_values_trends(profile_id, metric_id, filter_type, start_workday, end_workday, filter_id=filter_id, reference_workday=reference_workday, time_zone=time_zone)



Average performance values trends by metric of a division or a performance profile

Wraps GET /api/v2/gamification/scorecards/profiles/{profileId}/metrics/{metricId}/users/values/trends 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId
metric_id = 'metric_id_example' # str | metricId
filter_type = 'filter_type_example' # str | Filter type for the query request.
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
filter_id = 'filter_id_example' # str | ID for the filter type. Only required when filterType is Division. (optional)
reference_workday = '2013-10-20' # date | Reference workday for the trend. Used to determine the associated metric definition. If not set, then the value of endWorkday is used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Average performance values trends by metric of a division or a performance profile
    api_response = api_instance.get_gamification_scorecards_profile_metric_users_values_trends(profile_id, metric_id, filter_type, start_workday, end_workday, filter_id=filter_id, reference_workday=reference_workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_profile_metric_users_values_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
| **metric_id** | **str**| metricId |  |
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **filter_id** | **str**| ID for the filter type. Only required when filterType is Division. | [optional]  |
| **reference_workday** | **date**| Reference workday for the trend. Used to determine the associated metric definition. If not set, then the value of endWorkday is used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**MetricValueTrendAverage**](MetricValueTrendAverage.html)

<a name="get_gamification_scorecards_profile_metric_values_trends"></a>

## [**MetricValueTrendAverage**](MetricValueTrendAverage.html) get_gamification_scorecards_profile_metric_values_trends(profile_id, metric_id, start_workday, end_workday, filter_type=filter_type, reference_workday=reference_workday, time_zone=time_zone)



Average performance values trends by metric of the requesting user

Wraps GET /api/v2/gamification/scorecards/profiles/{profileId}/metrics/{metricId}/values/trends 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId
metric_id = 'metric_id_example' # str | metricId
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
filter_type = 'filter_type_example' # str | Filter type for the query request. If not set, returns the values trends of the requesting user (optional)
reference_workday = '2013-10-20' # date | Reference workday for the trend. Used to determine the associated metric definition. If not set, then the value of endWorkday is used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Average performance values trends by metric of the requesting user
    api_response = api_instance.get_gamification_scorecards_profile_metric_values_trends(profile_id, metric_id, start_workday, end_workday, filter_type=filter_type, reference_workday=reference_workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_profile_metric_values_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
| **metric_id** | **str**| metricId |  |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **filter_type** | **str**| Filter type for the query request. If not set, returns the values trends of the requesting user | [optional] <br />**Values**: PerformanceProfile, Division |
| **reference_workday** | **date**| Reference workday for the trend. Used to determine the associated metric definition. If not set, then the value of endWorkday is used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**MetricValueTrendAverage**](MetricValueTrendAverage.html)

<a name="get_gamification_scorecards_user"></a>

## [**WorkdayMetricListing**](WorkdayMetricListing.html) get_gamification_scorecards_user(user_id, workday, expand=expand)



Workday performance metrics for a user

Wraps GET /api/v2/gamification/scorecards/users/{userId} 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 
workday = '2013-10-20' # date | Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Workday performance metrics for a user
    api_response = api_instance.get_gamification_scorecards_user(user_id, workday, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **workday** | **date**| Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: objective |
{: class="table table-striped"}

### Return type

[**WorkdayMetricListing**](WorkdayMetricListing.html)

<a name="get_gamification_scorecards_user_attendance"></a>

## [**AttendanceStatusListing**](AttendanceStatusListing.html) get_gamification_scorecards_user_attendance(user_id, start_workday, end_workday)



Attendance status metrics for a user

Wraps GET /api/v2/gamification/scorecards/users/{userId}/attendance 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Attendance status metrics for a user
    api_response = api_instance.get_gamification_scorecards_user_attendance(user_id, start_workday, end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_user_attendance: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**AttendanceStatusListing**](AttendanceStatusListing.html)

<a name="get_gamification_scorecards_user_bestpoints"></a>

## [**UserBestPoints**](UserBestPoints.html) get_gamification_scorecards_user_bestpoints(user_id)



Best points of a user

Wraps GET /api/v2/gamification/scorecards/users/{userId}/bestpoints 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 

try:
    # Best points of a user
    api_response = api_instance.get_gamification_scorecards_user_bestpoints(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_user_bestpoints: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
{: class="table table-striped"}

### Return type

[**UserBestPoints**](UserBestPoints.html)

<a name="get_gamification_scorecards_user_points_alltime"></a>

## [**AllTimePoints**](AllTimePoints.html) get_gamification_scorecards_user_points_alltime(user_id, end_workday)



All-time points for a user

Wraps GET /api/v2/gamification/scorecards/users/{userId}/points/alltime 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # All-time points for a user
    api_response = api_instance.get_gamification_scorecards_user_points_alltime(user_id, end_workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_user_points_alltime: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**AllTimePoints**](AllTimePoints.html)

<a name="get_gamification_scorecards_user_points_trends"></a>

## [**WorkdayPointsTrend**](WorkdayPointsTrend.html) get_gamification_scorecards_user_points_trends(user_id, start_workday, end_workday, day_of_week=day_of_week)



Points trend for a user

Wraps GET /api/v2/gamification/scorecards/users/{userId}/points/trends 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
day_of_week = 'day_of_week_example' # str | Optional filter to specify which day of weeks to be included in the response (optional)

try:
    # Points trend for a user
    api_response = api_instance.get_gamification_scorecards_user_points_trends(user_id, start_workday, end_workday, day_of_week=day_of_week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_user_points_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **day_of_week** | **str**| Optional filter to specify which day of weeks to be included in the response | [optional] <br />**Values**: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday |
{: class="table table-striped"}

### Return type

[**WorkdayPointsTrend**](WorkdayPointsTrend.html)

<a name="get_gamification_scorecards_user_values_trends"></a>

## [**WorkdayValuesTrend**](WorkdayValuesTrend.html) get_gamification_scorecards_user_values_trends(user_id, start_workday, end_workday, time_zone=time_zone)



Values trends of a user

Wraps GET /api/v2/gamification/scorecards/users/{userId}/values/trends 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | 
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Values trends of a user
    api_response = api_instance.get_gamification_scorecards_user_values_trends(user_id, start_workday, end_workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_user_values_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**WorkdayValuesTrend**](WorkdayValuesTrend.html)

<a name="get_gamification_scorecards_users_points_average"></a>

## [**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints.html) get_gamification_scorecards_users_points_average(filter_type, filter_id, workday)



Workday average points by target group

Wraps GET /api/v2/gamification/scorecards/users/points/average 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
workday = '2013-10-20' # date | The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Workday average points by target group
    api_response = api_instance.get_gamification_scorecards_users_points_average(filter_type, filter_id, workday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_users_points_average: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **workday** | **date**| The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
{: class="table table-striped"}

### Return type

[**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints.html)

<a name="get_gamification_scorecards_users_values_average"></a>

## [**SingleWorkdayAverageValues**](SingleWorkdayAverageValues.html) get_gamification_scorecards_users_values_average(filter_type, filter_id, workday, time_zone=time_zone)



Workday average values by target group

Wraps GET /api/v2/gamification/scorecards/users/values/average 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type. For example, division Id
workday = '2013-10-20' # date | The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Workday average values by target group
    api_response = api_instance.get_gamification_scorecards_users_values_average(filter_type, filter_id, workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_users_values_average: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. For example, division Id |  |
| **workday** | **date**| The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**SingleWorkdayAverageValues**](SingleWorkdayAverageValues.html)

<a name="get_gamification_scorecards_users_values_trends"></a>

## [**WorkdayValuesTrend**](WorkdayValuesTrend.html) get_gamification_scorecards_users_values_trends(filter_type, filter_id, start_workday, end_workday, time_zone=time_zone)



Values trend by target group

Wraps GET /api/v2/gamification/scorecards/users/values/trends 

Requires ANY permissions: 

* gamification:scorecard:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
filter_type = 'filter_type_example' # str | Filter type for the query request.
filter_id = 'filter_id_example' # str | ID for the filter type.
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Values trend by target group
    api_response = api_instance.get_gamification_scorecards_users_values_trends(filter_type, filter_id, start_workday, end_workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_users_values_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**WorkdayValuesTrend**](WorkdayValuesTrend.html)

<a name="get_gamification_scorecards_values_average"></a>

## [**SingleWorkdayAverageValues**](SingleWorkdayAverageValues.html) get_gamification_scorecards_values_average(workday, time_zone=time_zone)



Average values of the requesting user's division or performance profile

Wraps GET /api/v2/gamification/scorecards/values/average 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
workday = '2013-10-20' # date | The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Average values of the requesting user's division or performance profile
    api_response = api_instance.get_gamification_scorecards_values_average(workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_values_average: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workday** | **date**| The target workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**SingleWorkdayAverageValues**](SingleWorkdayAverageValues.html)

<a name="get_gamification_scorecards_values_trends"></a>

## [**WorkdayValuesTrend**](WorkdayValuesTrend.html) get_gamification_scorecards_values_trends(start_workday, end_workday, filter_type=filter_type, reference_workday=reference_workday, time_zone=time_zone)



Values trends of the requesting user or group

Wraps GET /api/v2/gamification/scorecards/values/trends 

Requires ANY permissions: 

* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
start_workday = '2013-10-20' # date | Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
end_workday = '2013-10-20' # date | End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
filter_type = 'filter_type_example' # str | Filter type for the query request. If not set, then the request is for the requesting user. (optional)
reference_workday = '2013-10-20' # date | Reference workday for the trend. Used to determine the profile of the user as of this date. If not set, then the user's current profile will be used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
time_zone = ''UTC'' # str | Timezone for the workday. Defaults to UTC (optional) (default to 'UTC')

try:
    # Values trends of the requesting user or group
    api_response = api_instance.get_gamification_scorecards_values_trends(start_workday, end_workday, filter_type=filter_type, reference_workday=reference_workday, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_scorecards_values_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_workday** | **date**| Start workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **end_workday** | **date**| End workday of querying workdays range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **filter_type** | **str**| Filter type for the query request. If not set, then the request is for the requesting user. | [optional] <br />**Values**: PerformanceProfile, Division |
| **reference_workday** | **date**| Reference workday for the trend. Used to determine the profile of the user as of this date. If not set, then the user&#39;s current profile will be used. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **time_zone** | **str**| Timezone for the workday. Defaults to UTC | [optional] [default to &#39;UTC&#39;] |
{: class="table table-striped"}

### Return type

[**WorkdayValuesTrend**](WorkdayValuesTrend.html)

<a name="get_gamification_status"></a>

## [**GamificationStatus**](GamificationStatus.html) get_gamification_status()



Gamification activation status

Wraps GET /api/v2/gamification/status 

Requires ANY permissions: 

* gamification:profile:view
* gamification:profile:update
* gamification:scorecard:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()

try:
    # Gamification activation status
    api_response = api_instance.get_gamification_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_status: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**GamificationStatus**](GamificationStatus.html)

<a name="get_gamification_template"></a>

## [**ObjectiveTemplate**](ObjectiveTemplate.html) get_gamification_template(template_id)



Objective template by id

Wraps GET /api/v2/gamification/templates/{templateId} 

Requires ANY permissions: 

* gamification:profile:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
template_id = 'template_id_example' # str | template id

try:
    # Objective template by id
    api_response = api_instance.get_gamification_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **template_id** | **str**| template id |  |
{: class="table table-striped"}

### Return type

[**ObjectiveTemplate**](ObjectiveTemplate.html)

<a name="get_gamification_templates"></a>

## [**GetTemplatesResponse**](GetTemplatesResponse.html) get_gamification_templates()



All objective templates

Wraps GET /api/v2/gamification/templates 

Requires ANY permissions: 

* gamification:profile:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()

try:
    # All objective templates
    api_response = api_instance.get_gamification_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_templates: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**GetTemplatesResponse**](GetTemplatesResponse.html)

<a name="patch_employeeperformance_externalmetrics_definition"></a>

## [**ExternalMetricDefinition**](ExternalMetricDefinition.html) patch_employeeperformance_externalmetrics_definition(metric_id, body)



Update External Metric Definition

Wraps PATCH /api/v2/employeeperformance/externalmetrics/definitions/{metricId} 

Requires ANY permissions: 

* employeePerformance:externalMetricDefinition:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
metric_id = 'metric_id_example' # str | Specifies the metric definition ID
body = PureCloudPlatformClientV2.ExternalMetricDefinitionUpdateRequest() # ExternalMetricDefinitionUpdateRequest | The External Metric Definition parameters to be updated

try:
    # Update External Metric Definition
    api_response = api_instance.patch_employeeperformance_externalmetrics_definition(metric_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->patch_employeeperformance_externalmetrics_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **metric_id** | **str**| Specifies the metric definition ID |  |
| **body** | [**ExternalMetricDefinitionUpdateRequest**](ExternalMetricDefinitionUpdateRequest.html)| The External Metric Definition parameters to be updated |  |
{: class="table table-striped"}

### Return type

[**ExternalMetricDefinition**](ExternalMetricDefinition.html)

<a name="post_employeeperformance_externalmetrics_data"></a>

## [**ExternalMetricDataWriteResponse**](ExternalMetricDataWriteResponse.html) post_employeeperformance_externalmetrics_data(body=body)



Write External Metric Data

Wraps POST /api/v2/employeeperformance/externalmetrics/data 

Requires ANY permissions: 

* employeePerformance:externalMetricData:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
body = PureCloudPlatformClientV2.ExternalMetricDataWriteRequest() # ExternalMetricDataWriteRequest | The External Metric Data to be added (optional)

try:
    # Write External Metric Data
    api_response = api_instance.post_employeeperformance_externalmetrics_data(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_employeeperformance_externalmetrics_data: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalMetricDataWriteRequest**](ExternalMetricDataWriteRequest.html)| The External Metric Data to be added | [optional]  |
{: class="table table-striped"}

### Return type

[**ExternalMetricDataWriteResponse**](ExternalMetricDataWriteResponse.html)

<a name="post_employeeperformance_externalmetrics_definitions"></a>

## [**ExternalMetricDefinition**](ExternalMetricDefinition.html) post_employeeperformance_externalmetrics_definitions(body=body)



Create External Metric Definition

Wraps POST /api/v2/employeeperformance/externalmetrics/definitions 

Requires ANY permissions: 

* employeePerformance:externalMetricDefinition:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
body = PureCloudPlatformClientV2.ExternalMetricDefinitionCreateRequest() # ExternalMetricDefinitionCreateRequest | The External Metric Definition to be created (optional)

try:
    # Create External Metric Definition
    api_response = api_instance.post_employeeperformance_externalmetrics_definitions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_employeeperformance_externalmetrics_definitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalMetricDefinitionCreateRequest**](ExternalMetricDefinitionCreateRequest.html)| The External Metric Definition to be created | [optional]  |
{: class="table table-striped"}

### Return type

[**ExternalMetricDefinition**](ExternalMetricDefinition.html)

<a name="post_gamification_profile_activate"></a>

## [**PerformanceProfile**](PerformanceProfile.html) post_gamification_profile_activate(profile_id)



Activate a performance profile

Wraps POST /api/v2/gamification/profiles/{profileId}/activate 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId

try:
    # Activate a performance profile
    api_response = api_instance.post_gamification_profile_activate(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profile_activate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="post_gamification_profile_deactivate"></a>

## [**PerformanceProfile**](PerformanceProfile.html) post_gamification_profile_deactivate(profile_id)



Deactivate a performance profile

Wraps POST /api/v2/gamification/profiles/{profileId}/deactivate 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId

try:
    # Deactivate a performance profile
    api_response = api_instance.post_gamification_profile_deactivate(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profile_deactivate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="post_gamification_profile_members"></a>

## [**Assignment**](Assignment.html) post_gamification_profile_members(profile_id, body)



Assign members to a given performance profile

Wraps POST /api/v2/gamification/profiles/{profileId}/members 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Profile Id
body = PureCloudPlatformClientV2.AssignUsers() # AssignUsers | assignUsers

try:
    # Assign members to a given performance profile
    api_response = api_instance.post_gamification_profile_members(profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profile_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Profile Id |  |
| **body** | [**AssignUsers**](AssignUsers.html)| assignUsers |  |
{: class="table table-striped"}

### Return type

[**Assignment**](Assignment.html)

<a name="post_gamification_profile_members_validate"></a>

## [**AssignmentValidation**](AssignmentValidation.html) post_gamification_profile_members_validate(profile_id, body)



Validate member assignment

Wraps POST /api/v2/gamification/profiles/{profileId}/members/validate 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Profile Id
body = PureCloudPlatformClientV2.ValidateAssignUsers() # ValidateAssignUsers | memberAssignments

try:
    # Validate member assignment
    api_response = api_instance.post_gamification_profile_members_validate(profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profile_members_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Profile Id |  |
| **body** | [**ValidateAssignUsers**](ValidateAssignUsers.html)| memberAssignments |  |
{: class="table table-striped"}

### Return type

[**AssignmentValidation**](AssignmentValidation.html)

<a name="post_gamification_profile_metric_link"></a>

## [**Metric**](Metric.html) post_gamification_profile_metric_link(source_profile_id, source_metric_id, body)



Creates a linked metric

Wraps POST /api/v2/gamification/profiles/{sourceProfileId}/metrics/{sourceMetricId}/link 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
source_profile_id = 'source_profile_id_example' # str | Source Performance Profile Id
source_metric_id = 'source_metric_id_example' # str | Source Metric Id
body = PureCloudPlatformClientV2.TargetPerformanceProfile() # TargetPerformanceProfile | linkedMetric

try:
    # Creates a linked metric
    api_response = api_instance.post_gamification_profile_metric_link(source_profile_id, source_metric_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profile_metric_link: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **source_profile_id** | **str**| Source Performance Profile Id |  |
| **source_metric_id** | **str**| Source Metric Id |  |
| **body** | [**TargetPerformanceProfile**](TargetPerformanceProfile.html)| linkedMetric |  |
{: class="table table-striped"}

### Return type

[**Metric**](Metric.html)

<a name="post_gamification_profile_metrics"></a>

## [**Metric**](Metric.html) post_gamification_profile_metrics(profile_id, body)



Creates a gamified metric with a given metric definition and metric objective under in a performance profile

Wraps POST /api/v2/gamification/profiles/{profileId}/metrics 

Requires ALL permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Performance Profile Id
body = PureCloudPlatformClientV2.CreateMetric() # CreateMetric | Metric

try:
    # Creates a gamified metric with a given metric definition and metric objective under in a performance profile
    api_response = api_instance.post_gamification_profile_metrics(profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profile_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Performance Profile Id |  |
| **body** | [**CreateMetric**](CreateMetric.html)| Metric |  |
{: class="table table-striped"}

### Return type

[**Metric**](Metric.html)

<a name="post_gamification_profiles"></a>

## [**PerformanceProfile**](PerformanceProfile.html) post_gamification_profiles(body, copy_metrics=copy_metrics)



Create a new custom performance profile

Wraps POST /api/v2/gamification/profiles 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
body = PureCloudPlatformClientV2.CreatePerformanceProfile() # CreatePerformanceProfile | performanceProfile
copy_metrics = True # bool | Flag to copy metrics. If set to false, there will be no metrics associated with the new profile. If set to true or is absent (the default behavior), all metrics from the default profile will be copied over into the new profile. (optional) (default to True)

try:
    # Create a new custom performance profile
    api_response = api_instance.post_gamification_profiles(body, copy_metrics=copy_metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profiles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreatePerformanceProfile**](CreatePerformanceProfile.html)| performanceProfile |  |
| **copy_metrics** | **bool**| Flag to copy metrics. If set to false, there will be no metrics associated with the new profile. If set to true or is absent (the default behavior), all metrics from the default profile will be copied over into the new profile. | [optional] [default to True] |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="post_gamification_profiles_user_query"></a>

## [**UserProfilesInDateRange**](UserProfilesInDateRange.html) post_gamification_profiles_user_query(user_id, body)



Query performance profiles in date range for a user

Wraps POST /api/v2/gamification/profiles/users/{userId}/query 

Requires ANY permissions: 

* gamification:agentProfileMembership:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
user_id = 'user_id_example' # str | The ID of a user.
body = PureCloudPlatformClientV2.UserProfilesInDateRangeRequest() # UserProfilesInDateRangeRequest | The date range of work day.

try:
    # Query performance profiles in date range for a user
    api_response = api_instance.post_gamification_profiles_user_query(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profiles_user_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. |  |
| **body** | [**UserProfilesInDateRangeRequest**](UserProfilesInDateRangeRequest.html)| The date range of work day. |  |
{: class="table table-striped"}

### Return type

[**UserProfilesInDateRange**](UserProfilesInDateRange.html)

<a name="post_gamification_profiles_users_me_query"></a>

## [**UserProfilesInDateRange**](UserProfilesInDateRange.html) post_gamification_profiles_users_me_query(body)



Query performance profiles in date range for the current user

Wraps POST /api/v2/gamification/profiles/users/me/query 

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
api_instance = PureCloudPlatformClientV2.GamificationApi()
body = PureCloudPlatformClientV2.UserProfilesInDateRangeRequest() # UserProfilesInDateRangeRequest | The date range of work day.

try:
    # Query performance profiles in date range for the current user
    api_response = api_instance.post_gamification_profiles_users_me_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_profiles_users_me_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserProfilesInDateRangeRequest**](UserProfilesInDateRangeRequest.html)| The date range of work day. |  |
{: class="table table-striped"}

### Return type

[**UserProfilesInDateRange**](UserProfilesInDateRange.html)

<a name="put_gamification_profile"></a>

## [**PerformanceProfile**](PerformanceProfile.html) put_gamification_profile(profile_id, body=body)



Updates a performance profile

Wraps PUT /api/v2/gamification/profiles/{profileId} 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | performanceProfileId
body = PureCloudPlatformClientV2.PerformanceProfile() # PerformanceProfile | performanceProfile (optional)

try:
    # Updates a performance profile
    api_response = api_instance.put_gamification_profile(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->put_gamification_profile: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| performanceProfileId |  |
| **body** | [**PerformanceProfile**](PerformanceProfile.html)| performanceProfile | [optional]  |
{: class="table table-striped"}

### Return type

[**PerformanceProfile**](PerformanceProfile.html)

<a name="put_gamification_profile_metric"></a>

## [**Metric**](Metric.html) put_gamification_profile_metric(profile_id, metric_id, body)



Updates a metric in performance profile

Wraps PUT /api/v2/gamification/profiles/{profileId}/metrics/{metricId} 

Requires ALL permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
profile_id = 'profile_id_example' # str | Performance Profile Id
metric_id = 'metric_id_example' # str | Metric Id
body = PureCloudPlatformClientV2.CreateMetric() # CreateMetric | Metric

try:
    # Updates a metric in performance profile
    api_response = api_instance.put_gamification_profile_metric(profile_id, metric_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->put_gamification_profile_metric: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str**| Performance Profile Id |  |
| **metric_id** | **str**| Metric Id |  |
| **body** | [**CreateMetric**](CreateMetric.html)| Metric |  |
{: class="table table-striped"}

### Return type

[**Metric**](Metric.html)

<a name="put_gamification_status"></a>

## [**GamificationStatus**](GamificationStatus.html) put_gamification_status(status)



Update gamification activation status

Wraps PUT /api/v2/gamification/status 

Requires ANY permissions: 

* gamification:profile:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GamificationApi()
status = PureCloudPlatformClientV2.GamificationStatus() # GamificationStatus | Gamification status

try:
    # Update gamification activation status
    api_response = api_instance.put_gamification_status(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->put_gamification_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **status** | [**GamificationStatus**](GamificationStatus.html)| Gamification status |  |
{: class="table table-striped"}

### Return type

[**GamificationStatus**](GamificationStatus.html)

