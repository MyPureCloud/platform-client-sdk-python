---
title: UserRoutingStatusEvent
---
## UserRoutingStatusEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | **str** | A unique (UUID) eventId for this event | |
| **event_date_time** | **datetime** | A timestamp as epoch representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **agent_id** | **str** | Unique identifier of the agent. | |
| **status** | **str** | The agent&#39;s current routing status. | |
| **source_id** | **str** | The agent&#39;s source platform Id. | |
{: class="table table-striped"}


