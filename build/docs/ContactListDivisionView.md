---
title: ContactListDivisionView
---
## ContactListDivisionView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **column_names** | **list[str]** | The names of the contact data columns. | |
| **phone_columns** | [**list[ContactPhoneNumberColumn]**](ContactPhoneNumberColumn.html) | Indicates which columns are phone numbers. | |
| **import_status** | [**ImportStatus**](ImportStatus.html) | The status of the import process. | [optional] |
| **size** | **int** | The number of contacts in the ContactList. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


