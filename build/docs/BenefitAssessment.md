# BenefitAssessment

## BenefitAssessment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **queues** | [list[AddressableEntityRef]](AddressableEntityRef) | The list of queues that are assessed for Predictive Routing benefit. | [optional] |
| **kpi_assessments** | [list[KeyPerformanceIndicatorAssessment]](KeyPerformanceIndicatorAssessment) | A set of key performance indicators applied on the queue to determine suitability of Predictive Routing. | [optional] |
| **state** | str | State of the benefit assessment. | [optional] |
| **job_id** | str | The unique identifier of job that created this benefit assessment. | [optional] |
| **date_created** | datetime | Creation Date of the benefit assessment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Modified Date of the benefit assessment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
