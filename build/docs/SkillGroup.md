# SkillGroup

## SkillGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The group name. | |
| **division** | [WritableDivision](WritableDivision) | The division to which this entity belongs. | [optional] |
| **description** | str | Group description | [optional] |
| **member_count** | int | Estimated number of members in this group. It can take some time for the count to be updated after expressions are changed. | [optional] |
| **date_modified** | datetime | Last modified date/time of the skill group. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_created** | datetime | Created date/time of the skill group. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | Group&#39;s filling status | [optional] |
| **skill_conditions** | [list[SkillGroupCondition]](SkillGroupCondition) | Conditions for this group | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
