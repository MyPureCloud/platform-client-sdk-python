# DialerContactlistConfigChangeContactList

## DialerContactlistConfigChangeContactList

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **column_names** | list[str] | the contact column names | [optional] |
| **phone_columns** | [list[DialerContactlistConfigChangeContactPhoneNumberColumn]](DialerContactlistConfigChangeContactPhoneNumberColumn) | the columns containing phone numbers | [optional] |
| **email_columns** | [list[DialerContactlistConfigChangeEmailColumn]](DialerContactlistConfigChangeEmailColumn) | the columns containing email addresses | [optional] |
| **import_status** | [DialerContactlistConfigChangeImportStatus](DialerContactlistConfigChangeImportStatus) |  | [optional] |
| **preview_mode_column_name** | str | the name of the column that holds the indicators for contacts that are to be dialed in preview mode only | [optional] |
| **preview_mode_accepted_values** | list[str] | list of user-defined values indicating the contact is to be dialed in preview mode only | [optional] |
| **size** | int | the number of contacts in the contact list | [optional] |
| **attempt_limits** | [DialerContactlistConfigChangeUriReference](DialerContactlistConfigChangeUriReference) |  | [optional] |
| **automatic_time_zone_mapping** | bool | whether or not automatic time zone mapping is enabled on the list | [optional] |
| **zip_code_column_name** | str | zip code column from the contact list to be used optionally with automatic time zone mapping | [optional] |
| **division** | [DialerContactlistConfigChangeUriReference](DialerContactlistConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 215.0.0_
