# WebDeploymentsOAuthRequestParameters

## WebDeploymentsOAuthRequestParameters

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **code** | str | The authorization code to be sent to the authentication server during the token request.  Refer to https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest | |
| **redirect_uri** | str | Redirect URI sent in the \&quot;Authentication Request\&quot;Refer to https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest | |
| **nonce** | str | Required if provided in the \&quot;Authentication Request\&quot;. Otherwise should be empty.String value used to associate a Client session with an ID Token, and to mitigate replay attacks. The value is passed through unmodified from the Authentication Request to the ID Token. Refer to https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest | [optional] |
| **max_age** | int | Required if provided in the  \&quot;Authentication Request\&quot;. Otherwise should be empty.Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated.Refer to https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest | [optional] |
| **code_verifier** | str | Required if authorizing using Proof Key for Code Exchange (PKCE). Otherwise should be empty.Random URL-safe string with a minimum length of 43 characters generated at start of authorization flow to mitigate the threat of having the authorization code intercepted. Refer to https://datatracker.ietf.org/doc/html/rfc7636 | [optional] |
| **iss** | str | Optional parameter. Set it if authorization server discovery metadata authorization_response_iss_parameter_supported is enabled. Refer to https://datatracker.ietf.org/doc/html/rfc9207 | [optional] |



_PureCloudPlatformClientV2 231.0.0_
