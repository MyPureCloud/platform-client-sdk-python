# DashboardConfiguration

## DashboardConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of dashboard configuration. | |
| **rows** | int | The count of rows for the specific dashboard configuration. | [optional] |
| **columns** | int | The count of columns for the specific dashboard. | [optional] |
| **widgets** | [list[Widget]](Widget) | List of widgets for dashboard configuration. | |
| **favorite** | bool | The flag indicates if the dashboard is favorited by the user | [optional] |
| **public_dashboard** | bool | The flag to indicate if the dashboard is published by an user | [optional] |
| **restricted** | bool | The flag to indicate if the dashboard has any restricted data for that user | [optional] |
| **layout_type** | str | The layout type of the dashboard | [optional] |
| **date_created** | datetime | The created date of the dashboard. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_modified** | datetime | The last modified date of the dashboard. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_deleted** | datetime | The deleted date of the dashboard. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **created_by** | [AddressableEntityRef](AddressableEntityRef) | The id of user who created the dashboard | [optional] |
| **shared** | bool | The flag to indicate if the dashboard is shared | [optional] |
| **dashboards_shared_with** | [DashboardsSharedWith](DashboardsSharedWith) | The list of users and teams the dashboard is shared with | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_
