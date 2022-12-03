---
title: ContactList
---
## ContactList

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **division** | [**DomainEntityRef**](DomainEntityRef.html) | The division this entity belongs to. | [optional] |
| **column_names** | **list[str]** | The names of the contact data columns. | |
| **phone_columns** | [**list[ContactPhoneNumberColumn]**](ContactPhoneNumberColumn.html) | Indicates which columns are phone numbers. | [optional] |
| **email_columns** | [**list[EmailColumn]**](EmailColumn.html) | Indicates which columns are email addresses | [optional] |
| **import_status** | [**ImportStatus**](ImportStatus.html) | The status of the import process. | [optional] |
| **preview_mode_column_name** | **str** | A column to check if a contact should always be dialed in preview mode. | [optional] |
| **preview_mode_accepted_values** | **list[str]** | The values in the previewModeColumnName column that indicate a contact should always be dialed in preview mode. | [optional] |
| **size** | **int** | The number of contacts in the ContactList. | [optional] |
| **attempt_limits** | [**DomainEntityRef**](DomainEntityRef.html) | AttemptLimits for this ContactList. | [optional] |
| **automatic_time_zone_mapping** | **bool** | Indicates if automatic time zone mapping is to be used for this ContactList. | [optional] |
| **zip_code_column_name** | **str** | The name of contact list column containing the zip code for use with automatic time zone mapping. Only allowed if &#39;automaticTimeZoneMapping&#39; is set to true. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


