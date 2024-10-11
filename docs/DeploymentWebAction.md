# DeploymentWebAction

## DeploymentWebAction

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | System-generated UUID for the action. | |
| **media_type** | str | Action media type used to deliver the action. | |
| **customer_id** | str | ID string of the customer that the action was triggered for. | [optional] |
| **customer_id_type** | str | Type of the customer ID that the action was triggered for. | [optional] |
| **action_map_id** | str | ID of the action map that triggered the action. | |
| **action_map_version** | int | Version of the action map that triggered the action. | |
| **session_id** | str | ID of the session that the action was triggered for. | |
| **web_messaging_offer_properties** | [WebMessagingOfferProperties](WebMessagingOfferProperties) | Web messaging offer specific properties. | [optional] |
| **content_offer_properties** | [ContentOffer](ContentOffer) | Content offer specific properties. | [optional] |
| **open_action_properties** | [OpenActionProperties](OpenActionProperties) | Open action specific properties. | [optional] |



_PureCloudPlatformClientV2 213.0.0_
