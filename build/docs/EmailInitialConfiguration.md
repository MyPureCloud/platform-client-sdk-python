# EmailInitialConfiguration

## EmailInitialConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **to** | str | An email address that this email is to. | |
| **pcFrom** | str | An email address that this email is from. | |
| **cc** | list[str] | An email addresses that this email is carbon copied to. | [optional] |
| **bcc** | list[str] | An email addresses that this email is blind carbon copied to. | [optional] |
| **subject** | str | The subject for this email. | [optional] |
| **previous_email_id** | str | UUID identifying the most recent previous email communication ID from the same participant on this email conversation. Will be null if this is a new participant. | [optional] |
| **held** | bool | Indicates that this communication&#39;s initial state is held. | [optional] |
| **alerting** | bool | Indicates that this communication&#39;s initial state is alerting. If false, the communication started in a connected state. | [optional] |
| **inbound** | bool | Indicates the direction of this communication with respect to the contact center. &#x60;true&#x60; means the communication is INBOUND. &#x60;false&#x60; means the communication is OUTBOUND. | [optional] |
| **invited_by** | str | The id of the communication (the \&quot;peer\&quot;) that \&quot;invited\&quot; this communication, if this occurred. | [optional] |
| **additional_info** | dict(str, str) | Additional metadata about this session which should be recorded by the platform but which will not be indexed or searchable. Primarily for diagnostic value. Any information that needs to be accessible through other components like Analytics should be moved to dedicated fields. | [optional] |



_PureCloudPlatformClientV2 245.0.0_
