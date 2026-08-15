# CreateJoinVideoResponse

## CreateJoinVideoResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **communication_id** | str | The communication id for the video or modified by the command. | [optional] |
| **conversation_id** | str | The conversation id for the conversation created or modified by the command. | [optional] |
| **join_code** | str | The join code for the video conference. Only returned by the voice-to-video upgrade endpoint (POST /conversations/videos/{conversationId}/agentconference/communications/{communicationId}); not populated by POST /conversations/videos. Valid until the voice-to-video offer expires (default 5 minutes) or until used by a guest. One-time use. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
