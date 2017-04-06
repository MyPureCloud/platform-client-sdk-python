---
title: RecordingApi
---

## PureCloudPlatformClientV2.RecordingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_conversation_recording_annotation**](RecordingApi.html#delete_conversation_recording_annotation) | Delete annotation|
|[**delete_orphanrecording**](RecordingApi.html#delete_orphanrecording) | Deletes a single orphan recording|
|[**delete_recording_mediaretentionpolicies**](RecordingApi.html#delete_recording_mediaretentionpolicies) | Delete media retention policies|
|[**delete_recording_mediaretentionpolicy**](RecordingApi.html#delete_recording_mediaretentionpolicy) | Delete a media retention policy|
|[**get_conversation_recording**](RecordingApi.html#get_conversation_recording) | Gets a specific recording.|
|[**get_conversation_recording_annotation**](RecordingApi.html#get_conversation_recording_annotation) | Get annotation|
|[**get_conversation_recording_annotations**](RecordingApi.html#get_conversation_recording_annotations) | Get annotations for recording|
|[**get_conversation_recordings**](RecordingApi.html#get_conversation_recordings) | Get all of a Conversation&#39;s Recordings.|
|[**get_orphanrecording**](RecordingApi.html#get_orphanrecording) | Gets a single orphan recording|
|[**get_orphanrecording_media**](RecordingApi.html#get_orphanrecording_media) | Gets the media of a single orphan recording|
|[**get_orphanrecordings**](RecordingApi.html#get_orphanrecordings) | Gets all orphan recordings|
|[**get_recording_localkeys_setting**](RecordingApi.html#get_recording_localkeys_setting) | Get the local encryption settings|
|[**get_recording_localkeys_settings**](RecordingApi.html#get_recording_localkeys_settings) | gets a list local key settings data|
|[**get_recording_mediaretentionpolicies**](RecordingApi.html#get_recording_mediaretentionpolicies) | Gets media retention policy list with query options to filter on name and enabled.|
|[**get_recording_mediaretentionpolicy**](RecordingApi.html#get_recording_mediaretentionpolicy) | Get a media retention policy|
|[**get_recording_recordingkeys**](RecordingApi.html#get_recording_recordingkeys) | Get encryption key list|
|[**get_recording_recordingkeys_rotationschedule**](RecordingApi.html#get_recording_recordingkeys_rotationschedule) | Get key rotation schedule|
|[**get_recording_settings**](RecordingApi.html#get_recording_settings) | Get the Recording Settings for the Organization|
|[**get_recordings_screensessions**](RecordingApi.html#get_recordings_screensessions) | Retrieves a paged listing of screen recording sessions|
|[**patch_recording_mediaretentionpolicy**](RecordingApi.html#patch_recording_mediaretentionpolicy) | Patch a media retention policy|
|[**patch_recordings_screensession**](RecordingApi.html#patch_recordings_screensession) | Update a screen recording session|
|[**post_conversation_recording_annotations**](RecordingApi.html#post_conversation_recording_annotations) | Create annotation|
|[**post_recording_localkeys**](RecordingApi.html#post_recording_localkeys) | create a local recording key|
|[**post_recording_localkeys_settings**](RecordingApi.html#post_recording_localkeys_settings) | create settings for local key creation|
|[**post_recording_mediaretentionpolicies**](RecordingApi.html#post_recording_mediaretentionpolicies) | Create media retention policy|
|[**post_recording_recordingkeys**](RecordingApi.html#post_recording_recordingkeys) | Create encryption key|
|[**put_conversation_recording**](RecordingApi.html#put_conversation_recording) | Updates the retention records on a recording.|
|[**put_conversation_recording_annotation**](RecordingApi.html#put_conversation_recording_annotation) | Update annotation|
|[**put_orphanrecording**](RecordingApi.html#put_orphanrecording) | Updates an orphan recording to a regular recording with retention values|
|[**put_recording_localkeys_setting**](RecordingApi.html#put_recording_localkeys_setting) | Update the local encryption settings|
|[**put_recording_mediaretentionpolicy**](RecordingApi.html#put_recording_mediaretentionpolicy) | Update a media retention policy|
|[**put_recording_recordingkeys_rotationschedule**](RecordingApi.html#put_recording_recordingkeys_rotationschedule) | Update key rotation schedule|
|[**put_recording_settings**](RecordingApi.html#put_recording_settings) | Update the Recording Settings for the Organization|
{: class="table table-striped"}

<a name="delete_conversation_recording_annotation"></a>

## delete_conversation_recording_annotation(conversation_id, recording_id, annotation_id)

Delete annotation



Wraps DELETE /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations/{annotationId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
annotation_id = 'annotation_id_example' # str | Annotation ID

try:
    # Delete annotation
    api_instance.delete_conversation_recording_annotation(conversation_id, recording_id, annotation_id)
except ApiException as e:
    print "Exception when calling RecordingApi->delete_conversation_recording_annotation: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
| **annotation_id** | **str**| Annotation ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_orphanrecording"></a>

## [**OrphanRecording**](OrphanRecording.html)delete_orphanrecording(orphan_id)

Deletes a single orphan recording



Wraps DELETE /api/v2/orphanrecordings/{orphanId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID

try:
    # Deletes a single orphan recording
    api_response = api_instance.delete_orphanrecording(orphan_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->delete_orphanrecording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID | |
{: class="table table-striped"}

### Return type

[**OrphanRecording**](OrphanRecording.html)

<a name="delete_recording_mediaretentionpolicies"></a>

## str**delete_recording_mediaretentionpolicies(ids)

Delete media retention policies

Bulk delete of media retention policies, this will only delete the polices that match the ids specified in the query param.

Wraps DELETE /api/v2/recording/mediaretentionpolicies 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
ids = 'ids_example' # str | 

try:
    # Delete media retention policies
    api_response = api_instance.delete_recording_mediaretentionpolicies(ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->delete_recording_mediaretentionpolicies: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ids** | **str**|  | |
{: class="table table-striped"}

### Return type

**str**

<a name="delete_recording_mediaretentionpolicy"></a>

## str**delete_recording_mediaretentionpolicy(policy_id)

Delete a media retention policy



Wraps DELETE /api/v2/recording/mediaretentionpolicies/{policyId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID

try:
    # Delete a media retention policy
    api_response = api_instance.delete_recording_mediaretentionpolicy(policy_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->delete_recording_mediaretentionpolicy: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID | |
{: class="table table-striped"}

### Return type

**str**

<a name="get_conversation_recording"></a>

## [**Recording**](Recording.html)get_conversation_recording(conversation_id, recording_id, format_id=format_id, download=download, file_name=file_name)

Gets a specific recording.



Wraps GET /api/v2/conversations/{conversationId}/recordings/{recordingId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
format_id = 'WEBM' # str | The desired media format. (optional) (default to WEBM)
download = false # bool | requesting a download format of the recording (optional) (default to false)
file_name = 'file_name_example' # str | the name of the downloaded fileName (optional)

try:
    # Gets a specific recording.
    api_response = api_instance.get_conversation_recording(conversation_id, recording_id, format_id=format_id, download=download, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_conversation_recording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
| **format_id** | **str**| The desired media format. | [optional] [default to WEBM]|
| **download** | **bool**| requesting a download format of the recording | [optional] [default to false]|
| **file_name** | **str**| the name of the downloaded fileName | [optional] |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="get_conversation_recording_annotation"></a>

## [**Annotation**](Annotation.html)get_conversation_recording_annotation(conversation_id, recording_id, annotation_id)

Get annotation



Wraps GET /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations/{annotationId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
annotation_id = 'annotation_id_example' # str | Annotation ID

try:
    # Get annotation
    api_response = api_instance.get_conversation_recording_annotation(conversation_id, recording_id, annotation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_conversation_recording_annotation: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
| **annotation_id** | **str**| Annotation ID | |
{: class="table table-striped"}

### Return type

[**Annotation**](Annotation.html)

<a name="get_conversation_recording_annotations"></a>

## [**list[Annotation]**](Annotation.html)get_conversation_recording_annotations(conversation_id, recording_id)

Get annotations for recording



Wraps GET /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID

try:
    # Get annotations for recording
    api_response = api_instance.get_conversation_recording_annotations(conversation_id, recording_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_conversation_recording_annotations: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
{: class="table table-striped"}

### Return type

[**list[Annotation]**](Annotation.html)

<a name="get_conversation_recordings"></a>

## [**list[Recording]**](Recording.html)get_conversation_recordings(conversation_id, max_wait_ms=max_wait_ms, format_id=format_id)

Get all of a Conversation's Recordings.



Wraps GET /api/v2/conversations/{conversationId}/recordings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
max_wait_ms = 5000 # int | The maximum number of milliseconds to wait for the recording to be ready. Must be a positive value. (optional) (default to 5000)
format_id = 'WEBM' # str | The desired media format (optional) (default to WEBM)

try:
    # Get all of a Conversation's Recordings.
    api_response = api_instance.get_conversation_recordings(conversation_id, max_wait_ms=max_wait_ms, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_conversation_recordings: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **max_wait_ms** | **int**| The maximum number of milliseconds to wait for the recording to be ready. Must be a positive value. | [optional] [default to 5000]|
| **format_id** | **str**| The desired media format | [optional] [default to WEBM]|
{: class="table table-striped"}

### Return type

[**list[Recording]**](Recording.html)

<a name="get_orphanrecording"></a>

## [**OrphanRecording**](OrphanRecording.html)get_orphanrecording(orphan_id)

Gets a single orphan recording



Wraps GET /api/v2/orphanrecordings/{orphanId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID

try:
    # Gets a single orphan recording
    api_response = api_instance.get_orphanrecording(orphan_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_orphanrecording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID | |
{: class="table table-striped"}

### Return type

[**OrphanRecording**](OrphanRecording.html)

<a name="get_orphanrecording_media"></a>

## [**Recording**](Recording.html)get_orphanrecording_media(orphan_id, format_id=format_id, download=download, file_name=file_name)

Gets the media of a single orphan recording

A 202 response means the orphaned media is currently transcoding and will be available shortly.A 200 response denotes the transcoded orphan media is available now and is contained in the response body.

Wraps GET /api/v2/orphanrecordings/{orphanId}/media 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID
format_id = 'WEBM' # str | The desired media format. (optional) (default to WEBM)
download = false # bool | requesting a download format of the recording (optional) (default to false)
file_name = 'file_name_example' # str | the name of the downloaded fileName (optional)

try:
    # Gets the media of a single orphan recording
    api_response = api_instance.get_orphanrecording_media(orphan_id, format_id=format_id, download=download, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_orphanrecording_media: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID | |
| **format_id** | **str**| The desired media format. | [optional] [default to WEBM]|
| **download** | **bool**| requesting a download format of the recording | [optional] [default to false]|
| **file_name** | **str**| the name of the downloaded fileName | [optional] |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="get_orphanrecordings"></a>

## [**OrphanRecordingListing**](OrphanRecordingListing.html)get_orphanrecordings(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, has_conversation=has_conversation)

Gets all orphan recordings



Wraps GET /api/v2/orphanrecordings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = NULL # list[object] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
has_conversation = false # bool | Filter resulting orphans by whether the conversation is known. False returns all orphans for the organization. (optional) (default to false)

try:
    # Gets all orphan recordings
    api_response = api_instance.get_orphanrecordings(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, has_conversation=has_conversation)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_orphanrecordings: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25]|
| **page_number** | **int**| The page number requested | [optional] [default to 1]|
| **sort_by** | **str**| variable name requested to sort by | [optional] |
| **expand** | [**list[object]**](object.html)| variable name requested by expand list | [optional] |
| **next_page** | **str**| next page token | [optional] |
| **previous_page** | **str**| Previous page token | [optional] |
| **has_conversation** | **bool**| Filter resulting orphans by whether the conversation is known. False returns all orphans for the organization. | [optional] [default to false]|
{: class="table table-striped"}

### Return type

[**OrphanRecordingListing**](OrphanRecordingListing.html)

<a name="get_recording_localkeys_setting"></a>

## [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)get_recording_localkeys_setting(settings_id)

Get the local encryption settings



Wraps GET /api/v2/recording/localkeys/settings/{settingsId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
settings_id = 'settings_id_example' # str | Settings Id

try:
    # Get the local encryption settings
    api_response = api_instance.get_recording_localkeys_setting(settings_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_localkeys_setting: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings Id | |
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)

<a name="get_recording_localkeys_settings"></a>

## [**LocalEncryptionConfigurationListing**](LocalEncryptionConfigurationListing.html)get_recording_localkeys_settings()

gets a list local key settings data



Wraps GET /api/v2/recording/localkeys/settings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # gets a list local key settings data
    api_response = api_instance.get_recording_localkeys_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_localkeys_settings: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfigurationListing**](LocalEncryptionConfigurationListing.html)

<a name="get_recording_mediaretentionpolicies"></a>

## [**PolicyEntityListing**](PolicyEntityListing.html)get_recording_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors)

Gets media retention policy list with query options to filter on name and enabled.

for a less verbose response, add summary=true to this endpoint

Wraps GET /api/v2/recording/mediaretentionpolicies 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = NULL # list[object] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
name = 'name_example' # str | the policy name - used for filtering results in searches. (optional)
enabled = true # bool | checks to see if policy is enabled - use enabled = true or enabled = false (optional)
summary = false # bool | provides a less verbose response of policy lists. (optional) (default to false)
has_errors = true # bool | provides a way to fetch all policies with errors or policies that do not have errors (optional)

try:
    # Gets media retention policy list with query options to filter on name and enabled.
    api_response = api_instance.get_recording_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_mediaretentionpolicies: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25]|
| **page_number** | **int**| The page number requested | [optional] [default to 1]|
| **sort_by** | **str**| variable name requested to sort by | [optional] |
| **expand** | [**list[object]**](object.html)| variable name requested by expand list | [optional] |
| **next_page** | **str**| next page token | [optional] |
| **previous_page** | **str**| Previous page token | [optional] |
| **name** | **str**| the policy name - used for filtering results in searches. | [optional] |
| **enabled** | **bool**| checks to see if policy is enabled - use enabled &#x3D; true or enabled &#x3D; false | [optional] |
| **summary** | **bool**| provides a less verbose response of policy lists. | [optional] [default to false]|
| **has_errors** | **bool**| provides a way to fetch all policies with errors or policies that do not have errors | [optional] |
{: class="table table-striped"}

### Return type

[**PolicyEntityListing**](PolicyEntityListing.html)

<a name="get_recording_mediaretentionpolicy"></a>

## [**Policy**](Policy.html)get_recording_mediaretentionpolicy(policy_id)

Get a media retention policy



Wraps GET /api/v2/recording/mediaretentionpolicies/{policyId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID

try:
    # Get a media retention policy
    api_response = api_instance.get_recording_mediaretentionpolicy(policy_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_mediaretentionpolicy: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID | |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="get_recording_recordingkeys"></a>

## [**EncryptionKeyEntityListing**](EncryptionKeyEntityListing.html)get_recording_recordingkeys(page_size=page_size, page_number=page_number)

Get encryption key list



Wraps GET /api/v2/recording/recordingkeys 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get encryption key list
    api_response = api_instance.get_recording_recordingkeys(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_recordingkeys: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
{: class="table table-striped"}

### Return type

[**EncryptionKeyEntityListing**](EncryptionKeyEntityListing.html)

<a name="get_recording_recordingkeys_rotationschedule"></a>

## [**KeyRotationSchedule**](KeyRotationSchedule.html)get_recording_recordingkeys_rotationschedule()

Get key rotation schedule



Wraps GET /api/v2/recording/recordingkeys/rotationschedule 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # Get key rotation schedule
    api_response = api_instance.get_recording_recordingkeys_rotationschedule()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_recordingkeys_rotationschedule: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**KeyRotationSchedule**](KeyRotationSchedule.html)

<a name="get_recording_settings"></a>

## [**RecordingSettings**](RecordingSettings.html)get_recording_settings(create_default=create_default)

Get the Recording Settings for the Organization



Wraps GET /api/v2/recording/settings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
create_default = false # bool | If no settings are found, a new one is created with default values (optional) (default to false)

try:
    # Get the Recording Settings for the Organization
    api_response = api_instance.get_recording_settings(create_default=create_default)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recording_settings: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **create_default** | **bool**| If no settings are found, a new one is created with default values | [optional] [default to false]|
{: class="table table-striped"}

### Return type

[**RecordingSettings**](RecordingSettings.html)

<a name="get_recordings_screensessions"></a>

## [**ScreenRecordingSessionListing**](ScreenRecordingSessionListing.html)get_recordings_screensessions(page_size=page_size, page_number=page_number)

Retrieves a paged listing of screen recording sessions



Wraps GET /api/v2/recordings/screensessions 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Retrieves a paged listing of screen recording sessions
    api_response = api_instance.get_recordings_screensessions(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->get_recordings_screensessions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
{: class="table table-striped"}

### Return type

[**ScreenRecordingSessionListing**](ScreenRecordingSessionListing.html)

<a name="patch_recording_mediaretentionpolicy"></a>

## [**Policy**](Policy.html)patch_recording_mediaretentionpolicy(policy_id, body)

Patch a media retention policy



Wraps PATCH /api/v2/recording/mediaretentionpolicies/{policyId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID
body = PureCloudPlatformClientV2.Policy() # Policy | Policy

try:
    # Patch a media retention policy
    api_response = api_instance.patch_recording_mediaretentionpolicy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->patch_recording_mediaretentionpolicy: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID | |
| **body** | [**Policy**](Policy.html)| Policy | |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="patch_recordings_screensession"></a>

## patch_recordings_screensession(recording_session_id, body=body)

Update a screen recording session



Wraps PATCH /api/v2/recordings/screensessions/{recordingSessionId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
recording_session_id = 'recording_session_id_example' # str | Screen recording session ID
body = PureCloudPlatformClientV2.ScreenRecordingSessionRequest() # ScreenRecordingSessionRequest |  (optional)

try:
    # Update a screen recording session
    api_instance.patch_recordings_screensession(recording_session_id, body=body)
except ApiException as e:
    print "Exception when calling RecordingApi->patch_recordings_screensession: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_session_id** | **str**| Screen recording session ID | |
| **body** | [**ScreenRecordingSessionRequest**](ScreenRecordingSessionRequest.html)|  | [optional] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_recording_annotations"></a>

## [**Annotation**](Annotation.html)post_conversation_recording_annotations(conversation_id, recording_id, body)

Create annotation



Wraps POST /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
body = PureCloudPlatformClientV2.Annotation() # Annotation | annotation

try:
    # Create annotation
    api_response = api_instance.post_conversation_recording_annotations(conversation_id, recording_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->post_conversation_recording_annotations: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
| **body** | [**Annotation**](Annotation.html)| annotation | |
{: class="table table-striped"}

### Return type

[**Annotation**](Annotation.html)

<a name="post_recording_localkeys"></a>

## [**EncryptionKey**](EncryptionKey.html)post_recording_localkeys(body)

create a local recording key



Wraps POST /api/v2/recording/localkeys 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.LocalEncryptionKeyRequest() # LocalEncryptionKeyRequest | Local Encryption body

try:
    # create a local recording key
    api_response = api_instance.post_recording_localkeys(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->post_recording_localkeys: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocalEncryptionKeyRequest**](LocalEncryptionKeyRequest.html)| Local Encryption body | |
{: class="table table-striped"}

### Return type

[**EncryptionKey**](EncryptionKey.html)

<a name="post_recording_localkeys_settings"></a>

## [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)post_recording_localkeys_settings(body)

create settings for local key creation



Wraps POST /api/v2/recording/localkeys/settings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.LocalEncryptionConfiguration() # LocalEncryptionConfiguration | Local Encryption Configuration

try:
    # create settings for local key creation
    api_response = api_instance.post_recording_localkeys_settings(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->post_recording_localkeys_settings: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)| Local Encryption Configuration | |
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)

<a name="post_recording_mediaretentionpolicies"></a>

## [**Policy**](Policy.html)post_recording_mediaretentionpolicies(body)

Create media retention policy



Wraps POST /api/v2/recording/mediaretentionpolicies 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.PolicyCreate() # PolicyCreate | Policy

try:
    # Create media retention policy
    api_response = api_instance.post_recording_mediaretentionpolicies(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->post_recording_mediaretentionpolicies: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PolicyCreate**](PolicyCreate.html)| Policy | |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="post_recording_recordingkeys"></a>

## [**EncryptionKey**](EncryptionKey.html)post_recording_recordingkeys()

Create encryption key



Wraps POST /api/v2/recording/recordingkeys 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # Create encryption key
    api_response = api_instance.post_recording_recordingkeys()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->post_recording_recordingkeys: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**EncryptionKey**](EncryptionKey.html)

<a name="put_conversation_recording"></a>

## [**Recording**](Recording.html)put_conversation_recording(conversation_id, recording_id, body)

Updates the retention records on a recording.

Currently supports updating and removing both archive and delete dates for eligible recordings. A request to change the archival date of an archived recording will result in a restoration of the recording until the new date set. 

Wraps PUT /api/v2/conversations/{conversationId}/recordings/{recordingId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
body = PureCloudPlatformClientV2.Recording() # Recording | recording

try:
    # Updates the retention records on a recording.
    api_response = api_instance.put_conversation_recording(conversation_id, recording_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_conversation_recording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
| **body** | [**Recording**](Recording.html)| recording | |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="put_conversation_recording_annotation"></a>

## [**Annotation**](Annotation.html)put_conversation_recording_annotation(conversation_id, recording_id, annotation_id, body)

Update annotation



Wraps PUT /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations/{annotationId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
annotation_id = 'annotation_id_example' # str | Annotation ID
body = PureCloudPlatformClientV2.Annotation() # Annotation | annotation

try:
    # Update annotation
    api_response = api_instance.put_conversation_recording_annotation(conversation_id, recording_id, annotation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_conversation_recording_annotation: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID | |
| **recording_id** | **str**| Recording ID | |
| **annotation_id** | **str**| Annotation ID | |
| **body** | [**Annotation**](Annotation.html)| annotation | |
{: class="table table-striped"}

### Return type

[**Annotation**](Annotation.html)

<a name="put_orphanrecording"></a>

## [**Recording**](Recording.html)put_orphanrecording(orphan_id, body=body)

Updates an orphan recording to a regular recording with retention values

If this operation is successful the orphan will no longer exist. It will be replaced by the resulting recording in the response. This replacement recording is accessible by the normal Recording api.

Wraps PUT /api/v2/orphanrecordings/{orphanId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID
body = PureCloudPlatformClientV2.OrphanUpdateRequest() # OrphanUpdateRequest |  (optional)

try:
    # Updates an orphan recording to a regular recording with retention values
    api_response = api_instance.put_orphanrecording(orphan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_orphanrecording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID | |
| **body** | [**OrphanUpdateRequest**](OrphanUpdateRequest.html)|  | [optional] |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="put_recording_localkeys_setting"></a>

## [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)put_recording_localkeys_setting(settings_id, body)

Update the local encryption settings



Wraps PUT /api/v2/recording/localkeys/settings/{settingsId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
settings_id = 'settings_id_example' # str | Settings Id
body = PureCloudPlatformClientV2.LocalEncryptionConfiguration() # LocalEncryptionConfiguration | Local Encryption metadata

try:
    # Update the local encryption settings
    api_response = api_instance.put_recording_localkeys_setting(settings_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_recording_localkeys_setting: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings Id | |
| **body** | [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)| Local Encryption metadata | |
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)

<a name="put_recording_mediaretentionpolicy"></a>

## [**Policy**](Policy.html)put_recording_mediaretentionpolicy(policy_id, body)

Update a media retention policy



Wraps PUT /api/v2/recording/mediaretentionpolicies/{policyId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID
body = PureCloudPlatformClientV2.Policy() # Policy | Policy

try:
    # Update a media retention policy
    api_response = api_instance.put_recording_mediaretentionpolicy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_recording_mediaretentionpolicy: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID | |
| **body** | [**Policy**](Policy.html)| Policy | |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="put_recording_recordingkeys_rotationschedule"></a>

## [**KeyRotationSchedule**](KeyRotationSchedule.html)put_recording_recordingkeys_rotationschedule(body)

Update key rotation schedule



Wraps PUT /api/v2/recording/recordingkeys/rotationschedule 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.KeyRotationSchedule() # KeyRotationSchedule | KeyRotationSchedule

try:
    # Update key rotation schedule
    api_response = api_instance.put_recording_recordingkeys_rotationschedule(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_recording_recordingkeys_rotationschedule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KeyRotationSchedule**](KeyRotationSchedule.html)| KeyRotationSchedule | |
{: class="table table-striped"}

### Return type

[**KeyRotationSchedule**](KeyRotationSchedule.html)

<a name="put_recording_settings"></a>

## [**RecordingSettings**](RecordingSettings.html)put_recording_settings(body)

Update the Recording Settings for the Organization



Wraps PUT /api/v2/recording/settings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.RecordingSettings() # RecordingSettings | Recording settings

try:
    # Update the Recording Settings for the Organization
    api_response = api_instance.put_recording_settings(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecordingApi->put_recording_settings: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RecordingSettings**](RecordingSettings.html)| Recording settings | |
{: class="table table-striped"}

### Return type

[**RecordingSettings**](RecordingSettings.html)

