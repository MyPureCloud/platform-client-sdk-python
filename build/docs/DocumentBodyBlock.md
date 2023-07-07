---
title: DocumentBodyBlock
---
## DocumentBodyBlock

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | The type of the block for the body. This determines which body block object (paragraph, list, video, image or table) would have a value. | |
| **paragraph** | [**DocumentBodyParagraph**](DocumentBodyParagraph.html) | Paragraph. It must contain a value if the type of the block is Paragraph. | [optional] |
| **image** | [**DocumentBodyImage**](DocumentBodyImage.html) | Image. It must contain a value if the type of the block is Image. | [optional] |
| **video** | [**DocumentBodyVideo**](DocumentBodyVideo.html) | Video. It must contain a value if the type of the block is Video. | [optional] |
| **list** | [**DocumentBodyList**](DocumentBodyList.html) | List. It must contain a value if the type of the block is UnorderedList or OrderedList. | [optional] |
| **table** | [**DocumentBodyTable**](DocumentBodyTable.html) | Table. It must contain a value if type of the block is Table. | [optional] |
{: class="table table-striped"}


