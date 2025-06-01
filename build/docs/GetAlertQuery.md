# GetAlertQuery

## GetAlertQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **rule_type** | str | The rule type of the alerts the query will return | |
| **query_type** | str | The type of query being performed. | |
| **alert_status** | str | The status of the alerts the query will return. | [optional] |
| **viewed_status** | str | The view status of the alerts the query will return. | [optional] |
| **page_number** | int | The page number of the queried response | [optional] |
| **page_size** | int | The number of entities to return of the queried response.  The max is 25 | [optional] |
| **sort_by** | str | The field to sort responses by.  The accepted choices are Name and DateStart | [optional] |
| **sort_order** | str | The order in which response will be sorted.  The accepted choices are Asc and Desc | [optional] |



_PureCloudPlatformClientV2 230.0.0_
