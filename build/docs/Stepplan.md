# Stepplan

## Stepplan

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Stepplan. | [optional] |
| **description** | str | The description of the Stepplan. | [optional] |
| **caseplan** | [CaseplanReference](CaseplanReference) | The Caseplan of the Stepplan. | [optional] |
| **stageplan** | [StageplanReference](StageplanReference) | The Stageplan of the Stepplan. | [optional] |
| **date_created** | datetime | The Stepplan creation date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The Stepplan modification date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The ID of the User who modified the Stepplan. | [optional] |
| **activity_type** | str | The activityType of the Stepplan. | [optional] |
| **workitem_settings** | [WorkitemSettingsResponse](WorkitemSettingsResponse) | The workitemSettings of the Stepplan. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 256.0.0_
