# AlternativeShiftTradeBulkUpdateTemplateItem

## AlternativeShiftTradeBulkUpdateTemplateItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **trade_id** | str | The ID of this alternative shift trade | |
| **state** | str | The current state of this alternative shift trade request | |
| **failure_reason** | str | The reason the update failed, if applicable | [optional] |
| **admin_date_reviewed** | datetime | The timestamp of when the trade request was manually reviewed by an admin in ISO-8601 format | [optional] |
| **admin_reviewed_by** | [UserReference](UserReference) | The admin who manually reviewed this alternative shift trade after system denial | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this alternative shift trade | |



_PureCloudPlatformClientV2 236.0.0_
