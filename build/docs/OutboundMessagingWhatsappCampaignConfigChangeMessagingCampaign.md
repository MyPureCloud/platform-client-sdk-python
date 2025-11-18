# OutboundMessagingWhatsappCampaignConfigChangeMessagingCampaign

## OutboundMessagingWhatsappCampaignConfigChangeMessagingCampaign

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign_status** | str |  | [optional] |
| **callable_time_set** | [OutboundMessagingWhatsappCampaignConfigChangeUriReference](OutboundMessagingWhatsappCampaignConfigChangeUriReference) |  | [optional] |
| **contact_list** | [OutboundMessagingWhatsappCampaignConfigChangeUriReference](OutboundMessagingWhatsappCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **dnc_lists** | [list[OutboundMessagingWhatsappCampaignConfigChangeUriReference]](OutboundMessagingWhatsappCampaignConfigChangeUriReference) | The dnc lists to check before sending a message for this messaging campaign. | [optional] |
| **contact_list_filters** | [list[OutboundMessagingWhatsappCampaignConfigChangeUriReference]](OutboundMessagingWhatsappCampaignConfigChangeUriReference) | The contact list filters to check before sending a message for this messaging campaign. | [optional] |
| **always_running** | bool | Whether this messaging campaign is always running. | [optional] |
| **contact_sorts** | [list[OutboundMessagingWhatsappCampaignConfigChangeContactSort]](OutboundMessagingWhatsappCampaignConfigChangeContactSort) | The order in which to sort contacts for dialing, based on up to four columns. | [optional] |
| **messages_per_minute** | int | How many messages this messaging campaign will send per minute. | [optional] |
| **rule_sets** | [list[OutboundMessagingWhatsappCampaignConfigChangeUriReference]](OutboundMessagingWhatsappCampaignConfigChangeUriReference) |  | [optional] |
| **sms_config** | [OutboundMessagingWhatsappCampaignConfigChangeSmsConfig](OutboundMessagingWhatsappCampaignConfigChangeSmsConfig) |  | [optional] |
| **email_config** | [OutboundMessagingWhatsappCampaignConfigChangeEmailConfig](OutboundMessagingWhatsappCampaignConfigChangeEmailConfig) |  | [optional] |
| **whats_app_config** | [OutboundMessagingWhatsappCampaignConfigChangeWhatsAppConfig](OutboundMessagingWhatsappCampaignConfigChangeWhatsAppConfig) |  | [optional] |
| **errors** | [list[OutboundMessagingWhatsappCampaignConfigChangeErrorDetail]](OutboundMessagingWhatsappCampaignConfigChangeErrorDetail) | A list of current error conditions associated with this messaging campaign | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **division** | [OutboundMessagingWhatsappCampaignConfigChangeUriReference](OutboundMessagingWhatsappCampaignConfigChangeUriReference) | A UriReference for a resource | [optional] |



_PureCloudPlatformClientV2 243.0.0_
