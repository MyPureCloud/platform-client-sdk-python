---
title: AlertingApi
---

## PureCloudPlatformClientV2.AlertingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_alerting_interactionstats_alert**](AlertingApi.html#delete_alerting_interactionstats_alert) | Delete an interaction stats alert|
|[**delete_alerting_interactionstats_rule**](AlertingApi.html#delete_alerting_interactionstats_rule) | Delete an interaction stats rule.|
|[**get_alerting_alerts_active**](AlertingApi.html#get_alerting_alerts_active) | Gets active alert count for a user.|
|[**get_alerting_interactionstats_alert**](AlertingApi.html#get_alerting_interactionstats_alert) | Get an interaction stats alert|
|[**get_alerting_interactionstats_alerts**](AlertingApi.html#get_alerting_interactionstats_alerts) | Get interaction stats alert list.|
|[**get_alerting_interactionstats_alerts_unread**](AlertingApi.html#get_alerting_interactionstats_alerts_unread) | Gets user unread count of interaction stats alerts.|
|[**get_alerting_interactionstats_rule**](AlertingApi.html#get_alerting_interactionstats_rule) | Get an interaction stats rule.|
|[**get_alerting_interactionstats_rules**](AlertingApi.html#get_alerting_interactionstats_rules) | Get an interaction stats rule list.|
|[**post_alerting_interactionstats_rules**](AlertingApi.html#post_alerting_interactionstats_rules) | Create an interaction stats rule.|
|[**put_alerting_interactionstats_alert**](AlertingApi.html#put_alerting_interactionstats_alert) | Update an interaction stats alert read status|
|[**put_alerting_interactionstats_rule**](AlertingApi.html#put_alerting_interactionstats_rule) | Update an interaction stats rule|
{: class="table table-striped"}

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

