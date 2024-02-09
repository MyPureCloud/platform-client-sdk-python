---
title: WebActionEvent
---
## WebActionEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **action** | [**EventAction**](EventAction.html) | The action that triggered the event. | |
| **action_map** | [**ActionEventActionMap**](ActionEventActionMap.html) | The action map that triggered the action. | |
| **action_target** | [**AddressableEntityRef**](AddressableEntityRef.html) | The target for engagement actions. | |
| **time_to_disposition** | **int** | Milliseconds elapsed until the action is disposed. | [optional] |
| **error_code** | **str** | Code of the error returned when the action fails. | [optional] |
| **error_message** | **str** | Message of the error returned when the action fails. | [optional] |
| **user_agent_string** | **str** | HTTP User-Agent string (see https://tools.ietf.org/html/rfc1945#section-10.15). | |
| **browser** | [**Browser**](Browser.html) | Customer&#39;s browser. | |
| **device** | [**Device**](Device.html) | Customer&#39;s device. | |
| **geolocation** | [**JourneyGeolocation**](JourneyGeolocation.html) | Customer&#39;s geolocation. | [optional] |
| **ip_address** | **str** | Visitor&#39;s IP address. | [optional] |
| **ip_organization** | **str** | Visitor&#39;s IP-based organization or ISP name. | [optional] |
| **mkt_campaign** | [**JourneyCampaign**](JourneyCampaign.html) | Marketing / traffic source information. | [optional] |
| **visit_referrer** | [**Referrer**](Referrer.html) | Visit&#39;s referrer. | [optional] |
{: class="table table-striped"}


