# OutboundMessagingEmailCampaignProgressEventCampaignProgress

## OutboundMessagingEmailCampaignProgressEventCampaignProgress

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign** | [OutboundMessagingEmailCampaignProgressEventUriReference](OutboundMessagingEmailCampaignProgressEventUriReference) |  | [optional] |
| **number_of_contacts_called** | float | The number of contacts that have been called so far | [optional] |
| **number_of_contacts_messaged** | float | The number of contacts that have been messaged so far | [optional] |
| **total_number_of_contacts** | float | The total number of contacts in the contact list | [optional] |
| **percentage** | int | numberOfContactsContacted/totalNumberOfContacts*100 | [optional] |
| **number_of_contacts_skipped** | dict(str, int) | A map of skipped reasons and the number of contacts associated with each. | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 216.0.0_
