# AnswerOption

## AnswerOption

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **context_id** | str | An identifier for this answer that stays the same across versions of the form. | [optional] |
| **built_in_type** | str | The built-in type of this answer option. Only used for built-in answer options such as selection states for Multiple Select answer options. Possible values include: Selected, Unselected | [optional] |
| **text** | str |  | [optional] |
| **value** | int |  | [optional] |
| **assistance_conditions** | [list[AssistanceCondition]](AssistanceCondition) | List of assistance conditions which are combined together with a logical AND operator. Eg ( assistanceCondtion1 &amp;&amp; assistanceCondition2 ) wherein assistanceCondition could be ( EXISTS topic1 || topic2 || ... ) or (NOTEXISTS topic3 || topic4 || ...). | [optional] |



_PureCloudPlatformClientV2 247.0.0_
