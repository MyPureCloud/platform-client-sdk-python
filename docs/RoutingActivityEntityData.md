# RoutingActivityEntityData

## RoutingActivityEntityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **activity_date** | datetime | The time at which the activity was observed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **organization_presence_id** | str | Organization presence identifier | [optional] |
| **presence_date** | datetime | Date of the latest presence change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **queue_id** | str | Queue identifier | [optional] |
| **queue_membership_status** | str | Queue membership status (e.g. active or inactive) | [optional] |
| **routing_status** | str | Agent routing status | [optional] |
| **routing_status_date** | datetime | Date of the latest routing status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **system_presence** | str | System presence | [optional] |
| **team_id** | str | The team ID the user is a member of | [optional] |
| **user_id** | str | Unique identifier for the user | [optional] |



_PureCloudPlatformClientV2 218.0.0_
