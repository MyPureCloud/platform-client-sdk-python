# MaskingRule

## MaskingRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Masking rule name. | |
| **description** | str | Description about masking rule. | [optional] |
| **substitute_character** | str | Replacement character for masked text character. | |
| **definition** | str | Definition of masking rule (a valid regex or builtin AI based mask name). | |
| **enabled** | bool | True/False | |
| **type** | str | Masking rule type | |
| **direction** | str | inbound/outbound | [optional] |
| **integrations** | list[str] | Associated integration channels | [optional] |
| **date_created** | datetime | Date when the rule was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the rule was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 246.1.0_
