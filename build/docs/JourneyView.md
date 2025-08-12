# JourneyView

## JourneyView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | A description of the journey view | [optional] |
| **version** | int | The version of the journey view | [optional] |
| **created_by** | [JourneyViewUser](JourneyViewUser) | User that has created the view. | [optional] |
| **modified_by** | [JourneyViewUser](JourneyViewUser) | User that has modified the view. | [optional] |
| **interval** | str | An absolute timeframe for the journey view, expressed as an ISO 8601 interval. Only one of interval or duration must be specified. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **duration** | str | A relative timeframe for the journey view, expressed as an ISO 8601 duration. Only one of interval or duration must be specified. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **elements** | [list[JourneyViewElement]](JourneyViewElement) | The elements within the journey view | |
| **charts** | [list[JourneyViewChart]](JourneyViewChart) | A list of charts to measure within context of the elements of the the journey view | [optional] |
| **date_created** | datetime | The date when the journey view was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date when this version of the journey view was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.0.0_
