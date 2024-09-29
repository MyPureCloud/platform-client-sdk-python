# ManagementUnit

## ManagementUnit

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **business_unit** | [BusinessUnitReference](BusinessUnitReference) | The business unit to which this management unit belongs | [optional] |
| **start_day_of_week** | str | Start day of week for scheduling and forecasting purposes. Moving to Business Unit | [optional] |
| **time_zone** | str | The time zone for the management unit in standard Olson format.  Moving to Business Unit | [optional] |
| **settings** | [ManagementUnitSettingsResponse](ManagementUnitSettingsResponse) | The configuration settings for this management unit | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version info metadata for this management unit. Deprecated, use settings.metadata | [optional] |
| **division** | [DivisionReference](DivisionReference) | The division to which this entity belongs. | [optional] |
| **version** | int | The version of the underlying entity.  Deprecated, use field from settings.metadata instead | [optional] |
| **date_modified** | datetime | The date and time at which this entity was last modified.  Deprecated, use field from settings.metadata instead. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who last modified this entity.  Deprecated, use field from settings.metadata instead | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 212.0.0_
