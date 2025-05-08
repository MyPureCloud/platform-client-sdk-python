# DocumentListContentBlock

## DocumentListContentBlock

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The type of the list block. | |
| **text** | [DocumentText](DocumentText) | Text. It must contain a value if the type of the block is Text. | [optional] |
| **image** | [DocumentBodyImage](DocumentBodyImage) | Image. It must contain a value if the type of the block is Image. | [optional] |
| **video** | [DocumentBodyVideo](DocumentBodyVideo) | Video. It must contain a value if the type of the block is Video. | [optional] |
| **list** | [DocumentBodyList](DocumentBodyList) | List. It must contain a value if the type of the block is UnorderedList or OrderedList. | [optional] |



_PureCloudPlatformClientV2 227.1.0_
