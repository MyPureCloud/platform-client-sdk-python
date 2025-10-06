# ConversationContentDatePicker

## ConversationContentDatePicker

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Optional unique identifier to help map component replies to form messages where multiple DatePickers can be present. | [optional] |
| **title** | str | Text to show in the title. | [optional] |
| **subtitle** | str | Text to show in the description. | [optional] |
| **image_url** | str | URL of an image | [optional] |
| **date_minimum** | datetime | The minimum Date Enabled in the datepicker calendar, format: ISO 8601. | [optional] |
| **date_maximum** | datetime | The maximum Date Enabled in the datepicker calendar, format: ISO 8601. | [optional] |
| **location** | [ConversationContentLocation](ConversationContentLocation) | Location of the event. | [optional] |
| **available_times** | [list[ConversationContentDatePickerAvailableTime]](ConversationContentDatePickerAvailableTime) | An array of available times objects. | [optional] |
| **date_display_format** | str | The format the date should be presented to the end user. | [optional] |



_PureCloudPlatformClientV2 240.0.0_
