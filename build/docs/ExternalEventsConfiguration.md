# ExternalEventsConfiguration

## ExternalEventsConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The unique identifier for the external event configuration. | |
| **name** | str |  | [optional] |
| **description** | str | A description of the external event configuration. | |
| **division_id** | str | The division ID (UUID) associated with this configuration. | |
| **division_id_active** | bool | Indicates whether the divisionId field is valid. | |
| **schema_id** | str | The dynamic schema ID (UUID) that defines the structure of external events. | |
| **schema_active** | bool | Indicates whether the schema is active or inactive. | |
| **source** | str | The source of the external events e.g. Adobe, Salesforce. | |
| **date_last_modified** | datetime | The timestamp when the configuration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.0.0_
