# ContactListDivisionView

## ContactListDivisionView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **column_names** | list[str] | The names of the contact data columns. | |
| **phone_columns** | [list[ContactPhoneNumberColumn]](ContactPhoneNumberColumn) | Indicates which columns are phone numbers. | [optional] |
| **email_columns** | [list[EmailColumn]](EmailColumn) | Indicates which columns are email addresses. | [optional] |
| **whats_app_columns** | [list[WhatsAppColumn]](WhatsAppColumn) | Indicates which columns are whatsApp contacts. | [optional] |
| **import_status** | [ImportStatus](ImportStatus) | The status of the import process. | [optional] |
| **size** | int | The number of contacts in the ContactList. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_
