# TextBotPromptSegment

## TextBotPromptSegment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **text** | str | The text of this prompt segment. | |
| **type** | str | The segment type which describes any semantics about the &#39;text&#39; and also indicates which other field might include additional relevant info. | |
| **format** | [Format](Format) | Additional details describing the segment’s contents, which the client should honour where possible. | [optional] |
| **content** | [list[MessageContent]](MessageContent) | Details to display Rich Media content. This is only populated when the segment &#39;type&#39; is &#39;Rich Media&#39;. | [optional] |



_PureCloudPlatformClientV2 220.0.0_
