# TelephonyApi

## PureCloudPlatformClientV2.TelephonyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_telephony_mediaregions**](#get_telephony_mediaregions) | Retrieve the list of AWS regions media can stream through.|
|[**get_telephony_sipmessages_conversation**](#get_telephony_sipmessages_conversation) | Get a SIP message.|
|[**get_telephony_sipmessages_conversation_headers**](#get_telephony_sipmessages_conversation_headers) | Get SIP headers.|
|[**get_telephony_siptraces**](#get_telephony_siptraces) | Fetch SIP metadata|
|[**get_telephony_siptraces_download_download_id**](#get_telephony_siptraces_download_download_id) | Get signed S3 URL for a pcap download|
|[**post_telephony_siptraces_download**](#post_telephony_siptraces_download) | Request a download of a pcap file to S3|



## get_telephony_mediaregions

> [**MediaRegions**](MediaRegions) get_telephony_mediaregions()


Retrieve the list of AWS regions media can stream through.

Wraps GET /api/v2/telephony/mediaregions 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()

try:
    # Retrieve the list of AWS regions media can stream through.
    api_response = api_instance.get_telephony_mediaregions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_mediaregions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**MediaRegions**](MediaRegions)


## get_telephony_sipmessages_conversation

> [**Callmessage**](Callmessage) get_telephony_sipmessages_conversation(conversation_id)


Get a SIP message.

Get the raw form of the SIP message

Wraps GET /api/v2/telephony/sipmessages/conversations/{conversationId} 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
conversation_id = 'conversation_id_example' # str | Conversation id

try:
    # Get a SIP message.
    api_response = api_instance.get_telephony_sipmessages_conversation(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_sipmessages_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation id |  |

### Return type

[**Callmessage**](Callmessage)


## get_telephony_sipmessages_conversation_headers

> [**Callheader**](Callheader) get_telephony_sipmessages_conversation_headers(conversation_id, keys=keys)


Get SIP headers.

Get parsed SIP headers. Returns specific headers if key query parameters are added.

Wraps GET /api/v2/telephony/sipmessages/conversations/{conversationId}/headers 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
conversation_id = 'conversation_id_example' # str | Conversation id
keys = ['keys_example'] # list[str] | comma-separated list of header identifiers to query. e.g. ruri,to,from (optional)

try:
    # Get SIP headers.
    api_response = api_instance.get_telephony_sipmessages_conversation_headers(conversation_id, keys=keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_sipmessages_conversation_headers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation id |  |
| **keys** | [**list[str]**](str)| comma-separated list of header identifiers to query. e.g. ruri,to,from | [optional]  |

### Return type

[**Callheader**](Callheader)


## get_telephony_siptraces

> [**SipSearchResult**](SipSearchResult) get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)


Fetch SIP metadata

Fetch SIP metadata that matches a given parameter. If exactMatch is passed as a parameter only sip records that have exactly that value will be returned. For example, some records contain conversationId but not all relevant records for that call may contain the conversationId so only a partial view of the call will be reflected

Wraps GET /api/v2/telephony/siptraces 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
date_start = '2013-10-20T19:20:30+01:00' # datetime | Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
date_end = '2013-10-20T19:20:30+01:00' # datetime | End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
call_id = 'call_id_example' # str | unique identification of the placed call (optional)
to_user = 'to_user_example' # str | User to who the call was placed (optional)
from_user = 'from_user_example' # str | user who placed the call (optional)
conversation_id = 'conversation_id_example' # str | Unique identification of the conversation (optional)

try:
    # Fetch SIP metadata
    api_response = api_instance.get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **date_start** | **datetime**| Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **date_end** | **datetime**| End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **call_id** | **str**| unique identification of the placed call | [optional]  |
| **to_user** | **str**| User to who the call was placed | [optional]  |
| **from_user** | **str**| user who placed the call | [optional]  |
| **conversation_id** | **str**| Unique identification of the conversation | [optional]  |

### Return type

[**SipSearchResult**](SipSearchResult)


## get_telephony_siptraces_download_download_id

> [**SignedUrlResponse**](SignedUrlResponse) get_telephony_siptraces_download_download_id(download_id)


Get signed S3 URL for a pcap download

Wraps GET /api/v2/telephony/siptraces/download/{downloadId} 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
download_id = 'download_id_example' # str | unique id for the downloaded file in S3

try:
    # Get signed S3 URL for a pcap download
    api_response = api_instance.get_telephony_siptraces_download_download_id(download_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces_download_download_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **download_id** | **str**| unique id for the downloaded file in S3 |  |

### Return type

[**SignedUrlResponse**](SignedUrlResponse)


## post_telephony_siptraces_download

> [**SipDownloadResponse**](SipDownloadResponse) post_telephony_siptraces_download(sip_search_public_request)


Request a download of a pcap file to S3

Wraps POST /api/v2/telephony/siptraces/download 

Requires ALL permissions: 

* telephony:pcap:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
sip_search_public_request = PureCloudPlatformClientV2.SIPSearchPublicRequest() # SIPSearchPublicRequest | 

try:
    # Request a download of a pcap file to S3
    api_response = api_instance.post_telephony_siptraces_download(sip_search_public_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_siptraces_download: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sip_search_public_request** | [**SIPSearchPublicRequest**](SIPSearchPublicRequest)|  |  |

### Return type

[**SipDownloadResponse**](SipDownloadResponse)


_PureCloudPlatformClientV2 227.0.0_
