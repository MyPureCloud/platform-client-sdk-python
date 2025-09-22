# JourneyViewChart

## JourneyViewChart

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **version** | int | The version of the journey view chart | [optional] |
| **group_by_time** | str | A time unit to group the metrics by. There is a limit on the number of groupBy properties which can be specified. | [optional] |
| **group_by_attributes** | [list[JourneyViewChartGroupByAttribute]](JourneyViewChartGroupByAttribute) | A list of attributes to group the metrics by. There is a limit on the number of groupBy properties which can be specified. | [optional] |
| **metrics** | [list[JourneyViewChartMetric]](JourneyViewChartMetric) | A list of metrics to calculate within the chart by (aka the y axis) | |
| **display_attributes** | [JourneyViewChartDisplayAttributes](JourneyViewChartDisplayAttributes) | Optional display attributes for rendering the chart | [optional] |
| **group_by_max** | int | A maximum on the number of values being grouped by | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 237.0.0_
