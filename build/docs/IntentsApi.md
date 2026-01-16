# IntentsApi

## PureCloudPlatformClientV2.IntentsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_intents_category**](#delete_intents_category) | Delete category for categoryId|
|[**delete_intents_customerintent**](#delete_intents_customerintent) | Delete customer intent for customerIntentId|
|[**get_intents_assignments_externalcontact**](#get_intents_assignments_externalcontact) | Get customer intent assignments for externalContactId|
|[**get_intents_categories**](#get_intents_categories) | Get categories|
|[**get_intents_category**](#get_intents_category) | Get category for categoryId|
|[**get_intents_customerintent**](#get_intents_customerintent) | Get customer intent for customerIntentId|
|[**get_intents_customerintent_sourceintents**](#get_intents_customerintent_sourceintents) | Get source intents mapped to a customer intent|
|[**get_intents_customerintents**](#get_intents_customerintents) | Get customer intents|
|[**get_intents_sourceintents**](#get_intents_sourceintents) | Get all mapped source intents by type. If no type selected default is type Segment|
|[**patch_intents_category**](#patch_intents_category) | Patch category for categoryId|
|[**patch_intents_customerintent**](#patch_intents_customerintent) | Patch customer intent for customerIntentId|
|[**post_intents_assignments_externalcontact_customerintent_assignment**](#post_intents_assignments_externalcontact_customerintent_assignment) | Create customer intent assignment for external contact|
|[**post_intents_categories**](#post_intents_categories) | Create category|
|[**post_intents_customerintent_sourceintents_bulk_add**](#post_intents_customerintent_sourceintents_bulk_add) | Bulk add source intents to a customer intent|
|[**post_intents_customerintent_sourceintents_bulk_remove**](#post_intents_customerintent_sourceintents_bulk_remove) | Bulk remove source intents mapped to a customer intent|
|[**post_intents_customerintents**](#post_intents_customerintents) | Create customer intents|



## delete_intents_category

>  delete_intents_category(category_id)


Delete category for categoryId

Wraps DELETE /api/v2/intents/categories/{categoryId} 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
category_id = 'category_id_example' # str | Category id

try:
    # Delete category for categoryId
    api_instance.delete_intents_category(category_id)
except ApiException as e:
    print("Exception when calling IntentsApi->delete_intents_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category id |  |

### Return type

void (empty response body)


## delete_intents_customerintent

>  delete_intents_customerintent(customer_intent_id)


Delete customer intent for customerIntentId

Wraps DELETE /api/v2/intents/customerintents/{customerIntentId} 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id

try:
    # Delete customer intent for customerIntentId
    api_instance.delete_intents_customerintent(customer_intent_id)
except ApiException as e:
    print("Exception when calling IntentsApi->delete_intents_customerintent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_intent_id** | **str**| Customer Intent id |  |

### Return type

void (empty response body)


## get_intents_assignments_externalcontact

> [**CustomerIntentAssignmentListing**](CustomerIntentAssignmentListing) get_intents_assignments_externalcontact(external_contact_id, page_size=page_size, page_number=page_number)


Get customer intent assignments for externalContactId

Wraps GET /api/v2/intents/assignments/externalcontacts/{externalContactId} 

Requires ANY permissions: 

* externalContacts:customerIntentAssignments:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
external_contact_id = 'external_contact_id_example' # str | External Contact id
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)

try:
    # Get customer intent assignments for externalContactId
    api_response = api_instance.get_intents_assignments_externalcontact(external_contact_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_assignments_externalcontact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_contact_id** | **str**| External Contact id |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |

### Return type

[**CustomerIntentAssignmentListing**](CustomerIntentAssignmentListing)


## get_intents_categories

> [**IntentsCategoryListing**](IntentsCategoryListing) get_intents_categories(page_size=page_size, page_number=page_number, query_value=query_value)


Get categories

Wraps GET /api/v2/intents/categories 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
query_value = 'query_value_example' # str | Search query value to filter results by (optional)

try:
    # Get categories
    api_response = api_instance.get_intents_categories(page_size=page_size, page_number=page_number, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **query_value** | **str**| Search query value to filter results by | [optional]  |

### Return type

[**IntentsCategoryListing**](IntentsCategoryListing)


## get_intents_category

> [**IntentsCategory**](IntentsCategory) get_intents_category(category_id)


Get category for categoryId

Wraps GET /api/v2/intents/categories/{categoryId} 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
category_id = 'category_id_example' # str | Category id

try:
    # Get category for categoryId
    api_response = api_instance.get_intents_category(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category id |  |

### Return type

[**IntentsCategory**](IntentsCategory)


## get_intents_customerintent

> [**CustomerIntentResponse**](CustomerIntentResponse) get_intents_customerintent(customer_intent_id)


Get customer intent for customerIntentId

Wraps GET /api/v2/intents/customerintents/{customerIntentId} 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id

try:
    # Get customer intent for customerIntentId
    api_response = api_instance.get_intents_customerintent(customer_intent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_customerintent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_intent_id** | **str**| Customer Intent id |  |

### Return type

[**CustomerIntentResponse**](CustomerIntentResponse)


## get_intents_customerintent_sourceintents

> [**CustomerSourceIntentListing**](CustomerSourceIntentListing) get_intents_customerintent_sourceintents(customer_intent_id, page_size=page_size, page_number=page_number, query_value=query_value)


Get source intents mapped to a customer intent

Wraps GET /api/v2/intents/customerintents/{customerIntentId}/sourceintents 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
query_value = 'query_value_example' # str | Search query value to filter results by (optional)

try:
    # Get source intents mapped to a customer intent
    api_response = api_instance.get_intents_customerintent_sourceintents(customer_intent_id, page_size=page_size, page_number=page_number, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_customerintent_sourceintents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_intent_id** | **str**| Customer Intent id |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **query_value** | **str**| Search query value to filter results by | [optional]  |

### Return type

[**CustomerSourceIntentListing**](CustomerSourceIntentListing)


## get_intents_customerintents

> [**CustomerIntentListing**](CustomerIntentListing) get_intents_customerintents(page_size=page_size, page_number=page_number, query_value=query_value, category_id=category_id)


Get customer intents

Wraps GET /api/v2/intents/customerintents 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
query_value = 'query_value_example' # str | Search query value to filter results by (optional)
category_id = 'category_id_example' # str | CategoryId to filter query by (optional)

try:
    # Get customer intents
    api_response = api_instance.get_intents_customerintents(page_size=page_size, page_number=page_number, query_value=query_value, category_id=category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_customerintents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **query_value** | **str**| Search query value to filter results by | [optional]  |
| **category_id** | **str**| CategoryId to filter query by | [optional]  |

### Return type

[**CustomerIntentListing**](CustomerIntentListing)


## get_intents_sourceintents

> [**CustomerSourceIntentListing**](CustomerSourceIntentListing) get_intents_sourceintents(page_size=page_size, page_number=page_number, type=type, source_id=source_id)


Get all mapped source intents by type. If no type selected default is type Segment

Wraps GET /api/v2/intents/sourceintents 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
type = 'type_example' # str | Source Type to query by. If none selected default response will be for type Segment. (optional)
source_id = 'source_id_example' # str | Source Id to query by. Only required for sourceType: Copilot, Bot, Digitalbot (optional)

try:
    # Get all mapped source intents by type. If no type selected default is type Segment
    api_response = api_instance.get_intents_sourceintents(page_size=page_size, page_number=page_number, type=type, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->get_intents_sourceintents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **type** | **str**| Source Type to query by. If none selected default response will be for type Segment. | [optional] <br />**Values**: Bot, Copilot, Digitalbot, Segment, Topic, Unknown |
| **source_id** | **str**| Source Id to query by. Only required for sourceType: Copilot, Bot, Digitalbot | [optional]  |

### Return type

[**CustomerSourceIntentListing**](CustomerSourceIntentListing)


## patch_intents_category

> [**IntentsCategory**](IntentsCategory) patch_intents_category(category_id, body)


Patch category for categoryId

Wraps PATCH /api/v2/intents/categories/{categoryId} 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
category_id = 'category_id_example' # str | Category id
body = PureCloudPlatformClientV2.IntentsCategoryPatch() # IntentsCategoryPatch | category

try:
    # Patch category for categoryId
    api_response = api_instance.patch_intents_category(category_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->patch_intents_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category id |  |
| **body** | [**IntentsCategoryPatch**](IntentsCategoryPatch)| category |  |

### Return type

[**IntentsCategory**](IntentsCategory)


## patch_intents_customerintent

> [**CustomerIntentResponse**](CustomerIntentResponse) patch_intents_customerintent(customer_intent_id, body)


Patch customer intent for customerIntentId

Wraps PATCH /api/v2/intents/customerintents/{customerIntentId} 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id
body = PureCloudPlatformClientV2.CustomerIntentPatch() # CustomerIntentPatch | Customer intent

try:
    # Patch customer intent for customerIntentId
    api_response = api_instance.patch_intents_customerintent(customer_intent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->patch_intents_customerintent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_intent_id** | **str**| Customer Intent id |  |
| **body** | [**CustomerIntentPatch**](CustomerIntentPatch)| Customer intent |  |

### Return type

[**CustomerIntentResponse**](CustomerIntentResponse)


## post_intents_assignments_externalcontact_customerintent_assignment

> [**CustomerIntentAssignmentResponse**](CustomerIntentAssignmentResponse) post_intents_assignments_externalcontact_customerintent_assignment(external_contact_id, customer_intent_id, body)


Create customer intent assignment for external contact

Wraps POST /api/v2/intents/assignments/externalcontacts/{externalContactId}/customerintents/{customerIntentId}/assignment 

Requires ANY permissions: 

* externalContacts:customerIntentAssignments:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
external_contact_id = 'external_contact_id_example' # str | External Contact id
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id
body = PureCloudPlatformClientV2.CustomerIntentAssignmentRequest() # CustomerIntentAssignmentRequest | Customer intent assignment

try:
    # Create customer intent assignment for external contact
    api_response = api_instance.post_intents_assignments_externalcontact_customerintent_assignment(external_contact_id, customer_intent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->post_intents_assignments_externalcontact_customerintent_assignment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_contact_id** | **str**| External Contact id |  |
| **customer_intent_id** | **str**| Customer Intent id |  |
| **body** | [**CustomerIntentAssignmentRequest**](CustomerIntentAssignmentRequest)| Customer intent assignment |  |

### Return type

[**CustomerIntentAssignmentResponse**](CustomerIntentAssignmentResponse)


## post_intents_categories

> [**IntentsCategory**](IntentsCategory) post_intents_categories(body)


Create category

Wraps POST /api/v2/intents/categories 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
body = PureCloudPlatformClientV2.IntentsCategory() # IntentsCategory | category

try:
    # Create category
    api_response = api_instance.post_intents_categories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->post_intents_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IntentsCategory**](IntentsCategory)| category |  |

### Return type

[**IntentsCategory**](IntentsCategory)


## post_intents_customerintent_sourceintents_bulk_add

> [**BulkSourceIntentsResponse**](BulkSourceIntentsResponse) post_intents_customerintent_sourceintents_bulk_add(customer_intent_id, body)


Bulk add source intents to a customer intent

Wraps POST /api/v2/intents/customerintents/{customerIntentId}/sourceintents/bulk/add 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id
body = PureCloudPlatformClientV2.BulkAddSourceIntentsRequest() # BulkAddSourceIntentsRequest | Source intents to be added

try:
    # Bulk add source intents to a customer intent
    api_response = api_instance.post_intents_customerintent_sourceintents_bulk_add(customer_intent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->post_intents_customerintent_sourceintents_bulk_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_intent_id** | **str**| Customer Intent id |  |
| **body** | [**BulkAddSourceIntentsRequest**](BulkAddSourceIntentsRequest)| Source intents to be added |  |

### Return type

[**BulkSourceIntentsResponse**](BulkSourceIntentsResponse)


## post_intents_customerintent_sourceintents_bulk_remove

> [**BulkSourceIntentsResponse**](BulkSourceIntentsResponse) post_intents_customerintent_sourceintents_bulk_remove(customer_intent_id, body)


Bulk remove source intents mapped to a customer intent

Wraps POST /api/v2/intents/customerintents/{customerIntentId}/sourceintents/bulk/remove 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
customer_intent_id = 'customer_intent_id_example' # str | Customer Intent id
body = PureCloudPlatformClientV2.BulkRemoveSourceIntentsRequest() # BulkRemoveSourceIntentsRequest | Source intents to be removed

try:
    # Bulk remove source intents mapped to a customer intent
    api_response = api_instance.post_intents_customerintent_sourceintents_bulk_remove(customer_intent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->post_intents_customerintent_sourceintents_bulk_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_intent_id** | **str**| Customer Intent id |  |
| **body** | [**BulkRemoveSourceIntentsRequest**](BulkRemoveSourceIntentsRequest)| Source intents to be removed |  |

### Return type

[**BulkSourceIntentsResponse**](BulkSourceIntentsResponse)


## post_intents_customerintents

> [**CustomerIntentResponse**](CustomerIntentResponse) post_intents_customerintents(body)


Create customer intents

Wraps POST /api/v2/intents/customerintents 

Requires ANY permissions: 

* externalContacts:customerIntentTaxonomy:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IntentsApi()
body = PureCloudPlatformClientV2.CustomerIntent() # CustomerIntent | Customer intent

try:
    # Create customer intents
    api_response = api_instance.post_intents_customerintents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentsApi->post_intents_customerintents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CustomerIntent**](CustomerIntent)| Customer intent |  |

### Return type

[**CustomerIntentResponse**](CustomerIntentResponse)


_PureCloudPlatformClientV2 248.0.0_
