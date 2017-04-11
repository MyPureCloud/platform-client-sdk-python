---
title: AlertingApi
---

## PureCloudPlatformClientV2.AlertingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_alerting_heartbeat_alert**](AlertingApi.html#delete_alerting_heartbeat_alert) | Delete a heart beat alert|
|[**delete_alerting_heartbeat_rule**](AlertingApi.html#delete_alerting_heartbeat_rule) | Delete a heart beat rule.|
|[**delete_alerting_interactionstats_alert**](AlertingApi.html#delete_alerting_interactionstats_alert) | Delete an interaction stats alert|
|[**delete_alerting_interactionstats_rule**](AlertingApi.html#delete_alerting_interactionstats_rule) | Delete an interaction stats rule.|
|[**delete_alerting_routingstatus_alert**](AlertingApi.html#delete_alerting_routingstatus_alert) | Delete a routing status alert|
|[**delete_alerting_routingstatus_rule**](AlertingApi.html#delete_alerting_routingstatus_rule) | Delete a routing status rule.|
|[**delete_alerting_userpresence_alert**](AlertingApi.html#delete_alerting_userpresence_alert) | Delete a user presence alert|
|[**delete_alerting_userpresence_rule**](AlertingApi.html#delete_alerting_userpresence_rule) | Delete a user presence rule.|
|[**get_alerting_heartbeat_alert**](AlertingApi.html#get_alerting_heartbeat_alert) | Get a heart beat alert|
|[**get_alerting_heartbeat_alerts**](AlertingApi.html#get_alerting_heartbeat_alerts) | Get heart beat alert list.|
|[**get_alerting_heartbeat_rule**](AlertingApi.html#get_alerting_heartbeat_rule) | Get a heart beat rule.|
|[**get_alerting_heartbeat_rules**](AlertingApi.html#get_alerting_heartbeat_rules) | Get a heart beat rule list.|
|[**get_alerting_interactionstats_alert**](AlertingApi.html#get_alerting_interactionstats_alert) | Get an interaction stats alert|
|[**get_alerting_interactionstats_alerts**](AlertingApi.html#get_alerting_interactionstats_alerts) | Get interaction stats alert list.|
|[**get_alerting_interactionstats_alerts_unread**](AlertingApi.html#get_alerting_interactionstats_alerts_unread) | Gets user unread count of interaction stats alerts.|
|[**get_alerting_interactionstats_rule**](AlertingApi.html#get_alerting_interactionstats_rule) | Get an interaction stats rule.|
|[**get_alerting_interactionstats_rules**](AlertingApi.html#get_alerting_interactionstats_rules) | Get an interaction stats rule list.|
|[**get_alerting_routingstatus_alert**](AlertingApi.html#get_alerting_routingstatus_alert) | Get a routing status alert|
|[**get_alerting_routingstatus_alerts**](AlertingApi.html#get_alerting_routingstatus_alerts) | Get routing status alert list.|
|[**get_alerting_routingstatus_rule**](AlertingApi.html#get_alerting_routingstatus_rule) | Get a routing status rule.|
|[**get_alerting_routingstatus_rules**](AlertingApi.html#get_alerting_routingstatus_rules) | Get a routing status rule list.|
|[**get_alerting_userpresence_alert**](AlertingApi.html#get_alerting_userpresence_alert) | Get a user presence alert|
|[**get_alerting_userpresence_alerts**](AlertingApi.html#get_alerting_userpresence_alerts) | Get user presence alert list.|
|[**get_alerting_userpresence_rule**](AlertingApi.html#get_alerting_userpresence_rule) | Get a user presence rule.|
|[**get_alerting_userpresence_rules**](AlertingApi.html#get_alerting_userpresence_rules) | Get a user presence rule list.|
|[**post_alerting_heartbeat_rules**](AlertingApi.html#post_alerting_heartbeat_rules) | Create a heart beat rule.|
|[**post_alerting_interactionstats_rules**](AlertingApi.html#post_alerting_interactionstats_rules) | Create an interaction stats rule.|
|[**post_alerting_routingstatus_rules**](AlertingApi.html#post_alerting_routingstatus_rules) | Create a routing status rule.|
|[**post_alerting_userpresence_rules**](AlertingApi.html#post_alerting_userpresence_rules) | Create a user presence rule.|
|[**put_alerting_heartbeat_rule**](AlertingApi.html#put_alerting_heartbeat_rule) | Update a heart beat rule|
|[**put_alerting_interactionstats_alert**](AlertingApi.html#put_alerting_interactionstats_alert) | Update an interaction stats alert read status|
|[**put_alerting_interactionstats_rule**](AlertingApi.html#put_alerting_interactionstats_rule) | Update an interaction stats rule|
|[**put_alerting_routingstatus_rule**](AlertingApi.html#put_alerting_routingstatus_rule) | Update a routing status rule|
|[**put_alerting_userpresence_rule**](AlertingApi.html#put_alerting_userpresence_rule) | Update a user presence rule|
{: class="table table-striped"}

<a name="delete_alerting_heartbeat_alert"></a>

##  delete_alerting_heartbeat_alert(alert_id)

Delete a heart beat alert



Wraps DELETE /api/v2/alerting/heartbeat/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Delete a heart beat alert
    api_instance.delete_alerting_heartbeat_alert(alert_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_heartbeat_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_heartbeat_rule"></a>

##  delete_alerting_heartbeat_rule(rule_id)

Delete a heart beat rule.



Wraps DELETE /api/v2/alerting/heartbeat/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Delete a heart beat rule.
    api_instance.delete_alerting_heartbeat_rule(rule_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_heartbeat_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_interactionstats_alert"></a>

##  delete_alerting_interactionstats_alert(alert_id)

Delete an interaction stats alert



Wraps DELETE /api/v2/alerting/interactionstats/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Delete an interaction stats alert
    api_instance.delete_alerting_interactionstats_alert(alert_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_interactionstats_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_interactionstats_rule"></a>

##  delete_alerting_interactionstats_rule(rule_id)

Delete an interaction stats rule.



Wraps DELETE /api/v2/alerting/interactionstats/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Delete an interaction stats rule.
    api_instance.delete_alerting_interactionstats_rule(rule_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_interactionstats_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_routingstatus_alert"></a>

##  delete_alerting_routingstatus_alert(alert_id)

Delete a routing status alert



Wraps DELETE /api/v2/alerting/routingstatus/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Delete a routing status alert
    api_instance.delete_alerting_routingstatus_alert(alert_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_routingstatus_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_routingstatus_rule"></a>

##  delete_alerting_routingstatus_rule(rule_id)

Delete a routing status rule.



Wraps DELETE /api/v2/alerting/routingstatus/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Delete a routing status rule.
    api_instance.delete_alerting_routingstatus_rule(rule_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_routingstatus_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_userpresence_alert"></a>

##  delete_alerting_userpresence_alert(alert_id)

Delete a user presence alert



Wraps DELETE /api/v2/alerting/userpresence/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID

try:
    # Delete a user presence alert
    api_instance.delete_alerting_userpresence_alert(alert_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_userpresence_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_alerting_userpresence_rule"></a>

##  delete_alerting_userpresence_rule(rule_id)

Delete a user presence rule.



Wraps DELETE /api/v2/alerting/userpresence/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Delete a user presence rule.
    api_instance.delete_alerting_userpresence_rule(rule_id)
except ApiException as e:
    print "Exception when calling AlertingApi->delete_alerting_userpresence_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_alerting_heartbeat_alert"></a>

## [**HeartBeatAlert**](HeartBeatAlert.html) get_alerting_heartbeat_alert(alert_id, expand=expand)

Get a heart beat alert



Wraps GET /api/v2/alerting/heartbeat/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a heart beat alert
    api_response = api_instance.get_alerting_heartbeat_alert(alert_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_heartbeat_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**HeartBeatAlert**](HeartBeatAlert.html)

<a name="get_alerting_heartbeat_alerts"></a>

## [**HeartBeatAlertContainer**](HeartBeatAlertContainer.html) get_alerting_heartbeat_alerts(expand=expand)

Get heart beat alert list.



Wraps GET /api/v2/alerting/heartbeat/alerts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get heart beat alert list.
    api_response = api_instance.get_alerting_heartbeat_alerts(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_heartbeat_alerts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**HeartBeatAlertContainer**](HeartBeatAlertContainer.html)

<a name="get_alerting_heartbeat_rule"></a>

## [**HeartBeatRule**](HeartBeatRule.html) get_alerting_heartbeat_rule(rule_id, expand=expand)

Get a heart beat rule.



Wraps GET /api/v2/alerting/heartbeat/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a heart beat rule.
    api_response = api_instance.get_alerting_heartbeat_rule(rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_heartbeat_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**HeartBeatRule**](HeartBeatRule.html)

<a name="get_alerting_heartbeat_rules"></a>

## [**HeartBeatRuleContainer**](HeartBeatRuleContainer.html) get_alerting_heartbeat_rules(expand=expand)

Get a heart beat rule list.



Wraps GET /api/v2/alerting/heartbeat/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a heart beat rule list.
    api_response = api_instance.get_alerting_heartbeat_rules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_heartbeat_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**HeartBeatRuleContainer**](HeartBeatRuleContainer.html)

<a name="get_alerting_interactionstats_alert"></a>

## [**InteractionStatsAlert**](InteractionStatsAlert.html) get_alerting_interactionstats_alert(alert_id, expand=expand)

Get an interaction stats alert



Wraps GET /api/v2/alerting/interactionstats/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling AlertingApi->get_alerting_interactionstats_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**InteractionStatsAlert**](InteractionStatsAlert.html)

<a name="get_alerting_interactionstats_alerts"></a>

## [**InteractionStatsAlertContainer**](InteractionStatsAlertContainer.html) get_alerting_interactionstats_alerts(expand=expand)

Get interaction stats alert list.



Wraps GET /api/v2/alerting/interactionstats/alerts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get interaction stats alert list.
    api_response = api_instance.get_alerting_interactionstats_alerts(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_interactionstats_alerts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**InteractionStatsAlertContainer**](InteractionStatsAlertContainer.html)

<a name="get_alerting_interactionstats_alerts_unread"></a>

## [**UnreadMetric**](UnreadMetric.html) get_alerting_interactionstats_alerts_unread()

Gets user unread count of interaction stats alerts.



Wraps GET /api/v2/alerting/interactionstats/alerts/unread 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()

try:
    # Gets user unread count of interaction stats alerts.
    api_response = api_instance.get_alerting_interactionstats_alerts_unread()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_interactionstats_alerts_unread: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**UnreadMetric**](UnreadMetric.html)

<a name="get_alerting_interactionstats_rule"></a>

## [**InteractionStatsRule**](InteractionStatsRule.html) get_alerting_interactionstats_rule(rule_id, expand=expand)

Get an interaction stats rule.



Wraps GET /api/v2/alerting/interactionstats/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling AlertingApi->get_alerting_interactionstats_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**InteractionStatsRule**](InteractionStatsRule.html)

<a name="get_alerting_interactionstats_rules"></a>

## [**InteractionStatsRuleContainer**](InteractionStatsRuleContainer.html) get_alerting_interactionstats_rules(expand=expand)

Get an interaction stats rule list.



Wraps GET /api/v2/alerting/interactionstats/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get an interaction stats rule list.
    api_response = api_instance.get_alerting_interactionstats_rules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_interactionstats_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**InteractionStatsRuleContainer**](InteractionStatsRuleContainer.html)

<a name="get_alerting_routingstatus_alert"></a>

## [**RoutingStatusAlert**](RoutingStatusAlert.html) get_alerting_routingstatus_alert(alert_id, expand=expand)

Get a routing status alert



Wraps GET /api/v2/alerting/routingstatus/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a routing status alert
    api_response = api_instance.get_alerting_routingstatus_alert(alert_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_routingstatus_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**RoutingStatusAlert**](RoutingStatusAlert.html)

<a name="get_alerting_routingstatus_alerts"></a>

## [**RoutingStatusAlertContainer**](RoutingStatusAlertContainer.html) get_alerting_routingstatus_alerts(expand=expand)

Get routing status alert list.



Wraps GET /api/v2/alerting/routingstatus/alerts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get routing status alert list.
    api_response = api_instance.get_alerting_routingstatus_alerts(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_routingstatus_alerts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**RoutingStatusAlertContainer**](RoutingStatusAlertContainer.html)

<a name="get_alerting_routingstatus_rule"></a>

## [**RoutingStatusRule**](RoutingStatusRule.html) get_alerting_routingstatus_rule(rule_id, expand=expand)

Get a routing status rule.



Wraps GET /api/v2/alerting/routingstatus/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a routing status rule.
    api_response = api_instance.get_alerting_routingstatus_rule(rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_routingstatus_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**RoutingStatusRule**](RoutingStatusRule.html)

<a name="get_alerting_routingstatus_rules"></a>

## [**RoutingStatusRuleContainer**](RoutingStatusRuleContainer.html) get_alerting_routingstatus_rules(expand=expand)

Get a routing status rule list.



Wraps GET /api/v2/alerting/routingstatus/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a routing status rule list.
    api_response = api_instance.get_alerting_routingstatus_rules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_routingstatus_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**RoutingStatusRuleContainer**](RoutingStatusRuleContainer.html)

<a name="get_alerting_userpresence_alert"></a>

## [**UserPresenceAlert**](UserPresenceAlert.html) get_alerting_userpresence_alert(alert_id, expand=expand)

Get a user presence alert



Wraps GET /api/v2/alerting/userpresence/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
alert_id = 'alert_id_example' # str | Alert ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a user presence alert
    api_response = api_instance.get_alerting_userpresence_alert(alert_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_userpresence_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserPresenceAlert**](UserPresenceAlert.html)

<a name="get_alerting_userpresence_alerts"></a>

## [**UserPresenceAlertContainer**](UserPresenceAlertContainer.html) get_alerting_userpresence_alerts(expand=expand)

Get user presence alert list.



Wraps GET /api/v2/alerting/userpresence/alerts 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get user presence alert list.
    api_response = api_instance.get_alerting_userpresence_alerts(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_userpresence_alerts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserPresenceAlertContainer**](UserPresenceAlertContainer.html)

<a name="get_alerting_userpresence_rule"></a>

## [**UserPresenceRule**](UserPresenceRule.html) get_alerting_userpresence_rule(rule_id, expand=expand)

Get a user presence rule.



Wraps GET /api/v2/alerting/userpresence/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a user presence rule.
    api_response = api_instance.get_alerting_userpresence_rule(rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_userpresence_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserPresenceRule**](UserPresenceRule.html)

<a name="get_alerting_userpresence_rules"></a>

## [**UserPresenceRuleContainer**](UserPresenceRuleContainer.html) get_alerting_userpresence_rules(expand=expand)

Get a user presence rule list.



Wraps GET /api/v2/alerting/userpresence/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get a user presence rule list.
    api_response = api_instance.get_alerting_userpresence_rules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->get_alerting_userpresence_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserPresenceRuleContainer**](UserPresenceRuleContainer.html)

<a name="post_alerting_heartbeat_rules"></a>

## [**HeartBeatRule**](HeartBeatRule.html) post_alerting_heartbeat_rules(body, expand=expand)

Create a heart beat rule.



Wraps POST /api/v2/alerting/heartbeat/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.HeartBeatRule() # HeartBeatRule | HeartBeatRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Create a heart beat rule.
    api_response = api_instance.post_alerting_heartbeat_rules(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->post_alerting_heartbeat_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**HeartBeatRule**](HeartBeatRule.html)| HeartBeatRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**HeartBeatRule**](HeartBeatRule.html)

<a name="post_alerting_interactionstats_rules"></a>

## [**InteractionStatsRule**](InteractionStatsRule.html) post_alerting_interactionstats_rules(body, expand=expand)

Create an interaction stats rule.



Wraps POST /api/v2/alerting/interactionstats/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling AlertingApi->post_alerting_interactionstats_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**InteractionStatsRule**](InteractionStatsRule.html)| AlertingRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**InteractionStatsRule**](InteractionStatsRule.html)

<a name="post_alerting_routingstatus_rules"></a>

## [**RoutingStatusRule**](RoutingStatusRule.html) post_alerting_routingstatus_rules(body, expand=expand)

Create a routing status rule.



Wraps POST /api/v2/alerting/routingstatus/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.RoutingStatusRule() # RoutingStatusRule | RoutingStatusRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Create a routing status rule.
    api_response = api_instance.post_alerting_routingstatus_rules(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->post_alerting_routingstatus_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoutingStatusRule**](RoutingStatusRule.html)| RoutingStatusRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**RoutingStatusRule**](RoutingStatusRule.html)

<a name="post_alerting_userpresence_rules"></a>

## [**UserPresenceRule**](UserPresenceRule.html) post_alerting_userpresence_rules(body, expand=expand)

Create a user presence rule.



Wraps POST /api/v2/alerting/userpresence/rules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
body = PureCloudPlatformClientV2.UserPresenceRule() # UserPresenceRule | UserPresenceRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Create a user presence rule.
    api_response = api_instance.post_alerting_userpresence_rules(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->post_alerting_userpresence_rules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserPresenceRule**](UserPresenceRule.html)| UserPresenceRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserPresenceRule**](UserPresenceRule.html)

<a name="put_alerting_heartbeat_rule"></a>

## [**HeartBeatRule**](HeartBeatRule.html) put_alerting_heartbeat_rule(rule_id, body, expand=expand)

Update a heart beat rule



Wraps PUT /api/v2/alerting/heartbeat/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
body = PureCloudPlatformClientV2.HeartBeatRule() # HeartBeatRule | HeartBeatRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Update a heart beat rule
    api_response = api_instance.put_alerting_heartbeat_rule(rule_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->put_alerting_heartbeat_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **body** | [**HeartBeatRule**](HeartBeatRule.html)| HeartBeatRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**HeartBeatRule**](HeartBeatRule.html)

<a name="put_alerting_interactionstats_alert"></a>

## [**UnreadStatus**](UnreadStatus.html) put_alerting_interactionstats_alert(alert_id, body, expand=expand)

Update an interaction stats alert read status



Wraps PUT /api/v2/alerting/interactionstats/alerts/{alertId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling AlertingApi->put_alerting_interactionstats_alert: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **alert_id** | **str**| Alert ID | |
| **body** | [**UnreadStatus**](UnreadStatus.html)| InteractionStatsAlert | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UnreadStatus**](UnreadStatus.html)

<a name="put_alerting_interactionstats_rule"></a>

## [**InteractionStatsRule**](InteractionStatsRule.html) put_alerting_interactionstats_rule(rule_id, body, expand=expand)

Update an interaction stats rule



Wraps PUT /api/v2/alerting/interactionstats/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling AlertingApi->put_alerting_interactionstats_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **body** | [**InteractionStatsRule**](InteractionStatsRule.html)| AlertingRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**InteractionStatsRule**](InteractionStatsRule.html)

<a name="put_alerting_routingstatus_rule"></a>

## [**RoutingStatusRule**](RoutingStatusRule.html) put_alerting_routingstatus_rule(rule_id, body, expand=expand)

Update a routing status rule



Wraps PUT /api/v2/alerting/routingstatus/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
body = PureCloudPlatformClientV2.RoutingStatusRule() # RoutingStatusRule | RoutingStatusRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Update a routing status rule
    api_response = api_instance.put_alerting_routingstatus_rule(rule_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->put_alerting_routingstatus_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **body** | [**RoutingStatusRule**](RoutingStatusRule.html)| RoutingStatusRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**RoutingStatusRule**](RoutingStatusRule.html)

<a name="put_alerting_userpresence_rule"></a>

## [**UserPresenceRule**](UserPresenceRule.html) put_alerting_userpresence_rule(rule_id, body, expand=expand)

Update a user presence rule



Wraps PUT /api/v2/alerting/userpresence/rules/{ruleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AlertingApi()
rule_id = 'rule_id_example' # str | Rule ID
body = PureCloudPlatformClientV2.UserPresenceRule() # UserPresenceRule | UserPresenceRule
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Update a user presence rule
    api_response = api_instance.put_alerting_userpresence_rule(rule_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertingApi->put_alerting_userpresence_rule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID | |
| **body** | [**UserPresenceRule**](UserPresenceRule.html)| UserPresenceRule | |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserPresenceRule**](UserPresenceRule.html)

