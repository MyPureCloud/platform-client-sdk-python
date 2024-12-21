# Annotation

## Annotation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **type** | str |  | [optional] |
| **location** | int | Offset of annotation in milliseconds. | [optional] |
| **duration_ms** | int | Duration of annotation in milliseconds. | [optional] |
| **absolute_location** | int | Offset of annotation (milliseconds) from start of recording (after removing the cumulative duration of all pauses). | [optional] |
| **absolute_duration_ms** | int | Duration of annotation (milliseconds). | [optional] |
| **recording_location** | int | Offset of annotation (milliseconds) from start of recording, adjusted for any recording cuts | [optional] |
| **recording_duration_ms** | int | Duration of annotation (milliseconds), adjusted for any recording cuts. | [optional] |
| **user** | [User](User) | User that created this annotation (if any). | [optional] |
| **description** | str | Text of annotation. Maximum character limit is 500. | [optional] |
| **reason** | str | Reason for a pause annotation. Valid values: Hold,SecurePause,FlowOrQueue,Pause | [optional] |
| **annotations** | [list[Annotation]](Annotation) | List of annotations | [optional] |
| **realtime_location** | int | Offset of annotation (milliseconds) from start of the recording before removing the cumulative duration of all pauses before this annotation | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 219.0.0_
