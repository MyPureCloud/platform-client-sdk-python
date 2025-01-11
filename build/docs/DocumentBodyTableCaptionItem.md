# DocumentBodyTableCaptionItem

## DocumentBodyTableCaptionItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The type of the caption item. | |
| **text** | [DocumentText](DocumentText) | Text. It must contain a value if the type of the block is Text. | [optional] |
| **paragraph** | [DocumentBodyParagraph](DocumentBodyParagraph) | Paragraph. It must contain a value if the type of the block is Paragraph. | [optional] |
| **image** | [DocumentBodyImage](DocumentBodyImage) | Image. It must contain a value if the type of the block is Image. | [optional] |
| **video** | [DocumentBodyVideo](DocumentBodyVideo) | Video. It must contain a value if the type of the block is Video. | [optional] |
| **list** | [DocumentBodyList](DocumentBodyList) | List. It must contain a value if the type of the block is UnorderedList or OrderedList. | [optional] |



_PureCloudPlatformClientV2 219.1.0_
