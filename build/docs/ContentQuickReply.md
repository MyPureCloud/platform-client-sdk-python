---
title: ContentQuickReply
---
## ContentQuickReply

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | An ID assigned to the quick reply. Each object inside the content array has a unique ID. | [optional] |
| **text** | **str** | Text to show inside the quick reply. This is also used as the response text after clicking on the quick reply. | |
| **payload** | **str** | Content of the textback payload after clicking a quick reply | [optional] |
| **image** | **str** | Path or URI to an image file associated with quick reply | [optional] |
| **action** | **str** | Specifies the type of action that is triggered upon clicking the quick reply. Currently, the only supported action is \&quot;Message\&quot; which sends a message using the quick reply text. | [optional] |
{: class="table table-striped"}


