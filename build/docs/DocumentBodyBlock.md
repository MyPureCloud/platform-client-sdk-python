# DocumentBodyBlock

## DocumentBodyBlock

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The type of the block for the body. This determines which body block object (paragraph, list, video, image or table) would have a value. | |
| **image** | [DocumentBodyImage](DocumentBodyImage) | Image. It must contain a value if the type of the block is Image. | [optional] |
| **video** | [DocumentBodyVideo](DocumentBodyVideo) | Video. It must contain a value if the type of the block is Video. | [optional] |
| **paragraph** | [DocumentBodyParagraph](DocumentBodyParagraph) | Paragraph. It must contain a value if the type of the block is Paragraph. | [optional] |
| **list** | [DocumentBodyList](DocumentBodyList) | List. It must contain a value if the type of the block is UnorderedList or OrderedList. | [optional] |
| **table** | [DocumentBodyTable](DocumentBodyTable) | Table. It must contain a value if type of the block is Table. | [optional] |



_PureCloudPlatformClientV2 226.0.0_
