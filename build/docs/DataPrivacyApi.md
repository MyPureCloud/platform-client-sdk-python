# DataPrivacyApi

## PureCloudPlatformClientV2.DataPrivacyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_dataprivacy_maskingrule**](#delete_dataprivacy_maskingrule) | Delete a masking rule.|
|[**get_dataprivacy_maskingrule**](#get_dataprivacy_maskingrule) | Fetch details about a masking rule.|
|[**get_dataprivacy_maskingrules**](#get_dataprivacy_maskingrules) | Retrieve the list of masking rules.|
|[**patch_dataprivacy_maskingrule**](#patch_dataprivacy_maskingrule) | Update information about a masking rule.|
|[**post_dataprivacy_maskingrules**](#post_dataprivacy_maskingrules) | Create a new masking rule resource.|
|[**post_dataprivacy_maskingrules_validate**](#post_dataprivacy_maskingrules_validate) | Validate masking before creating.|



## delete_dataprivacy_maskingrule

>  delete_dataprivacy_maskingrule(rule_id)


Delete a masking rule.

Wraps DELETE /api/v2/dataprivacy/maskingrules/{ruleId} 

Requires ALL permissions: 

* dataprivacy:maskingrule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataPrivacyApi()
rule_id = 'rule_id_example' # str | ruleId

try:
    # Delete a masking rule.
    api_instance.delete_dataprivacy_maskingrule(rule_id)
except ApiException as e:
    print("Exception when calling DataPrivacyApi->delete_dataprivacy_maskingrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| ruleId |  |

### Return type

void (empty response body)


## get_dataprivacy_maskingrule

> [**MaskingRule**](MaskingRule) get_dataprivacy_maskingrule(rule_id)


Fetch details about a masking rule.

Wraps GET /api/v2/dataprivacy/maskingrules/{ruleId} 

Requires ALL permissions: 

* dataprivacy:maskingrule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataPrivacyApi()
rule_id = 'rule_id_example' # str | ruleId

try:
    # Fetch details about a masking rule.
    api_response = api_instance.get_dataprivacy_maskingrule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPrivacyApi->get_dataprivacy_maskingrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| ruleId |  |

### Return type

[**MaskingRule**](MaskingRule)


## get_dataprivacy_maskingrules

> [**MaskingRuleListing**](MaskingRuleListing) get_dataprivacy_maskingrules()


Retrieve the list of masking rules.

Wraps GET /api/v2/dataprivacy/maskingrules 

Requires ALL permissions: 

* dataprivacy:maskingrule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataPrivacyApi()

try:
    # Retrieve the list of masking rules.
    api_response = api_instance.get_dataprivacy_maskingrules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPrivacyApi->get_dataprivacy_maskingrules: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**MaskingRuleListing**](MaskingRuleListing)


## patch_dataprivacy_maskingrule

> [**MaskingRule**](MaskingRule) patch_dataprivacy_maskingrule(rule_id, body=body)


Update information about a masking rule.

Wraps PATCH /api/v2/dataprivacy/maskingrules/{ruleId} 

Requires ALL permissions: 

* dataprivacy:maskingrule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataPrivacyApi()
rule_id = 'rule_id_example' # str | ruleId
body = PureCloudPlatformClientV2.MaskingRule() # MaskingRule |  (optional)

try:
    # Update information about a masking rule.
    api_response = api_instance.patch_dataprivacy_maskingrule(rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPrivacyApi->patch_dataprivacy_maskingrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **rule_id** | **str**| ruleId |  |
| **body** | [**MaskingRule**](MaskingRule)|  | [optional]  |

### Return type

[**MaskingRule**](MaskingRule)


## post_dataprivacy_maskingrules

> [**MaskingRule**](MaskingRule) post_dataprivacy_maskingrules(body)


Create a new masking rule resource.

Wraps POST /api/v2/dataprivacy/maskingrules 

Requires ALL permissions: 

* dataprivacy:maskingrule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataPrivacyApi()
body = PureCloudPlatformClientV2.MaskingRule() # MaskingRule | Details for creating masking rule resource

try:
    # Create a new masking rule resource.
    api_response = api_instance.post_dataprivacy_maskingrules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPrivacyApi->post_dataprivacy_maskingrules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MaskingRule**](MaskingRule)| Details for creating masking rule resource |  |

### Return type

[**MaskingRule**](MaskingRule)


## post_dataprivacy_maskingrules_validate

> [**MaskingRuleValidateResponse**](MaskingRuleValidateResponse) post_dataprivacy_maskingrules_validate(body)


Validate masking before creating.

Wraps POST /api/v2/dataprivacy/maskingrules/validate 

Requires ALL permissions: 

* dataprivacy:maskingrule:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataPrivacyApi()
body = PureCloudPlatformClientV2.MaskingRuleValidateRequest() # MaskingRuleValidateRequest | Text to be masked

try:
    # Validate masking before creating.
    api_response = api_instance.post_dataprivacy_maskingrules_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPrivacyApi->post_dataprivacy_maskingrules_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MaskingRuleValidateRequest**](MaskingRuleValidateRequest)| Text to be masked |  |

### Return type

[**MaskingRuleValidateResponse**](MaskingRuleValidateResponse)


_PureCloudPlatformClientV2 225.0.0_
