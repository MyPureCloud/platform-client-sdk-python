---
title: KeywordSet
---
## KeywordSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **description** | **str** |  | [optional] |
| **queues** | [**list[Queue]**](Queue.html) |  | [optional] |
| **language** | **str** | Language code, such as &#39;en-US&#39; | |
| **agents** | [**list[User]**](User.html) |  | [optional] |
| **keywords** | [**list[Keyword]**](Keyword.html) | The list of keywords to be used for keyword spotting. | |
| **participant_purposes** | **list[str]** | The types of participants to use keyword spotting on. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


