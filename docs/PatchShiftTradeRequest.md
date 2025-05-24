# PatchShiftTradeRequest

## PatchShiftTradeRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **receiving_user_id** | [ValueWrapperString](ValueWrapperString) | Update the ID of the receiving user to direct the request at a specific user, or set the wrapped id to null to open up a trade to be matched by any user. | [optional] |
| **expiration** | [ValueWrapperDate](ValueWrapperDate) | Update the expiration time for this shift trade. | [optional] |
| **acceptable_intervals** | [ListWrapperInterval](ListWrapperInterval) | Update the acceptable intervals the initiating user is willing to accept in trade. Setting the enclosed list to empty will make this a one sided trade request | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata | |



_PureCloudPlatformClientV2 229.0.0_
