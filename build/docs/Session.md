---
title: Session
---
## Session

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **customer_id** | **str** | Primary identifier of the customer in the source where the events for the session originate from. | [optional] |
| **customer_id_type** | **str** | Type of source customer identifier (e.g. cookie, email, phone). | [optional] |
| **type** | **str** | Session types indicate the type or category of sessions (e.g. web, ticket, delivery, atm). | [optional] |
| **external_id** | **str** | Unique identifier in the external system where the events for the session originate from. | [optional] |
| **external_url** | **str** | A URL that identifies an external system-of-record resource that may have more detailed information on the session. | [optional] |
| **short_id** | **str** | Shortened numeric identifier of 4-6 digits. | [optional] |
| **outcome_achievements** | [**list[OutcomeAchievement]**](OutcomeAchievement.html) | List of the outcome achievements by the customer in this session. | [optional] |
| **segment_assignments** | [**list[SessionSegmentAssignment]**](SessionSegmentAssignment.html) | List of the segment assignments to the customer in this session. | [optional] |
| **attributes** | [**dict(str, CustomEventAttribute)**](CustomEventAttribute.html) | Attributes projected from the session&#39;s event stream. | [optional] |
| **attribute_lists** | [**dict(str, CustomEventAttributeList)**](CustomEventAttributeList.html) | List-type attributes projected from the session&#39;s event stream. | [optional] |
| **browser** | [**Browser**](Browser.html) | Customer&#39;s browser. | [optional] |
| **device** | [**Device**](Device.html) | Customer&#39;s device. | [optional] |
| **geolocation** | [**JourneyGeolocation**](JourneyGeolocation.html) | Customer&#39;s geolocation. | [optional] |
| **ip_address** | **str** | Customer&#39;s IP address. | [optional] |
| **ip_organization** | **str** | Customer&#39;s IP-based organization or ISP name. | [optional] |
| **last_page** | [**JourneyPage**](JourneyPage.html) | The webpage where the customer&#39;s last web interaction occurred. | [optional] |
| **mkt_campaign** | [**JourneyCampaign**](JourneyCampaign.html) | Marketing / traffic source information. | [optional] |
| **referrer** | [**Referrer**](Referrer.html) | Identifies the page URL that originally generated the request for the current page being viewed. | [optional] |
| **search_terms** | **list[str]** | Search terms associated with the session. | [optional] |
| **user_agent_string** | **str** | String identifying the user agent. | [optional] |
| **duration_in_seconds** | **int** | Indicates how long the session has been active (valid for an individual device). | [optional] |
| **event_count** | **int** | The count of all events performed during the session. | [optional] |
| **pageview_count** | **int** | The count of all pageviews performed during the session. | [optional] |
| **screenview_count** | **int** | The count of all screenviews performed during the session. | [optional] |
| **last_event** | [**SessionLastEvent**](SessionLastEvent.html) | Information about the most recent event in this session. | [optional] |
| **last_connected_queue** | [**ConnectedQueue**](ConnectedQueue.html) | The last queue connected to this session. | [optional] |
| **last_connected_user** | [**ConnectedUser**](ConnectedUser.html) | The last user connected to this session. | [optional] |
| **last_user_disposition** | [**ConversationUserDisposition**](ConversationUserDisposition.html) | The last user disposition connected to this session. | [optional] |
| **conversation_channels** | [**list[ConversationChannel]**](ConversationChannel.html) | Represents the channels used for this conversation. | [optional] |
| **originating_direction** | **str** | The original direction of the conversation. | [optional] |
| **conversation_subject** | **str** | The subject for the conversation, for example an email subject. | [optional] |
| **last_user_disconnect_type** | **str** | Disconnect reason for the last user connected to the conversation. | [optional] |
| **last_acd_outcome** | **str** | Last ACD outcome for the conversation. | [optional] |
| **authenticated** | **bool** | Indicates whether or not the session is authenticated. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **ended_date** | **datetime** | Timestamp indicating when the session was ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_contact** | [**AddressableEntityRef**](AddressableEntityRef.html) | The external contact associated with this session. | [optional] |
| **away_date** | **datetime** | Timestamp indicating when the visitor should be considered as away. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **idle_date** | **datetime** | Timestamp indicating when the visitor should be considered as idle. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation** | [**AddressableEntityRef**](AddressableEntityRef.html) | The conversation for this session. | [optional] |
{: class="table table-striped"}


