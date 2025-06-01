# JourneySessionEventsNotificationSessionEvent

## JourneySessionEventsNotificationSessionEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **self_uri** | str |  | [optional] |
| **created_date** | datetime |  | [optional] |
| **ended_date** | datetime |  | [optional] |
| **external_contact** | [JourneySessionEventsNotificationExternalContact](JourneySessionEventsNotificationExternalContact) |  | [optional] |
| **customer_id** | str |  | [optional] |
| **customer_id_type** | str |  | [optional] |
| **type** | str |  | [optional] |
| **outcome_achievements** | [list[JourneySessionEventsNotificationOutcomeAchievement]](JourneySessionEventsNotificationOutcomeAchievement) |  | [optional] |
| **segment_assignments** | [list[JourneySessionEventsNotificationSegmentAssignment]](JourneySessionEventsNotificationSegmentAssignment) |  | [optional] |
| **away_date** | datetime |  | [optional] |
| **browser** | [JourneySessionEventsNotificationBrowser](JourneySessionEventsNotificationBrowser) |  | [optional] |
| **device** | [JourneySessionEventsNotificationDevice](JourneySessionEventsNotificationDevice) |  | [optional] |
| **geolocation** | [JourneySessionEventsNotificationGeoLocation](JourneySessionEventsNotificationGeoLocation) |  | [optional] |
| **idle_date** | datetime |  | [optional] |
| **ip_address** | str |  | [optional] |
| **ip_organization** | str |  | [optional] |
| **last_page** | [JourneySessionEventsNotificationPage](JourneySessionEventsNotificationPage) |  | [optional] |
| **mkt_campaign** | [JourneySessionEventsNotificationMktCampaign](JourneySessionEventsNotificationMktCampaign) |  | [optional] |
| **referrer** | [JourneySessionEventsNotificationReferrer](JourneySessionEventsNotificationReferrer) |  | [optional] |
| **search_terms** | list[str] |  | [optional] |
| **user_agent_string** | str |  | [optional] |
| **duration_in_seconds** | int |  | [optional] |
| **event_count** | int |  | [optional] |
| **pageview_count** | int |  | [optional] |
| **screenview_count** | int |  | [optional] |
| **last_event** | [JourneySessionEventsNotificationSessionLastEvent](JourneySessionEventsNotificationSessionLastEvent) |  | [optional] |
| **conversation** | [JourneySessionEventsNotificationConversation](JourneySessionEventsNotificationConversation) |  | [optional] |
| **originating_direction** | str |  | [optional] |
| **conversation_subject** | str |  | [optional] |
| **last_user_disposition** | [JourneySessionEventsNotificationConversationUserDisposition](JourneySessionEventsNotificationConversationUserDisposition) |  | [optional] |
| **last_connected_user** | [JourneySessionEventsNotificationUser](JourneySessionEventsNotificationUser) |  | [optional] |
| **last_connected_queue** | [JourneySessionEventsNotificationConnectedQueue](JourneySessionEventsNotificationConnectedQueue) |  | [optional] |
| **conversation_channels** | [list[JourneySessionEventsNotificationConversationChannel]](JourneySessionEventsNotificationConversationChannel) |  | [optional] |
| **last_user_disconnect_type** | str |  | [optional] |
| **last_acd_outcome** | str |  | [optional] |
| **authenticated** | bool |  | [optional] |
| **app** | [JourneySessionEventsNotificationApp](JourneySessionEventsNotificationApp) |  | [optional] |
| **sdk_library** | [JourneySessionEventsNotificationSdkLibrary](JourneySessionEventsNotificationSdkLibrary) |  | [optional] |
| **network_connectivity** | [JourneySessionEventsNotificationNetworkConnectivity](JourneySessionEventsNotificationNetworkConnectivity) |  | [optional] |
| **division_ids** | list[str] |  | [optional] |
| **last_screen** | str |  | [optional] |



_PureCloudPlatformClientV2 230.0.0_
