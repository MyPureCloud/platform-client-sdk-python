---
title: ContactList
---
## ContactList

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **column_names** | **list[str]** | the contact column names | |
| **phone_columns** | [**list[ContactPhoneNumberColumn]**](ContactPhoneNumberColumn.html) | the columns containing phone numbers | |
| **import_status** | [**ImportStatus**](ImportStatus.html) | the status of the import process | [optional] |
| **preview_mode_column_name** | **str** | the name of the column that holds the indicators for contacts that are to be dialed in preview mode only | [optional] |
| **preview_mode_accepted_values** | **list[str]** | list of user-defined values indicating the contact is to be dialed in preview mode only | [optional] |
| **size** | **int** | the number of contacts in the contact list | [optional] |
| **attempt_limits** | [**UriReference**](UriReference.html) | the associated AttemptLimits | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


