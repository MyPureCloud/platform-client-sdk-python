# OpenSocialMediaPublicMetadata

## OpenSocialMediaPublicMetadata

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **root_id** | str | The id of the root public message. | |
| **reply_to_id** | str | The id of the message this public message is replying to. | [optional] |
| **source** | str | The source of the public message. Useful when there could be more than location. Channel specific, e.g., for Facebook it&#39;s a source page. | [optional] |
| **url** | str | The URL of the social post on the native platform. | [optional] |
| **mention_ids** | list[str] | IDs of accounts referenced by name within the message text or caption (for example &#39;@brandpage&#39; in a post body or comment). A &#39;mention&#39; here uses the same convention as Meta (Facebook, Instagram) and LinkedIn, where it denotes a textual reference to an account. Distinct from tagIds, which represent explicit associations with the message. Null or absent when no accounts are referenced in the text. | [optional] |
| **tag_ids** | list[str] | IDs of accounts attached to the message itself, independent of the text (for example a person tagged in an Instagram photo so their profile is linked from the image). A &#39;tag&#39; here uses the same convention as Meta (Facebook, Instagram) and LinkedIn, where it denotes an explicit association with content rather than a textual reference. Distinct from mentionIds, which represent in-text/caption references. Null or absent when no accounts are tagged on the message. | [optional] |



_PureCloudPlatformClientV2 265.0.0_
