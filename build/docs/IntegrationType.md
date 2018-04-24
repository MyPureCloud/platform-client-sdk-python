---
title: IntegrationType
---
## IntegrationType

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of the integration type. | |
| **name** | **str** |  | [optional] |
| **description** | **str** | Description of the integration type. | [optional] |
| **provider** | **str** | PureCloud provider of the integration type. | [optional] |
| **category** | **str** | Category describing the integration type. | [optional] |
| **images** | [**list[UserImage]**](UserImage.html) | Collection of logos. | [optional] |
| **config_properties_schema_uri** | **str** | URI of the schema describing the key-value properties needed to configure an integration of this type. | [optional] |
| **config_advanced_schema_uri** | **str** | URI of the schema describing the advanced JSON document needed to configure an integration of this type. | [optional] |
| **help_uri** | **str** | URI of a page with more information about the integration type | [optional] |
| **credentials** | [**dict(str, CredentialSpecification)**](CredentialSpecification.html) | Map of credentials for integrations of this type. The key is the name of a credential that can be provided in the credentials property of the integration configuration. | [optional] |
| **non_installable** | **bool** | Indicates if the integration type is installable or not. | [optional] |
| **max_instances** | **int** | The maximum number of integration instances allowable for this integration type | [optional] |
| **user_permissions** | **list[str]** | List of permissions required to permit user access to the integration type. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


