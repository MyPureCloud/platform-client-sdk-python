# Event

## Event

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | System-generated UUID for the event. | |
| **correlation_id** | str | UUID corresponding to triggering action that caused this event (e.g. HTTP POST, SIP invite, another event). | |
| **customer_id** | str | Primary identifier of the customer in the source of the events. | [optional] |
| **customer_id_type** | str | Type of primary identifier (e.g. cookie, email, phone). | [optional] |
| **session** | [EventSession](EventSession) | The session that the event belongs to. | |
| **event_type** | str | The name representing the type of event. | |
| **outcome_achieved_event** | [OutcomeAchievedEvent](OutcomeAchievedEvent) | Event where a customer has achieved a specific outcome or goal. | [optional] |
| **segment_assignment_event** | [SegmentAssignmentEvent](SegmentAssignmentEvent) | Event that represents a segment being assigned. | [optional] |
| **web_action_event** | [WebActionEvent](WebActionEvent) | Event triggered by web actions. | [optional] |
| **web_event** | [WebEvent](WebEvent) | Event that tracks user interactions with content in a browser such as pageviews, downloads, mobile ad clicks, etc. | [optional] |
| **app_event** | [AppEvent](AppEvent) | Event that tracks user interactions with content in an application such as screen views, searches, etc. | [optional] |
| **created_date** | datetime | Timestamp indicating when the event actually took place. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 248.0.0_
