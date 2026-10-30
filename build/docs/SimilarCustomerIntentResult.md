# SimilarCustomerIntentResult

## SimilarCustomerIntentResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Name of the customer intent | |
| **description** | str | Description of the customer intent | |
| **expiry_time** | int | Expiry time in hours of the customer intent | |
| **distance** | float | The distance score indicating similarity (lower is more similar) | [optional] |
| **category** | [SimilarEntityRef](SimilarEntityRef) | The category of the similar customer intent | [optional] |
| **date_created** | datetime | Creation date of the customer intent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 270.0.0_
