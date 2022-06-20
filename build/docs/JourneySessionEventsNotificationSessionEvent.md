---
title: JourneySessionEventsNotificationSessionEvent
---
## JourneySessionEventsNotificationSessionEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **self_uri** | **str** |  | [optional] |
| **created_date** | **datetime** |  | [optional] |
| **ended_date** | **datetime** |  | [optional] |
| **external_contact** | [**JourneySessionEventsNotificationExternalContact**](JourneySessionEventsNotificationExternalContact.html) |  | [optional] |
| **customer_id** | **str** |  | [optional] |
| **customer_id_type** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **external_id** | **str** |  | [optional] |
| **external_url** | **str** |  | [optional] |
| **outcome_achievements** | [**list[JourneySessionEventsNotificationOutcomeAchievement]**](JourneySessionEventsNotificationOutcomeAchievement.html) |  | [optional] |
| **segment_assignments** | [**list[JourneySessionEventsNotificationSegmentAssignment]**](JourneySessionEventsNotificationSegmentAssignment.html) |  | [optional] |
| **attributes** | [**dict(str, JourneySessionEventsNotificationCustomEventAttribute)**](JourneySessionEventsNotificationCustomEventAttribute.html) |  | [optional] |
| **attribute_lists** | [**dict(str, JourneySessionEventsNotificationCustomEventAttributeList)**](JourneySessionEventsNotificationCustomEventAttributeList.html) |  | [optional] |
| **away_date** | **datetime** |  | [optional] |
| **browser** | [**JourneySessionEventsNotificationBrowser**](JourneySessionEventsNotificationBrowser.html) |  | [optional] |
| **device** | [**JourneySessionEventsNotificationDevice**](JourneySessionEventsNotificationDevice.html) |  | [optional] |
| **geolocation** | [**JourneySessionEventsNotificationGeoLocation**](JourneySessionEventsNotificationGeoLocation.html) |  | [optional] |
| **idle_date** | **datetime** |  | [optional] |
| **ip_address** | **str** |  | [optional] |
| **ip_organization** | **str** |  | [optional] |
| **last_page** | [**JourneySessionEventsNotificationPage**](JourneySessionEventsNotificationPage.html) |  | [optional] |
| **mkt_campaign** | [**JourneySessionEventsNotificationMktCampaign**](JourneySessionEventsNotificationMktCampaign.html) |  | [optional] |
| **referrer** | [**JourneySessionEventsNotificationReferrer**](JourneySessionEventsNotificationReferrer.html) |  | [optional] |
| **search_terms** | **list[str]** |  | [optional] |
| **user_agent_string** | **str** |  | [optional] |
| **duration_in_seconds** | **int** |  | [optional] |
| **event_count** | **int** |  | [optional] |
| **pageview_count** | **int** |  | [optional] |
| **screenview_count** | **int** |  | [optional] |
| **last_event** | [**JourneySessionEventsNotificationSessionLastEvent**](JourneySessionEventsNotificationSessionLastEvent.html) |  | [optional] |
| **conversation** | [**JourneySessionEventsNotificationConversation**](JourneySessionEventsNotificationConversation.html) |  | [optional] |
| **originating_direction** | **str** |  | [optional] |
| **conversation_subject** | **str** |  | [optional] |
| **last_user_disposition** | [**JourneySessionEventsNotificationConversationUserDisposition**](JourneySessionEventsNotificationConversationUserDisposition.html) |  | [optional] |
| **last_connected_user** | [**JourneySessionEventsNotificationUser**](JourneySessionEventsNotificationUser.html) |  | [optional] |
| **last_connected_queue** | [**JourneySessionEventsNotificationConnectedQueue**](JourneySessionEventsNotificationConnectedQueue.html) |  | [optional] |
| **conversation_channels** | [**list[JourneySessionEventsNotificationConversationChannel]**](JourneySessionEventsNotificationConversationChannel.html) |  | [optional] |
| **last_user_disconnect_type** | **str** |  | [optional] |
| **last_acd_outcome** | **str** |  | [optional] |
| **authenticated** | **bool** |  | [optional] |
{: class="table table-striped"}


