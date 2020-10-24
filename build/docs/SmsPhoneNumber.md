---
title: SmsPhoneNumber
---
## SmsPhoneNumber

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **phone_number** | **str** | A phone number provisioned for SMS communications in E.164 format. E.g. +13175555555 or +34234234234 | |
| **phone_number_type** | **str** | Type of the phone number provisioned. | [optional] |
| **provisioned_through_pure_cloud** | **bool** | Is set to false, if the phone number is provisioned through a SMS provider, outside of PureCloud | [optional] |
| **phone_number_status** | **str** | Status of the provisioned phone number. | [optional] |
| **capabilities** | **list[str]** | The capabilities of the phone number available for provisioning. | [optional] |
| **country_code** | **str** | The ISO 3166-1 alpha-2 country code of the country this phone number is associated with. | [optional] |
| **date_created** | **datetime** | Date this phone number was provisioned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date this phone number was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**User**](User.html) | User that provisioned this phone number | [optional] |
| **modified_by** | [**User**](User.html) | User that last modified this phone number | [optional] |
| **version** | **int** | Version number required for updates. | |
| **purchase_date** | **datetime** | Date this phone number was purchased, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **cancellation_date** | **datetime** | Contract end date of this phone number, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **renewal_date** | **datetime** | Contract renewal date of this phone number, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **auto_renewable** | **str** | Renewal time period of this phone number, if the phoneNumberType is shortcode. | [optional] |
| **address_id** | [**SmsAddress**](SmsAddress.html) | The id of an address attached to this phone number. | [optional] |
| **short_code_billing_type** | **str** | BillingType of this phone number, if the phoneNumberType is shortcode. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


