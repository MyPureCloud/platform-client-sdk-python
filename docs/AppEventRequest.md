# AppEventRequest

## AppEventRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_name** | str | Represents the action the customer performed. Event types are created for each unique event name and can be faceted on in segment and outcome conditions. A valid event name must only contain alphanumeric characters and underscores. A good event name is typically an object followed by the action performed in past tense, e.g. screen_viewed, search_performed, user_registered. | |
| **screen_name** | str | The name of the screen, view, or fragment in the app where the event took place. | |
| **app** | [JourneyApp](JourneyApp) | Application that the customer is interacting with. | |
| **device** | [RequestDevice](RequestDevice) | Customer&#39;s device. | |
| **sdk_library** | [SdkLibrary](SdkLibrary) | SDK library used to generate the event. | [optional] |
| **network_connectivity** | [NetworkConnectivity](NetworkConnectivity) | Information relating to the device&#39;s network connectivity. | [optional] |
| **referrer_url** | str | The referrer URL of the first event in the app session. | [optional] |
| **search_query** | str | Represents the keywords in a customer search query. | [optional] |
| **attributes** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | User-defined attributes associated with a particular event. These attributes provide additional context about the event. For example, items_in_cart or subscription_level. | [optional] |
| **traits** | [dict(str, CustomEventAttribute)](CustomEventAttribute) | Traits are attributes intrinsic to the customer that may be sent in selected events, (e.g. email, lastName, cellPhone). Traits are used to collect information for identity resolution. For example, the same person might be using an application on different devices which might create two sessions with different customerIds. Additional information can be provided as traits to help link those two sessions and customers to a single external contact through common identifiers that were submitted via a form fill, message, or other input in both sessions. | [optional] |
| **customer_cookie_id** | str | A UUID representing the customer associated with the app event. This is expected to be set per application install or device and can be used to identify a single customer across multiple sessions. This identifier, along with others passed as traits, is used for identity resolution. | |
| **created_date** | datetime | UTC timestamp indicating when the event actually took place, events older than an hour will be rejected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 210.0.0_
