# ContactListUploadUrlRequest

## ContactListUploadUrlRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **signed_url_timeout_seconds** | int | The number of seconds the presigned URL is valid for (from 1 to 604800 seconds). If none provided, defaults to 600 seconds | [optional] |
| **content_type** | str | The content type of the file to upload. Allows MIME types are text/csv, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | |
| **id** | str | Id of your contact list to upload to | [optional] |
| **contact_id_name** | str | The column name from your file to use as the contact id. | [optional] |
| **import_template_id** | str | Id of your import template to use. | [optional] |
| **list_name_prefix** | str | String that will replace %N in the listNameFormat specified on the import template. | [optional] |
| **clear_system_data** | bool | Whether to clear system data | [optional] |
| **division_id_for_target_contact_lists** | str | Id of the division to be used for the creation of the target contact lists. If not provided, Home division will be used. | [optional] |
| **file_specification_template_id** | str | File specification template ID | [optional] |



_PureCloudPlatformClientV2 252.1.0_
