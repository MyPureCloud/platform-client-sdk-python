# AuthenticatorSelection

## AuthenticatorSelection

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **authenticator_attachment** | str | Desired authenticator attachment modality (&#39;platform&#39; or &#39;cross-platform&#39;). | [optional] |
| **require_resident_key** | bool | Whether a resident (discoverable) credential is required. Deprecated by the WebAuthn spec in favor of residentKey. | [optional] |
| **resident_key** | str | The relying party&#39;s requirement for resident (discoverable) credentials (&#39;discouraged&#39;, &#39;preferred&#39;, or &#39;required&#39;). | [optional] |
| **user_verification** | str | The user verification requirement (&#39;discouraged&#39;, &#39;preferred&#39;, or &#39;required&#39;). | [optional] |



_PureCloudPlatformClientV2 263.0.0_
