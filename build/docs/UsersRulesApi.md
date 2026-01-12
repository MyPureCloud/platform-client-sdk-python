# UsersRulesApi

## PureCloudPlatformClientV2.UsersRulesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_users_rule**](#delete_users_rule) | Delete an existing users rule|
|[**get_users_rule**](#get_users_rule) | Get a users rule|
|[**get_users_rule_dependent_type_id**](#get_users_rule_dependent_type_id) | Get dependent of a users rule|
|[**get_users_rule_dependents**](#get_users_rule_dependents) | Get dependents for a users rule|
|[**get_users_rules**](#get_users_rules) | Get the list of users rules|
|[**get_users_rules_setting**](#get_users_rules_setting) | Get the settings for a specific users rule type|
|[**patch_users_rule**](#patch_users_rule) | Update an existing users rule|
|[**post_users_rules**](#post_users_rules) | Create a new rule|
|[**post_users_rules_query**](#post_users_rules_query) | Query the result of a users rule|



## delete_users_rule

>  delete_users_rule(rule_id)


Delete an existing users rule

delete_users_rule is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/users/rules/{ruleId} 

Requires ANY permissions: 

* users:rules:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
rule_id = 'rule_id_example' # str | The id of the rule

try:
    # Delete an existing users rule
    api_instance.delete_users_rule(rule_id)
except ApiException as e:
    print("Exception when calling UsersRulesApi->delete_users_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| The id of the rule |  |

### Return type

void (empty response body)


## get_users_rule

> [**UsersRulesRule**](UsersRulesRule) get_users_rule(rule_id)


Get a users rule

get_users_rule is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/users/rules/{ruleId} 

Requires ANY permissions: 

* users:rules:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
rule_id = 'rule_id_example' # str | The ID of the rule to retrieve

try:
    # Get a users rule
    api_response = api_instance.get_users_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->get_users_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| The ID of the rule to retrieve |  |

### Return type

[**UsersRulesRule**](UsersRulesRule)


## get_users_rule_dependent_type_id

> [**UsersRulesDependent**](UsersRulesDependent) get_users_rule_dependent_type_id(rule_id, rule_type, type_id)


Get dependent of a users rule

get_users_rule_dependent_type_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/users/rules/{ruleId}/dependents/{ruleType}/{typeId} 

Requires ANY permissions: 

* users:ruleDependents:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
rule_id = 'rule_id_example' # str | The ID of the rule for which to retrieve dependents
rule_type = 'rule_type_example' # str | The type of the dependent
type_id = 'type_id_example' # str | The type ID of the dependent

try:
    # Get dependent of a users rule
    api_response = api_instance.get_users_rule_dependent_type_id(rule_id, rule_type, type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->get_users_rule_dependent_type_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| The ID of the rule for which to retrieve dependents |  |
| **rule_type** | **str**| The type of the dependent | <br />**Values**: learning |
| **type_id** | **str**| The type ID of the dependent |  |

### Return type

[**UsersRulesDependent**](UsersRulesDependent)


## get_users_rule_dependents

> [**UsersRulesDependentList**](UsersRulesDependentList) get_users_rule_dependents(rule_id, page_size=page_size, page_number=page_number, sort_order=sort_order)


Get dependents for a users rule

get_users_rule_dependents is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/users/rules/{ruleId}/dependents 

Requires ANY permissions: 

* users:ruleDependents:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
rule_id = 'rule_id_example' # str | The ID of the rule for which to retrieve dependents
page_size = 25 # int | Number of results per page (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''descending'' # str | Sort order for dependents (by last run date, then created date) (optional) (default to 'descending')

try:
    # Get dependents for a users rule
    api_response = api_instance.get_users_rule_dependents(rule_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->get_users_rule_dependents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| The ID of the rule for which to retrieve dependents |  |
| **page_size** | **int**| Number of results per page | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order for dependents (by last run date, then created date) | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |

### Return type

[**UsersRulesDependentList**](UsersRulesDependentList)


## get_users_rules

> [**UsersRulesRuleList**](UsersRulesRuleList) get_users_rules(types, page_number=page_number, page_size=page_size, expand=expand, search_term=search_term, sort_order=sort_order)


Get the list of users rules

get_users_rules is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/users/rules 

Requires ANY permissions: 

* users:rules:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
types = ['types_example'] # list[str] | The types of the rule
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Number of results per page (optional) (default to 25)
expand = ['expand_example'] # list[str] | Fields to expand in response (optional)
search_term = 'search_term_example' # str | a search term for finding a rule by name (optional)
sort_order = ''ascending'' # str | sort rules by name, ascending, descending (optional) (default to 'ascending')

try:
    # Get the list of users rules
    api_response = api_instance.get_users_rules(types, page_number=page_number, page_size=page_size, expand=expand, search_term=search_term, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->get_users_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **types** | [**list[str]**](str)| The types of the rule | <br />**Values**: Learning, ActivityPlan |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Number of results per page | [optional] [default to 25] |
| **expand** | [**list[str]**](str)| Fields to expand in response | [optional] <br />**Values**: criteria |
| **search_term** | **str**| a search term for finding a rule by name | [optional]  |
| **sort_order** | **str**| sort rules by name, ascending, descending | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |

### Return type

[**UsersRulesRuleList**](UsersRulesRuleList)


## get_users_rules_setting

> [**UsersRulesRuleSettings**](UsersRulesRuleSettings) get_users_rules_setting(rule_type)


Get the settings for a specific users rule type

get_users_rules_setting is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/users/rules/settings/{ruleType} 

Requires ANY permissions: 

* users:rules:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
rule_type = 'rule_type_example' # str | The type of the rule

try:
    # Get the settings for a specific users rule type
    api_response = api_instance.get_users_rules_setting(rule_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->get_users_rules_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_type** | **str**| The type of the rule | <br />**Values**: Learning, ActivityPlan |

### Return type

[**UsersRulesRuleSettings**](UsersRulesRuleSettings)


## patch_users_rule

> [**UsersRulesRule**](UsersRulesRule) patch_users_rule(rule_id, body)


Update an existing users rule

This will update an existing users rule with the specified fields.

patch_users_rule is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/users/rules/{ruleId} 

Requires ANY permissions: 

* users:rules:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
rule_id = 'rule_id_example' # str | The ID of the rule to update
body = PureCloudPlatformClientV2.UsersRulesUpdateRuleRequest() # UsersRulesUpdateRuleRequest | updateRuleRequest

try:
    # Update an existing users rule
    api_response = api_instance.patch_users_rule(rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->patch_users_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| The ID of the rule to update |  |
| **body** | [**UsersRulesUpdateRuleRequest**](UsersRulesUpdateRuleRequest)| updateRuleRequest |  |

### Return type

[**UsersRulesRule**](UsersRulesRule)


## post_users_rules

> [**UsersRulesRule**](UsersRulesRule) post_users_rules(body)


Create a new rule

This will create a new rule with the specified fields.

post_users_rules is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/users/rules 

Requires ANY permissions: 

* users:rules:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
body = PureCloudPlatformClientV2.UsersRulesCreateRuleRequest() # UsersRulesCreateRuleRequest | usersRulesCreateRuleRequest

try:
    # Create a new rule
    api_response = api_instance.post_users_rules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->post_users_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UsersRulesCreateRuleRequest**](UsersRulesCreateRuleRequest)| usersRulesCreateRuleRequest |  |

### Return type

[**UsersRulesRule**](UsersRulesRule)


## post_users_rules_query

> [**UsersRulesQueryResponse**](UsersRulesQueryResponse) post_users_rules_query(body, page_number=page_number, page_size=page_size)


Query the result of a users rule

This will query the result of a rule.

post_users_rules_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/users/rules/query 

Requires ANY permissions: 

* users:ruleUsers:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersRulesApi()
body = PureCloudPlatformClientV2.UsersRulesQueryRuleRequest() # UsersRulesQueryRuleRequest | usersRulesQueryRuleRequest
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Number of results per page (optional) (default to 25)

try:
    # Query the result of a users rule
    api_response = api_instance.post_users_rules_query(body, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRulesApi->post_users_rules_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UsersRulesQueryRuleRequest**](UsersRulesQueryRuleRequest)| usersRulesQueryRuleRequest |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Number of results per page | [optional] [default to 25] |

### Return type

[**UsersRulesQueryResponse**](UsersRulesQueryResponse)


_PureCloudPlatformClientV2 247.0.0_
