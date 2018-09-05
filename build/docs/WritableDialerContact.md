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
| **callable** | **bool** | Indicates whether or not the contact can be called. | [optional] |
| **phone_number_status** | [**dict(str, PhoneNumberStatus)**](PhoneNumberStatus.html) | A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not. | [optional] |
{: class="table table-striped"}


