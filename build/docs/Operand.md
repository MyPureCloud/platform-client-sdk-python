# Operand

## Operand

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The Operand type of the category | |
| **occurrence** | int | The minimum number of occurrences of the defined operand type | [optional] |
| **inverted** | bool | Applies a NOT modifier to the operand group | [optional] |
| **term** | [Term](Term) | Filter interaction by word(s) | [optional] |
| **topic_id** | str | Filter interaction by topic ID | [optional] |
| **voice_seconds_position** | [OperandPosition](OperandPosition) | Dictates when the operand must occur in a voice interaction | [optional] |
| **digital_words_position** | [OperandPosition](OperandPosition) | Dictates when the operand must occur in a digital interaction | [optional] |
| **infix_operator** | [InfixOperator](InfixOperator) | Defines a logical operation that is applied on the current operand, against the following operand | [optional] |
| **operands** | [list[Operand]](Operand) | Contains a new level of operands | [optional] |



_PureCloudPlatformClientV2 229.0.0_
