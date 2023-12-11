---
title: AppEventResponse
---
## AppEventResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | System-generated UUID for the event. | [optional] |
| **customer_id** | **str** | Identifier of the customer in the source of the event. | [optional] |
| **customer_id_type** | **str** | Type of identifier for the customer ID (cookie, email etc.). | [optional] |
| **event_name** | **str** | Represents the action the customer performed. A good event name is typically an object followed by the action performed in past tense (e.g. screen_viewed, order_completed, user_registered). | [optional] |
| **screen_name** | **str** | The name of the screen in the app that the event took place. | [optional] |
| **app** | [**JourneyApp**](JourneyApp.html) | Application that the customer is interacting with. | [optional] |
| **device** | [**Device**](Device.html) | Customer&#39;s device. | [optional] |
| **ip_organization** | **str** | Customer&#39;s IP-based organization or ISP name. | [optional] |
| **geolocation** | [**JourneyGeolocation**](JourneyGeolocation.html) | Customer&#39;s geolocation. | [optional] |
| **sdk_library** | [**SdkLibrary**](SdkLibrary.html) | SDK library used to generate the event. | [optional] |
| **network_connectivity** | [**NetworkConnectivity**](NetworkConnectivity.html) | Information relating to the device&#39;s network connectivity. | [optional] |
| **mkt_campaign** | [**JourneyCampaign**](JourneyCampaign.html) | Marketing / traffic source information. | [optional] |
| **session** | [**AppEventResponseSession**](AppEventResponseSession.html) | The app session the event belongs to. | [optional] |
| **search_query** | **str** | Represents the keywords in a customer search query. | [optional] |
| **attributes** | [**dict(str, CustomEventAttribute)**](CustomEventAttribute.html) | User-defined attributes associated with a particular event. | [optional] |
| **traits** | [**dict(str, CustomEventAttribute)**](CustomEventAttribute.html) | Traits are attributes intrinsic to the customer that may be sent in selected events (e.g. email, name, phone). | [optional] |
| **created_date** | **datetime** | UTC timestamp indicating when the event actually took place. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


