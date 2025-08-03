# GetRulesQuery

## GetRulesQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **rule_type** | str | The rule type of the alerts the query will return | |
| **query_type** | str | The type of query being performed. | |
| **enabled_type** | str | The state of the rule the query will return.  The accepted choices are Enabled, Disabled, or All | [optional] |
| **page_number** | int | The page number of the queried response | [optional] |
| **page_size** | int | The number of entities to return of the queried response.  The max is 25 | [optional] |
| **sort_by** | str | The field to sort responses by.  The accepted choices are Name and DateStart | [optional] |
| **sort_order** | str | The order in which response will be sorted.  The accepted choices are Asc and Desc | [optional] |
| **rule_name** | str | The name of the rule being queries. | [optional] |
| **name_search_type** | str | Specifies how strict the name search needs to be. Expected values are Exact and Contains if querying by name. | [optional] |



_PureCloudPlatformClientV2 234.0.0_
