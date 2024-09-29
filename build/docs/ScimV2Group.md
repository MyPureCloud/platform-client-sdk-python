# ScimV2Group

## ScimV2Group

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the SCIM resource. Set by the service provider. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readOnly\&quot;. \&quot;returned\&quot; is set to \&quot;always\&quot;. | [optional] |
| **schemas** | list[str] | The list of supported schemas. | [optional] |
| **display_name** | str | The display name of the group. | |
| **external_id** | str | The external ID of the group. Set by the provisioning client. \&quot;caseExact\&quot; is set to \&quot;true\&quot;. \&quot;mutability\&quot; is set to \&quot;readWrite\&quot;. | [optional] |
| **members** | [list[ScimV2MemberReference]](ScimV2MemberReference) | The list of members in the group. | [optional] |
| **meta** | [ScimMetadata](ScimMetadata) | The metadata of the SCIM resource. Metadata is defined as immutable per SCIM RFC. | [optional] |



_PureCloudPlatformClientV2 212.0.0_
