# NamedEntityTypeMechanism

## NamedEntityTypeMechanism

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **items** | [list[NamedEntityTypeItem]](NamedEntityTypeItem) | The items that define the named entity type. | |
| **restricted** | bool | Whether the named entity type is restricted to the items provided. Default: false | [optional] |
| **type** | str | The type of the mechanism. | |
| **sub_type** | str | Subtype of detection mechanism | [optional] |
| **max_length** | int | The maximum length of the entity resolved value | [optional] |
| **min_length** | int | The minimum length of the entity resolved value | [optional] |
| **allow_special_chars** | bool | Flag whether to allow for special characters during AI slot capture | [optional] |
| **examples** | [list[NamedEntityTypeMechanismExample]](NamedEntityTypeMechanismExample) | Examples for entity detection | [optional] |



_PureCloudPlatformClientV2 248.0.0_
