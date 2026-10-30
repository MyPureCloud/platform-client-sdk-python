# SelfScheduleOffersJob

## SelfScheduleOffersJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **status** | str | The status of the job | |
| **download_url** | str | URL from which to fetch results for requests. Populated if status &#x3D;&#x3D; ‘Complete&#39;. The downloaded data will conform to the schema defined in downloadResultTemplate | [optional] |
| **download_result_template** | [SelfScheduleOffersResultTemplate](SelfScheduleOffersResultTemplate) | Schema template for deserializing lookup offers results returned from the downloadUrl | [optional] |
| **error** | [ErrorBody](ErrorBody) | Any error information, only set if the status &#x3D;&#x3D; &#39;Error&#39; | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 270.0.0_
