---
title: UserDevelopmentApi
---

## PureCloudPlatformClientV2.UserDevelopmentApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_users_development_activities**](UserDevelopmentApi.html#get_users_development_activities) | Get list of Development Activities|
|[**get_users_development_activities_me**](UserDevelopmentApi.html#get_users_development_activities_me) | Get list of Development Activities for current user|
|[**get_users_development_activity**](UserDevelopmentApi.html#get_users_development_activity) | Get a Development Activity|
|[**post_users_development_activities_aggregates_query**](UserDevelopmentApi.html#post_users_development_activities_aggregates_query) | Retrieve aggregated development activity data|
{: class="table table-striped"}

<a name="get_users_development_activities"></a>

## [**DevelopmentActivityListing**](DevelopmentActivityListing.html) get_users_development_activities(user_id=user_id, module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)



Get list of Development Activities

Either moduleId or userId is required. Results are filtered based on the applicable permissions.

Wraps GET /api/v2/users/development/activities 

Requires ANY permissions: 

* learning:assignment:view
* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserDevelopmentApi()
user_id = ['user_id_example'] # list[str] | Specifies the list of user IDs to be queried, up to 100 user IDs. It searches for any relationship for the userId. (optional)
module_id = 'module_id_example' # str | Specifies the ID of the learning module. (optional)
interval = 'interval_example' # str | Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = 'Any' # str | Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned (optional) (default to Any)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'Desc' # str | Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) (optional) (default to Desc)
types = ['types_example'] # list[str] | Specifies the activity types. (optional)
statuses = ['statuses_example'] # list[str] | Specifies the activity statuses to filter by (optional)
relationship = ['relationship_example'] # list[str] | Specifies how the current user relation should be interpreted, and filters the activities returned to only those that have the specified relationship. If not specified, all relationships are returned. (optional)

try:
    # Get list of Development Activities
    api_response = api_instance.get_users_development_activities(user_id=user_id, module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserDevelopmentApi->get_users_development_activities: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | [**list[str]**](str.html)| Specifies the list of user IDs to be queried, up to 100 user IDs. It searches for any relationship for the userId. | [optional]  |
| **module_id** | **str**| Specifies the ID of the learning module. | [optional]  |
| **interval** | **str**| Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned | [optional] [default to Any]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) | [optional] [default to Desc]<br />**Values**: Asc, Desc |
| **types** | [**list[str]**](str.html)| Specifies the activity types. | [optional] <br />**Values**: Informational, Coaching |
| **statuses** | [**list[str]**](str.html)| Specifies the activity statuses to filter by | [optional] <br />**Values**: Planned, InProgress, Completed, InvalidSchedule |
| **relationship** | [**list[str]**](str.html)| Specifies how the current user relation should be interpreted, and filters the activities returned to only those that have the specified relationship. If not specified, all relationships are returned. | [optional] <br />**Values**: Creator, Facilitator, Attendee |
{: class="table table-striped"}

### Return type

[**DevelopmentActivityListing**](DevelopmentActivityListing.html)

<a name="get_users_development_activities_me"></a>

## [**DevelopmentActivityListing**](DevelopmentActivityListing.html) get_users_development_activities_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)



Get list of Development Activities for current user

Results are filtered based on the applicable permissions.

Wraps GET /api/v2/users/development/activities/me 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserDevelopmentApi()
module_id = 'module_id_example' # str | Specifies the ID of the learning module. (optional)
interval = 'interval_example' # str | Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = 'Any' # str | Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned (optional) (default to Any)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'Desc' # str | Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) (optional) (default to Desc)
types = ['types_example'] # list[str] | Specifies the activity types. (optional)
statuses = ['statuses_example'] # list[str] | Specifies the activity statuses to filter by (optional)
relationship = ['relationship_example'] # list[str] | Specifies how the current user relation should be interpreted, and filters the activities returned to only those that have the specified relationship. If not specified, all relationships are returned. (optional)

try:
    # Get list of Development Activities for current user
    api_response = api_instance.get_users_development_activities_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserDevelopmentApi->get_users_development_activities_me: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| Specifies the ID of the learning module. | [optional]  |
| **interval** | **str**| Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned | [optional] [default to Any]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) | [optional] [default to Desc]<br />**Values**: Asc, Desc |
| **types** | [**list[str]**](str.html)| Specifies the activity types. | [optional] <br />**Values**: Informational, Coaching |
| **statuses** | [**list[str]**](str.html)| Specifies the activity statuses to filter by | [optional] <br />**Values**: Planned, InProgress, Completed, InvalidSchedule |
| **relationship** | [**list[str]**](str.html)| Specifies how the current user relation should be interpreted, and filters the activities returned to only those that have the specified relationship. If not specified, all relationships are returned. | [optional] <br />**Values**: Creator, Facilitator, Attendee |
{: class="table table-striped"}

### Return type

[**DevelopmentActivityListing**](DevelopmentActivityListing.html)

<a name="get_users_development_activity"></a>

## [**DevelopmentActivity**](DevelopmentActivity.html) get_users_development_activity(activity_id, type)



Get a Development Activity



Wraps GET /api/v2/users/development/activities/{activityId} 

Requires ANY permissions: 

* learning:assignment:view
* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserDevelopmentApi()
activity_id = 'activity_id_example' # str | Specifies the activity ID, maps to either assignment or appointment ID
type = 'type_example' # str | Specifies the activity type.

try:
    # Get a Development Activity
    api_response = api_instance.get_users_development_activity(activity_id, type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserDevelopmentApi->get_users_development_activity: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **activity_id** | **str**| Specifies the activity ID, maps to either assignment or appointment ID |  |
| **type** | **str**| Specifies the activity type. | <br />**Values**: Informational, Coaching |
{: class="table table-striped"}

### Return type

[**DevelopmentActivity**](DevelopmentActivity.html)

<a name="post_users_development_activities_aggregates_query"></a>

## [**DevelopmentActivityAggregateResponse**](DevelopmentActivityAggregateResponse.html) post_users_development_activities_aggregates_query(body)



Retrieve aggregated development activity data

Results are filtered based on the applicable permissions.

Wraps POST /api/v2/users/development/activities/aggregates/query 

Requires ANY permissions: 

* learning:assignment:view
* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserDevelopmentApi()
body = PureCloudPlatformClientV2.DevelopmentActivityAggregateParam() # DevelopmentActivityAggregateParam | Aggregate Request

try:
    # Retrieve aggregated development activity data
    api_response = api_instance.post_users_development_activities_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserDevelopmentApi->post_users_development_activities_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DevelopmentActivityAggregateParam**](DevelopmentActivityAggregateParam.html)| Aggregate Request |  |
{: class="table table-striped"}

### Return type

[**DevelopmentActivityAggregateResponse**](DevelopmentActivityAggregateResponse.html)

