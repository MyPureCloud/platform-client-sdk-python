# IntegrationType

## IntegrationType

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the integration type. | |
| **name** | str |  | [optional] |
| **description** | str | Description of the integration type. | [optional] |
| **provider** | str | PureCloud provider of the integration type. | [optional] |
| **category** | str | Category describing the integration type. | [optional] |
| **images** | [list[Image]](Image) | Collection of logos. | [optional] |
| **config_properties_schema_uri** | str | URI of the schema describing the key-value properties needed to configure an integration of this type. | [optional] |
| **config_advanced_schema_uri** | str | URI of the schema describing the advanced JSON document needed to configure an integration of this type. | [optional] |
| **help_uri** | str | URI of a page with more information about the integration type | [optional] |
| **terms_of_service_uri** | str | URI of a page with terms and conditions for the integration type | [optional] |
| **vendor_name** | str | Name of the vendor of this integration type | [optional] |
| **vendor_website_uri** | str | URI of the vendor&#39;s website | [optional] |
| **marketplace_uri** | str | URI of the marketplace listing for this integration type | [optional] |
| **faq_uri** | str | URI of frequently asked questions about the integration type | [optional] |
| **privacy_policy_uri** | str | URI of a privacy policy for users of the integration type | [optional] |
| **support_contact_uri** | str | URI for vendor support | [optional] |
| **sales_contact_uri** | str | URI for vendor sales information | [optional] |
| **help_links** | [list[HelpLink]](HelpLink) | List of links to additional help resources | [optional] |
| **credentials** | [dict(str, CredentialSpecification)](CredentialSpecification) | Map of credentials for integrations of this type. The key is the name of a credential that can be provided in the credentials property of the integration configuration. | [optional] |
| **non_installable** | bool | Indicates if the integration type is installable or not. | [optional] |
| **max_instances** | int | The maximum number of integration instances allowable for this integration type | [optional] |
| **user_permissions** | list[str] | List of permissions required to permit user access to the integration type. | [optional] |
| **vendor_o_auth_client_ids** | list[str] | List of OAuth Client IDs that must be authorized when the integration is created. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
