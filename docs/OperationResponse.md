# OperationResponse

## OperationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str | Status of the operation. | [optional] |
| **type** | str | Type of the operation. | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the operation. | [optional] |
| **date_created** | datetime | Operation creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Operation last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **source** | [KnowledgeOperationSource](KnowledgeOperationSource) | Source of the operation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.0.0_
