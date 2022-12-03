---
title: DialerContact
---
## DialerContact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **contact_list_id** | **str** | The identifier of the contact list containing this contact. | |
| **data** | **dict(str, object)** | An ordered map of the contact&#39;s columns and corresponding values. | |
| **call_records** | [**dict(str, CallRecord)**](CallRecord.html) | A map of call records for the contact phone columns. | [optional] |
| **latest_sms_evaluations** | [**dict(str, MessageEvaluation)**](MessageEvaluation.html) | A map of SMS records for the contact phone columns. | [optional] |
| **latest_email_evaluations** | [**dict(str, MessageEvaluation)**](MessageEvaluation.html) | A map of email records for the contact email columns. | [optional] |
| **callable** | **bool** | Indicates whether or not the contact can be called. | [optional] |
| **phone_number_status** | [**dict(str, PhoneNumberStatus)**](PhoneNumberStatus.html) | A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not. | [optional] |
| **contactable_status** | [**dict(str, ContactableStatus)**](ContactableStatus.html) | A map of media types (Voice, SMS and Email) to ContactableStatus, which indicates if the contact can be contacted using the specified media type. | [optional] |
| **contact_column_time_zones** | [**dict(str, ContactColumnTimeZone)**](ContactColumnTimeZone.html) | Map containing data about the timezone the contact is mapped to. This will only be populated if the contact list has automatic timezone mapping turned on. The key is the column name. The value is the timezone it mapped to and the type of column: Phone or Zip | [optional] |
| **configuration_overrides** | [**ConfigurationOverrides**](ConfigurationOverrides.html) | the priority property within ConfigurationOverides indicates whether or not the contact to be placed in front of the queue or at the end of the queue | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


