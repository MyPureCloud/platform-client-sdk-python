---
title: ScimUserExtensions
---
## ScimUserExtensions

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **routing_skills** | [**list[ScimUserRoutingSkill]**](ScimUserRoutingSkill.html) | The list of routing skills assigned to a user. Maximum 50 skills. | [optional] |
| **routing_languages** | [**list[ScimUserRoutingLanguage]**](ScimUserRoutingLanguage.html) | The list of routing languages assigned to a user. Maximum 50 languages. | [optional] |
| **external_ids** | [**list[ScimGenesysUserExternalId]**](ScimGenesysUserExternalId.html) | The list of external identifiers assigned to user. Always includes an immutable SCIM authority prefixed with \&quot;x-pc:scimv2:v1\&quot;. ExternalIds are searchable with complex filter query parameter using &#39;authority&#39; and &#39;value&#39;, e.g., filter=urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds[authority eq \&quot;matchAuthName\&quot; and value eq \&quot;matchingExternalKeyValue\&quot;]. | [optional] |
{: class="table table-striped"}


