# GuideContentGenerationJob

## GuideContentGenerationJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str | The status of the job. | [optional] |
| **errors** | [list[ErrorBody]](ErrorBody) | The list of errors in case of job failure. | [optional] |
| **guide** | [AddressableEntityRef](AddressableEntityRef) |  | [optional] |
| **guide_content** | [GeneratedGuideContent](GeneratedGuideContent) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 237.0.0_
