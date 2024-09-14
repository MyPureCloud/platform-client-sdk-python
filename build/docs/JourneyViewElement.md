# JourneyViewElement

## JourneyViewElement

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The unique identifier of the element within the elements list | |
| **name** | str | The unique name of the element within the view | |
| **attributes** | [JourneyViewElementAttributes](JourneyViewElementAttributes) | Required attributes of the element | |
| **filter** | [JourneyViewElementFilter](JourneyViewElementFilter) | Any filters applied to this element | [optional] |
| **followed_by** | [list[JourneyViewLink]](JourneyViewLink) | A list of JourneyViewLink objects, listing the elements downstream of this element | [optional] |



_PureCloudPlatformClientV2 211.1.0_
