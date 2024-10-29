# DialerDnclistConfigChangeDncList

## DialerDnclistConfigChangeDncList

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **import_status** | [DialerDnclistConfigChangeImportStatus](DialerDnclistConfigChangeImportStatus) |  | [optional] |
| **size** | int | the number of phone numbers in the do not call list | [optional] |
| **dnc_source_type** | str | the type of dnc list being created, rds (csv file), gryphon, or dnc.com | [optional] |
| **login_id** | str | the loginId if the dncSourceType is dnc.com | [optional] |
| **dnc_codes** | list[str] | the list of dnc.com codes to be treated as DNC | [optional] |
| **license_id** | str | the license number if the dncSourceType is gryphon | [optional] |
| **contact_method** | str |  | [optional] |
| **division** | [DialerDnclistConfigChangeUriReference](DialerDnclistConfigChangeUriReference) |  | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 215.0.0_
