# DNCListUploadUrlRequest

## DNCListUploadUrlRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **signed_url_timeout_seconds** | int | The number of seconds the presigned URL is valid for (from 1 to 604800 seconds). If none provided, defaults to 600 seconds | [optional] |
| **content_type** | str | The content type of the file to upload. Allows all types are text/csv, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | |
| **id** | str | Id of your dnc list to upload to | |
| **phone_columns** | str | The column names from your file from which to upload dnc phone numbers. | [optional] |
| **email_columns** | str | The column names from your file from which to upload dnc emails. | [optional] |
| **custom_exclusion_columns** | str | The column names from your file from which to upload dnc custom exclusion column entries. | [optional] |
| **expiration_date_time_column** | str | The column name from your file to use as the dnc expiration date time. | [optional] |
| **whats_app_columns** | str | The column names from your file from which to upload dnc whatsapp. | [optional] |



_PureCloudPlatformClientV2 255.0.0_
