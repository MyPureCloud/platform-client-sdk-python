# AlertingApi

## PureCloudPlatformClientV2.AlertingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_alerting_alert**](#delete_alerting_alert) | Delete an alert|
|[**delete_alerting_alerts_all**](#delete_alerting_alerts_all) | Delete all alerts for the user|
|[**delete_alerting_rule**](#delete_alerting_rule) | Delete a rule.|
|[**get_alerting_alert**](#get_alerting_alert) | Get an alert|
|[**get_alerting_rule**](#get_alerting_rule) | Get a rule.|
|[**patch_alerting_alert**](#patch_alerting_alert) | Allows an entity to mute/snooze an alert or update the unread status of the alert.|
|[**patch_alerting_alerts_all**](#patch_alerting_alerts_all) | Updates all alerts|
|[**patch_alerting_alerts_bulk**](#patch_alerting_alerts_bulk) | Bulk alert updates|
|[**patch_alerting_rules_bulk**](#patch_alerting_rules_bulk) | Bulk update of notification lists|
|[**post_alerting_alerts_query**](#post_alerting_alerts_query) | Gets a paged list of alerts. The max page size is 50|
|[**post_alerting_rules**](#post_alerting_rules) | Create a Rule.|
|[**post_alerting_rules_bulk_remove**](#post_alerting_rules_bulk_remove) | Bulk remove rules|
|[**post_alerting_rules_query**](#post_alerting_rules_query) | Get a paged list of rules.  The max size of the page is 50 items.|
|[**put_alerting_alert**](#put_alerting_alert) | Update an alert read status|
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

> [**AlertingUnreadStatus**](AlertingUnreadStatus) put_alerting_alert(alert_id, body=body)


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

[**AlertingUnreadStatus**](AlertingUnreadStatus)


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


_PureCloudPlatformClientV2 244.0.0_
