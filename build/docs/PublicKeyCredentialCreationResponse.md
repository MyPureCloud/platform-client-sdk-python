# PublicKeyCredentialCreationResponse

## PublicKeyCredentialCreationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The credential identifier (base64url-encoded). | |
| **type** | str | The credential type (must be &#39;public-key&#39;). | |
| **raw_id** | str | The raw credential identifier as a binary value (base64url-encoded). | |
| **authenticator_attachment** | str | The authenticator attachment modality used (&#39;platform&#39; or &#39;cross-platform&#39;). | [optional] |
| **client_extension_results** | dict(str, object) | Outputs from client-side WebAuthn extensions. | [optional] |
| **response** | [AuthenticatorAttestationResponse](AuthenticatorAttestationResponse) | The authenticator&#39;s attestation response. | |



_PureCloudPlatformClientV2 266.0.0_
