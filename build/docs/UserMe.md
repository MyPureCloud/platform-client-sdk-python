---
title: UserMe
---
## UserMe

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **chat** | [**Chat**](Chat.html) |  | [optional] |
| **department** | **str** |  | [optional] |
| **email** | **str** |  | [optional] |
| **primary_contact_info** | [**list[Contact]**](Contact.html) | Auto populated from addresses. | [optional] |
| **addresses** | [**list[Contact]**](Contact.html) | Email addresses and phone numbers for this user | [optional] |
| **state** | **str** | The current state for this user. | [optional] |
| **title** | **str** |  | [optional] |
| **username** | **str** |  | [optional] |
| **manager** | [**User**](User.html) |  | [optional] |
| **images** | [**list[UserImage]**](UserImage.html) |  | [optional] |
| **version** | **int** | Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH. | |
| **certifications** | **list[str]** |  | [optional] |
| **biography** | [**Biography**](Biography.html) |  | [optional] |
| **employer_info** | [**EmployerInfo**](EmployerInfo.html) |  | [optional] |
| **routing_status** | [**RoutingStatus**](RoutingStatus.html) | ACD routing status | [optional] |
| **presence** | [**UserPresence**](UserPresence.html) | Active presence | [optional] |
| **conversation_summary** | [**UserConversationSummary**](UserConversationSummary.html) | Summary of conversion statistics for conversation types. | [optional] |
| **out_of_office** | [**OutOfOffice**](OutOfOffice.html) | Determine if out of office is enabled | [optional] |
| **geolocation** | [**Geolocation**](Geolocation.html) | Current geolocation position | [optional] |
| **station** | [**UserStations**](UserStations.html) | Effective, default, and last station information | [optional] |
| **authorization** | [**UserAuthorization**](UserAuthorization.html) | Roles and permissions assigned to the user | [optional] |
| **profile_skills** | **list[str]** | Profile skills possessed by the user | [optional] |
| **locations** | [**list[Location]**](Location.html) | The user placement at each site location. | [optional] |
| **groups** | [**list[Group]**](Group.html) | The groups the user is a member of | [optional] |
| **skills** | [**list[UserRoutingSkill]**](UserRoutingSkill.html) | Routing (ACD) skills possessed by the user | [optional] |
| **languages** | [**list[UserRoutingLanguage]**](UserRoutingLanguage.html) | Routing (ACD) languages possessed by the user | [optional] |
| **acd_auto_answer** | **bool** | acd auto answer | [optional] |
| **language_preference** | **str** | preferred language by the user | [optional] |
| **last_token_issued** | [**OAuthLastTokenIssued**](OAuthLastTokenIssued.html) |  | [optional] |
| **date** | [**ServerDate**](ServerDate.html) | The PureCloud system date time. | [optional] |
| **geolocation_settings** | [**GeolocationSettings**](GeolocationSettings.html) | Geolocation settings for user&#39;s organization. | [optional] |
| **organization** | [**Organization**](Organization.html) | Organization details for this user. | [optional] |
| **presence_definitions** | [**list[OrganizationPresence]**](OrganizationPresence.html) | The first 100 presence definitions for user&#39;s organization. | [optional] |
| **location_definitions** | [**list[LocationDefinition]**](LocationDefinition.html) | The first 100 site locations for user&#39;s organization | [optional] |
| **org_authorization** | [**list[DomainOrganizationRole]**](DomainOrganizationRole.html) | The first 100 organization roles, with applicable permission policies, for user&#39;s organization. | [optional] |
| **favorites** | [**list[User]**](User.html) | The first 50 favorited users. | [optional] |
| **superiors** | [**list[User]**](User.html) | The first 50 superiors of this user. | [optional] |
| **direct_reports** | [**list[User]**](User.html) | The first 50 direct reports to this user. | [optional] |
| **adjacents** | [**Adjacents**](Adjacents.html) | The first 50 superiors, direct reports, and siblings of this user. Mutually exclusive with superiors and direct reports expands. | [optional] |
| **routing_skills** | [**list[RoutingSkill]**](RoutingSkill.html) | The first 50 routing skills for user&#39;s organizations | [optional] |
| **field_configs** | [**FieldConfigs**](FieldConfigs.html) | The field config for all entities types of user&#39;s organization | [optional] |
| **token** | [**TokenInfo**](TokenInfo.html) | Information about the current token | [optional] |
| **trustors** | [**list[Trustor]**](Trustor.html) | Organizations having this user as a trustee | [optional] |
| **org_products** | [**list[DomainOrganizationProduct]**](DomainOrganizationProduct.html) | Products enabled in this organization | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


