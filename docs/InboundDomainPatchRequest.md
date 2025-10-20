# InboundDomainPatchRequest

## InboundDomainPatchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **mail_from_settings** | [MailFromResult](MailFromResult) | The DNS settings if the inbound domain is using a custom Mail From. These settings can only be used on InboundDomains where subDomain is false. | [optional] |
| **custom_smtp_server** | [DomainEntityRef](DomainEntityRef) | The custom SMTP server integration to use when sending outbound emails from this domain. | [optional] |
| **imap_settings** | [ImapSettings](ImapSettings) | The IMAP server integration and settings to use for processing inbound emails. | [optional] |
| **email_setting** | [EmailSettingReference](EmailSettingReference) | The email settings to associate with this domain. | [optional] |



_PureCloudPlatformClientV2 241.0.0_
