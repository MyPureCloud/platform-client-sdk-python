# Stage

## Stage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Stage. | [optional] |
| **description** | str | The description of the Stage. | [optional] |
| **date_created** | datetime | The Stage creation date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The Stage modification date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | The Stage completion date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_started** | datetime | The Stage start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The ID of the User who modified the Stage. | [optional] |
| **version** | int | The version of the Stage. | [optional] |
| **status** | str | The Status of the Stage. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **case** | [CaseReference](CaseReference) | The parent case of the Stage. | [optional] |



_PureCloudPlatformClientV2 257.0.0_
