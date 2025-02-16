# AlertingApi

## PureCloudPlatformClientV2.AlertingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_alerting_alert**](#delete_alerting_alert) | Delete an alert|
|[**delete_alerting_alerts_all**](#delete_alerting_alerts_all) | Delete all alerts for the user|
|[**delete_alerting_interactionstats_alert**](#delete_alerting_interactionstats_alert) | Delete an interaction stats alert|
|[**delete_alerting_interactionstats_rule**](#delete_alerting_interactionstats_rule) | Delete an interaction stats rule|
|[**delete_alerting_rule**](#delete_alerting_rule) | Delete a rule.|
|[**get_alerting_alert**](#get_alerting_alert) | Get an alert|
|[**get_alerting_alerts_active**](#get_alerting_alerts_active) | Gets active alert count for a user|
|[**get_alerting_interactionstats_alert**](#get_alerting_interactionstats_alert) | Get an interaction stats alert|
|[**get_alerting_interactionstats_alerts**](#get_alerting_interactionstats_alerts) | Get interaction stats alert list|
|[**get_alerting_interactionstats_alerts_unread**](#get_alerting_interactionstats_alerts_unread) | Gets user unread count of interaction stats alerts|
|[**get_alerting_interactionstats_rule**](#get_alerting_interactionstats_rule) | Get an interaction stats rule|
|[**get_alerting_interactionstats_rules**](#get_alerting_interactionstats_rules) | Get an interaction stats rule list|
|[**get_alerting_rule**](#get_alerting_rule) | Get a rule.|
|[**patch_alerting_alert**](#patch_alerting_alert) | Allows an entity to mute/snooze an alert or update the unread status of the alert.|
|[**patch_alerting_alerts_all**](#patch_alerting_alerts_all) | Updates all alerts|
|[**patch_alerting_alerts_bulk**](#patch_alerting_alerts_bulk) | Bulk alert updates|
|[**patch_alerting_rules_bulk**](#patch_alerting_rules_bulk) | Bulk update of notification lists|
|[**post_alerting_alerts_query**](#post_alerting_alerts_query) | Gets a paged list of alerts. The max page size is 50|
|[**post_alerting_interactionstats_rules**](#post_alerting_interactionstats_rules) | Create an interaction stats rule|
|[**post_alerting_rules**](#post_alerting_rules) | Create a Rule.|
|[**post_alerting_rules_bulk_remove**](#post_alerting_rules_bulk_remove) | Bulk remove rules|
|[**post_alerting_rules_query**](#post_alerting_rules_query) | Get a paged list of rules.  The max size of the page is 50 items.|
|[**put_alerting_alert**](#put_alerting_alert) | Update an alert read status|
|[**put_alerting_interactionstats_alert**](#put_alerting_interactionstats_alert) | Update an interaction stats alert read status|
|[**put_alerting_interactionstats_rule**](#put_alerting_interactionstats_rule) | Update an interaction stats rule|
|[**put_alerting_rule**](#put_alerting_rule) | Update a rule|



## delete_alerting_alert

>  delete_alerting_alert(alert_id)


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

### Return type

void (empty response body)


## delete_alerting_alerts_all

> object** delete_alerting_alerts_all()


Delete all alerts for the user

Wraps DELETE /api/v2/alerting/alerts/all 

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

try:
    # Delete all alerts for the user
    api_response = api_instance.delete_alerting_alerts_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->delete_alerting_alerts_all: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_alerting_interactionstats_alert

>  delete_alerting_interactionstats_alert(alert_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete an interaction stats alert

Apps should migrate to use DELETE /api/v2/alerting/alerts/{alertId}.

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

### Return type

void (empty response body)


## delete_alerting_interactionstats_rule

>  delete_alerting_interactionstats_rule(rule_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete an interaction stats rule

Apps should migrate to use DELETE /api/v2/alerting/rules/{ruleId}.

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
    # Delete an interaction stats rule
    api_instance.delete_alerting_interactionstats_rule(rule_id)
except ApiException as e:
    print("Exception when calling AlertingApi->delete_alerting_interactionstats_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID |  |

### Return type

void (empty response body)


## delete_alerting_rule

>  delete_alerting_rule(rule_id)


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

### Return type

void (empty response body)


## get_alerting_alert

> [**CommonAlert**](CommonAlert) get_alerting_alert(alert_id)


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

### Return type

[**CommonAlert**](CommonAlert)


## get_alerting_alerts_active

> [**ActiveAlertCount**](ActiveAlertCount) get_alerting_alerts_active()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Gets active alert count for a user

Apps should migrate to use POST /api/v2/alerting/alerts/query with the queryType set to 'Count' and alertStatus to 'Active' in the request body.

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
    # Gets active alert count for a user
    api_response = api_instance.get_alerting_alerts_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_alerts_active: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ActiveAlertCount**](ActiveAlertCount)


## get_alerting_interactionstats_alert

> [**InteractionStatsAlert**](InteractionStatsAlert) get_alerting_interactionstats_alert(alert_id, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get an interaction stats alert

Apps should migrate to use GET /api/v2/alerting/alerts/{alertId}.

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**InteractionStatsAlert**](InteractionStatsAlert)


## get_alerting_interactionstats_alerts

> [**InteractionStatsAlertContainer**](InteractionStatsAlertContainer) get_alerting_interactionstats_alerts(expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get interaction stats alert list

Apps should migrate to use POST /api/v2/alerting/alerts/query.

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
    # Get interaction stats alert list
    api_response = api_instance.get_alerting_interactionstats_alerts(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_alerts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**InteractionStatsAlertContainer**](InteractionStatsAlertContainer)


## get_alerting_interactionstats_alerts_unread

> [**UnreadMetric**](UnreadMetric) get_alerting_interactionstats_alerts_unread()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Gets user unread count of interaction stats alerts

Apps should migrate to use POST /api/v2/alerting/alerts/query with the queryType set to 'Count' and viewStatus to 'Unread' in the request body.

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
    # Gets user unread count of interaction stats alerts
    api_response = api_instance.get_alerting_interactionstats_alerts_unread()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_alerts_unread: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**UnreadMetric**](UnreadMetric)


## get_alerting_interactionstats_rule

> [**InteractionStatsRule**](InteractionStatsRule) get_alerting_interactionstats_rule(rule_id, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get an interaction stats rule

Apps should migrate to use GET /api/v2/alerting/rules/{ruleId}.

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
    # Get an interaction stats rule
    api_response = api_instance.get_alerting_interactionstats_rule(rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_rule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| Rule ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**InteractionStatsRule**](InteractionStatsRule)


## get_alerting_interactionstats_rules

> [**InteractionStatsRuleContainer**](InteractionStatsRuleContainer) get_alerting_interactionstats_rules(expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get an interaction stats rule list

Apps should migrate to use POST /api/v2/alerting/rules/query.

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
    # Get an interaction stats rule list
    api_response = api_instance.get_alerting_interactionstats_rules(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->get_alerting_interactionstats_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**InteractionStatsRuleContainer**](InteractionStatsRuleContainer)


## get_alerting_rule

> [**CommonRule**](CommonRule) get_alerting_rule(rule_id)


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

### Return type

[**CommonRule**](CommonRule)


## patch_alerting_alert

> [**CommonAlert**](CommonAlert) patch_alerting_alert(alert_id, body=body)


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
| **body** | [**AlertRequest**](AlertRequest)|  | [optional]  |

### Return type

[**CommonAlert**](CommonAlert)


## patch_alerting_alerts_all

> object** patch_alerting_alerts_all(body=body)


Updates all alerts

Wraps PATCH /api/v2/alerting/alerts/all 

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
body = PureCloudPlatformClientV2.CommonAllAlertUpdateRequest() # CommonAllAlertUpdateRequest |  (optional)

try:
    # Updates all alerts
    api_response = api_instance.patch_alerting_alerts_all(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->patch_alerting_alerts_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CommonAllAlertUpdateRequest**](CommonAllAlertUpdateRequest)|  | [optional]  |

### Return type

**object**


## patch_alerting_alerts_bulk

> [**BulkResponse**](BulkResponse) patch_alerting_alerts_bulk(body)


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
| **body** | [**CommonAlertBulkUpdateRequest**](CommonAlertBulkUpdateRequest)|  |  |

### Return type

[**BulkResponse**](BulkResponse)


## patch_alerting_rules_bulk

> [**BulkResponse**](BulkResponse) patch_alerting_rules_bulk(body)


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
| **body** | [**CommonRuleBulkUpdateNotificationsRequest**](CommonRuleBulkUpdateNotificationsRequest)|  |  |

### Return type

[**BulkResponse**](BulkResponse)


## post_alerting_alerts_query

> [**AlertListing**](AlertListing) post_alerting_alerts_query(body=body)


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
| **body** | [**GetAlertQuery**](GetAlertQuery)|  | [optional]  |

### Return type

[**AlertListing**](AlertListing)


## post_alerting_interactionstats_rules

> [**InteractionStatsRule**](InteractionStatsRule) post_alerting_interactionstats_rules(body, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Create an interaction stats rule

Apps should migrate to use POST /api/v2/alerting/rules.

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
    # Create an interaction stats rule
    api_response = api_instance.post_alerting_interactionstats_rules(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingApi->post_alerting_interactionstats_rules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**InteractionStatsRule**](InteractionStatsRule)| AlertingRule |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**InteractionStatsRule**](InteractionStatsRule)


## post_alerting_rules

> [**CommonRule**](CommonRule) post_alerting_rules(body)


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
| **body** | [**CommonRule**](CommonRule)| rule to be created |  |

### Return type

[**CommonRule**](CommonRule)


## post_alerting_rules_bulk_remove

> [**BulkResponse**](BulkResponse) post_alerting_rules_bulk_remove(body)


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
| **body** | [**CommonRuleBulkDeleteRequest**](CommonRuleBulkDeleteRequest)|  |  |

### Return type

[**BulkResponse**](BulkResponse)


## post_alerting_rules_query

> [**CommonRuleContainer**](CommonRuleContainer) post_alerting_rules_query(body=body)


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
| **body** | [**GetRulesQuery**](GetRulesQuery)|  | [optional]  |

### Return type

[**CommonRuleContainer**](CommonRuleContainer)


## put_alerting_alert

> [**UnreadStatus**](UnreadStatus) put_alerting_alert(alert_id, body=body)


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
| **body** | [**AlertingUnreadStatus**](AlertingUnreadStatus)|  | [optional]  |

### Return type

[**UnreadStatus**](UnreadStatus)


## put_alerting_interactionstats_alert

> [**UnreadStatus**](UnreadStatus) put_alerting_interactionstats_alert(alert_id, body, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update an interaction stats alert read status

Apps should migrate to use PUT /api/v2/alerting/alerts/{alertId}.

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
| **body** | [**UnreadStatus**](UnreadStatus)| InteractionStatsAlert |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**UnreadStatus**](UnreadStatus)


## put_alerting_interactionstats_rule

> [**InteractionStatsRule**](InteractionStatsRule) put_alerting_interactionstats_rule(rule_id, body, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update an interaction stats rule

Apps should migrate to use PUT /api/v2/alerting/rules/{ruleId}.

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
| **body** | [**InteractionStatsRule**](InteractionStatsRule)| AlertingRule |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: notificationUsers |

### Return type

[**InteractionStatsRule**](InteractionStatsRule)


## put_alerting_rule

> [**CommonRule**](CommonRule) put_alerting_rule(rule_id, body)


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
| **body** | [**ModifiableRuleProperties**](ModifiableRuleProperties)| rule to be updated |  |

### Return type

[**CommonRule**](CommonRule)


_PureCloudPlatformClientV2 222.0.0_
