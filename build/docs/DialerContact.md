---
title: DialerContact
---
## DialerContact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **contact_list_id** | **str** | Identifier of the contact list containing this contact | |
| **data** | **dict(str, object)** | An ordered map of the contact&#39;s data attributes and values | [optional] |
| **call_records** | [**dict(str, CallRecord)**](CallRecord.html) | A map of call records for the contact phone columns | [optional] |
| **callable** | **bool** | false if the contact is not to be called | [optional] |
| **phone_number_status** | [**dict(str, PhoneNumberStatus)**](PhoneNumberStatus.html) | A map of statuses for the contact phone columns | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


