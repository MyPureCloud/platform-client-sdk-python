# TrusteeBillingOverview

## TrusteeBillingOverview

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **organization** | [NamedEntity](NamedEntity) | Organization | |
| **currency** | str | The currency type. | |
| **enabled_products** | list[str] | The charge short names for products enabled during the specified period. | |
| **subscription_type** | str | The subscription type. | |
| **ramp_period_start_date** | datetime | Date-time the ramp period starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **ramp_period_end_date** | datetime | Date-time the ramp period ends. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **billing_period_start_date** | datetime | Date-time the billing period started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **billing_period_end_date** | datetime | Date-time the billing period ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **usages** | [list[SubscriptionOverviewUsage]](SubscriptionOverviewUsage) | Usages for the specified period. | |
| **contract_amendment_date** | datetime | Date-time the contract was last amended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **contract_effective_date** | datetime | Date-time the contract became effective. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **contract_end_date** | datetime | Date-time the contract ends. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **minimum_monthly_amount** | str | Minimum amount that will be charged for the month | [optional] |
| **in_ramp_period** | bool |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
