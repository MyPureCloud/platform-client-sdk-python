# PatchOutcome

## PatchOutcome

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **is_active** | bool | Whether or not the outcome is active. | [optional] |
| **display_name** | str | The display name of the outcome. | |
| **version** | int | The version of the outcome. | [optional] |
| **description** | str | A description of the outcome. | [optional] |
| **is_positive** | bool | Whether or not the outcome is positive. | [optional] |
| **context** | [PatchContext](PatchContext) | The context of the outcome. | [optional] |
| **journey** | [PatchJourney](PatchJourney) | The pattern of rules defining the filter of the outcome. | [optional] |
| **associated_value_field** | [PatchAssociatedValueField](PatchAssociatedValueField) | The field from the event indicating the associated value. | [optional] |



_PureCloudPlatformClientV2 233.0.0_
