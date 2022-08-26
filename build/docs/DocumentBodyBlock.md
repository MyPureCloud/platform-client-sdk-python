---
title: DocumentBodyBlock
---
## DocumentBodyBlock

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | The type of the block for the body. This determines which body block object (paragraph, list, video or image) would have a value. | |
| **paragraph** | [**DocumentBodyParagraph**](DocumentBodyParagraph.html) | Paragraph. It must contain a value if the type of the block is Paragraph. | |
| **image** | [**DocumentBodyImage**](DocumentBodyImage.html) | Image. It must contain a value if the type of the block is Image. | |
| **video** | [**DocumentBodyVideo**](DocumentBodyVideo.html) | Video. It must contain a value if the type of the block is Video. | |
| **list** | [**DocumentBodyList**](DocumentBodyList.html) | List. It must contain a value if the type of the block is UnorderedList or OrderedList. | |
{: class="table table-striped"}


