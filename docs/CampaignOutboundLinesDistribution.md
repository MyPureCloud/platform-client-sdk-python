# CampaignOutboundLinesDistribution

## CampaignOutboundLinesDistribution

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign** | [AddressableEntityRef](AddressableEntityRef) | The Campaign for which dialing group distribution information was requested | [optional] |
| **max_outbound_line_count** | int | Maximum outbound calls that can be placed for Campaign&#39;s Edge Group or Site | [optional] |
| **max_line_utilization** | float | Maximum ratio of dialer calls to Campaign&#39;s Edge Group or Site capacity | [optional] |
| **available_outbound_lines** | int | Number of available outbound lines in Campaign&#39;s Edge Group or Site | [optional] |
| **reserved_lines** | int | Number of reserved outbound lines in Campaign&#39;s Edge Group or Site | [optional] |
| **campaigns_with_reserved_lines** | [list[CampaignOutboundLinesReservation]](CampaignOutboundLinesReservation) | Information about campaigns with reserving lines in Campaign&#39;s Edge Group or Site | [optional] |
| **campaigns_with_dynamically_allocated_lines** | [list[CampaignOutboundLinesAllocation]](CampaignOutboundLinesAllocation) | Information about campaigns using dynamic lines allocation in Campaign&#39;s Edge Group or Site | [optional] |



_PureCloudPlatformClientV2 215.0.0_
