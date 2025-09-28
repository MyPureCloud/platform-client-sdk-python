# AppEventResponse

## AppEventResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | System-generated UUID for the event. | |
| **customer_id** | str | Identifier of the customer in the source of the event. | |
| **customer_id_type** | str | Type of identifier for the customer ID (cookie, email etc.). | |
| **event_name** | str | Represents the action the customer performed. A good event name is typically an object followed by the action performed in past tense (e.g. screen_viewed, order_completed, user_registered). | |
| **screen_name** | str | The name of the screen in the app that the event took place. | |
| **app** | [JourneyApp](JourneyApp) | Application that the customer is interacting with. | |
| **device** | [Device](Device) | Customer&#39;s device. | |
| **ip_organization** | str | Customer&#39;s IP-based organization or ISP name. | [optional] |
| **geolocation** | [JourneyGeolocation](JourneyGeolocation) | Customer&#39;s geolocation. | [optional] |
| **sdk_library** | [SdkLibrary](SdkLibrary) | SDK library used to generate the event. | [optional] |
| **network_connectivity** | [NetworkConnectivity](NetworkConnectivity) | Information relating to the device&#39;s network connectivity. | [optional] |
| **mkt_campaign** | [JourneyCampaign](JourneyCampaign) | Marketing / traffic source information. | [optional] |
| **session** | [AppEventResponseSession](AppEventResponseSession) | The app session the event belongs to. | |
| **search_query** | str | Represents the keywords in a customer search query. | [optional] |
| **attributes** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | User-defined attributes associated with a particular event. | |
| **traits** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | Traits are attributes intrinsic to the customer that may be sent in selected events (e.g. email, givenName, cellPhone). | |
| **created_date** | datetime | UTC timestamp indicating when the event actually took place. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 238.0.0_
