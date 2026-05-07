# PredictiveRoutingCustomKpiAttributionEvent

## PredictiveRoutingCustomKpiAttributionEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (UUID) eventId for this event | |
| **event_date_time** | datetime | A timestamp as epoch representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **external_contact_id** | str | The UUID of the external contact associated with this event | [optional] |
| **conversation_id** | str | The UUID of the conversation associated with this event | [optional] |
| **agent_id** | str | The UUID of the agent associated with this event | [optional] |
| **kpi_id** | str | The UUID of the KPI associated with this event | |
| **associated_value** | float | The value associated with this outcome attribution | |



_PureCloudPlatformClientV2 257.0.0_
