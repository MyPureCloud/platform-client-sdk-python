# ServiceNowSourceRequest

## ServiceNowSourceRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the integration source. | |
| **integration_id** | str | The integration associated with the source. | [optional] |
| **schedule_period** | int | The schedule period of the source in hours. Must be at least 6 and at most 48 hours. | [optional] |
| **settings** | [ServiceNowSettings](ServiceNowSettings) | The settings of the source. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
