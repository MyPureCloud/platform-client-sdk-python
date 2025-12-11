# DeploymentIdentityResolutionConfig

## DeploymentIdentityResolutionConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division** | [WritableStarrableDivision](WritableStarrableDivision) | The division to use when performing identity resolution. | [optional] |
| **resolve_identities** | bool | Whether the channel should resolve identities | |
| **external_source** | [IdentityResolutionExternalSource](IdentityResolutionExternalSource) | The external source used for stitching this channel. | [optional] |
| **automerge** | [IdentityResolutionAutomergeConfig](IdentityResolutionAutomergeConfig) | Whether automerging of contacts should be enabled for each channel. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_
