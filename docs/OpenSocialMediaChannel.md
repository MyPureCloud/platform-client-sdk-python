# OpenSocialMediaChannel

## OpenSocialMediaChannel

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The topic ID. | [optional] |
| **platform** | str | The provider type. | [optional] |
| **type** | str | Specifies if this message is part of a private or public conversation. | [optional] |
| **message_id** | str | Unique provider ID of the message such as a Facebook message ID. | |
| **to** | [OpenSocialMediaRecipient](OpenSocialMediaRecipient) | Information about the recipient the message is sent to. | [optional] |
| **pcFrom** | [OpenSocialMediaRecipient](OpenSocialMediaRecipient) | Information about the recipient the message is received from. | |
| **time** | datetime | Original time of the event. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **metadata** | object | Information about the channel. | [optional] |
| **public_metadata** | [OpenSocialMediaPublicMetadata](OpenSocialMediaPublicMetadata) | Meta data of this public post. For example, used to define where in the thread the post exists. | |



_PureCloudPlatformClientV2 244.0.0_
