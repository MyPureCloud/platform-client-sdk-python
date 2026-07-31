# PublicKeyCredentialCreationOptions

## PublicKeyCredentialCreationOptions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **challenge** | str | Cryptographic challenge from the relying party (base64url-encoded). Must be returned to the relying party in the authenticator&#39;s response. | |
| **rp** | [RelyingPartyEntity](RelyingPartyEntity) | Information about the relying party. | |
| **user** | [UserEntity](UserEntity) | Information about the user being registered. | |
| **pub_key_cred_params** | [list[CredentialParameter]](CredentialParameter) | Public key credential parameters acceptable to the relying party, in order of preference. | |
| **timeout** | int | Time in milliseconds the relying party is willing to wait for the registration operation to complete. | [optional] |
| **exclude_credentials** | [list[CredentialDescriptor]](CredentialDescriptor) | Credentials that should be excluded from registration (e.g., to prevent re-registering an existing authenticator). | [optional] |
| **authenticator_selection** | [AuthenticatorSelection](AuthenticatorSelection) | Constraints on the type of authenticator that can be used. | [optional] |
| **hints** | list[str] | Hints about the type of authenticator the user should use (e.g., &#39;security-key&#39;, &#39;client-device&#39;, &#39;hybrid&#39;). | [optional] |
| **attestation** | str | The relying party&#39;s attestation conveyance preference (&#39;none&#39;, &#39;indirect&#39;, &#39;direct&#39;, or &#39;enterprise&#39;). | [optional] |
| **attestation_formats** | list[str] | Acceptable attestation statement formats, in order of preference. | [optional] |
| **extensions** | dict(str, object) | Inputs to client-side WebAuthn extensions. | [optional] |



_PureCloudPlatformClientV2 263.0.0_
