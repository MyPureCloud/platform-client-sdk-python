# InboundDomainCreateRequest

## InboundDomainCreateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Unique Id of the domain such as: example.com | |
| **sub_domain** | bool | Indicates if this a PureCloud sub-domain. If true, then the appropriate DNS records are created for sending/receiving email. | [optional] |
| **mail_from_settings** | [MailFromResult](MailFromResult) | The DNS settings if the inbound domain is using a custom Mail From. These settings can only be used on InboundDomains where subDomain is false. | [optional] |
| **custom_smtp_server** | [DomainEntityRef](DomainEntityRef) | The custom SMTP server integration to use when sending outbound emails from this domain. | [optional] |
| **email_setting** | [EmailSettingReference](EmailSettingReference) | The email settings to associate with this domain. | [optional] |



_PureCloudPlatformClientV2 249.0.0_
