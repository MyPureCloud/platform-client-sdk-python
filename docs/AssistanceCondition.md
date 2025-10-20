# AssistanceCondition

## AssistanceCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operator** | str | The operator for the assistance condition. The operator defines whether the listed topicIds should EXIST or NOTEXIST for the condition to be evaluated as true. | [optional] |
| **topic_ids** | list[str] | List of topicIds within the assistance condition which would be combined together using logical OR operator. Eg ( topicId_1 || topicId_2 ) . | [optional] |



_PureCloudPlatformClientV2 241.0.0_
