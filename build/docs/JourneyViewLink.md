# JourneyViewLink

## JourneyViewLink

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The identifier of the element downstream | |
| **constraint_within** | [JourneyViewLinkTimeConstraint](JourneyViewLinkTimeConstraint) | A time constraint on this link, which requires a customer to complete the downstream element within this amount of time to be counted. | [optional] |
| **constraint_after** | [JourneyViewLinkTimeConstraint](JourneyViewLinkTimeConstraint) | A time constraint on this link, which requires a customer must complete the downstream element after this amount of time to be counted. | [optional] |
| **event_count_type** | str | The type of events that will be counted. Note: Concurrent will override any JourneyViewLinkTimeConstraint. Default is Sequential. | [optional] |
| **join_attributes** | list[str] | Other (secondary) attributes on which this link should join the customers being counted | [optional] |



_PureCloudPlatformClientV2 237.0.0_
