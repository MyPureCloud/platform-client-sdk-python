# TrustUser

## TrustUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **chat** | [Chat](Chat) |  | [optional] |
| **department** | str |  | [optional] |
| **email** | str |  | [optional] |
| **primary_contact_info** | [list[Contact]](Contact) | Auto populated from addresses. | [optional] |
| **addresses** | [list[Contact]](Contact) | Email addresses and phone numbers for this user | [optional] |
| **state** | str | The current state for this user. | [optional] |
| **title** | str |  | [optional] |
| **username** | str |  | [optional] |
| **manager** | [User](User) |  | [optional] |
| **images** | [list[Image]](Image) |  | [optional] |
| **version** | int | Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH. | |
| **certifications** | list[str] |  | [optional] |
| **biography** | [Biography](Biography) |  | [optional] |
| **employer_info** | [EmployerInfo](EmployerInfo) |  | [optional] |
| **preferred_name** | str | Preferred full name of the agent | [optional] |
| **routing_status** | [RoutingStatus](RoutingStatus) | ACD routing status | [optional] |
| **presence** | [UserPresence](UserPresence) | Active presence | [optional] |
| **integration_presence** | [UserPresence](UserPresence) | Integration presence | [optional] |
| **conversation_summary** | [UserConversationSummary](UserConversationSummary) | Summary of conversion statistics for conversation types. | [optional] |
| **out_of_office** | [OutOfOffice](OutOfOffice) | Determine if out of office is enabled | [optional] |
| **geolocation** | [Geolocation](Geolocation) | Current geolocation position | [optional] |
| **station** | [UserStations](UserStations) | Effective, default, and last station information | [optional] |
| **authorization** | [UserAuthorization](UserAuthorization) | Roles and permissions assigned to the user | [optional] |
| **profile_skills** | list[str] | Profile skills possessed by the user | [optional] |
| **locations** | [list[Location]](Location) | The user placement at each site location. | [optional] |
| **groups** | [list[Group]](Group) | The groups the user is a member of | [optional] |
| **team** | [Team](Team) | The team the user is a member of | [optional] |
| **work_plan_bid_ranks** | [WorkPlanBidRanks](WorkPlanBidRanks) | The WFM work plan bid rank settings for the user | [optional] |
| **skills** | [list[UserRoutingSkill]](UserRoutingSkill) | Routing (ACD) skills possessed by the user | [optional] |
| **languages** | [list[UserRoutingLanguage]](UserRoutingLanguage) | Routing (ACD) languages possessed by the user | [optional] |
| **acd_auto_answer** | bool | acd auto answer | [optional] |
| **language_preference** | str | preferred language by the user | [optional] |
| **last_token_issued** | [OAuthLastTokenIssued](OAuthLastTokenIssued) |  | [optional] |
| **date_last_login** | datetime | The last time the user logged in using username and password. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_welcome_sent** | datetime | The date &amp; time the user was sent their welcome email. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **trust_user_details** | [TrustUserDetails](TrustUserDetails) |  | [optional] |



_PureCloudPlatformClientV2 238.0.0_
