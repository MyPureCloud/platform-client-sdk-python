# CreateWebChatConversationRequest

## CreateWebChatConversationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **organization_id** | str | The organization identifier. | |
| **deployment_id** | str | The web chat Deployment ID which contains the appropriate settings for this chat conversation. | |
| **routing_target** | [WebChatRoutingTarget](WebChatRoutingTarget) | The routing information to use for the new chat conversation. | |
| **member_info** | [GuestMemberInfo](GuestMemberInfo) | The guest member info to use for the new chat conversation. | |
| **member_auth_token** | str | If the guest member is an authenticated member (ie, not anonymous) his JWT is provided here. The token will have been previously generated with the \&quot;POST /api/v2/signeddata\&quot; resource. | [optional] |
| **journey_context** | [JourneyContext](JourneyContext) | A subset of the Journey System&#39;s data relevant to this conversation/session request (for external linkage and internal usage/context). | [optional] |



_PureCloudPlatformClientV2 219.1.0_
