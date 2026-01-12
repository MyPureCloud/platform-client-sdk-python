# PolicyConditions

## PolicyConditions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **for_users** | [list[PolicyUser]](PolicyUser) | List of users to apply this policy to. Each user object can include the &#39;id&#39; field containing the user&#39;s unique identifier. Example: [{\&quot;id\&quot;:\&quot;&lt;userId&gt;\&quot;}]. | [optional] |
| **directions** | list[str] |  | [optional] |
| **date_ranges** | list[str] |  | [optional] |
| **media_types** | list[str] |  | [optional] |
| **for_queues** | [list[Queue]](Queue) |  | [optional] |
| **duration** | [DurationCondition](DurationCondition) |  | [optional] |
| **wrapup_codes** | [list[WrapupCode]](WrapupCode) |  | [optional] |
| **time_allowed** | [TimeAllowed](TimeAllowed) |  | [optional] |
| **teams** | [list[Team]](Team) | Teams to match conversations against | [optional] |
| **customer_participation** | str | This condition is to filter out conversation with and without customer participation. | [optional] |



_PureCloudPlatformClientV2 247.0.0_
