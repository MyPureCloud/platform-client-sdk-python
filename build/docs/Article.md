---
title: Article
---
## Article

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **title** | **str** | The article title. | [optional] |
| **uri** | **str** | The URI for the article. | [optional] |
| **snippets** | **list[str]** | This contains snippets of text from the article matching the query. | [optional] |
| **confidence** | **float** | Value between 0 and 1. 1 corresponds to very confident, 0 to not confident at all. | [optional] |
| **metadata** | [**dict(str, MetadataAttribute)**](MetadataAttribute.html) | A map that contains custom metadata about the article answer. | [optional] |
| **version** | [**AddressableEntityRef**](AddressableEntityRef.html) | The version of the Article. | [optional] |
| **variations** | [**list[AddressableEntityRef]**](AddressableEntityRef.html) | Variations of the Article. | [optional] |
{: class="table table-striped"}

