# BulkUpdateShiftTradeStateResultItem

## BulkUpdateShiftTradeStateResultItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **state** | str | The state of the shift trade after the update request is processed | [optional] |
| **reviewed_by** | [UserReference](UserReference) | The user who reviewed the request, if applicable. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **reviewed_date** | datetime | The date the request was reviewed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **failure_reason** | str | The reason the update failed, if applicable | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the shift trade | [optional] |



_PureCloudPlatformClientV2 224.0.0_
