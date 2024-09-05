# OutcomeAchievedEvent

## OutcomeAchievedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outcome** | [OutcomeAchievedEventOutcome](OutcomeAchievedEventOutcome) | The outcome achieved. | |
| **user_agent_string** | str | HTTP User-Agent string (see https://tools.ietf.org/html/rfc1945#section-10.15). | [optional] |
| **browser** | [Browser](Browser) | Customer&#39;s browser. | [optional] |
| **device** | [Device](Device) | Customer&#39;s device. | [optional] |
| **geolocation** | [JourneyGeolocation](JourneyGeolocation) | Customer&#39;s geolocation. | [optional] |
| **ip_address** | str | Visitor&#39;s IP address. | [optional] |
| **ip_organization** | str | Visitor&#39;s IP-based organization or ISP name. | [optional] |
| **mkt_campaign** | [JourneyCampaign](JourneyCampaign) | Marketing / traffic source information. | [optional] |
| **visit_referrer** | [Referrer](Referrer) | Visit&#39;s referrer. | [optional] |
| **visit_created_date** | datetime | When visit was created (e.g. timestamp of the first event in visit). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 210.0.0_
