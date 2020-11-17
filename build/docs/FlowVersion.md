---
title: FlowVersion
---
## FlowVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The flow version identifier | [optional] |
| **name** | **str** |  | [optional] |
| **commit_version** | **str** |  | [optional] |
| **configuration_version** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **secure** | **bool** |  | [optional] |
| **debug** | **bool** |  | [optional] |
| **created_by** | [**User**](User.html) |  | [optional] |
| **created_by_client** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **configuration_uri** | **str** |  | [optional] |
| **date_created** | **int** |  | [optional] |
| **generation_id** | **str** |  | [optional] |
| **publish_result_uri** | **str** |  | [optional] |
| **input_schema** | [**JsonSchemaDocument**](JsonSchemaDocument.html) |  | [optional] |
| **output_schema** | [**JsonSchemaDocument**](JsonSchemaDocument.html) |  | [optional] |
| **nlu_info** | [**NluInfo**](NluInfo.html) | Information about the natural language understanding configuration for the flow version | [optional] |
| **supported_languages** | [**list[SupportedLanguage]**](SupportedLanguage.html) | List of supported languages for this version of the flow | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


