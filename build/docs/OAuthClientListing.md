---
title: OAuthClientListing
---
## OAuthClientListing

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the OAuth client. | |
| **access_token_validity_seconds** | **int** | The number of seconds, between 5mins and 48hrs, until tokens created with this client expire. If this field is omitted, a default of 24 hours will be applied. | [optional] |
| **description** | **str** |  | [optional] |
| **registered_redirect_uri** | **list[str]** | List of allowed callbacks for this client. For example: https://myap.example.com/auth/callback | [optional] |
| **secret** | **str** | System created secret assigned to this client. Secrets are required for code authorization and client credential grants. | [optional] |
| **role_ids** | **list[str]** | Roles assigned to this client. Roles only apply to clients using the client_credential grant | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


