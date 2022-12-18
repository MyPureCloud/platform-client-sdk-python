---
title: IntentDefinition
---
## IntentDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | ID of the intent. | [optional] |
| **name** | **str** | The name of the intent. | |
| **entity_type_bindings** | [**list[NamedEntityTypeBinding]**](NamedEntityTypeBinding.html) | The bindings for the named entity types used in this intent.This field is mutually exclusive with entityNameReferences and entities | [optional] |
| **entity_name_references** | **list[str]** | The references for the named entity used in this intent.This field is mutually exclusive with entityTypeBindings | [optional] |
| **utterances** | [**list[NluUtterance]**](NluUtterance.html) | The utterances that act as training phrases for the intent. | |
| **additional_languages** | [**dict(str, AdditionalLanguagesIntent)**](AdditionalLanguagesIntent.html) | Additional languages for intents | [optional] |
{: class="table table-striped"}


