---
title: Event
---
## Event

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | System-generated UUID for the event. | [optional] |
| **correlation_id** | **str** | UUID corresponding to triggering action that caused this event (e.g. HTTP POST, SIP invite, another event). | [optional] |
| **customer_id** | **str** | Primary identifier of the customer in the source of the events. | [optional] |
| **customer_id_type** | **str** | Type of primary identifier (e.g. cookie, email, phone). | [optional] |
| **session** | [**EventSession**](EventSession.html) | The session that the event belongs to. | [optional] |
| **event_type** | **str** | The name representing the type of event. | |
| **generic_action_event** | [**GenericActionEvent**](GenericActionEvent.html) | Event triggered by generic actions. | [optional] |
| **outcome_achieved_event** | [**OutcomeAchievedEvent**](OutcomeAchievedEvent.html) | Event where a customer has achieved a specific outcome or goal. | [optional] |
| **segment_assigned_event** | [**SegmentAssignedEvent**](SegmentAssignedEvent.html) | Event that represents a segment being assigned (deprecated). | [optional] |
| **segment_assignment_event** | [**SegmentAssignmentEvent**](SegmentAssignmentEvent.html) | Event that represents a segment being assigned. | [optional] |
| **web_action_event** | [**WebActionEvent**](WebActionEvent.html) | Event triggered by web actions. | [optional] |
| **web_event** | [**WebEvent**](WebEvent.html) | Event that tracks user interactions with content in a browser such as pageviews, downloads, mobile ad clicks, etc. | [optional] |
| **app_event** | [**AppEvent**](AppEvent.html) | Event that tracks user interactions with content in an application such as screen views, searches, etc. | [optional] |
| **created_date** | **datetime** | Timestamp indicating when the event actually took place. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}

