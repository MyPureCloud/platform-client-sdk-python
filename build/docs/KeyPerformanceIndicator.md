# KeyPerformanceIndicator

## KeyPerformanceIndicator

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Key Performance Indicator. | [optional] |
| **optimization_type** | str | The optimization type of the Key Performance Indicator. | [optional] |
| **problem_type** | str | The problem type of the Key Performance Indicator. | [optional] |
| **date_created** | datetime | DateTime indicating when the Key Performance Indicator was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | DateTime indicating when the Key Performance Indicator was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **description** | str | The description of the Key Performance Indicator. | [optional] |
| **kpi_type** | str | The type of Key Performance Indicator. | [optional] |
| **source** | str | Source of values for Key Performance Indicator. | [optional] |
| **wrap_up_code_config** | [WrapUpCodeConfig](WrapUpCodeConfig) | Defines what wrap up codes are mapped to Key Performance Indicator. | [optional] |
| **outcome_config** | [OutcomeConfig](OutcomeConfig) | Defines what outcome ids are mapped to Key Performance Indicator. | [optional] |
| **status** | str | The status of the Key Performance Indicator. | [optional] |
| **kpi_group** | str | The group the Key Performance Indicator belongs to. | [optional] |
| **queues** | list[str] | Queue IDs on which KPI specification is used. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.0.0_
