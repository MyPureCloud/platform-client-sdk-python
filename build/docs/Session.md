# Session

## Session

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the session. | |
| **customer_id** | str | Primary identifier of the customer in the source where the events for the session originate from. | [optional] |
| **customer_id_type** | str | Type of source customer identifier (e.g. cookie, email, phone). | [optional] |
| **type** | str | Session types indicate the type or category of sessions (e.g. web, app). | |
| **external_id** | str | Unique identifier in the external system where the events for the session originate from. | [optional] |
| **external_url** | str | A URL that identifies an external system-of-record resource that may have more detailed information on the session. | [optional] |
| **short_id** | str | Shortened numeric identifier of 4-6 digits. | [optional] |
| **outcome_achievements** | [list[OutcomeAchievement]](OutcomeAchievement) | List of the outcome achievements by the customer in this session. | [optional] |
| **segment_assignments** | [list[SessionSegmentAssignment]](SessionSegmentAssignment) | List of the segment assignments to the customer in this session. | [optional] |
| **attributes** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | Attributes projected from the session&#39;s event stream. | [optional] |
| **attribute_lists** | [dict(str, CustomEventAttributeList)](CustomEventAttributeList) | List-type attributes projected from the session&#39;s event stream. | [optional] |
| **browser** | [Browser](Browser) | Customer&#39;s browser. | [optional] |
| **device** | [Device](Device) | Customer&#39;s device. | [optional] |
| **geolocation** | [JourneyGeolocation](JourneyGeolocation) | Customer&#39;s geolocation. | [optional] |
| **ip_address** | str | Customer&#39;s IP address. | [optional] |
| **ip_organization** | str | Customer&#39;s IP-based organization or ISP name. | [optional] |
| **last_page** | [JourneyPage](JourneyPage) | The webpage where the customer&#39;s last web interaction occurred. | [optional] |
| **mkt_campaign** | [JourneyCampaign](JourneyCampaign) | Marketing / traffic source information. | [optional] |
| **referrer** | [Referrer](Referrer) | Identifies the page URL that originally generated the request for the current page being viewed. | [optional] |
| **app** | [JourneyApp](JourneyApp) | Application that the customer is interacting with (for app sessions). | [optional] |
| **sdk_library** | [SdkLibrary](SdkLibrary) | SDK library used to generate the events for the session (for app and web sessions). | [optional] |
| **network_connectivity** | [NetworkConnectivity](NetworkConnectivity) | Information relating to the device&#39;s network connectivity (for app sessions). | [optional] |
| **search_terms** | list[str] | Search terms associated with the session. | [optional] |
| **user_agent_string** | str | String identifying the user agent. | [optional] |
| **duration_in_seconds** | int | Indicates how long the session has been active (valid for an individual device). | [optional] |
| **event_count** | int | The count of all events performed during the session. | |
| **pageview_count** | int | The count of all pageviews performed during the session. | [optional] |
| **screenview_count** | int | The count of all screenviews performed during the session. | [optional] |
| **last_event** | [SessionLastEvent](SessionLastEvent) | Information about the most recent event in this session. | |
| **last_connected_queue** | [ConnectedQueue](ConnectedQueue) | The last queue connected to this session. | [optional] |
| **last_connected_user** | [ConnectedUser](ConnectedUser) | The last user connected to this session. | [optional] |
| **last_user_disposition** | [ConversationUserDisposition](ConversationUserDisposition) | The last user disposition connected to this session. | [optional] |
| **conversation_channels** | [list[ConversationChannel]](ConversationChannel) | Represents the channels used for this conversation. | [optional] |
| **originating_direction** | str | The original direction of the conversation. | [optional] |
| **conversation_subject** | str | The subject for the conversation, for example an email subject. | [optional] |
| **last_user_disconnect_type** | str | Disconnect reason for the last user connected to the conversation. | [optional] |
| **last_acd_outcome** | str | Last ACD outcome for the conversation. | [optional] |
| **authenticated** | bool | Indicates whether or not the session is authenticated. | |
| **division_ids** | list[str] | List of division IDs associated with the session. | [optional] |
| **last_screen** | str | The app screen name where the customer&#39;s last app interaction occurred. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **created_date** | datetime | Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **ended_date** | datetime | Timestamp indicating when the session was ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_contact** | [AddressableEntityRef](AddressableEntityRef) | The external contact associated with this session. | [optional] |
| **away_date** | datetime | Timestamp indicating when the visitor should be considered as away. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **idle_date** | datetime | Timestamp indicating when the visitor should be considered as idle. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation** | [AddressableEntityRef](AddressableEntityRef) | The conversation for this session. | [optional] |



_PureCloudPlatformClientV2 224.1.0_
