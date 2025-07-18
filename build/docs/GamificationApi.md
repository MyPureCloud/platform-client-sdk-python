# GamificationApi

## PureCloudPlatformClientV2.GamificationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_employeeperformance_externalmetrics_definition**](#delete_employeeperformance_externalmetrics_definition) | Delete an External Metric Definition|
|[**delete_gamification_contest**](#delete_gamification_contest) | Delete a Contest by Id|
|[**get_employeeperformance_externalmetrics_definition**](#get_employeeperformance_externalmetrics_definition) | Get an External Metric Definition|
|[**get_employeeperformance_externalmetrics_definitions**](#get_employeeperformance_externalmetrics_definitions) | Get a list of External Metric Definitions of an organization, sorted by name in ascending order|
|[**get_gamification_contest**](#get_gamification_contest) | Get a Contest by Id|
|[**get_gamification_contest_agents_scores**](#get_gamification_contest_agents_scores) | Get Contest Scores (Admin)|
|[**get_gamification_contest_agents_scores_me**](#get_gamification_contest_agents_scores_me) | Get Contest Scores for the requesting Agent/Supervisor|
|[**get_gamification_contest_agents_scores_trends**](#get_gamification_contest_agents_scores_trends) | Get a Contest Score Trend (Average Trend)|
|[**get_gamification_contest_agents_scores_trends_me**](#get_gamification_contest_agents_scores_trends_me) | Get a Contest Score Trend for the requesting Agent|
|[**get_gamification_contest_prizeimage**](#get_gamification_contest_prizeimage) | Get a Contest Prize Image by Id|
|[**get_gamification_contests**](#get_gamification_contests) | Get a List of Contests (Admin)|
|[**get_gamification_contests_me**](#get_gamification_contests_me) | Get a List of Contests (Agent/Supervisor)|
|[**get_gamification_insights**](#get_gamification_insights) | Get insights summary|
|[**get_gamification_insights_details**](#get_gamification_insights_details) | Get insights details for the current user|
|[**get_gamification_insights_groups_trends**](#get_gamification_insights_groups_trends) | Get insights overall trend for the current user|
|[**get_gamification_insights_groups_trends_all**](#get_gamification_insights_groups_trends_all) | Get insights overall trend|
|[**get_gamification_insights_members**](#get_gamification_insights_members) | Query users in a profile during a period of time|
|[**get_gamification_insights_rankings**](#get_gamification_insights_rankings) | Get insights rankings|
|[**get_gamification_insights_trends**](#get_gamification_insights_trends) | Get insights user trend for the current user|
|[**get_gamification_insights_user_details**](#get_gamification_insights_user_details) | Get insights details for the user|
|[**get_gamification_insights_user_trends**](#get_gamification_insights_user_trends) | Get insights user trend for the user|
|[**get_gamification_leaderboard**](#get_gamification_leaderboard) | Leaderboard of the requesting user&#39;s division or performance profile|
|[**get_gamification_leaderboard_all**](#get_gamification_leaderboard_all) | Leaderboard by filter type|
|[**get_gamification_leaderboard_all_bestpoints**](#get_gamification_leaderboard_all_bestpoints) | Best Points by division or performance profile|
|[**get_gamification_leaderboard_bestpoints**](#get_gamification_leaderboard_bestpoints) | Best Points of the requesting user&#39;s current performance profile or division|
|[**get_gamification_metricdefinition**](#get_gamification_metricdefinition) | Metric definition by id|
|[**get_gamification_metricdefinitions**](#get_gamification_metricdefinitions) | All metric definitions|
|[**get_gamification_profile**](#get_gamification_profile) | Performance profile by id|
|[**get_gamification_profile_members**](#get_gamification_profile_members) | Members of a given performance profile|
|[**get_gamification_profile_metric**](#get_gamification_profile_metric) | Performance profile gamified metric by id|
|[**get_gamification_profile_metrics**](#get_gamification_profile_metrics) | All gamified metrics for a given performance profile|
|[**get_gamification_profile_metrics_objectivedetails**](#get_gamification_profile_metrics_objectivedetails) | All metrics for a given performance profile with objective details such as order and maxPoints|
|[**get_gamification_profiles**](#get_gamification_profiles) | All performance profiles|
|[**get_gamification_profiles_user**](#get_gamification_profiles_user) | Performance profile of a user|
|[**get_gamification_profiles_users_me**](#get_gamification_profiles_users_me) | Performance profile of the requesting user|
|[**get_gamification_scorecards**](#get_gamification_scorecards) | Workday performance metrics of the requesting user|
|[**get_gamification_scorecards_attendance**](#get_gamification_scorecards_attendance) | Attendance status metrics of the requesting user|
|[**get_gamification_scorecards_bestpoints**](#get_gamification_scorecards_bestpoints) | Best points of the requesting user|
|[**get_gamification_scorecards_points_alltime**](#get_gamification_scorecards_points_alltime) | All-time points of the requesting user|
|[**get_gamification_scorecards_points_average**](#get_gamification_scorecards_points_average) | Average points of the requesting user&#39;s division or performance profile|
|[**get_gamification_scorecards_points_trends**](#get_gamification_scorecards_points_trends) | Points trends of the requesting user|
|[**get_gamification_scorecards_profile_metric_user_values_trends**](#get_gamification_scorecards_profile_metric_user_values_trends) | Average performance values trends by metric of a user|
|[**get_gamification_scorecards_profile_metric_users_values_trends**](#get_gamification_scorecards_profile_metric_users_values_trends) | Average performance values trends by metric of a division or a performance profile|
|[**get_gamification_scorecards_profile_metric_values_trends**](#get_gamification_scorecards_profile_metric_values_trends) | Average performance values trends by metric of the requesting user|
|[**get_gamification_scorecards_user**](#get_gamification_scorecards_user) | Workday performance metrics for a user|
|[**get_gamification_scorecards_user_attendance**](#get_gamification_scorecards_user_attendance) | Attendance status metrics for a user|
|[**get_gamification_scorecards_user_bestpoints**](#get_gamification_scorecards_user_bestpoints) | Best points of a user|
|[**get_gamification_scorecards_user_points_alltime**](#get_gamification_scorecards_user_points_alltime) | All-time points for a user|
|[**get_gamification_scorecards_user_points_trends**](#get_gamification_scorecards_user_points_trends) | Points trend for a user|
|[**get_gamification_scorecards_user_values_trends**](#get_gamification_scorecards_user_values_trends) | Values trends of a user|
|[**get_gamification_scorecards_users_points_average**](#get_gamification_scorecards_users_points_average) | Workday average points by target group|
|[**get_gamification_scorecards_users_values_average**](#get_gamification_scorecards_users_values_average) | Workday average values by target group|
|[**get_gamification_scorecards_users_values_trends**](#get_gamification_scorecards_users_values_trends) | Values trend by target group|
|[**get_gamification_scorecards_values_average**](#get_gamification_scorecards_values_average) | Average values of the requesting user&#39;s division or performance profile|
|[**get_gamification_scorecards_values_trends**](#get_gamification_scorecards_values_trends) | Values trends of the requesting user or group|
|[**get_gamification_status**](#get_gamification_status) | Gamification activation status|
|[**get_gamification_template**](#get_gamification_template) | Objective template by id|
|[**get_gamification_templates**](#get_gamification_templates) | All objective templates|
|[**patch_employeeperformance_externalmetrics_definition**](#patch_employeeperformance_externalmetrics_definition) | Update External Metric Definition|
|[**patch_gamification_contest**](#patch_gamification_contest) | Finalize a Contest by Id|
|[**post_employeeperformance_externalmetrics_data**](#post_employeeperformance_externalmetrics_data) | Write External Metric Data|
|[**post_employeeperformance_externalmetrics_definitions**](#post_employeeperformance_externalmetrics_definitions) | Create External Metric Definition|
|[**post_gamification_contests**](#post_gamification_contests) | Creates a Contest|
|[**post_gamification_contests_uploads_prizeimages**](#post_gamification_contests_uploads_prizeimages) | Generates pre-signed URL to upload a prize image for gamification contests|
|[**post_gamification_profile_activate**](#post_gamification_profile_activate) | Activate a performance profile|
|[**post_gamification_profile_deactivate**](#post_gamification_profile_deactivate) | Deactivate a performance profile|
|[**post_gamification_profile_members**](#post_gamification_profile_members) | Assign members to a given performance profile|
|[**post_gamification_profile_members_validate**](#post_gamification_profile_members_validate) | Validate member assignment|
|[**post_gamification_profile_metric_link**](#post_gamification_profile_metric_link) | Creates a linked metric|
|[**post_gamification_profile_metrics**](#post_gamification_profile_metrics) | Creates a gamified metric with a given metric definition and metric objective under in a performance profile|
|[**post_gamification_profiles**](#post_gamification_profiles) | Create a new custom performance profile|
|[**post_gamification_profiles_user_query**](#post_gamification_profiles_user_query) | Query performance profiles in date range for a user|
|[**post_gamification_profiles_users_me_query**](#post_gamification_profiles_users_me_query) | Query performance profiles in date range for the current user|
|[**put_gamification_contest**](#put_gamification_contest) | Update a Contest by Id|
|[**put_gamification_profile**](#put_gamification_profile) | Updates a performance profile|
|[**put_gamification_profile_metric**](#put_gamification_profile_metric) | Updates a metric in performance profile|
|[**put_gamification_status**](#put_gamification_status) | Update gamification activation status|



## delete_employeeperformance_externalmetrics_definition

>  delete_employeeperformance_externalmetrics_definition(metric_id)


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

### Return type

void (empty response body)


## delete_gamification_contest

>  delete_gamification_contest(contest_id)


Delete a Contest by Id

Wraps DELETE /api/v2/gamification/contests/{contestId} 

Requires ANY permissions: 

* gamification:contest:delete
* gamification:contest:deleteAll

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
contest_id = 'contest_id_example' # str | The ID of the contest

try:
    # Delete a Contest by Id
    api_instance.delete_gamification_contest(contest_id)
except ApiException as e:
    print("Exception when calling GamificationApi->delete_gamification_contest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |

### Return type

void (empty response body)


## get_employeeperformance_externalmetrics_definition

> [**ExternalMetricDefinition**](ExternalMetricDefinition) get_employeeperformance_externalmetrics_definition(metric_id)


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

### Return type

[**ExternalMetricDefinition**](ExternalMetricDefinition)


## get_employeeperformance_externalmetrics_definitions

> [**ExternalMetricDefinitionListing**](ExternalMetricDefinitionListing) get_employeeperformance_externalmetrics_definitions(page_size=page_size, page_number=page_number)


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

### Return type

[**ExternalMetricDefinitionListing**](ExternalMetricDefinitionListing)


## get_gamification_contest

> [**ContestsResponse**](ContestsResponse) get_gamification_contest(contest_id)


Get a Contest by Id

Wraps GET /api/v2/gamification/contests/{contestId} 

Requires ANY permissions: 

* gamification:contest:view

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
contest_id = 'contest_id_example' # str | The ID of the contest

try:
    # Get a Contest by Id
    api_response = api_instance.get_gamification_contest(contest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |

### Return type

[**ContestsResponse**](ContestsResponse)


## get_gamification_contest_agents_scores

> [**ContestScoresAgentsPagedList**](ContestScoresAgentsPagedList) get_gamification_contest_agents_scores(contest_id, page_number=page_number, page_size=page_size, workday=workday, returns_view=returns_view)


Get Contest Scores (Admin)

Wraps GET /api/v2/gamification/contests/{contestId}/agents/scores 

Requires ANY permissions: 

* gamification:contest:viewAll

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
contest_id = 'contest_id_example' # str | The ID of the contest
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)
workday = '2013-10-20' # date | Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
returns_view = ''All'' # str | Desired response results (optional) (default to 'All')

try:
    # Get Contest Scores (Admin)
    api_response = api_instance.get_gamification_contest_agents_scores(contest_id, page_number=page_number, page_size=page_size, workday=workday, returns_view=returns_view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contest_agents_scores: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
| **workday** | **date**| Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **returns_view** | **str**| Desired response results | [optional] [default to &#39;All&#39;]<br />**Values**: All, TopAndBottom |

### Return type

[**ContestScoresAgentsPagedList**](ContestScoresAgentsPagedList)


## get_gamification_contest_agents_scores_me

> [**ContestScoresAgentsPagedList**](ContestScoresAgentsPagedList) get_gamification_contest_agents_scores_me(contest_id, page_number=page_number, page_size=page_size, workday=workday, returns_view=returns_view)


Get Contest Scores for the requesting Agent/Supervisor

Wraps GET /api/v2/gamification/contests/{contestId}/agents/scores/me 

Requires ALL permissions: 

* gamification:contest:view

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
contest_id = 'contest_id_example' # str | The ID of the contest
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)
workday = '2013-10-20' # date | Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
returns_view = ''All'' # str | Desired response results (Supervisor Only) (optional) (default to 'All')

try:
    # Get Contest Scores for the requesting Agent/Supervisor
    api_response = api_instance.get_gamification_contest_agents_scores_me(contest_id, page_number=page_number, page_size=page_size, workday=workday, returns_view=returns_view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contest_agents_scores_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
| **workday** | **date**| Target querying workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **returns_view** | **str**| Desired response results (Supervisor Only) | [optional] [default to &#39;All&#39;]<br />**Values**: All, TopAndBottom |

### Return type

[**ContestScoresAgentsPagedList**](ContestScoresAgentsPagedList)


## get_gamification_contest_agents_scores_trends

> [**ContestScoresGroupTrendList**](ContestScoresGroupTrendList) get_gamification_contest_agents_scores_trends(contest_id)


Get a Contest Score Trend (Average Trend)

Wraps GET /api/v2/gamification/contests/{contestId}/agents/scores/trends 

Requires ANY permissions: 

* gamification:contest:view

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
contest_id = 'contest_id_example' # str | The ID of the contest

try:
    # Get a Contest Score Trend (Average Trend)
    api_response = api_instance.get_gamification_contest_agents_scores_trends(contest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contest_agents_scores_trends: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |

### Return type

[**ContestScoresGroupTrendList**](ContestScoresGroupTrendList)


## get_gamification_contest_agents_scores_trends_me

> [**ContestScoresAgentTrendList**](ContestScoresAgentTrendList) get_gamification_contest_agents_scores_trends_me(contest_id)


Get a Contest Score Trend for the requesting Agent

Wraps GET /api/v2/gamification/contests/{contestId}/agents/scores/trends/me 

Requires ANY permissions: 

* gamification:contest:view

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
contest_id = 'contest_id_example' # str | The ID of the contest

try:
    # Get a Contest Score Trend for the requesting Agent
    api_response = api_instance.get_gamification_contest_agents_scores_trends_me(contest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contest_agents_scores_trends_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |

### Return type

[**ContestScoresAgentTrendList**](ContestScoresAgentTrendList)


## get_gamification_contest_prizeimage

> [**PrizeImages**](PrizeImages) get_gamification_contest_prizeimage(contest_id, prize_image_id)


Get a Contest Prize Image by Id

Wraps GET /api/v2/gamification/contests/{contestId}/prizeimages/{prizeImageId} 

Requires ANY permissions: 

* gamification:contest:view
* gamification:contest:viewAll

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
contest_id = 'contest_id_example' # str | The ID of the contest
prize_image_id = 'prize_image_id_example' # str | The ID of the prize image

try:
    # Get a Contest Prize Image by Id
    api_response = api_instance.get_gamification_contest_prizeimage(contest_id, prize_image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contest_prizeimage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |
| **prize_image_id** | **str**| The ID of the prize image |  |

### Return type

[**PrizeImages**](PrizeImages)


## get_gamification_contests

> [**GetContestsEssentialsListing**](GetContestsEssentialsListing) get_gamification_contests(page_number=page_number, page_size=page_size, date_start=date_start, date_end=date_end, status=status, sort_by=sort_by, sort_order=sort_order)


Get a List of Contests (Admin)

Wraps GET /api/v2/gamification/contests 

Requires ANY permissions: 

* gamification:contest:viewAll

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
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)
date_start = '2013-10-20' # date | Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
status = ['status_example'] # list[str] |  (optional)
sort_by = ''dateStart'' # str |  (optional) (default to 'dateStart')
sort_order = ''desc'' # str |  (optional) (default to 'desc')

try:
    # Get a List of Contests (Admin)
    api_response = api_instance.get_gamification_contests(page_number=page_number, page_size=page_size, date_start=date_start, date_end=date_end, status=status, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
| **date_start** | **date**| Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **status** | [**list[str]**](str)|  | [optional] <br />**Values**: Upcoming, Ongoing, Pending, RecentlyCompleted, Completed, Cancelled |
| **sort_by** | **str**|  | [optional] [default to &#39;dateStart&#39;]<br />**Values**: title, dateStart, dateEnd, dateFinalized, status, profile, participantCount |
| **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]<br />**Values**: asc, desc |

### Return type

[**GetContestsEssentialsListing**](GetContestsEssentialsListing)


## get_gamification_contests_me

> [**GetContestsEssentialsListing**](GetContestsEssentialsListing) get_gamification_contests_me(page_number=page_number, page_size=page_size, date_start=date_start, date_end=date_end, status=status, sort_by=sort_by, sort_order=sort_order, view=view)


Get a List of Contests (Agent/Supervisor)

Wraps GET /api/v2/gamification/contests/me 

Requires ALL permissions: 

* gamification:contest:view

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
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)
date_start = '2013-10-20' # date | Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
status = ['status_example'] # list[str] |  (optional)
sort_by = ''dateStart'' # str |  (optional) (default to 'dateStart')
sort_order = ''desc'' # str |  (optional) (default to 'desc')
view = ''participant'' # str |  (optional) (default to 'participant')

try:
    # Get a List of Contests (Agent/Supervisor)
    api_response = api_instance.get_gamification_contests_me(page_number=page_number, page_size=page_size, date_start=date_start, date_end=date_end, status=status, sort_by=sort_by, sort_order=sort_order, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_contests_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
| **date_start** | **date**| Start date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| End date for the query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **status** | [**list[str]**](str)|  | [optional] <br />**Values**: Upcoming, Ongoing, Pending, RecentlyCompleted, Completed, Cancelled |
| **sort_by** | **str**|  | [optional] [default to &#39;dateStart&#39;]<br />**Values**: title, dateStart, dateEnd, dateFinalized, status, profile, participantCount |
| **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]<br />**Values**: asc, desc |
| **view** | **str**|  | [optional] [default to &#39;participant&#39;]<br />**Values**: participant, creator |

### Return type

[**GetContestsEssentialsListing**](GetContestsEssentialsListing)


## get_gamification_insights

> [**InsightsSummary**](InsightsSummary) get_gamification_insights(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday, page_size=page_size, page_number=page_number, sort_key=sort_key, sort_metric_id=sort_metric_id, sort_order=sort_order, user_ids=user_ids)


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

### Return type

[**InsightsSummary**](InsightsSummary)


## get_gamification_insights_details

> [**InsightsDetails**](InsightsDetails) get_gamification_insights_details(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday)


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

### Return type

[**InsightsDetails**](InsightsDetails)


## get_gamification_insights_groups_trends

> [**InsightsTrend**](InsightsTrend) get_gamification_insights_groups_trends(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)


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

### Return type

[**InsightsTrend**](InsightsTrend)


## get_gamification_insights_groups_trends_all

> [**InsightsTrend**](InsightsTrend) get_gamification_insights_groups_trends_all(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)


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

### Return type

[**InsightsTrend**](InsightsTrend)


## get_gamification_insights_members

> [**InsightsAgents**](InsightsAgents) get_gamification_insights_members(filter_type, filter_id, granularity, start_workday)


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

### Return type

[**InsightsAgents**](InsightsAgents)


## get_gamification_insights_rankings

> [**InsightsRankings**](InsightsRankings) get_gamification_insights_rankings(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday, sort_key, sort_metric_id=sort_metric_id, section_size=section_size, user_ids=user_ids)


Get insights rankings

Wraps GET /api/v2/gamification/insights/rankings 

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
sort_key = 'sort_key_example' # str | Sort key
sort_metric_id = 'sort_metric_id_example' # str | Sort Metric Id (optional)
section_size = 56 # int | The number of top and bottom users to return before ties (optional)
user_ids = 'user_ids_example' # str | A list of up to 100 comma-separated user Ids (optional)

try:
    # Get insights rankings
    api_response = api_instance.get_gamification_insights_rankings(filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday, sort_key, sort_metric_id=sort_metric_id, section_size=section_size, user_ids=user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->get_gamification_insights_rankings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter_type** | **str**| Filter type for the query request. | <br />**Values**: PerformanceProfile, Division |
| **filter_id** | **str**| ID for the filter type. |  |
| **granularity** | **str**| Granularity | <br />**Values**: Weekly, Monthly |
| **comparative_period_start_workday** | **date**| The start work day of comparative period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **primary_period_start_workday** | **date**| The start work day of primary period. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **sort_key** | **str**| Sort key | <br />**Values**: percentOfGoal, percentOfGoalChange, overallPercentOfGoal, overallPercentOfGoalChange, value, valueChange |
| **sort_metric_id** | **str**| Sort Metric Id | [optional]  |
| **section_size** | **int**| The number of top and bottom users to return before ties | [optional]  |
| **user_ids** | **str**| A list of up to 100 comma-separated user Ids | [optional]  |

### Return type

[**InsightsRankings**](InsightsRankings)


## get_gamification_insights_trends

> [**UserInsightsTrend**](UserInsightsTrend) get_gamification_insights_trends(filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)


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

### Return type

[**UserInsightsTrend**](UserInsightsTrend)


## get_gamification_insights_user_details

> [**InsightsDetails**](InsightsDetails) get_gamification_insights_user_details(user_id, filter_type, filter_id, granularity, comparative_period_start_workday, primary_period_start_workday)


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

### Return type

[**InsightsDetails**](InsightsDetails)


## get_gamification_insights_user_trends

> [**UserInsightsTrend**](UserInsightsTrend) get_gamification_insights_user_trends(user_id, filter_type, filter_id, granularity, comparative_period_start_workday, comparative_period_end_workday, primary_period_start_workday, primary_period_end_workday)


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

### Return type

[**UserInsightsTrend**](UserInsightsTrend)


## get_gamification_leaderboard

> [**Leaderboard**](Leaderboard) get_gamification_leaderboard(start_workday, end_workday, metric_id=metric_id)


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

### Return type

[**Leaderboard**](Leaderboard)


## get_gamification_leaderboard_all

> [**Leaderboard**](Leaderboard) get_gamification_leaderboard_all(filter_type, filter_id, start_workday, end_workday, metric_id=metric_id)


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

### Return type

[**Leaderboard**](Leaderboard)


## get_gamification_leaderboard_all_bestpoints

> [**OverallBestPoints**](OverallBestPoints) get_gamification_leaderboard_all_bestpoints(filter_type, filter_id)


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

### Return type

[**OverallBestPoints**](OverallBestPoints)


## get_gamification_leaderboard_bestpoints

> [**OverallBestPoints**](OverallBestPoints) get_gamification_leaderboard_bestpoints()


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

[**OverallBestPoints**](OverallBestPoints)


## get_gamification_metricdefinition

> [**MetricDefinition**](MetricDefinition) get_gamification_metricdefinition(metric_definition_id)


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

### Return type

[**MetricDefinition**](MetricDefinition)


## get_gamification_metricdefinitions

> [**GetMetricDefinitionsResponse**](GetMetricDefinitionsResponse) get_gamification_metricdefinitions()


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

[**GetMetricDefinitionsResponse**](GetMetricDefinitionsResponse)


## get_gamification_profile

> [**PerformanceProfile**](PerformanceProfile) get_gamification_profile(profile_id)


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

### Return type

[**PerformanceProfile**](PerformanceProfile)


## get_gamification_profile_members

> [**MemberListing**](MemberListing) get_gamification_profile_members(profile_id)


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

### Return type

[**MemberListing**](MemberListing)


## get_gamification_profile_metric

> [**Metric**](Metric) get_gamification_profile_metric(profile_id, metric_id, workday=workday)


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

### Return type

[**Metric**](Metric)


## get_gamification_profile_metrics

> [**GetMetricResponse**](GetMetricResponse) get_gamification_profile_metrics(profile_id, expand=expand, workday=workday, metric_ids=metric_ids)


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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: objective |
| **workday** | **date**| The objective query workday. If not specified, then it retrieves the current objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **metric_ids** | **str**| List of metric ids to filter the response (Optional, comma-separated). | [optional]  |

### Return type

[**GetMetricResponse**](GetMetricResponse)


## get_gamification_profile_metrics_objectivedetails

> [**GetMetricsResponse**](GetMetricsResponse) get_gamification_profile_metrics_objectivedetails(profile_id, workday=workday)


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

### Return type

[**GetMetricsResponse**](GetMetricsResponse)


## get_gamification_profiles

> [**GetProfilesResponse**](GetProfilesResponse) get_gamification_profiles()


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

[**GetProfilesResponse**](GetProfilesResponse)


## get_gamification_profiles_user

> [**PerformanceProfile**](PerformanceProfile) get_gamification_profiles_user(user_id, workday=workday)


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

### Return type

[**PerformanceProfile**](PerformanceProfile)


## get_gamification_profiles_users_me

> [**PerformanceProfile**](PerformanceProfile) get_gamification_profiles_users_me(workday=workday)


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

### Return type

[**PerformanceProfile**](PerformanceProfile)


## get_gamification_scorecards

> [**WorkdayMetricListing**](WorkdayMetricListing) get_gamification_scorecards(workday, expand=expand)


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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: objective |

### Return type

[**WorkdayMetricListing**](WorkdayMetricListing)


## get_gamification_scorecards_attendance

> [**AttendanceStatusListing**](AttendanceStatusListing) get_gamification_scorecards_attendance(start_workday, end_workday)


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

### Return type

[**AttendanceStatusListing**](AttendanceStatusListing)


## get_gamification_scorecards_bestpoints

> [**UserBestPoints**](UserBestPoints) get_gamification_scorecards_bestpoints()


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

[**UserBestPoints**](UserBestPoints)


## get_gamification_scorecards_points_alltime

> [**AllTimePoints**](AllTimePoints) get_gamification_scorecards_points_alltime(end_workday)


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

### Return type

[**AllTimePoints**](AllTimePoints)


## get_gamification_scorecards_points_average

> [**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints) get_gamification_scorecards_points_average(workday)


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

### Return type

[**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints)


## get_gamification_scorecards_points_trends

> [**WorkdayPointsTrend**](WorkdayPointsTrend) get_gamification_scorecards_points_trends(start_workday, end_workday, day_of_week=day_of_week)


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

### Return type

[**WorkdayPointsTrend**](WorkdayPointsTrend)


## get_gamification_scorecards_profile_metric_user_values_trends

> [**MetricValueTrendAverage**](MetricValueTrendAverage) get_gamification_scorecards_profile_metric_user_values_trends(profile_id, metric_id, user_id, start_workday, end_workday, reference_workday=reference_workday, time_zone=time_zone)


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

### Return type

[**MetricValueTrendAverage**](MetricValueTrendAverage)


## get_gamification_scorecards_profile_metric_users_values_trends

> [**MetricValueTrendAverage**](MetricValueTrendAverage) get_gamification_scorecards_profile_metric_users_values_trends(profile_id, metric_id, filter_type, start_workday, end_workday, filter_id=filter_id, reference_workday=reference_workday, time_zone=time_zone)


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

### Return type

[**MetricValueTrendAverage**](MetricValueTrendAverage)


## get_gamification_scorecards_profile_metric_values_trends

> [**MetricValueTrendAverage**](MetricValueTrendAverage) get_gamification_scorecards_profile_metric_values_trends(profile_id, metric_id, start_workday, end_workday, filter_type=filter_type, reference_workday=reference_workday, time_zone=time_zone)


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

### Return type

[**MetricValueTrendAverage**](MetricValueTrendAverage)


## get_gamification_scorecards_user

> [**WorkdayMetricListing**](WorkdayMetricListing) get_gamification_scorecards_user(user_id, workday, expand=expand)


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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: objective |

### Return type

[**WorkdayMetricListing**](WorkdayMetricListing)


## get_gamification_scorecards_user_attendance

> [**AttendanceStatusListing**](AttendanceStatusListing) get_gamification_scorecards_user_attendance(user_id, start_workday, end_workday)


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

### Return type

[**AttendanceStatusListing**](AttendanceStatusListing)


## get_gamification_scorecards_user_bestpoints

> [**UserBestPoints**](UserBestPoints) get_gamification_scorecards_user_bestpoints(user_id)


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

### Return type

[**UserBestPoints**](UserBestPoints)


## get_gamification_scorecards_user_points_alltime

> [**AllTimePoints**](AllTimePoints) get_gamification_scorecards_user_points_alltime(user_id, end_workday)


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

### Return type

[**AllTimePoints**](AllTimePoints)


## get_gamification_scorecards_user_points_trends

> [**WorkdayPointsTrend**](WorkdayPointsTrend) get_gamification_scorecards_user_points_trends(user_id, start_workday, end_workday, day_of_week=day_of_week)


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

### Return type

[**WorkdayPointsTrend**](WorkdayPointsTrend)


## get_gamification_scorecards_user_values_trends

> [**WorkdayValuesTrend**](WorkdayValuesTrend) get_gamification_scorecards_user_values_trends(user_id, start_workday, end_workday, time_zone=time_zone)


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

### Return type

[**WorkdayValuesTrend**](WorkdayValuesTrend)


## get_gamification_scorecards_users_points_average

> [**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints) get_gamification_scorecards_users_points_average(filter_type, filter_id, workday)


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

### Return type

[**SingleWorkdayAveragePoints**](SingleWorkdayAveragePoints)


## get_gamification_scorecards_users_values_average

> [**SingleWorkdayAverageValues**](SingleWorkdayAverageValues) get_gamification_scorecards_users_values_average(filter_type, filter_id, workday, time_zone=time_zone)


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

### Return type

[**SingleWorkdayAverageValues**](SingleWorkdayAverageValues)


## get_gamification_scorecards_users_values_trends

> [**WorkdayValuesTrend**](WorkdayValuesTrend) get_gamification_scorecards_users_values_trends(filter_type, filter_id, start_workday, end_workday, time_zone=time_zone)


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

### Return type

[**WorkdayValuesTrend**](WorkdayValuesTrend)


## get_gamification_scorecards_values_average

> [**SingleWorkdayAverageValues**](SingleWorkdayAverageValues) get_gamification_scorecards_values_average(workday, time_zone=time_zone)


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

### Return type

[**SingleWorkdayAverageValues**](SingleWorkdayAverageValues)


## get_gamification_scorecards_values_trends

> [**WorkdayValuesTrend**](WorkdayValuesTrend) get_gamification_scorecards_values_trends(start_workday, end_workday, filter_type=filter_type, reference_workday=reference_workday, time_zone=time_zone)


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

### Return type

[**WorkdayValuesTrend**](WorkdayValuesTrend)


## get_gamification_status

> [**GamificationStatus**](GamificationStatus) get_gamification_status()


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

[**GamificationStatus**](GamificationStatus)


## get_gamification_template

> [**ObjectiveTemplate**](ObjectiveTemplate) get_gamification_template(template_id)


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

### Return type

[**ObjectiveTemplate**](ObjectiveTemplate)


## get_gamification_templates

> [**GetTemplatesResponse**](GetTemplatesResponse) get_gamification_templates()


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

[**GetTemplatesResponse**](GetTemplatesResponse)


## patch_employeeperformance_externalmetrics_definition

> [**ExternalMetricDefinition**](ExternalMetricDefinition) patch_employeeperformance_externalmetrics_definition(metric_id, body)


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
| **body** | [**ExternalMetricDefinitionUpdateRequest**](ExternalMetricDefinitionUpdateRequest)| The External Metric Definition parameters to be updated |  |

### Return type

[**ExternalMetricDefinition**](ExternalMetricDefinition)


## patch_gamification_contest

> [**ContestsResponse**](ContestsResponse) patch_gamification_contest(contest_id, body)


Finalize a Contest by Id

Wraps PATCH /api/v2/gamification/contests/{contestId} 

Requires ANY permissions: 

* gamification:contestStatus:edit
* gamification:contestStatus:editAll

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
contest_id = 'contest_id_example' # str | The ID of the contest
body = PureCloudPlatformClientV2.ContestsFinalizeRequest() # ContestsFinalizeRequest | Finalize Contest

try:
    # Finalize a Contest by Id
    api_response = api_instance.patch_gamification_contest(contest_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->patch_gamification_contest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |
| **body** | [**ContestsFinalizeRequest**](ContestsFinalizeRequest)| Finalize Contest |  |

### Return type

[**ContestsResponse**](ContestsResponse)


## post_employeeperformance_externalmetrics_data

> [**ExternalMetricDataWriteResponse**](ExternalMetricDataWriteResponse) post_employeeperformance_externalmetrics_data(body=body)


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
| **body** | [**ExternalMetricDataWriteRequest**](ExternalMetricDataWriteRequest)| The External Metric Data to be added | [optional]  |

### Return type

[**ExternalMetricDataWriteResponse**](ExternalMetricDataWriteResponse)


## post_employeeperformance_externalmetrics_definitions

> [**ExternalMetricDefinition**](ExternalMetricDefinition) post_employeeperformance_externalmetrics_definitions(body=body)


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
| **body** | [**ExternalMetricDefinitionCreateRequest**](ExternalMetricDefinitionCreateRequest)| The External Metric Definition to be created | [optional]  |

### Return type

[**ExternalMetricDefinition**](ExternalMetricDefinition)


## post_gamification_contests

> [**ContestsResponse**](ContestsResponse) post_gamification_contests(body)


Creates a Contest

Wraps POST /api/v2/gamification/contests 

Requires ANY permissions: 

* gamification:contest:add

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
body = PureCloudPlatformClientV2.ContestsCreateRequest() # ContestsCreateRequest | Create Contest

try:
    # Creates a Contest
    api_response = api_instance.post_gamification_contests(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_contests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContestsCreateRequest**](ContestsCreateRequest)| Create Contest |  |

### Return type

[**ContestsResponse**](ContestsResponse)


## post_gamification_contests_uploads_prizeimages

> [**UploadUrlResponse**](UploadUrlResponse) post_gamification_contests_uploads_prizeimages(body)


Generates pre-signed URL to upload a prize image for gamification contests

Wraps POST /api/v2/gamification/contests/uploads/prizeimages 

Requires ALL permissions: 

* gamification:contestPrizeImage:upload

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
body = PureCloudPlatformClientV2.GamificationContestPrizeImageUploadUrlRequest() # GamificationContestPrizeImageUploadUrlRequest | query

try:
    # Generates pre-signed URL to upload a prize image for gamification contests
    api_response = api_instance.post_gamification_contests_uploads_prizeimages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->post_gamification_contests_uploads_prizeimages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GamificationContestPrizeImageUploadUrlRequest**](GamificationContestPrizeImageUploadUrlRequest)| query |  |

### Return type

[**UploadUrlResponse**](UploadUrlResponse)


## post_gamification_profile_activate

> [**PerformanceProfile**](PerformanceProfile) post_gamification_profile_activate(profile_id)


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

### Return type

[**PerformanceProfile**](PerformanceProfile)


## post_gamification_profile_deactivate

> [**PerformanceProfile**](PerformanceProfile) post_gamification_profile_deactivate(profile_id)


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

### Return type

[**PerformanceProfile**](PerformanceProfile)


## post_gamification_profile_members

> [**Assignment**](Assignment) post_gamification_profile_members(profile_id, body)


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
| **body** | [**AssignUsers**](AssignUsers)| assignUsers |  |

### Return type

[**Assignment**](Assignment)


## post_gamification_profile_members_validate

> [**AssignmentValidation**](AssignmentValidation) post_gamification_profile_members_validate(profile_id, body)


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
| **body** | [**ValidateAssignUsers**](ValidateAssignUsers)| memberAssignments |  |

### Return type

[**AssignmentValidation**](AssignmentValidation)


## post_gamification_profile_metric_link

> [**Metric**](Metric) post_gamification_profile_metric_link(source_profile_id, source_metric_id, body)


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
| **body** | [**TargetPerformanceProfile**](TargetPerformanceProfile)| linkedMetric |  |

### Return type

[**Metric**](Metric)


## post_gamification_profile_metrics

> [**Metric**](Metric) post_gamification_profile_metrics(profile_id, body)


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
| **body** | [**CreateMetric**](CreateMetric)| Metric |  |

### Return type

[**Metric**](Metric)


## post_gamification_profiles

> [**PerformanceProfile**](PerformanceProfile) post_gamification_profiles(body, copy_metrics=copy_metrics)


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
| **body** | [**CreatePerformanceProfile**](CreatePerformanceProfile)| performanceProfile |  |
| **copy_metrics** | **bool**| Flag to copy metrics. If set to false, there will be no metrics associated with the new profile. If set to true or is absent (the default behavior), all metrics from the default profile will be copied over into the new profile. | [optional] [default to True] |

### Return type

[**PerformanceProfile**](PerformanceProfile)


## post_gamification_profiles_user_query

> [**UserProfilesInDateRange**](UserProfilesInDateRange) post_gamification_profiles_user_query(user_id, body)


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
| **body** | [**UserProfilesInDateRangeRequest**](UserProfilesInDateRangeRequest)| The date range of work day. |  |

### Return type

[**UserProfilesInDateRange**](UserProfilesInDateRange)


## post_gamification_profiles_users_me_query

> [**UserProfilesInDateRange**](UserProfilesInDateRange) post_gamification_profiles_users_me_query(body)


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
| **body** | [**UserProfilesInDateRangeRequest**](UserProfilesInDateRangeRequest)| The date range of work day. |  |

### Return type

[**UserProfilesInDateRange**](UserProfilesInDateRange)


## put_gamification_contest

> [**ContestsResponse**](ContestsResponse) put_gamification_contest(contest_id, body)


Update a Contest by Id

Wraps PUT /api/v2/gamification/contests/{contestId} 

Requires ANY permissions: 

* gamification:contest:edit
* gamification:contest:editAll

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
contest_id = 'contest_id_example' # str | The ID of the contest
body = PureCloudPlatformClientV2.ContestsCreateRequest() # ContestsCreateRequest | Contest

try:
    # Update a Contest by Id
    api_response = api_instance.put_gamification_contest(contest_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationApi->put_gamification_contest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contest_id** | **str**| The ID of the contest |  |
| **body** | [**ContestsCreateRequest**](ContestsCreateRequest)| Contest |  |

### Return type

[**ContestsResponse**](ContestsResponse)


## put_gamification_profile

> [**PerformanceProfile**](PerformanceProfile) put_gamification_profile(profile_id, body=body)


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
| **body** | [**PerformanceProfile**](PerformanceProfile)| performanceProfile | [optional]  |

### Return type

[**PerformanceProfile**](PerformanceProfile)


## put_gamification_profile_metric

> [**Metric**](Metric) put_gamification_profile_metric(profile_id, metric_id, body)


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
| **body** | [**CreateMetric**](CreateMetric)| Metric |  |

### Return type

[**Metric**](Metric)


## put_gamification_status

> [**GamificationStatus**](GamificationStatus) put_gamification_status(status)


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
| **status** | [**GamificationStatus**](GamificationStatus)| Gamification status |  |

### Return type

[**GamificationStatus**](GamificationStatus)


_PureCloudPlatformClientV2 233.0.0_
