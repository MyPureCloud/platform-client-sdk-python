# OutboundMessagingMessagingCampaignConfigChangeMessagingCampaign

## OutboundMessagingMessagingCampaignConfigChangeMessagingCampaign

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign_status** | str |  | [optional] |
| **callable_time_set** | [OutboundMessagingMessagingCampaignConfigChangeUriReference](OutboundMessagingMessagingCampaignConfigChangeUriReference) |  | [optional] |
| **contact_list** | [OutboundMessagingMessagingCampaignConfigChangeUriReference](OutboundMessagingMessagingCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **dnc_lists** | [list[OutboundMessagingMessagingCampaignConfigChangeUriReference]](OutboundMessagingMessagingCampaignConfigChangeUriReference) | The dnc lists to check before sending a message for this messaging campaign. | [optional] |
| **contact_list_filters** | [list[OutboundMessagingMessagingCampaignConfigChangeUriReference]](OutboundMessagingMessagingCampaignConfigChangeUriReference) | The contact list filters to check before sending a message for this messaging campaign. | [optional] |
| **always_running** | bool | Whether this messaging campaign is always running. | [optional] |
| **contact_sorts** | [list[OutboundMessagingMessagingCampaignConfigChangeContactSort]](OutboundMessagingMessagingCampaignConfigChangeContactSort) | The order in which to sort contacts for dialing, based on up to four columns. | [optional] |
| **messages_per_minute** | int | How many messages this messaging campaign will send per minute. | [optional] |
| **rule_sets** | [list[OutboundMessagingMessagingCampaignConfigChangeUriReference]](OutboundMessagingMessagingCampaignConfigChangeUriReference) |  | [optional] |
| **sms_config** | [OutboundMessagingMessagingCampaignConfigChangeSmsConfig](OutboundMessagingMessagingCampaignConfigChangeSmsConfig) |  | [optional] |
| **email_config** | [OutboundMessagingMessagingCampaignConfigChangeEmailConfig](OutboundMessagingMessagingCampaignConfigChangeEmailConfig) |  | [optional] |
| **whats_app_config** | [OutboundMessagingMessagingCampaignConfigChangeWhatsAppConfig](OutboundMessagingMessagingCampaignConfigChangeWhatsAppConfig) |  | [optional] |
| **errors** | [list[OutboundMessagingMessagingCampaignConfigChangeErrorDetail]](OutboundMessagingMessagingCampaignConfigChangeErrorDetail) | A list of current error conditions associated with this messaging campaign | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **division** | [OutboundMessagingMessagingCampaignConfigChangeUriReference](OutboundMessagingMessagingCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |



_PureCloudPlatformClientV2 245.0.0_
