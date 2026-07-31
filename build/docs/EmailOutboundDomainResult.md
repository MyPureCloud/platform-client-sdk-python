# EmailOutboundDomainResult

## EmailOutboundDomainResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **dns_cname_bounce_record** | [DnsRecordEntry](DnsRecordEntry) |  | [optional] |
| **dns_txt_sending_record** | [DnsRecordEntry](DnsRecordEntry) |  | [optional] |
| **domain_name** | str |  | [optional] |
| **sender_status** | str |  | [optional] |
| **sender_type** | str |  | [optional] |
| **email_setting** | [EmailSetting](EmailSetting) | The email settings associated with this domain. | [optional] |
| **dmarc_verification_result** | [DmarcResult](DmarcResult) | The DMARC verification status for this domain. | [optional] |



_PureCloudPlatformClientV2 263.0.0_
