---
title: SkillGroupRoutingCondition
---
## SkillGroupRoutingCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **routing_skill** | **str** | The routing skill to be used in the skill condition query | |
| **comparator** | **str** | Comparator that will be applied to the proficiency | |
| **proficiency** | **int** | The skill proficiency that will be used for the routing skill. Integer range 0-5 | |
| **child_conditions** | [**list[SkillGroupCondition]**](SkillGroupCondition.html) | Nested conditions to be applied to this skill condition | [optional] |
{: class="table table-striped"}


