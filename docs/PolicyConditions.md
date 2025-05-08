# PolicyConditions

## PolicyConditions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **for_users** | [list[User]](User) |  | [optional] |
| **directions** | list[str] |  | [optional] |
| **date_ranges** | list[str] |  | [optional] |
| **media_types** | list[str] |  | [optional] |
| **for_queues** | [list[Queue]](Queue) |  | [optional] |
| **duration** | [DurationCondition](DurationCondition) |  | [optional] |
| **wrapup_codes** | [list[WrapupCode]](WrapupCode) |  | [optional] |
| **time_allowed** | [TimeAllowed](TimeAllowed) |  | [optional] |
| **teams** | [list[Team]](Team) | Teams to match conversations against | [optional] |
| **customer_participation** | str | This condition is to filter out conversation with and without customer participation. | [optional] |



_PureCloudPlatformClientV2 227.1.0_
