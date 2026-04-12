# GoogleBusinessProfileDataIngestionRuleRequest

## GoogleBusinessProfileDataIngestionRuleRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the data ingestion rule. | |
| **description** | str | A description of the data ingestion rule. | [optional] |
| **integration_id** | str | The Integration Id from which to ingest public social posts. This entity is created using the /conversations/messaging/integrations/open/extensions/googlebusinessprofile resource | |
| **external_source** | [DomainEntityRef](DomainEntityRef) | The external source associated with this data ingestion rule, which will be used when performing identity resolution | |



_PureCloudPlatformClientV2 256.0.0_
