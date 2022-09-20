---
title: WritableDialerContact
---
## WritableDialerContact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **contact_list_id** | **str** | The identifier of the contact list containing this contact. | |
| **data** | **dict(str, object)** | An ordered map of the contact&#39;s columns and corresponding values. | |
| **latest_sms_evaluations** | [**dict(str, MessageEvaluation)**](MessageEvaluation.html) | A map of SMS records for the contact phone columns. | [optional] |
| **callable** | **bool** | Indicates whether or not the contact can be called. | [optional] |
| **phone_number_status** | [**dict(str, PhoneNumberStatus)**](PhoneNumberStatus.html) | A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not. | [optional] |
| **contactable_status** | [**dict(str, ContactableStatus)**](ContactableStatus.html) | A map of media types(voice, sms and email) to ContactableStatus, which indicates where or not the contact can be contacted using the specified media type. | [optional] |
{: class="table table-striped"}


