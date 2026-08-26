# Domains

## Domains

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **authorized_domains** | [AuthorizedDomains](AuthorizedDomains) | The authorized domains settings for email processing. | [optional] |
| **allow_existing_email_participants** | bool | Allow reply and forward to recipients included in the previous email, ignoring the authorized domains list | [optional] |
| **allow_outbound_to_any_domain_acd** | bool | Allow new outbound email (no existing conversation) to be sent to any domain, ignoring the authorized domains list.This setting applies only to new outbound emails sent on behalf of queue or agentless, NOT campaigns.This setting can only be true if allowExistingEmailParticipants is also true. | [optional] |



_PureCloudPlatformClientV2 265.0.0_
