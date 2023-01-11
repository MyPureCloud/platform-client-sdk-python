---
title: RecordingApi
---

## PureCloudPlatformClientV2.RecordingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_conversation_recording_annotation**](RecordingApi.html#delete_conversation_recording_annotation) | Delete annotation|
|[**delete_orphanrecording**](RecordingApi.html#delete_orphanrecording) | Deletes a single orphan recording|
|[**delete_recording_crossplatform_mediaretentionpolicies**](RecordingApi.html#delete_recording_crossplatform_mediaretentionpolicies) | Delete media retention policies|
|[**delete_recording_crossplatform_mediaretentionpolicy**](RecordingApi.html#delete_recording_crossplatform_mediaretentionpolicy) | Delete a media retention policy|
|[**delete_recording_job**](RecordingApi.html#delete_recording_job) | Delete the recording bulk job|
|[**delete_recording_mediaretentionpolicies**](RecordingApi.html#delete_recording_mediaretentionpolicies) | Delete media retention policies|
|[**delete_recording_mediaretentionpolicy**](RecordingApi.html#delete_recording_mediaretentionpolicy) | Delete a media retention policy|
|[**get_conversation_recording**](RecordingApi.html#get_conversation_recording) | Gets a specific recording.|
|[**get_conversation_recording_annotation**](RecordingApi.html#get_conversation_recording_annotation) | Get annotation|
|[**get_conversation_recording_annotations**](RecordingApi.html#get_conversation_recording_annotations) | Get annotations for recording|
|[**get_conversation_recordingmetadata**](RecordingApi.html#get_conversation_recordingmetadata) | Get recording metadata for a conversation. Does not return playable media. Annotations won&#39;t be included in the response if recording:recording:view permission is missing.|
|[**get_conversation_recordingmetadata_recording_id**](RecordingApi.html#get_conversation_recordingmetadata_recording_id) | Get metadata for a specific recording. Does not return playable media.|
|[**get_conversation_recordings**](RecordingApi.html#get_conversation_recordings) | Get all of a Conversation&#39;s Recordings.|
|[**get_orphanrecording**](RecordingApi.html#get_orphanrecording) | Gets a single orphan recording|
|[**get_orphanrecording_media**](RecordingApi.html#get_orphanrecording_media) | Gets the media of a single orphan recording|
|[**get_orphanrecordings**](RecordingApi.html#get_orphanrecordings) | Gets all orphan recordings|
|[**get_recording_batchrequest**](RecordingApi.html#get_recording_batchrequest) | Get the status and results for a batch request job, only the user that submitted the job may retrieve results|
|[**get_recording_crossplatform_mediaretentionpolicies**](RecordingApi.html#get_recording_crossplatform_mediaretentionpolicies) | Gets media retention policy list with query options to filter on name and enabled.|
|[**get_recording_crossplatform_mediaretentionpolicy**](RecordingApi.html#get_recording_crossplatform_mediaretentionpolicy) | Get a media retention policy|
|[**get_recording_job**](RecordingApi.html#get_recording_job) | Get the status of the job associated with the job id.|
|[**get_recording_job_failedrecordings**](RecordingApi.html#get_recording_job_failedrecordings) | Get IDs of recordings that the bulk job failed for|
|[**get_recording_jobs**](RecordingApi.html#get_recording_jobs) | Get the status of all jobs within the user&#39;s organization|
|[**get_recording_keyconfiguration**](RecordingApi.html#get_recording_keyconfiguration) | Get the encryption key configurations|
|[**get_recording_keyconfigurations**](RecordingApi.html#get_recording_keyconfigurations) | Get a list of key configurations data|
|[**get_recording_localkeys_setting**](RecordingApi.html#get_recording_localkeys_setting) | Get the local encryption settings. Replaced by API recording/keyconfigurations/{keyConfigurationId}|
|[**get_recording_localkeys_settings**](RecordingApi.html#get_recording_localkeys_settings) | gets a list local key settings data. Replaced by API recording/keyconfigurations|
|[**get_recording_mediaretentionpolicies**](RecordingApi.html#get_recording_mediaretentionpolicies) | Gets media retention policy list with query options to filter on name and enabled.|
|[**get_recording_mediaretentionpolicy**](RecordingApi.html#get_recording_mediaretentionpolicy) | Get a media retention policy|
|[**get_recording_recordingkeys**](RecordingApi.html#get_recording_recordingkeys) | Get encryption key list|
|[**get_recording_recordingkeys_rotationschedule**](RecordingApi.html#get_recording_recordingkeys_rotationschedule) | Get key rotation schedule|
|[**get_recording_settings**](RecordingApi.html#get_recording_settings) | Get the Recording Settings for the Organization|
|[**get_recording_uploads_report**](RecordingApi.html#get_recording_uploads_report) | Get the status of a recording upload status report|
|[**get_recordings_retention_query**](RecordingApi.html#get_recordings_retention_query) | Query for recording retention data|
|[**get_recordings_screensessions**](RecordingApi.html#get_recordings_screensessions) | Retrieves a paged listing of screen recording sessions|
|[**patch_recording_crossplatform_mediaretentionpolicy**](RecordingApi.html#patch_recording_crossplatform_mediaretentionpolicy) | Patch a media retention policy|
|[**patch_recording_mediaretentionpolicy**](RecordingApi.html#patch_recording_mediaretentionpolicy) | Patch a media retention policy|
|[**patch_recordings_screensession**](RecordingApi.html#patch_recordings_screensession) | Update a screen recording session|
|[**post_conversation_recording_annotations**](RecordingApi.html#post_conversation_recording_annotations) | Create annotation|
|[**post_recording_batchrequests**](RecordingApi.html#post_recording_batchrequests) | Submit a batch download request for recordings. Recordings in response will be in their original format/codec - configured in the Trunk configuration.|
|[**post_recording_crossplatform_mediaretentionpolicies**](RecordingApi.html#post_recording_crossplatform_mediaretentionpolicies) | Create media retention policy|
|[**post_recording_jobs**](RecordingApi.html#post_recording_jobs) | Create a recording bulk job.|
|[**post_recording_keyconfigurations**](RecordingApi.html#post_recording_keyconfigurations) | Setup configurations for encryption key creation|
|[**post_recording_keyconfigurations_validate**](RecordingApi.html#post_recording_keyconfigurations_validate) | Validate encryption key configurations without saving it|
|[**post_recording_localkeys**](RecordingApi.html#post_recording_localkeys) | create a local key management recording key|
|[**post_recording_localkeys_settings**](RecordingApi.html#post_recording_localkeys_settings) | create settings for local key creation. Replaced by API recording/keyconfigurations|
|[**post_recording_mediaretentionpolicies**](RecordingApi.html#post_recording_mediaretentionpolicies) | Create media retention policy|
|[**post_recording_recordingkeys**](RecordingApi.html#post_recording_recordingkeys) | Create encryption key|
|[**post_recording_uploads_reports**](RecordingApi.html#post_recording_uploads_reports) | Creates a recording upload status report|
|[**post_recordings_deletionprotection**](RecordingApi.html#post_recordings_deletionprotection) | Get a list of conversations with protected recordings|
|[**post_recordings_screensessions_acknowledge**](RecordingApi.html#post_recordings_screensessions_acknowledge) | Acknowledge a screen recording.|
|[**post_recordings_screensessions_metadata**](RecordingApi.html#post_recordings_screensessions_metadata) | Provide meta-data a screen recording.|
|[**put_conversation_recording**](RecordingApi.html#put_conversation_recording) | Updates the retention records on a recording.|
|[**put_conversation_recording_annotation**](RecordingApi.html#put_conversation_recording_annotation) | Update annotation|
|[**put_orphanrecording**](RecordingApi.html#put_orphanrecording) | Updates an orphan recording to a regular recording with retention values|
|[**put_recording_crossplatform_mediaretentionpolicy**](RecordingApi.html#put_recording_crossplatform_mediaretentionpolicy) | Update a media retention policy|
|[**put_recording_job**](RecordingApi.html#put_recording_job) | Execute the recording bulk job.|
|[**put_recording_keyconfiguration**](RecordingApi.html#put_recording_keyconfiguration) | Update the encryption key configurations|
|[**put_recording_localkeys_setting**](RecordingApi.html#put_recording_localkeys_setting) | Update the local encryption settings. Replaced by API recording/keyconfigurations/{keyConfigurationId}|
|[**put_recording_mediaretentionpolicy**](RecordingApi.html#put_recording_mediaretentionpolicy) | Update a media retention policy|
|[**put_recording_recordingkeys_rotationschedule**](RecordingApi.html#put_recording_recordingkeys_rotationschedule) | Update key rotation schedule|
|[**put_recording_settings**](RecordingApi.html#put_recording_settings) | Update the Recording Settings for the Organization|
|[**put_recordings_deletionprotection**](RecordingApi.html#put_recordings_deletionprotection) | Apply or revoke recording protection for conversations|
{: class="table table-striped"}

<a name="delete_conversation_recording_annotation"></a>

##  delete_conversation_recording_annotation(conversation_id, recording_id, annotation_id)



Delete annotation



Wraps DELETE /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations/{annotationId} 

Requires ANY permissions: 

* recording:annotation:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->delete_conversation_recording_annotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
| **annotation_id** | **str**| Annotation ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_orphanrecording"></a>

## [**OrphanRecording**](OrphanRecording.html) delete_orphanrecording(orphan_id)



Deletes a single orphan recording



Wraps DELETE /api/v2/orphanrecordings/{orphanId} 

Requires ANY permissions: 

* recording:orphan:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID

try:
    # Deletes a single orphan recording
    api_response = api_instance.delete_orphanrecording(orphan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->delete_orphanrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID |  |
{: class="table table-striped"}

### Return type

[**OrphanRecording**](OrphanRecording.html)

<a name="delete_recording_crossplatform_mediaretentionpolicies"></a>

##  delete_recording_crossplatform_mediaretentionpolicies(ids)



Delete media retention policies

Bulk delete of media retention policies, this will only delete the polices that match the ids specified in the query param.



Wraps DELETE /api/v2/recording/crossplatform/mediaretentionpolicies 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
ids = 'ids_example' # str | 

try:
    # Delete media retention policies
    api_instance.delete_recording_crossplatform_mediaretentionpolicies(ids)
except ApiException as e:
    print("Exception when calling RecordingApi->delete_recording_crossplatform_mediaretentionpolicies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ids** | **str**|  |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_recording_crossplatform_mediaretentionpolicy"></a>

##  delete_recording_crossplatform_mediaretentionpolicy(policy_id)



Delete a media retention policy



Wraps DELETE /api/v2/recording/crossplatform/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID

try:
    # Delete a media retention policy
    api_instance.delete_recording_crossplatform_mediaretentionpolicy(policy_id)
except ApiException as e:
    print("Exception when calling RecordingApi->delete_recording_crossplatform_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_recording_job"></a>

##  delete_recording_job(job_id)



Delete the recording bulk job



Wraps DELETE /api/v2/recording/jobs/{jobId} 

Requires ALL permissions: 

* recording:job:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete the recording bulk job
    api_instance.delete_recording_job(job_id)
except ApiException as e:
    print("Exception when calling RecordingApi->delete_recording_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_recording_mediaretentionpolicies"></a>

##  delete_recording_mediaretentionpolicies(ids)



Delete media retention policies

Bulk delete of media retention policies, this will only delete the polices that match the ids specified in the query param.



Wraps DELETE /api/v2/recording/mediaretentionpolicies 

Requires ANY permissions: 

* recording:retentionPolicy:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
ids = 'ids_example' # str | 

try:
    # Delete media retention policies
    api_instance.delete_recording_mediaretentionpolicies(ids)
except ApiException as e:
    print("Exception when calling RecordingApi->delete_recording_mediaretentionpolicies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ids** | **str**|  |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_recording_mediaretentionpolicy"></a>

##  delete_recording_mediaretentionpolicy(policy_id)



Delete a media retention policy



Wraps DELETE /api/v2/recording/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:retentionPolicy:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID

try:
    # Delete a media retention policy
    api_instance.delete_recording_mediaretentionpolicy(policy_id)
except ApiException as e:
    print("Exception when calling RecordingApi->delete_recording_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_conversation_recording"></a>

## [**Recording**](Recording.html) get_conversation_recording(conversation_id, recording_id, format_id=format_id, email_format_id=email_format_id, chat_format_id=chat_format_id, message_format_id=message_format_id, download=download, file_name=file_name, locale=locale, media_formats=media_formats)



Gets a specific recording.



Wraps GET /api/v2/conversations/{conversationId}/recordings/{recordingId} 

Requires ANY permissions: 

* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
format_id = ''WEBM'' # str | The desired media format. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3,NONE (optional) (default to 'WEBM')
email_format_id = ''EML'' # str | The desired media format when downloading an email recording. Valid values:EML,NONE (optional) (default to 'EML')
chat_format_id = ''ZIP'' # str | The desired media format when downloading a chat recording. Valid values:ZIP,NONE  (optional) (default to 'ZIP')
message_format_id = ''ZIP'' # str | The desired media format when downloading a message recording. Valid values:ZIP,NONE (optional) (default to 'ZIP')
download = False # bool | requesting a download format of the recording. Valid values:true,false (optional) (default to False)
file_name = 'file_name_example' # str | the name of the downloaded fileName (optional)
locale = 'locale_example' # str | The locale for the requested file when downloading, as an ISO 639-1 code (optional)
media_formats = ['media_formats_example'] # list[str] | All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3 (optional)

try:
    # Gets a specific recording.
    api_response = api_instance.get_conversation_recording(conversation_id, recording_id, format_id=format_id, email_format_id=email_format_id, chat_format_id=chat_format_id, message_format_id=message_format_id, download=download, file_name=file_name, locale=locale, media_formats=media_formats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_conversation_recording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
| **format_id** | **str**| The desired media format. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3,NONE | [optional] [default to &#39;WEBM&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |
| **email_format_id** | **str**| The desired media format when downloading an email recording. Valid values:EML,NONE | [optional] [default to &#39;EML&#39;]<br />**Values**: EML, NONE |
| **chat_format_id** | **str**| The desired media format when downloading a chat recording. Valid values:ZIP,NONE  | [optional] [default to &#39;ZIP&#39;]<br />**Values**: ZIP, NONE |
| **message_format_id** | **str**| The desired media format when downloading a message recording. Valid values:ZIP,NONE | [optional] [default to &#39;ZIP&#39;]<br />**Values**: ZIP, NONE |
| **download** | **bool**| requesting a download format of the recording. Valid values:true,false | [optional] [default to False]<br />**Values**: true, false |
| **file_name** | **str**| the name of the downloaded fileName | [optional]  |
| **locale** | **str**| The locale for the requested file when downloading, as an ISO 639-1 code | [optional]  |
| **media_formats** | [**list[str]**](str.html)| All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3 | [optional]  |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="get_conversation_recording_annotation"></a>

## [**Annotation**](Annotation.html) get_conversation_recording_annotation(conversation_id, recording_id, annotation_id)



Get annotation



Wraps GET /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations/{annotationId} 

Requires ANY permissions: 

* recording:annotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->get_conversation_recording_annotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
| **annotation_id** | **str**| Annotation ID |  |
{: class="table table-striped"}

### Return type

[**Annotation**](Annotation.html)

<a name="get_conversation_recording_annotations"></a>

## [**list[Annotation]**](Annotation.html) get_conversation_recording_annotations(conversation_id, recording_id)



Get annotations for recording



Wraps GET /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations 

Requires ANY permissions: 

* recording:annotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->get_conversation_recording_annotations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
{: class="table table-striped"}

### Return type

[**list[Annotation]**](Annotation.html)

<a name="get_conversation_recordingmetadata"></a>

## [**list[RecordingMetadata]**](RecordingMetadata.html) get_conversation_recordingmetadata(conversation_id)



Get recording metadata for a conversation. Does not return playable media. Annotations won't be included in the response if recording:recording:view permission is missing.



Wraps GET /api/v2/conversations/{conversationId}/recordingmetadata 

Requires ANY permissions: 

* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID

try:
    # Get recording metadata for a conversation. Does not return playable media. Annotations won't be included in the response if recording:recording:view permission is missing.
    api_response = api_instance.get_conversation_recordingmetadata(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_conversation_recordingmetadata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
{: class="table table-striped"}

### Return type

[**list[RecordingMetadata]**](RecordingMetadata.html)

<a name="get_conversation_recordingmetadata_recording_id"></a>

## [**RecordingMetadata**](RecordingMetadata.html) get_conversation_recordingmetadata_recording_id(conversation_id, recording_id)



Get metadata for a specific recording. Does not return playable media.



Wraps GET /api/v2/conversations/{conversationId}/recordingmetadata/{recordingId} 

Requires ANY permissions: 

* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID

try:
    # Get metadata for a specific recording. Does not return playable media.
    api_response = api_instance.get_conversation_recordingmetadata_recording_id(conversation_id, recording_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_conversation_recordingmetadata_recording_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
{: class="table table-striped"}

### Return type

[**RecordingMetadata**](RecordingMetadata.html)

<a name="get_conversation_recordings"></a>

## [**list[Recording]**](Recording.html) get_conversation_recordings(conversation_id, max_wait_ms=max_wait_ms, format_id=format_id, media_formats=media_formats)



Get all of a Conversation's Recordings.



Wraps GET /api/v2/conversations/{conversationId}/recordings 

Requires ANY permissions: 

* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
max_wait_ms = 5000 # int | The maximum number of milliseconds to wait for the recording to be ready. Must be a positive value. (optional) (default to 5000)
format_id = ''WEBM'' # str | The desired media format. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3,NONE. (optional) (default to 'WEBM')
media_formats = ['media_formats_example'] # list[str] | All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3. (optional)

try:
    # Get all of a Conversation's Recordings.
    api_response = api_instance.get_conversation_recordings(conversation_id, max_wait_ms=max_wait_ms, format_id=format_id, media_formats=media_formats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_conversation_recordings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **max_wait_ms** | **int**| The maximum number of milliseconds to wait for the recording to be ready. Must be a positive value. | [optional] [default to 5000] |
| **format_id** | **str**| The desired media format. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3,NONE. | [optional] [default to &#39;WEBM&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |
| **media_formats** | [**list[str]**](str.html)| All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3. | [optional]  |
{: class="table table-striped"}

### Return type

[**list[Recording]**](Recording.html)

<a name="get_orphanrecording"></a>

## [**OrphanRecording**](OrphanRecording.html) get_orphanrecording(orphan_id)



Gets a single orphan recording



Wraps GET /api/v2/orphanrecordings/{orphanId} 

Requires ANY permissions: 

* recording:orphan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID

try:
    # Gets a single orphan recording
    api_response = api_instance.get_orphanrecording(orphan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_orphanrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID |  |
{: class="table table-striped"}

### Return type

[**OrphanRecording**](OrphanRecording.html)

<a name="get_orphanrecording_media"></a>

## [**Recording**](Recording.html) get_orphanrecording_media(orphan_id, format_id=format_id, email_format_id=email_format_id, chat_format_id=chat_format_id, message_format_id=message_format_id, download=download, file_name=file_name, locale=locale, media_formats=media_formats)



Gets the media of a single orphan recording

A 202 response means the orphaned media is currently transcoding and will be available shortly.A 200 response denotes the transcoded orphan media is available now and is contained in the response body.



Wraps GET /api/v2/orphanrecordings/{orphanId}/media 

Requires ANY permissions: 

* recording:orphan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
orphan_id = 'orphan_id_example' # str | Orphan ID
format_id = ''WEBM'' # str | The desired media format. (optional) (default to 'WEBM')
email_format_id = ''EML'' # str | The desired media format when downloading an email recording. (optional) (default to 'EML')
chat_format_id = ''ZIP'' # str | The desired media format when downloading a chat recording. (optional) (default to 'ZIP')
message_format_id = ''ZIP'' # str | The desired media format when downloading a message recording. (optional) (default to 'ZIP')
download = False # bool | requesting a download format of the recording (optional) (default to False)
file_name = 'file_name_example' # str | the name of the downloaded fileName (optional)
locale = 'locale_example' # str | The locale for the requested file when downloading, as an ISO 639-1 code (optional)
media_formats = ['media_formats_example'] # list[str] | All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3 (optional)

try:
    # Gets the media of a single orphan recording
    api_response = api_instance.get_orphanrecording_media(orphan_id, format_id=format_id, email_format_id=email_format_id, chat_format_id=chat_format_id, message_format_id=message_format_id, download=download, file_name=file_name, locale=locale, media_formats=media_formats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_orphanrecording_media: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WEBM&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |
| **email_format_id** | **str**| The desired media format when downloading an email recording. | [optional] [default to &#39;EML&#39;]<br />**Values**: EML, NONE |
| **chat_format_id** | **str**| The desired media format when downloading a chat recording. | [optional] [default to &#39;ZIP&#39;]<br />**Values**: ZIP, NONE |
| **message_format_id** | **str**| The desired media format when downloading a message recording. | [optional] [default to &#39;ZIP&#39;]<br />**Values**: ZIP, NONE |
| **download** | **bool**| requesting a download format of the recording | [optional] [default to False]<br />**Values**: true, false |
| **file_name** | **str**| the name of the downloaded fileName | [optional]  |
| **locale** | **str**| The locale for the requested file when downloading, as an ISO 639-1 code | [optional]  |
| **media_formats** | [**list[str]**](str.html)| All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3 | [optional]  |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="get_orphanrecordings"></a>

## [**OrphanRecordingListing**](OrphanRecordingListing.html) get_orphanrecordings(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, has_conversation=has_conversation, media=media)



Gets all orphan recordings



Wraps GET /api/v2/orphanrecordings 

Requires ANY permissions: 

* recording:orphan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
has_conversation = False # bool | Filter resulting orphans by whether the conversation is known. False returns all orphans for the organization. (optional) (default to False)
media = 'media_example' # str | Filter resulting orphans based on their media type (optional)

try:
    # Gets all orphan recordings
    api_response = api_instance.get_orphanrecordings(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, has_conversation=has_conversation, media=media)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_orphanrecordings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **has_conversation** | **bool**| Filter resulting orphans by whether the conversation is known. False returns all orphans for the organization. | [optional] [default to False] |
| **media** | **str**| Filter resulting orphans based on their media type | [optional] <br />**Values**: Call, Screen |
{: class="table table-striped"}

### Return type

[**OrphanRecordingListing**](OrphanRecordingListing.html)

<a name="get_recording_batchrequest"></a>

## [**BatchDownloadJobStatusResult**](BatchDownloadJobStatusResult.html) get_recording_batchrequest(job_id)



Get the status and results for a batch request job, only the user that submitted the job may retrieve results



Wraps GET /api/v2/recording/batchrequests/{jobId} 

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
api_instance = PureCloudPlatformClientV2.RecordingApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get the status and results for a batch request job, only the user that submitted the job may retrieve results
    api_response = api_instance.get_recording_batchrequest(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_batchrequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**BatchDownloadJobStatusResult**](BatchDownloadJobStatusResult.html)

<a name="get_recording_crossplatform_mediaretentionpolicies"></a>

## [**PolicyEntityListing**](PolicyEntityListing.html) get_recording_crossplatform_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors, delete_days_threshold=delete_days_threshold)



Gets media retention policy list with query options to filter on name and enabled.

for a less verbose response, add summary=true to this endpoint



Wraps GET /api/v2/recording/crossplatform/mediaretentionpolicies 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
name = 'name_example' # str | the policy name - used for filtering results in searches. (optional)
enabled = True # bool | checks to see if policy is enabled - use enabled = true or enabled = false (optional)
summary = False # bool | provides a less verbose response of policy lists. (optional) (default to False)
has_errors = True # bool | provides a way to fetch all policies with errors or policies that do not have errors (optional)
delete_days_threshold = 56 # int | provides a way to fetch all policies with any actions having deleteDays exceeding the provided value (optional)

try:
    # Gets media retention policy list with query options to filter on name and enabled.
    api_response = api_instance.get_recording_crossplatform_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors, delete_days_threshold=delete_days_threshold)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_crossplatform_mediaretentionpolicies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **name** | **str**| the policy name - used for filtering results in searches. | [optional]  |
| **enabled** | **bool**| checks to see if policy is enabled - use enabled &#x3D; true or enabled &#x3D; false | [optional]  |
| **summary** | **bool**| provides a less verbose response of policy lists. | [optional] [default to False] |
| **has_errors** | **bool**| provides a way to fetch all policies with errors or policies that do not have errors | [optional]  |
| **delete_days_threshold** | **int**| provides a way to fetch all policies with any actions having deleteDays exceeding the provided value | [optional]  |
{: class="table table-striped"}

### Return type

[**PolicyEntityListing**](PolicyEntityListing.html)

<a name="get_recording_crossplatform_mediaretentionpolicy"></a>

## [**CrossPlatformPolicy**](CrossPlatformPolicy.html) get_recording_crossplatform_mediaretentionpolicy(policy_id)



Get a media retention policy



Wraps GET /api/v2/recording/crossplatform/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID

try:
    # Get a media retention policy
    api_response = api_instance.get_recording_crossplatform_mediaretentionpolicy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_crossplatform_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
{: class="table table-striped"}

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy.html)

<a name="get_recording_job"></a>

## [**RecordingJob**](RecordingJob.html) get_recording_job(job_id)



Get the status of the job associated with the job id.



Wraps GET /api/v2/recording/jobs/{jobId} 

Requires ALL permissions: 

* recording:job:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get the status of the job associated with the job id.
    api_response = api_instance.get_recording_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**RecordingJob**](RecordingJob.html)

<a name="get_recording_job_failedrecordings"></a>

## [**FailedRecordingEntityListing**](FailedRecordingEntityListing.html) get_recording_job_failedrecordings(job_id, page_size=page_size, page_number=page_number, include_total=include_total, cursor=cursor)



Get IDs of recordings that the bulk job failed for



Wraps GET /api/v2/recording/jobs/{jobId}/failedrecordings 

Requires ALL permissions: 

* recording:job:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
job_id = 'job_id_example' # str | jobId
page_size = 25 # int | Page size. Maximum is 100. (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
include_total = True # bool | If false, cursor will be used to locate the page instead of pageNumber. (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)

try:
    # Get IDs of recordings that the bulk job failed for
    api_response = api_instance.get_recording_job_failedrecordings(job_id, page_size=page_size, page_number=page_number, include_total=include_total, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_job_failedrecordings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **page_size** | **int**| Page size. Maximum is 100. | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **include_total** | **bool**| If false, cursor will be used to locate the page instead of pageNumber. | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
{: class="table table-striped"}

### Return type

[**FailedRecordingEntityListing**](FailedRecordingEntityListing.html)

<a name="get_recording_jobs"></a>

## [**RecordingJobEntityListing**](RecordingJobEntityListing.html) get_recording_jobs(page_size=page_size, page_number=page_number, sort_by=sort_by, state=state, show_only_my_jobs=show_only_my_jobs, job_type=job_type, include_total=include_total, cursor=cursor)



Get the status of all jobs within the user's organization



Wraps GET /api/v2/recording/jobs 

Requires ALL permissions: 

* recording:job:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''userId'' # str | Sort by (optional) (default to 'userId')
state = 'state_example' # str | Filter by state (optional)
show_only_my_jobs = True # bool | Show only my jobs (optional)
job_type = 'job_type_example' # str | Job Type (Can be left empty for both) (optional)
include_total = True # bool | If false, cursor will be used to locate the page instead of pageNumber. (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)

try:
    # Get the status of all jobs within the user's organization
    api_response = api_instance.get_recording_jobs(page_size=page_size, page_number=page_number, sort_by=sort_by, state=state, show_only_my_jobs=show_only_my_jobs, job_type=job_type, include_total=include_total, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;userId&#39;]<br />**Values**: userId, dateCreated |
| **state** | **str**| Filter by state | [optional] <br />**Values**: FULFILLED, PENDING, READY, PROCESSING, CANCELLED, FAILED |
| **show_only_my_jobs** | **bool**| Show only my jobs | [optional]  |
| **job_type** | **str**| Job Type (Can be left empty for both) | [optional] <br />**Values**: DELETE, EXPORT |
| **include_total** | **bool**| If false, cursor will be used to locate the page instead of pageNumber. | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
{: class="table table-striped"}

### Return type

[**RecordingJobEntityListing**](RecordingJobEntityListing.html)

<a name="get_recording_keyconfiguration"></a>

## [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html) get_recording_keyconfiguration(key_configuration_id)



Get the encryption key configurations



Wraps GET /api/v2/recording/keyconfigurations/{keyConfigurationId} 

Requires ANY permissions: 

* recording:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
key_configuration_id = 'key_configuration_id_example' # str | Key Configurations Id

try:
    # Get the encryption key configurations
    api_response = api_instance.get_recording_keyconfiguration(key_configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_keyconfiguration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **key_configuration_id** | **str**| Key Configurations Id |  |
{: class="table table-striped"}

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)

<a name="get_recording_keyconfigurations"></a>

## [**RecordingEncryptionConfigurationListing**](RecordingEncryptionConfigurationListing.html) get_recording_keyconfigurations()



Get a list of key configurations data



Wraps GET /api/v2/recording/keyconfigurations 

Requires ANY permissions: 

* recording:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # Get a list of key configurations data
    api_response = api_instance.get_recording_keyconfigurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_keyconfigurations: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**RecordingEncryptionConfigurationListing**](RecordingEncryptionConfigurationListing.html)

<a name="get_recording_localkeys_setting"></a>

## [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html) get_recording_localkeys_setting(settings_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the local encryption settings. Replaced by API recording/keyconfigurations/{keyConfigurationId}



Wraps GET /api/v2/recording/localkeys/settings/{settingsId} 

Requires ANY permissions: 

* recording:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
settings_id = 'settings_id_example' # str | Settings Id

try:
    # Get the local encryption settings. Replaced by API recording/keyconfigurations/{keyConfigurationId}
    api_response = api_instance.get_recording_localkeys_setting(settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_localkeys_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings Id |  |
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)

<a name="get_recording_localkeys_settings"></a>

## [**LocalEncryptionConfigurationListing**](LocalEncryptionConfigurationListing.html) get_recording_localkeys_settings()

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

gets a list local key settings data. Replaced by API recording/keyconfigurations



Wraps GET /api/v2/recording/localkeys/settings 

Requires ANY permissions: 

* recording:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # gets a list local key settings data. Replaced by API recording/keyconfigurations
    api_response = api_instance.get_recording_localkeys_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_localkeys_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**LocalEncryptionConfigurationListing**](LocalEncryptionConfigurationListing.html)

<a name="get_recording_mediaretentionpolicies"></a>

## [**PolicyEntityListing**](PolicyEntityListing.html) get_recording_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors, delete_days_threshold=delete_days_threshold)



Gets media retention policy list with query options to filter on name and enabled.

for a less verbose response, add summary=true to this endpoint



Wraps GET /api/v2/recording/mediaretentionpolicies 

Requires ANY permissions: 

* recording:retentionPolicy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
name = 'name_example' # str | the policy name - used for filtering results in searches. (optional)
enabled = True # bool | checks to see if policy is enabled - use enabled = true or enabled = false (optional)
summary = False # bool | provides a less verbose response of policy lists. (optional) (default to False)
has_errors = True # bool | provides a way to fetch all policies with errors or policies that do not have errors (optional)
delete_days_threshold = 56 # int | provides a way to fetch all policies with any actions having deleteDays exceeding the provided value (optional)

try:
    # Gets media retention policy list with query options to filter on name and enabled.
    api_response = api_instance.get_recording_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors, delete_days_threshold=delete_days_threshold)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_mediaretentionpolicies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **name** | **str**| the policy name - used for filtering results in searches. | [optional]  |
| **enabled** | **bool**| checks to see if policy is enabled - use enabled &#x3D; true or enabled &#x3D; false | [optional]  |
| **summary** | **bool**| provides a less verbose response of policy lists. | [optional] [default to False] |
| **has_errors** | **bool**| provides a way to fetch all policies with errors or policies that do not have errors | [optional]  |
| **delete_days_threshold** | **int**| provides a way to fetch all policies with any actions having deleteDays exceeding the provided value | [optional]  |
{: class="table table-striped"}

### Return type

[**PolicyEntityListing**](PolicyEntityListing.html)

<a name="get_recording_mediaretentionpolicy"></a>

## [**Policy**](Policy.html) get_recording_mediaretentionpolicy(policy_id)



Get a media retention policy



Wraps GET /api/v2/recording/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:retentionPolicy:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID

try:
    # Get a media retention policy
    api_response = api_instance.get_recording_mediaretentionpolicy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="get_recording_recordingkeys"></a>

## [**EncryptionKeyEntityListing**](EncryptionKeyEntityListing.html) get_recording_recordingkeys(page_size=page_size, page_number=page_number)



Get encryption key list



Wraps GET /api/v2/recording/recordingkeys 

Requires ANY permissions: 

* recording:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->get_recording_recordingkeys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**EncryptionKeyEntityListing**](EncryptionKeyEntityListing.html)

<a name="get_recording_recordingkeys_rotationschedule"></a>

## [**KeyRotationSchedule**](KeyRotationSchedule.html) get_recording_recordingkeys_rotationschedule()



Get key rotation schedule



Wraps GET /api/v2/recording/recordingkeys/rotationschedule 

Requires ANY permissions: 

* recording:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # Get key rotation schedule
    api_response = api_instance.get_recording_recordingkeys_rotationschedule()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_recordingkeys_rotationschedule: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**KeyRotationSchedule**](KeyRotationSchedule.html)

<a name="get_recording_settings"></a>

## [**RecordingSettings**](RecordingSettings.html) get_recording_settings(create_default=create_default)



Get the Recording Settings for the Organization



Wraps GET /api/v2/recording/settings 

Requires ANY permissions: 

* recording:screenRecording:view
* recording:settings:editScreenRecordings

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
create_default = False # bool | If no settings are found, a new one is created with default values (optional) (default to False)

try:
    # Get the Recording Settings for the Organization
    api_response = api_instance.get_recording_settings(create_default=create_default)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **create_default** | **bool**| If no settings are found, a new one is created with default values | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**RecordingSettings**](RecordingSettings.html)

<a name="get_recording_uploads_report"></a>

## [**RecordingUploadReport**](RecordingUploadReport.html) get_recording_uploads_report(report_id)



Get the status of a recording upload status report



Wraps GET /api/v2/recording/uploads/reports/{reportId} 

Requires ALL permissions: 

* recording:uploadReport:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
report_id = 'report_id_example' # str | reportId

try:
    # Get the status of a recording upload status report
    api_response = api_instance.get_recording_uploads_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_uploads_report: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **report_id** | **str**| reportId |  |
{: class="table table-striped"}

### Return type

[**RecordingUploadReport**](RecordingUploadReport.html)

<a name="get_recordings_retention_query"></a>

## [**RecordingRetentionCursorEntityListing**](RecordingRetentionCursorEntityListing.html) get_recordings_retention_query(retention_threshold_days, cursor=cursor, page_size=page_size)



Query for recording retention data



Wraps GET /api/v2/recordings/retention/query 

Requires ANY permissions: 

* recording:recording:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
retention_threshold_days = 56 # int | Fetch retention data for recordings retained for more days than the provided value.
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 25 # int | Page size. Maximum is 500. (optional) (default to 25)

try:
    # Query for recording retention data
    api_response = api_instance.get_recordings_retention_query(retention_threshold_days, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recordings_retention_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **retention_threshold_days** | **int**| Fetch retention data for recordings retained for more days than the provided value. |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| Page size. Maximum is 500. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**RecordingRetentionCursorEntityListing**](RecordingRetentionCursorEntityListing.html)

<a name="get_recordings_screensessions"></a>

## [**ScreenRecordingSessionListing**](ScreenRecordingSessionListing.html) get_recordings_screensessions(page_size=page_size, page_number=page_number)



Retrieves a paged listing of screen recording sessions



Wraps GET /api/v2/recordings/screensessions 

Requires ANY permissions: 

* recording:screenRecording:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->get_recordings_screensessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**ScreenRecordingSessionListing**](ScreenRecordingSessionListing.html)

<a name="patch_recording_crossplatform_mediaretentionpolicy"></a>

## [**CrossPlatformPolicy**](CrossPlatformPolicy.html) patch_recording_crossplatform_mediaretentionpolicy(policy_id, body)



Patch a media retention policy



Wraps PATCH /api/v2/recording/crossplatform/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID
body = PureCloudPlatformClientV2.CrossPlatformPolicyUpdate() # CrossPlatformPolicyUpdate | Policy

try:
    # Patch a media retention policy
    api_response = api_instance.patch_recording_crossplatform_mediaretentionpolicy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->patch_recording_crossplatform_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
| **body** | [**CrossPlatformPolicyUpdate**](CrossPlatformPolicyUpdate.html)| Policy |  |
{: class="table table-striped"}

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy.html)

<a name="patch_recording_mediaretentionpolicy"></a>

## [**Policy**](Policy.html) patch_recording_mediaretentionpolicy(policy_id, body)



Patch a media retention policy



Wraps PATCH /api/v2/recording/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:retentionPolicy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID
body = PureCloudPlatformClientV2.PolicyUpdate() # PolicyUpdate | Policy

try:
    # Patch a media retention policy
    api_response = api_instance.patch_recording_mediaretentionpolicy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->patch_recording_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
| **body** | [**PolicyUpdate**](PolicyUpdate.html)| Policy |  |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="patch_recordings_screensession"></a>

##  patch_recordings_screensession(recording_session_id, body=body)



Update a screen recording session



Wraps PATCH /api/v2/recordings/screensessions/{recordingSessionId} 

Requires ANY permissions: 

* recording:screenRecording:stop

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
recording_session_id = 'recording_session_id_example' # str | Screen recording session ID
body = PureCloudPlatformClientV2.ScreenRecordingSessionRequest() # ScreenRecordingSessionRequest |  (optional)

try:
    # Update a screen recording session
    api_instance.patch_recordings_screensession(recording_session_id, body=body)
except ApiException as e:
    print("Exception when calling RecordingApi->patch_recordings_screensession: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_session_id** | **str**| Screen recording session ID |  |
| **body** | [**ScreenRecordingSessionRequest**](ScreenRecordingSessionRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_recording_annotations"></a>

## [**Annotation**](Annotation.html) post_conversation_recording_annotations(conversation_id, recording_id, body)



Create annotation



Wraps POST /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations 

Requires ANY permissions: 

* recording:annotation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->post_conversation_recording_annotations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
| **body** | [**Annotation**](Annotation.html)| annotation |  |
{: class="table table-striped"}

### Return type

[**Annotation**](Annotation.html)

<a name="post_recording_batchrequests"></a>

## [**BatchDownloadJobSubmissionResult**](BatchDownloadJobSubmissionResult.html) post_recording_batchrequests(body)



Submit a batch download request for recordings. Recordings in response will be in their original format/codec - configured in the Trunk configuration.



Wraps POST /api/v2/recording/batchrequests 

Requires ANY permissions: 

* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.BatchDownloadJobSubmission() # BatchDownloadJobSubmission | Job submission criteria

try:
    # Submit a batch download request for recordings. Recordings in response will be in their original format/codec - configured in the Trunk configuration.
    api_response = api_instance.post_recording_batchrequests(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_batchrequests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BatchDownloadJobSubmission**](BatchDownloadJobSubmission.html)| Job submission criteria |  |
{: class="table table-striped"}

### Return type

[**BatchDownloadJobSubmissionResult**](BatchDownloadJobSubmissionResult.html)

<a name="post_recording_crossplatform_mediaretentionpolicies"></a>

## [**CrossPlatformPolicy**](CrossPlatformPolicy.html) post_recording_crossplatform_mediaretentionpolicies(body)



Create media retention policy

Policy does not work retroactively



Wraps POST /api/v2/recording/crossplatform/mediaretentionpolicies 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.CrossPlatformPolicyCreate() # CrossPlatformPolicyCreate | Policy

try:
    # Create media retention policy
    api_response = api_instance.post_recording_crossplatform_mediaretentionpolicies(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_crossplatform_mediaretentionpolicies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CrossPlatformPolicyCreate**](CrossPlatformPolicyCreate.html)| Policy |  |
{: class="table table-striped"}

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy.html)

<a name="post_recording_jobs"></a>

## [**RecordingJob**](RecordingJob.html) post_recording_jobs(body)



Create a recording bulk job.

Each organization can run up to a maximum of two concurrent jobs that are either in pending or processing state. Furthermore, the recording:recording:viewSensitiveData permission is required to access recordings with PCI DSS and/or PII data. If the requester does not have that permission and includeRecordingsWithSensitiveData is set to true, then their request will be rejected.



Wraps POST /api/v2/recording/jobs 

Requires ALL permissions: 

* recording:job:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.RecordingJobsQuery() # RecordingJobsQuery | query

try:
    # Create a recording bulk job.
    api_response = api_instance.post_recording_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RecordingJobsQuery**](RecordingJobsQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**RecordingJob**](RecordingJob.html)

<a name="post_recording_keyconfigurations"></a>

## [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html) post_recording_keyconfigurations(body)



Setup configurations for encryption key creation



Wraps POST /api/v2/recording/keyconfigurations 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.RecordingEncryptionConfiguration() # RecordingEncryptionConfiguration | Encryption Configuration

try:
    # Setup configurations for encryption key creation
    api_response = api_instance.post_recording_keyconfigurations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_keyconfigurations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)| Encryption Configuration |  |
{: class="table table-striped"}

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)

<a name="post_recording_keyconfigurations_validate"></a>

## [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html) post_recording_keyconfigurations_validate(body)



Validate encryption key configurations without saving it



Wraps POST /api/v2/recording/keyconfigurations/validate 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.RecordingEncryptionConfiguration() # RecordingEncryptionConfiguration | Encryption Configuration

try:
    # Validate encryption key configurations without saving it
    api_response = api_instance.post_recording_keyconfigurations_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_keyconfigurations_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)| Encryption Configuration |  |
{: class="table table-striped"}

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)

<a name="post_recording_localkeys"></a>

## [**EncryptionKey**](EncryptionKey.html) post_recording_localkeys(body)



create a local key management recording key



Wraps POST /api/v2/recording/localkeys 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.LocalEncryptionKeyRequest() # LocalEncryptionKeyRequest | Local Encryption body

try:
    # create a local key management recording key
    api_response = api_instance.post_recording_localkeys(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_localkeys: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocalEncryptionKeyRequest**](LocalEncryptionKeyRequest.html)| Local Encryption body |  |
{: class="table table-striped"}

### Return type

[**EncryptionKey**](EncryptionKey.html)

<a name="post_recording_localkeys_settings"></a>

## [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html) post_recording_localkeys_settings(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

create settings for local key creation. Replaced by API recording/keyconfigurations



Wraps POST /api/v2/recording/localkeys/settings 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.LocalEncryptionConfiguration() # LocalEncryptionConfiguration | Local Encryption Configuration

try:
    # create settings for local key creation. Replaced by API recording/keyconfigurations
    api_response = api_instance.post_recording_localkeys_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_localkeys_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)| Local Encryption Configuration |  |
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)

<a name="post_recording_mediaretentionpolicies"></a>

## [**Policy**](Policy.html) post_recording_mediaretentionpolicies(body)



Create media retention policy

Policy does not work retroactively



Wraps POST /api/v2/recording/mediaretentionpolicies 

Requires ANY permissions: 

* recording:retentionPolicy:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.PolicyCreate() # PolicyCreate | Policy

try:
    # Create media retention policy
    api_response = api_instance.post_recording_mediaretentionpolicies(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_mediaretentionpolicies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PolicyCreate**](PolicyCreate.html)| Policy |  |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="post_recording_recordingkeys"></a>

## [**EncryptionKey**](EncryptionKey.html) post_recording_recordingkeys()



Create encryption key



Wraps POST /api/v2/recording/recordingkeys 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()

try:
    # Create encryption key
    api_response = api_instance.post_recording_recordingkeys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_recordingkeys: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EncryptionKey**](EncryptionKey.html)

<a name="post_recording_uploads_reports"></a>

## [**RecordingUploadReport**](RecordingUploadReport.html) post_recording_uploads_reports(body)



Creates a recording upload status report



Wraps POST /api/v2/recording/uploads/reports 

Requires ALL permissions: 

* recording:uploadReport:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.RecordingUploadReportRequest() # RecordingUploadReportRequest | Report parameters

try:
    # Creates a recording upload status report
    api_response = api_instance.post_recording_uploads_reports(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recording_uploads_reports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RecordingUploadReportRequest**](RecordingUploadReportRequest.html)| Report parameters |  |
{: class="table table-striped"}

### Return type

[**RecordingUploadReport**](RecordingUploadReport.html)

<a name="post_recordings_deletionprotection"></a>

## [**list[AddressableEntityRef]**](AddressableEntityRef.html) post_recordings_deletionprotection(body)



Get a list of conversations with protected recordings



Wraps POST /api/v2/recordings/deletionprotection 

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
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.ConversationDeletionProtectionQuery() # ConversationDeletionProtectionQuery | conversationIds

try:
    # Get a list of conversations with protected recordings
    api_response = api_instance.post_recordings_deletionprotection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recordings_deletionprotection: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationDeletionProtectionQuery**](ConversationDeletionProtectionQuery.html)| conversationIds |  |
{: class="table table-striped"}

### Return type

[**list[AddressableEntityRef]**](AddressableEntityRef.html)

<a name="post_recordings_screensessions_acknowledge"></a>

##  post_recordings_screensessions_acknowledge(body)



Acknowledge a screen recording.



Wraps POST /api/v2/recordings/screensessions/acknowledge 

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
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.AcknowledgeScreenRecordingRequest() # AcknowledgeScreenRecordingRequest | AcknowledgeScreenRecordingRequest

try:
    # Acknowledge a screen recording.
    api_instance.post_recordings_screensessions_acknowledge(body)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recordings_screensessions_acknowledge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AcknowledgeScreenRecordingRequest**](AcknowledgeScreenRecordingRequest.html)| AcknowledgeScreenRecordingRequest |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_recordings_screensessions_metadata"></a>

##  post_recordings_screensessions_metadata(body)



Provide meta-data a screen recording.



Wraps POST /api/v2/recordings/screensessions/metadata 

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
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.ScreenRecordingMetaDataRequest() # ScreenRecordingMetaDataRequest | ScreenRecordingMetaDataRequest

try:
    # Provide meta-data a screen recording.
    api_instance.post_recordings_screensessions_metadata(body)
except ApiException as e:
    print("Exception when calling RecordingApi->post_recordings_screensessions_metadata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScreenRecordingMetaDataRequest**](ScreenRecordingMetaDataRequest.html)| ScreenRecordingMetaDataRequest |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="put_conversation_recording"></a>

## [**Recording**](Recording.html) put_conversation_recording(conversation_id, recording_id, body, clear_export=clear_export)



Updates the retention records on a recording.

Currently supports updating and removing both archive and delete dates for eligible recordings. A request to change the archival date of an archived recording will result in a restoration of the recording until the new date set. The recording:recording:view permission is required for the recording, as well as either the recording:recording:editRetention or recording:screenRecording:editRetention permissions depending on the type of recording.



Wraps PUT /api/v2/conversations/{conversationId}/recordings/{recordingId} 

Requires ANY permissions: 

* recording:recording:view
* recording:recording:editRetention
* recording:screenRecording:editRetention

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
recording_id = 'recording_id_example' # str | Recording ID
body = PureCloudPlatformClientV2.Recording() # Recording | recording
clear_export = True # bool | Whether to clear the pending export for the recording (optional)

try:
    # Updates the retention records on a recording.
    api_response = api_instance.put_conversation_recording(conversation_id, recording_id, body, clear_export=clear_export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_conversation_recording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
| **body** | [**Recording**](Recording.html)| recording |  |
| **clear_export** | **bool**| Whether to clear the pending export for the recording | [optional]  |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="put_conversation_recording_annotation"></a>

## [**Annotation**](Annotation.html) put_conversation_recording_annotation(conversation_id, recording_id, annotation_id, body)



Update annotation



Wraps PUT /api/v2/conversations/{conversationId}/recordings/{recordingId}/annotations/{annotationId} 

Requires ANY permissions: 

* recording:annotation:edit
* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->put_conversation_recording_annotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **recording_id** | **str**| Recording ID |  |
| **annotation_id** | **str**| Annotation ID |  |
| **body** | [**Annotation**](Annotation.html)| annotation |  |
{: class="table table-striped"}

### Return type

[**Annotation**](Annotation.html)

<a name="put_orphanrecording"></a>

## [**Recording**](Recording.html) put_orphanrecording(orphan_id, body=body)



Updates an orphan recording to a regular recording with retention values

If this operation is successful the orphan will no longer exist. It will be replaced by the resulting recording in the response. This replacement recording is accessible by the normal Recording api.



Wraps PUT /api/v2/orphanrecordings/{orphanId} 

Requires ANY permissions: 

* recording:orphan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->put_orphanrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orphan_id** | **str**| Orphan ID |  |
| **body** | [**OrphanUpdateRequest**](OrphanUpdateRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**Recording**](Recording.html)

<a name="put_recording_crossplatform_mediaretentionpolicy"></a>

## [**CrossPlatformPolicy**](CrossPlatformPolicy.html) put_recording_crossplatform_mediaretentionpolicy(policy_id, body)



Update a media retention policy

Policy does not work retroactively



Wraps PUT /api/v2/recording/crossplatform/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:crossPlatformRetentionPolicy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
policy_id = 'policy_id_example' # str | Policy ID
body = PureCloudPlatformClientV2.CrossPlatformPolicy() # CrossPlatformPolicy | Policy

try:
    # Update a media retention policy
    api_response = api_instance.put_recording_crossplatform_mediaretentionpolicy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recording_crossplatform_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
| **body** | [**CrossPlatformPolicy**](CrossPlatformPolicy.html)| Policy |  |
{: class="table table-striped"}

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy.html)

<a name="put_recording_job"></a>

## [**RecordingJob**](RecordingJob.html) put_recording_job(job_id, body)



Execute the recording bulk job.

A job must be executed by the same user whom originally created the job.  In addition, the user must have permission to update the recording's retention.



Wraps PUT /api/v2/recording/jobs/{jobId} 

Requires ALL permissions: 

* recording:job:edit
* recording:recording:editRetention
* recording:screenRecording:editRetention

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
job_id = 'job_id_example' # str | jobId
body = PureCloudPlatformClientV2.ExecuteRecordingJobsQuery() # ExecuteRecordingJobsQuery | query

try:
    # Execute the recording bulk job.
    api_response = api_instance.put_recording_job(job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recording_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **body** | [**ExecuteRecordingJobsQuery**](ExecuteRecordingJobsQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**RecordingJob**](RecordingJob.html)

<a name="put_recording_keyconfiguration"></a>

## [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html) put_recording_keyconfiguration(key_configuration_id, body)



Update the encryption key configurations



Wraps PUT /api/v2/recording/keyconfigurations/{keyConfigurationId} 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
key_configuration_id = 'key_configuration_id_example' # str | Key Configurations Id
body = PureCloudPlatformClientV2.RecordingEncryptionConfiguration() # RecordingEncryptionConfiguration | Encryption key configuration metadata

try:
    # Update the encryption key configurations
    api_response = api_instance.put_recording_keyconfiguration(key_configuration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recording_keyconfiguration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **key_configuration_id** | **str**| Key Configurations Id |  |
| **body** | [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)| Encryption key configuration metadata |  |
{: class="table table-striped"}

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration.html)

<a name="put_recording_localkeys_setting"></a>

## [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html) put_recording_localkeys_setting(settings_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update the local encryption settings. Replaced by API recording/keyconfigurations/{keyConfigurationId}



Wraps PUT /api/v2/recording/localkeys/settings/{settingsId} 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
settings_id = 'settings_id_example' # str | Settings Id
body = PureCloudPlatformClientV2.LocalEncryptionConfiguration() # LocalEncryptionConfiguration | Local Encryption metadata

try:
    # Update the local encryption settings. Replaced by API recording/keyconfigurations/{keyConfigurationId}
    api_response = api_instance.put_recording_localkeys_setting(settings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recording_localkeys_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings Id |  |
| **body** | [**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)| Local Encryption metadata |  |
{: class="table table-striped"}

### Return type

[**LocalEncryptionConfiguration**](LocalEncryptionConfiguration.html)

<a name="put_recording_mediaretentionpolicy"></a>

## [**Policy**](Policy.html) put_recording_mediaretentionpolicy(policy_id, body)



Update a media retention policy

Policy does not work retroactively



Wraps PUT /api/v2/recording/mediaretentionpolicies/{policyId} 

Requires ANY permissions: 

* recording:retentionPolicy:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling RecordingApi->put_recording_mediaretentionpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **policy_id** | **str**| Policy ID |  |
| **body** | [**Policy**](Policy.html)| Policy |  |
{: class="table table-striped"}

### Return type

[**Policy**](Policy.html)

<a name="put_recording_recordingkeys_rotationschedule"></a>

## [**KeyRotationSchedule**](KeyRotationSchedule.html) put_recording_recordingkeys_rotationschedule(body)



Update key rotation schedule



Wraps PUT /api/v2/recording/recordingkeys/rotationschedule 

Requires ANY permissions: 

* recording:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.KeyRotationSchedule() # KeyRotationSchedule | KeyRotationSchedule

try:
    # Update key rotation schedule
    api_response = api_instance.put_recording_recordingkeys_rotationschedule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recording_recordingkeys_rotationschedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KeyRotationSchedule**](KeyRotationSchedule.html)| KeyRotationSchedule |  |
{: class="table table-striped"}

### Return type

[**KeyRotationSchedule**](KeyRotationSchedule.html)

<a name="put_recording_settings"></a>

## [**RecordingSettings**](RecordingSettings.html) put_recording_settings(body)



Update the Recording Settings for the Organization



Wraps PUT /api/v2/recording/settings 

Requires ANY permissions: 

* recording:settings:editScreenRecordings

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
body = PureCloudPlatformClientV2.RecordingSettings() # RecordingSettings | Recording settings

try:
    # Update the Recording Settings for the Organization
    api_response = api_instance.put_recording_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recording_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RecordingSettings**](RecordingSettings.html)| Recording settings |  |
{: class="table table-striped"}

### Return type

[**RecordingSettings**](RecordingSettings.html)

<a name="put_recordings_deletionprotection"></a>

##  put_recordings_deletionprotection(protect=protect, body=body)



Apply or revoke recording protection for conversations



Wraps PUT /api/v2/recordings/deletionprotection 

Requires ANY permissions: 

* recording:deletionProtection:apply
* recording:deletionProtection:revoke

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.RecordingApi()
protect = True # bool | Check for apply, uncheck for revoke (each action requires the respective permission) (optional) (default to True)
body = PureCloudPlatformClientV2.ConversationDeletionProtectionQuery() # ConversationDeletionProtectionQuery |  (optional)

try:
    # Apply or revoke recording protection for conversations
    api_instance.put_recordings_deletionprotection(protect=protect, body=body)
except ApiException as e:
    print("Exception when calling RecordingApi->put_recordings_deletionprotection: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **protect** | **bool**| Check for apply, uncheck for revoke (each action requires the respective permission) | [optional] [default to True] |
| **body** | [**ConversationDeletionProtectionQuery**](ConversationDeletionProtectionQuery.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

