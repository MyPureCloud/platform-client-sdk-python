# WritableDialerContact

## WritableDialerContact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **contact_list_id** | str | The identifier of the contact list containing this contact. | |
| **data** | dict(str, str) | An ordered map of the contact&#39;s columns and corresponding values. | |
| **latest_sms_evaluations** | [dict(str, MessageEvaluation)](MessageEvaluation) | A map of SMS records for the contact phone columns. | [optional] |
| **latest_email_evaluations** | [dict(str, MessageEvaluation)](MessageEvaluation) | A map of email records for the contact email columns. | [optional] |
| **callable** | bool | Indicates whether or not the contact can be called. | [optional] |
| **phone_number_status** | [dict(str, PhoneNumberStatus)](PhoneNumberStatus) | A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not. | [optional] |
| **contactable_status** | [dict(str, ContactableStatus)](ContactableStatus) | A map of media types (Voice, SMS and Email) to ContactableStatus, which indicates if the contact can be contacted using the specified media type. | [optional] |
| **date_created** | datetime | Timestamp for when the contact was added. Contacts added prior to 2023 September 1 may be missing this value. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 217.0.0_
