# EmailMediaPolicyConditions

## EmailMediaPolicyConditions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **for_users** | [list[PolicyUser]](PolicyUser) | List of users to apply this policy to. Each user object can include the &#39;id&#39; field containing the user&#39;s unique identifier. Example: [{\&quot;id\&quot;:\&quot;&lt;userId&gt;\&quot;}]. | [optional] |
| **date_ranges** | list[str] |  | [optional] |
| **for_queues** | [list[Queue]](Queue) |  | [optional] |
| **wrapup_codes** | [list[WrapupCode]](WrapupCode) |  | [optional] |
| **languages** | [list[Language]](Language) |  | [optional] |
| **time_allowed** | [TimeAllowed](TimeAllowed) |  | [optional] |
| **teams** | [list[Team]](Team) | Teams to match conversations against | [optional] |
| **customer_participation** | str |  | [optional] |



_PureCloudPlatformClientV2 246.1.0_
