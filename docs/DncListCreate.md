# DncListCreate

## DncListCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the DncList. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **import_status** | [ImportStatus](ImportStatus) | The status of the import process | [optional] |
| **size** | int | The total number of phone numbers in the DncList. | [optional] |
| **dnc_source_type** | str | The type of the DncList. | |
| **contact_method** | str | The contact method. Required if dncSourceType is rds. | [optional] |
| **login_id** | str | A dnc.com loginId. Required if the dncSourceType is dnc.com. | [optional] |
| **campaign_id** | str | A dnc.com campaignId. Optional if the dncSourceType is dnc.com. | [optional] |
| **dnc_codes** | list[str] | The list of dnc.com codes to be treated as DNC. Required if the dncSourceType is dnc.com. | [optional] |
| **license_id** | str | A gryphon license number. Required if the dncSourceType is gryphon. | [optional] |
| **division** | [DomainEntityRef](DomainEntityRef) | The division this DncList belongs to. | [optional] |
| **custom_exclusion_column** | str | The column to evaluate exclusion against. Required if the dncSourceType is rds_custom. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
