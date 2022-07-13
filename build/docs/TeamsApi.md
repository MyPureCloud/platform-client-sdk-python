---
title: TeamsApi
---

## PureCloudPlatformClientV2.TeamsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_team**](TeamsApi.html#delete_team) | Delete team|
|[**get_team**](TeamsApi.html#get_team) | Get team|
|[**get_teams**](TeamsApi.html#get_teams) | Get Team listing|
|[**patch_team**](TeamsApi.html#patch_team) | Update team|
|[**post_teams**](TeamsApi.html#post_teams) | Create a team|
|[**post_teams_search**](TeamsApi.html#post_teams_search) | Search resources.|
{: class="table table-striped"}

<a name="delete_team"></a>

##  delete_team(team_id)



Delete team



Wraps DELETE /api/v2/teams/{teamId} 

Requires ANY permissions: 

* groups:team:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TeamsApi()
team_id = 'team_id_example' # str | Team ID

try:
    # Delete team
    api_instance.delete_team(team_id)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **team_id** | **str**| Team ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_team"></a>

## [**Team**](Team.html) get_team(team_id)



Get team



Wraps GET /api/v2/teams/{teamId} 

Requires ANY permissions: 

* groups:team:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TeamsApi()
team_id = 'team_id_example' # str | Team ID

try:
    # Get team
    api_response = api_instance.get_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **team_id** | **str**| Team ID |  |
{: class="table table-striped"}

### Return type

[**Team**](Team.html)

<a name="get_teams"></a>

## [**TeamEntityListing**](TeamEntityListing.html) get_teams(page_size=page_size, name=name, after=after, before=before, expand=expand)



Get Team listing



Wraps GET /api/v2/teams 

Requires ANY permissions: 

* groups:team:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TeamsApi()
page_size = 25 # int | Page size (optional) (default to 25)
name = 'name_example' # str | Return only teams whose names start with this value (case-insensitive matching) (optional)
after = 'after_example' # str | The cursor that points to the next item in the complete list of teams (optional)
before = 'before_example' # str | The cursor that points to the previous item in the complete list of teams (optional)
expand = 'expand_example' # str | Expand the name on each user (optional)

try:
    # Get Team listing
    api_response = api_instance.get_teams(page_size=page_size, name=name, after=after, before=before, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name** | **str**| Return only teams whose names start with this value (case-insensitive matching) | [optional]  |
| **after** | **str**| The cursor that points to the next item in the complete list of teams | [optional]  |
| **before** | **str**| The cursor that points to the previous item in the complete list of teams | [optional]  |
| **expand** | **str**| Expand the name on each user | [optional] <br />**Values**: entities.division |
{: class="table table-striped"}

### Return type

[**TeamEntityListing**](TeamEntityListing.html)

<a name="patch_team"></a>

## [**Team**](Team.html) patch_team(team_id, body)



Update team



Wraps PATCH /api/v2/teams/{teamId} 

Requires ANY permissions: 

* groups:team:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TeamsApi()
team_id = 'team_id_example' # str | Team ID
body = PureCloudPlatformClientV2.Team() # Team | Team

try:
    # Update team
    api_response = api_instance.patch_team(team_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->patch_team: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **team_id** | **str**| Team ID |  |
| **body** | [**Team**](Team.html)| Team |  |
{: class="table table-striped"}

### Return type

[**Team**](Team.html)

<a name="post_teams"></a>

## [**Team**](Team.html) post_teams(body)



Create a team



Wraps POST /api/v2/teams 

Requires ANY permissions: 

* groups:team:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TeamsApi()
body = PureCloudPlatformClientV2.Team() # Team | Team

try:
    # Create a team
    api_response = api_instance.post_teams(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->post_teams: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Team**](Team.html)| Team |  |
{: class="table table-striped"}

### Return type

[**Team**](Team.html)

<a name="post_teams_search"></a>

## [**TeamsSearchResponse**](TeamsSearchResponse.html) post_teams_search(body)



Search resources.



Wraps POST /api/v2/teams/search 

Requires ANY permissions: 

* groups:team:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TeamsApi()
body = PureCloudPlatformClientV2.TeamSearchRequest() # TeamSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_teams_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->post_teams_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TeamSearchRequest**](TeamSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**TeamsSearchResponse**](TeamsSearchResponse.html)

