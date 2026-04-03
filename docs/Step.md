# Step

## Step

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Step. | [optional] |
| **description** | str | The description of the Step. | [optional] |
| **date_created** | datetime | The Step creation date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The Step modification date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | The Step completion date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_started** | datetime | The Step start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The ID of the User who modified the Step. | [optional] |
| **version** | int | The version of the Step. | [optional] |
| **status** | str | The Status of the Step. | [optional] |
| **stage** | [StageReference](StageReference) | The parent stage of the step. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **case** | [CaseReference](CaseReference) | The parent case of the step. | [optional] |



_PureCloudPlatformClientV2 255.0.0_
