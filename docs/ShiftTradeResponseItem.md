# ShiftTradeResponseItem

## ShiftTradeResponseItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of this shift trade | |
| **state** | str | The state of this shift trade | |
| **expiration_date** | datetime | When this shift trade will expire. Date time is represented as an ISO-8601 string | [optional] |
| **initiating** | [ShiftTradeInitiatingSideResponseItem](ShiftTradeInitiatingSideResponseItem) | Details about the initiating user involved in this shift trade | |
| **receiving** | [ShiftTradeReceivingSideResponseItem](ShiftTradeReceivingSideResponseItem) | Details about the receiving user involved in this shift trade | [optional] |
| **acceptable_intervals** | [list[RequiredDateRange]](RequiredDateRange) | Time frames when the initiating user is willing to accept trades. Empty means giving up the shift | |
| **one_sided** | bool | Whether this is a one-sided shift trade (e.g. the initiating user is not asking for a shift in return) | |
| **target** | [ShiftTradeTargetResponseItem](ShiftTradeTargetResponseItem) | The user to whom the shift trade request was sent in a direct trade, or the user with whom a shift trade was Matched | [optional] |
| **reviewed_by** | [UserReference](UserReference) | The admin who approved or denied this shift trade | [optional] |
| **reviewed_date** | datetime | The timestamp of when the trade request was reviewed by an admin in ISO-8601 format | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this shift trade | |



_PureCloudPlatformClientV2 257.0.0_
