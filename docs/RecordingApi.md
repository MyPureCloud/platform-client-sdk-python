# RecordingApi

## PureCloudPlatformClientV2.RecordingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_conversation_recording_annotation**](#delete_conversation_recording_annotation) | Delete annotation|
|[**delete_orphanrecording**](#delete_orphanrecording) | Deletes a single orphan recording|
|[**delete_recording_crossplatform_mediaretentionpolicies**](#delete_recording_crossplatform_mediaretentionpolicies) | Delete media retention policies|
|[**delete_recording_crossplatform_mediaretentionpolicy**](#delete_recording_crossplatform_mediaretentionpolicy) | Delete a media retention policy|
|[**delete_recording_job**](#delete_recording_job) | Delete the recording bulk job|
|[**delete_recording_mediaretentionpolicies**](#delete_recording_mediaretentionpolicies) | Delete media retention policies|
|[**delete_recording_mediaretentionpolicy**](#delete_recording_mediaretentionpolicy) | Delete a media retention policy|
|[**get_conversation_recording**](#get_conversation_recording) | Gets a specific recording.|
|[**get_conversation_recording_annotation**](#get_conversation_recording_annotation) | Get annotation|
|[**get_conversation_recording_annotations**](#get_conversation_recording_annotations) | Get annotations for recording|
|[**get_conversation_recordingmetadata**](#get_conversation_recordingmetadata) | Get recording metadata for a conversation. Does not return playable media. Annotations won&#39;t be included in the response if either recording:recording:view or recording:annotation:view permission is missing.|
|[**get_conversation_recordingmetadata_recording_id**](#get_conversation_recordingmetadata_recording_id) | Get metadata for a specific recording. Does not return playable media.|
|[**get_conversation_recordings**](#get_conversation_recordings) | Get all of a Conversation&#39;s Recordings.|
|[**get_orphanrecording**](#get_orphanrecording) | Gets a single orphan recording|
|[**get_orphanrecording_media**](#get_orphanrecording_media) | Gets the media of a single orphan recording|
|[**get_orphanrecordings**](#get_orphanrecordings) | Gets all orphan recordings|
|[**get_recording_batchrequest**](#get_recording_batchrequest) | Get the status and results for a batch request job, only the user that submitted the job may retrieve results. Each result may contain either a URL to a recording or an error; additionally, a recording could be associated with multiple results.|
|[**get_recording_crossplatform_mediaretentionpolicies**](#get_recording_crossplatform_mediaretentionpolicies) | Gets media retention policy list with query options to filter on name and enabled.|
|[**get_recording_crossplatform_mediaretentionpolicy**](#get_recording_crossplatform_mediaretentionpolicy) | Get a media retention policy|
|[**get_recording_job**](#get_recording_job) | Get the status of the job associated with the job id.|
|[**get_recording_job_failedrecordings**](#get_recording_job_failedrecordings) | Get IDs of recordings that the bulk job failed for|
|[**get_recording_jobs**](#get_recording_jobs) | Get the status of all jobs within the user&#39;s organization|
|[**get_recording_keyconfiguration**](#get_recording_keyconfiguration) | Get the encryption key configurations|
|[**get_recording_keyconfigurations**](#get_recording_keyconfigurations) | Get a list of key configurations data|
|[**get_recording_mediaretentionpolicies**](#get_recording_mediaretentionpolicies) | Gets media retention policy list with query options to filter on name and enabled.|
|[**get_recording_mediaretentionpolicy**](#get_recording_mediaretentionpolicy) | Get a media retention policy|
|[**get_recording_recordingkeys**](#get_recording_recordingkeys) | Get encryption key list|
|[**get_recording_recordingkeys_rotationschedule**](#get_recording_recordingkeys_rotationschedule) | Get key rotation schedule|
|[**get_recording_settings**](#get_recording_settings) | Get the Recording Settings for the Organization|
|[**get_recording_uploads_report**](#get_recording_uploads_report) | Get the status of a recording upload status report|
|[**get_recordings_retention_query**](#get_recordings_retention_query) | Query for recording retention data|
|[**get_recordings_screensessions**](#get_recordings_screensessions) | Retrieves a paged listing of screen recording sessions|
|[**get_recordings_screensessions_details**](#get_recordings_screensessions_details) | Retrieves an object containing the total number of concurrent active screen recordings|
|[**patch_recording_crossplatform_mediaretentionpolicy**](#patch_recording_crossplatform_mediaretentionpolicy) | Patch a media retention policy|
|[**patch_recording_mediaretentionpolicy**](#patch_recording_mediaretentionpolicy) | Patch a media retention policy|
|[**post_conversation_recording_annotations**](#post_conversation_recording_annotations) | Create annotation|
|[**post_recording_batchrequests**](#post_recording_batchrequests) | Submit a batch download request for recordings. Recordings in response will be in their original format/codec - configured in the Trunk configuration.|
|[**post_recording_crossplatform_mediaretentionpolicies**](#post_recording_crossplatform_mediaretentionpolicies) | Create media retention policy|
|[**post_recording_jobs**](#post_recording_jobs) | Create a recording bulk job.|
|[**post_recording_keyconfigurations**](#post_recording_keyconfigurations) | Setup configurations for encryption key creation|
|[**post_recording_keyconfigurations_validate**](#post_recording_keyconfigurations_validate) | Validate encryption key configurations without saving it|
|[**post_recording_localkeys**](#post_recording_localkeys) | create a local key management recording key|
|[**post_recording_mediaretentionpolicies**](#post_recording_mediaretentionpolicies) | Create media retention policy|
|[**post_recording_recordingkeys**](#post_recording_recordingkeys) | Create encryption key|
|[**post_recording_uploads_reports**](#post_recording_uploads_reports) | Creates a recording upload status report|
|[**post_recordings_deletionprotection**](#post_recordings_deletionprotection) | Get a list of conversations with protected recordings|
|[**post_recordings_screensessions_acknowledge**](#post_recordings_screensessions_acknowledge) | Acknowledge a screen recording.|
|[**post_recordings_screensessions_metadata**](#post_recordings_screensessions_metadata) | Provide meta-data a screen recording.|
|[**put_conversation_recording**](#put_conversation_recording) | Updates the retention records on a recording.|
|[**put_conversation_recording_annotation**](#put_conversation_recording_annotation) | Update annotation|
|[**put_orphanrecording**](#put_orphanrecording) | Updates an orphan recording to a regular recording with retention values|
|[**put_recording_crossplatform_mediaretentionpolicy**](#put_recording_crossplatform_mediaretentionpolicy) | Update a media retention policy|
|[**put_recording_job**](#put_recording_job) | Execute the recording bulk job.|
|[**put_recording_keyconfiguration**](#put_recording_keyconfiguration) | Update the encryption key configurations|
|[**put_recording_mediaretentionpolicy**](#put_recording_mediaretentionpolicy) | Update a media retention policy|
|[**put_recording_recordingkeys_rotationschedule**](#put_recording_recordingkeys_rotationschedule) | Update key rotation schedule|
|[**put_recording_settings**](#put_recording_settings) | Update the Recording Settings for the Organization|
|[**put_recordings_deletionprotection**](#put_recordings_deletionprotection) | Apply or revoke recording protection for conversations|



## delete_conversation_recording_annotation

>  delete_conversation_recording_annotation(conversation_id, recording_id, annotation_id)


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

### Return type

void (empty response body)


## delete_orphanrecording

> [**OrphanRecording**](OrphanRecording) delete_orphanrecording(orphan_id)


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

### Return type

[**OrphanRecording**](OrphanRecording)


## delete_recording_crossplatform_mediaretentionpolicies

>  delete_recording_crossplatform_mediaretentionpolicies(ids)


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

### Return type

void (empty response body)


## delete_recording_crossplatform_mediaretentionpolicy

>  delete_recording_crossplatform_mediaretentionpolicy(policy_id)


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

### Return type

void (empty response body)


## delete_recording_job

>  delete_recording_job(job_id)


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

### Return type

void (empty response body)


## delete_recording_mediaretentionpolicies

>  delete_recording_mediaretentionpolicies(ids)


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

### Return type

void (empty response body)


## delete_recording_mediaretentionpolicy

>  delete_recording_mediaretentionpolicy(policy_id)


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

### Return type

void (empty response body)


## get_conversation_recording

> [**Recording**](Recording) get_conversation_recording(conversation_id, recording_id, format_id=format_id, email_format_id=email_format_id, chat_format_id=chat_format_id, message_format_id=message_format_id, download=download, file_name=file_name, locale=locale, media_formats=media_formats)


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
| **media_formats** | [**list[str]**](str)| All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3 | [optional]  |

### Return type

[**Recording**](Recording)


## get_conversation_recording_annotation

> [**Annotation**](Annotation) get_conversation_recording_annotation(conversation_id, recording_id, annotation_id)


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

### Return type

[**Annotation**](Annotation)


## get_conversation_recording_annotations

> [**list[Annotation]**](Annotation) get_conversation_recording_annotations(conversation_id, recording_id)


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

### Return type

[**list[Annotation]**](Annotation)


## get_conversation_recordingmetadata

> [**list[RecordingMetadata]**](RecordingMetadata) get_conversation_recordingmetadata(conversation_id)


Get recording metadata for a conversation. Does not return playable media. Annotations won't be included in the response if either recording:recording:view or recording:annotation:view permission is missing.

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
    # Get recording metadata for a conversation. Does not return playable media. Annotations won't be included in the response if either recording:recording:view or recording:annotation:view permission is missing.
    api_response = api_instance.get_conversation_recordingmetadata(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_conversation_recordingmetadata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |

### Return type

[**list[RecordingMetadata]**](RecordingMetadata)


## get_conversation_recordingmetadata_recording_id

> [**RecordingMetadata**](RecordingMetadata) get_conversation_recordingmetadata_recording_id(conversation_id, recording_id)


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

### Return type

[**RecordingMetadata**](RecordingMetadata)


## get_conversation_recordings

> [**list[Recording]**](Recording) get_conversation_recordings(conversation_id, max_wait_ms=max_wait_ms, format_id=format_id, media_formats=media_formats)


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
| **media_formats** | [**list[str]**](str)| All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3. | [optional]  |

### Return type

[**list[Recording]**](Recording)


## get_orphanrecording

> [**OrphanRecording**](OrphanRecording) get_orphanrecording(orphan_id)


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

### Return type

[**OrphanRecording**](OrphanRecording)


## get_orphanrecording_media

> [**Recording**](Recording) get_orphanrecording_media(orphan_id, format_id=format_id, email_format_id=email_format_id, chat_format_id=chat_format_id, message_format_id=message_format_id, download=download, file_name=file_name, locale=locale, media_formats=media_formats)


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
| **media_formats** | [**list[str]**](str)| All acceptable media formats. Overrides formatId. Valid values:WAV,WEBM,WAV_ULAW,OGG_VORBIS,OGG_OPUS,MP3 | [optional]  |

### Return type

[**Recording**](Recording)


## get_orphanrecordings

> [**OrphanRecordingListing**](OrphanRecordingListing) get_orphanrecordings(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, has_conversation=has_conversation, media=media)


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
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **has_conversation** | **bool**| Filter resulting orphans by whether the conversation is known. False returns all orphans for the organization. | [optional] [default to False] |
| **media** | **str**| Filter resulting orphans based on their media type | [optional] <br />**Values**: Call, Screen |

### Return type

[**OrphanRecordingListing**](OrphanRecordingListing)


## get_recording_batchrequest

> [**BatchDownloadJobStatusResult**](BatchDownloadJobStatusResult) get_recording_batchrequest(job_id)


Get the status and results for a batch request job, only the user that submitted the job may retrieve results. Each result may contain either a URL to a recording or an error; additionally, a recording could be associated with multiple results.

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
    # Get the status and results for a batch request job, only the user that submitted the job may retrieve results. Each result may contain either a URL to a recording or an error; additionally, a recording could be associated with multiple results.
    api_response = api_instance.get_recording_batchrequest(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recording_batchrequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**BatchDownloadJobStatusResult**](BatchDownloadJobStatusResult)


## get_recording_crossplatform_mediaretentionpolicies

> [**PolicyEntityListing**](PolicyEntityListing) get_recording_crossplatform_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors, delete_days_threshold=delete_days_threshold)


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
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **name** | **str**| the policy name - used for filtering results in searches. | [optional]  |
| **enabled** | **bool**| checks to see if policy is enabled - use enabled &#x3D; true or enabled &#x3D; false | [optional]  |
| **summary** | **bool**| provides a less verbose response of policy lists. | [optional] [default to False] |
| **has_errors** | **bool**| provides a way to fetch all policies with errors or policies that do not have errors | [optional]  |
| **delete_days_threshold** | **int**| provides a way to fetch all policies with any actions having deleteDays exceeding the provided value | [optional]  |

### Return type

[**PolicyEntityListing**](PolicyEntityListing)


## get_recording_crossplatform_mediaretentionpolicy

> [**CrossPlatformPolicy**](CrossPlatformPolicy) get_recording_crossplatform_mediaretentionpolicy(policy_id)


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

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy)


## get_recording_job

> [**RecordingJob**](RecordingJob) get_recording_job(job_id)


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

### Return type

[**RecordingJob**](RecordingJob)


## get_recording_job_failedrecordings

> [**FailedRecordingEntityListing**](FailedRecordingEntityListing) get_recording_job_failedrecordings(job_id, page_size=page_size, page_number=page_number, include_total=include_total, cursor=cursor)


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

### Return type

[**FailedRecordingEntityListing**](FailedRecordingEntityListing)


## get_recording_jobs

> [**RecordingJobEntityListing**](RecordingJobEntityListing) get_recording_jobs(page_size=page_size, page_number=page_number, sort_by=sort_by, state=state, show_only_my_jobs=show_only_my_jobs, job_type=job_type, include_total=include_total, cursor=cursor)


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
| **job_type** | **str**| Job Type (Can be left empty for both) | [optional] <br />**Values**: ARCHIVE, DELETE, EXPORT |
| **include_total** | **bool**| If false, cursor will be used to locate the page instead of pageNumber. | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |

### Return type

[**RecordingJobEntityListing**](RecordingJobEntityListing)


## get_recording_keyconfiguration

> [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration) get_recording_keyconfiguration(key_configuration_id)


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

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)


## get_recording_keyconfigurations

> [**RecordingEncryptionConfigurationListing**](RecordingEncryptionConfigurationListing) get_recording_keyconfigurations()


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

[**RecordingEncryptionConfigurationListing**](RecordingEncryptionConfigurationListing)


## get_recording_mediaretentionpolicies

> [**PolicyEntityListing**](PolicyEntityListing) get_recording_mediaretentionpolicies(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, enabled=enabled, summary=summary, has_errors=has_errors, delete_days_threshold=delete_days_threshold)


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
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **name** | **str**| the policy name - used for filtering results in searches. | [optional]  |
| **enabled** | **bool**| checks to see if policy is enabled - use enabled &#x3D; true or enabled &#x3D; false | [optional]  |
| **summary** | **bool**| provides a less verbose response of policy lists. | [optional] [default to False] |
| **has_errors** | **bool**| provides a way to fetch all policies with errors or policies that do not have errors | [optional]  |
| **delete_days_threshold** | **int**| provides a way to fetch all policies with any actions having deleteDays exceeding the provided value | [optional]  |

### Return type

[**PolicyEntityListing**](PolicyEntityListing)


## get_recording_mediaretentionpolicy

> [**Policy**](Policy) get_recording_mediaretentionpolicy(policy_id)


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

### Return type

[**Policy**](Policy)


## get_recording_recordingkeys

> [**EncryptionKeyEntityListing**](EncryptionKeyEntityListing) get_recording_recordingkeys(page_size=page_size, page_number=page_number)


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

### Return type

[**EncryptionKeyEntityListing**](EncryptionKeyEntityListing)


## get_recording_recordingkeys_rotationschedule

> [**KeyRotationSchedule**](KeyRotationSchedule) get_recording_recordingkeys_rotationschedule()


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

[**KeyRotationSchedule**](KeyRotationSchedule)


## get_recording_settings

> [**RecordingSettings**](RecordingSettings) get_recording_settings(create_default=create_default)


Get the Recording Settings for the Organization

Wraps GET /api/v2/recording/settings 

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

### Return type

[**RecordingSettings**](RecordingSettings)


## get_recording_uploads_report

> [**RecordingUploadReport**](RecordingUploadReport) get_recording_uploads_report(report_id)


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

### Return type

[**RecordingUploadReport**](RecordingUploadReport)


## get_recordings_retention_query

> [**RecordingRetentionCursorEntityListing**](RecordingRetentionCursorEntityListing) get_recordings_retention_query(retention_threshold_days, cursor=cursor, page_size=page_size)


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

### Return type

[**RecordingRetentionCursorEntityListing**](RecordingRetentionCursorEntityListing)


## get_recordings_screensessions

> [**ScreenRecordingSessionListing**](ScreenRecordingSessionListing) get_recordings_screensessions(page_size=page_size, page_number=page_number)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Retrieves a paged listing of screen recording sessions

Coming soon: This API is deprecated and will be replaced by /api/v2/recordings/screensessions/details

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

### Return type

[**ScreenRecordingSessionListing**](ScreenRecordingSessionListing)


## get_recordings_screensessions_details

> [**ScreenRecordingActiveSessions**](ScreenRecordingActiveSessions) get_recordings_screensessions_details()


Retrieves an object containing the total number of concurrent active screen recordings

Wraps GET /api/v2/recordings/screensessions/details 

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

try:
    # Retrieves an object containing the total number of concurrent active screen recordings
    api_response = api_instance.get_recordings_screensessions_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordingApi->get_recordings_screensessions_details: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ScreenRecordingActiveSessions**](ScreenRecordingActiveSessions)


## patch_recording_crossplatform_mediaretentionpolicy

> [**CrossPlatformPolicy**](CrossPlatformPolicy) patch_recording_crossplatform_mediaretentionpolicy(policy_id, body)


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
| **body** | [**CrossPlatformPolicyUpdate**](CrossPlatformPolicyUpdate)| Policy |  |

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy)


## patch_recording_mediaretentionpolicy

> [**Policy**](Policy) patch_recording_mediaretentionpolicy(policy_id, body)


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
| **body** | [**PolicyUpdate**](PolicyUpdate)| Policy |  |

### Return type

[**Policy**](Policy)


## post_conversation_recording_annotations

> [**Annotation**](Annotation) post_conversation_recording_annotations(conversation_id, recording_id, body)


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
| **body** | [**Annotation**](Annotation)| annotation |  |

### Return type

[**Annotation**](Annotation)


## post_recording_batchrequests

> [**BatchDownloadJobSubmissionResult**](BatchDownloadJobSubmissionResult) post_recording_batchrequests(body)


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
| **body** | [**BatchDownloadJobSubmission**](BatchDownloadJobSubmission)| Job submission criteria |  |

### Return type

[**BatchDownloadJobSubmissionResult**](BatchDownloadJobSubmissionResult)


## post_recording_crossplatform_mediaretentionpolicies

> [**CrossPlatformPolicy**](CrossPlatformPolicy) post_recording_crossplatform_mediaretentionpolicies(body)


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
| **body** | [**CrossPlatformPolicyCreate**](CrossPlatformPolicyCreate)| Policy |  |

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy)


## post_recording_jobs

> [**RecordingJob**](RecordingJob) post_recording_jobs(body)


Create a recording bulk job.

Each organization can run up to a maximum of two concurrent jobs that are either in pending or processing state. Furthermore, the recording:recording:viewSensitiveData permission is required to access recordings with PCI DSS and/or PII data when redaction is enabled for their organization. If the requester does not have that permission and includeRecordingsWithSensitiveData is set to true, then their request will be rejected.

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
| **body** | [**RecordingJobsQuery**](RecordingJobsQuery)| query |  |

### Return type

[**RecordingJob**](RecordingJob)


## post_recording_keyconfigurations

> [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration) post_recording_keyconfigurations(body)


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
| **body** | [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)| Encryption Configuration |  |

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)


## post_recording_keyconfigurations_validate

> [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration) post_recording_keyconfigurations_validate(body)


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
| **body** | [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)| Encryption Configuration |  |

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)


## post_recording_localkeys

> [**EncryptionKey**](EncryptionKey) post_recording_localkeys(body)


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
| **body** | [**LocalEncryptionKeyRequest**](LocalEncryptionKeyRequest)| Local Encryption body |  |

### Return type

[**EncryptionKey**](EncryptionKey)


## post_recording_mediaretentionpolicies

> [**Policy**](Policy) post_recording_mediaretentionpolicies(body)


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
| **body** | [**PolicyCreate**](PolicyCreate)| Policy |  |

### Return type

[**Policy**](Policy)


## post_recording_recordingkeys

> [**EncryptionKey**](EncryptionKey) post_recording_recordingkeys()


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

[**EncryptionKey**](EncryptionKey)


## post_recording_uploads_reports

> [**RecordingUploadReport**](RecordingUploadReport) post_recording_uploads_reports(body)


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
| **body** | [**RecordingUploadReportRequest**](RecordingUploadReportRequest)| Report parameters |  |

### Return type

[**RecordingUploadReport**](RecordingUploadReport)


## post_recordings_deletionprotection

> [**list[AddressableEntityRef]**](AddressableEntityRef) post_recordings_deletionprotection(body)


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
| **body** | [**ConversationDeletionProtectionQuery**](ConversationDeletionProtectionQuery)| conversationIds |  |

### Return type

[**list[AddressableEntityRef]**](AddressableEntityRef)


## post_recordings_screensessions_acknowledge

>  post_recordings_screensessions_acknowledge(body)


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
| **body** | [**AcknowledgeScreenRecordingRequest**](AcknowledgeScreenRecordingRequest)| AcknowledgeScreenRecordingRequest |  |

### Return type

void (empty response body)


## post_recordings_screensessions_metadata

>  post_recordings_screensessions_metadata(body)


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
| **body** | [**ScreenRecordingMetaDataRequest**](ScreenRecordingMetaDataRequest)| ScreenRecordingMetaDataRequest |  |

### Return type

void (empty response body)


## put_conversation_recording

> [**Recording**](Recording) put_conversation_recording(conversation_id, recording_id, body, clear_export=clear_export)


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
| **body** | [**Recording**](Recording)| recording |  |
| **clear_export** | **bool**| Whether to clear the pending export for the recording | [optional]  |

### Return type

[**Recording**](Recording)


## put_conversation_recording_annotation

> [**Annotation**](Annotation) put_conversation_recording_annotation(conversation_id, recording_id, annotation_id, body)


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
| **body** | [**Annotation**](Annotation)| annotation |  |

### Return type

[**Annotation**](Annotation)


## put_orphanrecording

> [**Recording**](Recording) put_orphanrecording(orphan_id, body=body)


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
| **body** | [**OrphanUpdateRequest**](OrphanUpdateRequest)|  | [optional]  |

### Return type

[**Recording**](Recording)


## put_recording_crossplatform_mediaretentionpolicy

> [**CrossPlatformPolicy**](CrossPlatformPolicy) put_recording_crossplatform_mediaretentionpolicy(policy_id, body)


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
| **body** | [**CrossPlatformPolicy**](CrossPlatformPolicy)| Policy |  |

### Return type

[**CrossPlatformPolicy**](CrossPlatformPolicy)


## put_recording_job

> [**RecordingJob**](RecordingJob) put_recording_job(job_id, body)


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
| **body** | [**ExecuteRecordingJobsQuery**](ExecuteRecordingJobsQuery)| query |  |

### Return type

[**RecordingJob**](RecordingJob)


## put_recording_keyconfiguration

> [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration) put_recording_keyconfiguration(key_configuration_id, body)


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
| **body** | [**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)| Encryption key configuration metadata |  |

### Return type

[**RecordingEncryptionConfiguration**](RecordingEncryptionConfiguration)


## put_recording_mediaretentionpolicy

> [**Policy**](Policy) put_recording_mediaretentionpolicy(policy_id, body)


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
| **body** | [**Policy**](Policy)| Policy |  |

### Return type

[**Policy**](Policy)


## put_recording_recordingkeys_rotationschedule

> [**KeyRotationSchedule**](KeyRotationSchedule) put_recording_recordingkeys_rotationschedule(body)


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
| **body** | [**KeyRotationSchedule**](KeyRotationSchedule)| KeyRotationSchedule |  |

### Return type

[**KeyRotationSchedule**](KeyRotationSchedule)


## put_recording_settings

> [**RecordingSettings**](RecordingSettings) put_recording_settings(body)


Update the Recording Settings for the Organization

Wraps PUT /api/v2/recording/settings 

Requires ANY permissions: 

* recording:settings:editScreenRecordings
* recording:settings:editRegionalStorage
* recording:settings:editUrlExpiration

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
| **body** | [**RecordingSettings**](RecordingSettings)| Recording settings |  |

### Return type

[**RecordingSettings**](RecordingSettings)


## put_recordings_deletionprotection

>  put_recordings_deletionprotection(protect=protect, body=body)


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
| **body** | [**ConversationDeletionProtectionQuery**](ConversationDeletionProtectionQuery)|  | [optional]  |

### Return type

void (empty response body)


_PureCloudPlatformClientV2 222.0.0_
