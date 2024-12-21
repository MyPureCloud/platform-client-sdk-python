# BillingUsageReport

## BillingUsageReport

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **start_date** | datetime | The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **end_date** | datetime | The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **status** | str | Generation status of report | [optional] |
| **usages** | [list[BillingUsage]](BillingUsage) | The usages for the given period. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 219.0.0_
