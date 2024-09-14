# Organization

## Organization

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **default_language** | str | The default language for this organization. Example: &#39;en&#39; | [optional] |
| **default_country_code** | str | The default country code for this organization. Example: &#39;US&#39; | [optional] |
| **third_party_org_name** | str | The short name for the organization. This field is globally unique and cannot be changed. | [optional] |
| **third_party_uri** | str |  | [optional] |
| **domain** | str |  | [optional] |
| **version** | int | The current version of the organization. | |
| **state** | str | The current state. Examples are active, inactive, deleted. | [optional] |
| **default_site_id** | str |  | [optional] |
| **support_uri** | str | Email address where support tickets are sent to. | [optional] |
| **voicemail_enabled** | bool |  | [optional] |
| **product_platform** | str | Organizations Originating Platform. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **features** | dict(str, bool) | The state of features available for the organization. | [optional] |



_PureCloudPlatformClientV2 211.1.0_
