---
title: InboundDomainPatchRequest
---
## InboundDomainPatchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **mail_from_settings** | [**MailFromResult**](MailFromResult.html) | The DNS settings if the inbound domain is using a custom Mail From. These settings can only be used on InboundDomains where subDomain is false. | [optional] |
| **custom_smtp_server** | [**DomainEntityRef**](DomainEntityRef.html) | The custom SMTP server integration to use when sending outbound emails from this domain. | [optional] |
{: class="table table-striped"}


