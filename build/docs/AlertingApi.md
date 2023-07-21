---
title: AlertingApi
---

## PureCloudPlatformClientV2.AlertingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_alerting_alert**](AlertingApi.html#delete_alerting_alert) | Delete an alert|
|[**delete_alerting_interactionstats_alert**](AlertingApi.html#delete_alerting_interactionstats_alert) | Delete an interaction stats alert|
|[**delete_alerting_interactionstats_rule**](AlertingApi.html#delete_alerting_interactionstats_rule) | Delete an interaction stats rule.|
|[**delete_alerting_rule**](AlertingApi.html#delete_alerting_rule) | Delete a rule.|
|[**get_alerting_alert**](AlertingApi.html#get_alerting_alert) | Get an alert|
|[**get_alerting_alerts_active**](AlertingApi.html#get_alerting_alerts_active) | Gets active alert count for a user.|
|[**get_alerting_interactionstats_alert**](AlertingApi.html#get_alerting_interactionstats_alert) | Get an interaction stats alert|
|[**get_alerting_interactionstats_alerts**](AlertingApi.html#get_alerting_interactionstats_alerts) | Get interaction stats alert list.|
|[**get_alerting_interactionstats_alerts_unread**](AlertingApi.html#get_alerting_interactionstats_alerts_unread) | Gets user unread count of interaction stats alerts.|
|[**get_alerting_interactionstats_rule**](AlertingApi.html#get_alerting_interactionstats_rule) | Get an interaction stats rule.|
|[**get_alerting_interactionstats_rules**](AlertingApi.html#get_alerting_interactionstats_rules) | Get an interaction stats rule list.|
|[**get_alerting_rule**](AlertingApi.html#get_alerting_rule) | Get a rule.|
|[**patch_alerting_alert**](AlertingApi.html#patch_alerting_alert) | Allows an entity to mute/snooze an alert or update the unread status of the alert.|
|[**patch_alerting_alerts_bulk**](AlertingApi.html#patch_alerting_alerts_bulk) | Bulk alert updates|
|[**patch_alerting_rules_bulk**](AlertingApi.html#patch_alerting_rules_bulk) | Bulk update of notification lists|
|[**post_alerting_alerts_query**](AlertingApi.html#post_alerting_alerts_query) | Gets a paged list of alerts. The max page size is 50|
|[**post_alerting_interactionstats_rules**](AlertingApi.html#post_alerting_interactionstats_rules) | Create an interaction stats rule.|
|[**post_alerting_rules**](AlertingApi.html#post_alerting_rules) | Create a Rule.|
|[**post_alerting_rules_bulk_remove**](AlertingApi.html#post_alerting_rules_bulk_remove) | Bulk remove rules|
|[**post_alerting_rules_query**](AlertingApi.html#post_alerting_rules_query) | Get a paged list of rules.  The max size of the page is 50 items.|
|[**put_alerting_alert**](AlertingApi.html#put_alerting_alert) | Update an alert read status|
|[**put_alerting_interactionstats_alert**](AlertingApi.html#put_alerting_interactionstats_alert) | Update an interaction stats alert read status|
|[**put_alerting_interactionstats_rule**](AlertingApi.html#put_alerting_interactionstats_rule) | Update an interaction stats rule|
|[**put_alerting_rule**](AlertingApi.html#put_alerting_rule) | Update a rule|
{: class="table table-striped"}

<a name="delete_alerting_alert"></a>

##  delete_alerting_alert(alert_id)



Delete an alert

Wraps DELETE /api/v2/alerting/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Delete an alert
    api_instance.delete_alerting_alert(alert_id)
except ApiException as e:
    print("Exception when calling AlertingApi->delete_alerting_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_interactionstats_alert"></a>

##  delete_alerting_interactionstats_alert(alert_id)



Delete an interaction stats alert

Wraps DELETE /api/v2/alerting/interactionstats/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Delete an interaction stats alert
    api_instance.delete_alerting_interactionstats_alert(alert_id)
except ApiException as e:
    print("Exception when calling AlertingApi->delete_alerting_interactionstats_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_interactionstats_rule"></a>

##  delete_alerting_interactionstats_rule(rule_id)



Delete an interaction stats rule.

Wraps DELETE /api/v2/alerting/interactionstats/rules/{ruleId} 

Requires ALL permissions: 

* alerting:rule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Delete an interaction stats rule.
    api_instance.delete_alerting_interactionstats_rule(rule_id)
except ApiException as e:
    print("Exception when calling AlertingApi->delete_alerting_interactionstats_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_rule"></a>

##  delete_alerting_rule(rule_id)



Delete a rule.

Wraps DELETE /api/v2/alerting/rules/{ruleId} 

Requires ALL permissions: 

* alerting:rule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule Id

try:
    # Delete a rule.
    api_instance.delete_alerting_rule(rule_id)
except ApiException as e:
    print("Exception when calling AlertingApi->delete_alerting_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_alerting_alert"></a>

## [**CommonAlert**](CommonAlert.html) get_alerting_alert(alert_id)



Get an alert

Wraps GET /api/v2/alerting/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Get an alert
    api_response = api_instance.get_alerting_alert(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
{: class="table table-striped"}

### Return type

[**CommonAlert**](CommonAlert.html)

<a name="get_alerting_alerts_active"></a>

## [**ActiveAlertCount**](ActiveAlertCount.html) get_alerting_alerts_active()



Gets active alert count for a user.

Wraps GET /api/v2/alerting/alerts/active 

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
api_instance = PureCloudPlatformClientV2.AlertingApi()

try:
    # Gets active alert count for a user.
    api_response = api_instance.get_alerting_alerts_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_alerts_active: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ActiveAlertCount**](ActiveAlertCount.html)

<a name="get_alerting_interactionstats_alert"></a>

## [**InteractionStatsAlert**](InteractionStatsAlert.html) get_alerting_interactionstats_alert(alert_id, expand=expand)



Get an interaction stats alert

Wraps GET /api/v2/alerting/interactionstats/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get an interaction stats alert
    api_response = api_instance.get_alerting_interactionstats_alert(alert_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**InteractionStatsAlert**](InteractionStatsAlert.html)

<a name="get_alerting_interactionstats_alerts"></a>

## [**InteractionStatsAlertContainer**](InteractionStatsAlertContainer.html) get_alerting_interactionstats_alerts(expand=expand)



Get interaction stats alert list.

Wraps GET /api/v2/alerting/interactionstats/alerts 

Requires ALL permissions: 

* alerting:alert:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get interaction stats alert list.
    api_response = api_instance.get_alerting_interactionstats_alerts(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_alerts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**InteractionStatsAlertContainer**](InteractionStatsAlertContainer.html)

<a name="get_alerting_interactionstats_alerts_unread"></a>

## [**UnreadMetric**](UnreadMetric.html) get_alerting_interactionstats_alerts_unread()



Gets user unread count of interaction stats alerts.

Wraps GET /api/v2/alerting/interactionstats/alerts/unread 

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
api_instance = PureCloudPlatformClientV2.AlertingApi()

try:
    # Gets user unread count of interaction stats alerts.
    api_response = api_instance.get_alerting_interactionstats_alerts_unread()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_alerts_unread: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**UnreadMetric**](UnreadMetric.html)

<a name="get_alerting_interactionstats_rule"></a>

## [**InteractionStatsRule**](InteractionStatsRule.html) get_alerting_interactionstats_rule(rule_id, expand=expand)



Get an interaction stats rule.

Wraps GET /api/v2/alerting/interactionstats/rules/{ruleId} 

Requires ALL permissions: 

* alerting:rule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get an interaction stats rule.
    api_response = api_instance.get_alerting_interactionstats_rule(rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**InteractionStatsRule**](InteractionStatsRule.html)

<a name="get_alerting_interactionstats_rules"></a>

## [**InteractionStatsRuleContainer**](InteractionStatsRuleContainer.html) get_alerting_interactionstats_rules(expand=expand)



Get an interaction stats rule list.

Wraps GET /api/v2/alerting/interactionstats/rules 

Requires ALL permissions: 

* alerting:rule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get an interaction stats rule list.
    api_response = api_instance.get_alerting_interactionstats_rules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**InteractionStatsRuleContainer**](InteractionStatsRuleContainer.html)

<a name="get_alerting_rule"></a>

## [**CommonRule**](CommonRule.html) get_alerting_rule(rule_id)



Get a rule.

Wraps GET /api/v2/alerting/rules/{ruleId} 

Requires ALL permissions: 

* alerting:rule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule Id

try:
    # Get a rule.
    api_response = api_instance.get_alerting_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule Id |  |
{: class="table table-striped"}

### Return type

[**CommonRule**](CommonRule.html)

<a name="patch_alerting_alert"></a>

## [**CommonAlert**](CommonAlert.html) patch_alerting_alert(alert_id, body=body)



Allows an entity to mute/snooze an alert or update the unread status of the alert.

Snoozing an alert temporarily stop it from resending notifications to individualsas well as other services within Genesys Cloud for a given period.  Muting an alert will only block the notifications to individuals.

Wraps PATCH /api/v2/alerting/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
body = PureCloudPlatformClientV2.AlertRequest() # AlertRequest |  (optional)

try:
    # Allows an entity to mute/snooze an alert or update the unread status of the alert.
    api_response = api_instance.patch_alerting_alert(alert_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->patch_alerting_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
| **body** | [**AlertRequest**](AlertRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**CommonAlert**](CommonAlert.html)

<a name="patch_alerting_alerts_bulk"></a>

## [**BulkResponse**](BulkResponse.html) patch_alerting_alerts_bulk(body)



Bulk alert updates

Wraps PATCH /api/v2/alerting/alerts/bulk 

Requires ALL permissions: 

* alerting:alert:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.CommonAlertBulkUpdateRequest() # CommonAlertBulkUpdateRequest | 

try:
    # Bulk alert updates
    api_response = api_instance.patch_alerting_alerts_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->patch_alerting_alerts_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CommonAlertBulkUpdateRequest**](CommonAlertBulkUpdateRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**BulkResponse**](BulkResponse.html)

<a name="patch_alerting_rules_bulk"></a>

## [**BulkResponse**](BulkResponse.html) patch_alerting_rules_bulk(body)



Bulk update of notification lists

Wraps PATCH /api/v2/alerting/rules/bulk 

Requires ALL permissions: 

* alerting:rule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.CommonRuleBulkUpdateNotificationsRequest() # CommonRuleBulkUpdateNotificationsRequest | 

try:
    # Bulk update of notification lists
    api_response = api_instance.patch_alerting_rules_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->patch_alerting_rules_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CommonRuleBulkUpdateNotificationsRequest**](CommonRuleBulkUpdateNotificationsRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**BulkResponse**](BulkResponse.html)

<a name="post_alerting_alerts_query"></a>

## [**AlertListing**](AlertListing.html) post_alerting_alerts_query(body=body)



Gets a paged list of alerts. The max page size is 50

Wraps POST /api/v2/alerting/alerts/query 

Requires ALL permissions: 

* alerting:alert:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.GetAlertQuery() # GetAlertQuery |  (optional)

try:
    # Gets a paged list of alerts. The max page size is 50
    api_response = api_instance.post_alerting_alerts_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->post_alerting_alerts_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GetAlertQuery**](GetAlertQuery.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**AlertListing**](AlertListing.html)

<a name="post_alerting_interactionstats_rules"></a>

## [**InteractionStatsRule**](InteractionStatsRule.html) post_alerting_interactionstats_rules(body, expand=expand)



Create an interaction stats rule.

Wraps POST /api/v2/alerting/interactionstats/rules 

Requires ALL permissions: 

* alerting:rule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.InteractionStatsRule() # InteractionStatsRule | AlertingRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Create an interaction stats rule.
    api_response = api_instance.post_alerting_interactionstats_rules(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->post_alerting_interactionstats_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**InteractionStatsRule**](InteractionStatsRule.html)| AlertingRule |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**InteractionStatsRule**](InteractionStatsRule.html)

<a name="post_alerting_rules"></a>

## [**CommonRule**](CommonRule.html) post_alerting_rules(body)



Create a Rule.

Wraps POST /api/v2/alerting/rules 

Requires ALL permissions: 

* alerting:rule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.CommonRule() # CommonRule | rule to be created

try:
    # Create a Rule.
    api_response = api_instance.post_alerting_rules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->post_alerting_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CommonRule**](CommonRule.html)| rule to be created |  |
{: class="table table-striped"}

### Return type

[**CommonRule**](CommonRule.html)

<a name="post_alerting_rules_bulk_remove"></a>

## [**BulkResponse**](BulkResponse.html) post_alerting_rules_bulk_remove(body)



Bulk remove rules

Wraps POST /api/v2/alerting/rules/bulk/remove 

Requires ALL permissions: 

* alerting:rule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.CommonRuleBulkDeleteRequest() # CommonRuleBulkDeleteRequest | 

try:
    # Bulk remove rules
    api_response = api_instance.post_alerting_rules_bulk_remove(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->post_alerting_rules_bulk_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CommonRuleBulkDeleteRequest**](CommonRuleBulkDeleteRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**BulkResponse**](BulkResponse.html)

<a name="post_alerting_rules_query"></a>

## [**CommonRuleContainer**](CommonRuleContainer.html) post_alerting_rules_query(body=body)



Get a paged list of rules.  The max size of the page is 50 items.

Wraps POST /api/v2/alerting/rules/query 

Requires ALL permissions: 

* alerting:rule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.GetRulesQuery() # GetRulesQuery |  (optional)

try:
    # Get a paged list of rules.  The max size of the page is 50 items.
    api_response = api_instance.post_alerting_rules_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->post_alerting_rules_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GetRulesQuery**](GetRulesQuery.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**CommonRuleContainer**](CommonRuleContainer.html)

<a name="put_alerting_alert"></a>

## [**UnreadStatus**](UnreadStatus.html) put_alerting_alert(alert_id, body=body)



Update an alert read status

Wraps PUT /api/v2/alerting/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
body = PureCloudPlatformClientV2.AlertingUnreadStatus() # AlertingUnreadStatus |  (optional)

try:
    # Update an alert read status
    api_response = api_instance.put_alerting_alert(alert_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->put_alerting_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
| **body** | [**AlertingUnreadStatus**](AlertingUnreadStatus.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**UnreadStatus**](UnreadStatus.html)

<a name="put_alerting_interactionstats_alert"></a>

## [**UnreadStatus**](UnreadStatus.html) put_alerting_interactionstats_alert(alert_id, body, expand=expand)



Update an interaction stats alert read status

Wraps PUT /api/v2/alerting/interactionstats/alerts/{alertId} 

Requires ALL permissions: 

* alerting:alert:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
body = PureCloudPlatformClientV2.UnreadStatus() # UnreadStatus | InteractionStatsAlert
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Update an interaction stats alert read status
    api_response = api_instance.put_alerting_interactionstats_alert(alert_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->put_alerting_interactionstats_alert: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID |  |
| **body** | [**UnreadStatus**](UnreadStatus.html)| InteractionStatsAlert |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**UnreadStatus**](UnreadStatus.html)

<a name="put_alerting_interactionstats_rule"></a>

## [**InteractionStatsRule**](InteractionStatsRule.html) put_alerting_interactionstats_rule(rule_id, body, expand=expand)



Update an interaction stats rule

Wraps PUT /api/v2/alerting/interactionstats/rules/{ruleId} 

Requires ALL permissions: 

* alerting:rule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
body = PureCloudPlatformClientV2.InteractionStatsRule() # InteractionStatsRule | AlertingRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Update an interaction stats rule
    api_response = api_instance.put_alerting_interactionstats_rule(rule_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->put_alerting_interactionstats_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID |  |
| **body** | [**InteractionStatsRule**](InteractionStatsRule.html)| AlertingRule |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |
{: class="table table-striped"}

### Return type

[**InteractionStatsRule**](InteractionStatsRule.html)

<a name="put_alerting_rule"></a>

## [**CommonRule**](CommonRule.html) put_alerting_rule(rule_id, body)



Update a rule

Wraps PUT /api/v2/alerting/rules/{ruleId} 

Requires ALL permissions: 

* alerting:rule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule Id
body = PureCloudPlatformClientV2.ModifiableRuleProperties() # ModifiableRuleProperties | rule to be updated

try:
    # Update a rule
    api_response = api_instance.put_alerting_rule(rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->put_alerting_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule Id |  |
| **body** | [**ModifiableRuleProperties**](ModifiableRuleProperties.html)| rule to be updated |  |
{: class="table table-striped"}

### Return type

[**CommonRule**](CommonRule.html)

