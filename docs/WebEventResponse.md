# WebEventResponse

## WebEventResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **customer_id** | str | Identifier of the customer in the source of the event. | |
| **event_name** | str | Represents the action the customer performed. Event types are created for each unique event name and can be faceted on in segment and outcome conditions. A valid event name must only contain alphanumeric characters and underscores. A good event name is typically an object followed by the action performed in past tense, e.g. page_viewed, order_completed, user_registered. | |
| **customer_id_type** | str | Type of identifier for the customer ID (e.g., cookie). | |
| **page** | [ResponsePage](ResponsePage) | The webpage where the user interaction occurred. | |
| **user_agent_string** | str | HTTP User-Agent string (see https://tools.ietf.org/html/rfc1945#section-10.15). | |
| **browser** | [WebEventBrowser](WebEventBrowser) | Customer&#39;s browser. | |
| **device** | [WebEventDevice](WebEventDevice) | Customer&#39;s device. | |
| **search_query** | str | Represents the keywords in a customer search query. | [optional] |
| **ip_organization** | str | Customer&#39;s IP-based organization or ISP name. | [optional] |
| **geolocation** | [JourneyGeolocation](JourneyGeolocation) | Customer&#39;s geolocation. | [optional] |
| **mkt_campaign** | [JourneyCampaign](JourneyCampaign) | Urchin Tracking Module (UTM) parameters used to track the effectiveness of online marketing campaigns. | [optional] |
| **session** | [WebEventResponseSession](WebEventResponseSession) | The session that the event belongs to. | |
| **referrer** | [Referrer](Referrer) | Identifies the web page that originally generated the request for the current page being viewed. | [optional] |
| **attributes** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | User-defined attributes associated with a particular event. These attributes provide additional context about the event. For example, items_in_cart or subscription_level. | |
| **traits** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | Traits are attributes intrinsic to the customer that may be sent in selected events, (e.g. email, givenName, cellPhone). Traits are used to collect information for identity resolution. For example, the same person might be using an application on different devices which might create two sessions with different customerIds. Additional information can be provided as traits to help link those two sessions and customers to a single external contact through common identifiers that were submitted via a form fill, message, or other input in both sessions. | |
| **authenticated** | bool | Indicates whether the event was produced during an authenticated session. | |
| **created_date** | datetime | UTC timestamp indicating when the event actually took place, events older than an hour will be rejected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 249.0.0_
