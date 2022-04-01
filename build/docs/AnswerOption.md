---
title: AnswerOption
---
## AnswerOption

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **text** | **str** |  | [optional] |
| **value** | **int** |  | [optional] |
| **assistance_conditions** | [**list[AssistanceCondition]**](AssistanceCondition.html) | List of assistance conditions which are combined together with a logical AND operator. Eg ( assistanceCondtion1 &amp;&amp; assistanceCondition2 ) wherein assistanceCondition could be ( EXISTS topic1 || topic2 || ... ) or (NOTEXISTS topic3 || topic4 || ...). | [optional] |
{: class="table table-striped"}


