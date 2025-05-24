# Outcome

## Outcome

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the outcome. | |
| **is_active** | bool | Whether or not the outcome is active. | |
| **display_name** | str | The display name of the outcome. | |
| **version** | int | The version of the outcome. | |
| **description** | str | A description of the outcome. | [optional] |
| **is_positive** | bool | Whether or not the outcome is positive. | |
| **context** | [Context](Context) | The context of the outcome. | |
| **journey** | [Journey](Journey) | The pattern of rules defining the filter of the outcome. | |
| **associated_value_field** | [AssociatedValueField](AssociatedValueField) | The field from the event indicating the associated value. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **created_date** | datetime | Timestamp indicating when the outcome was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **modified_date** | datetime | Timestamp indicating when the outcome was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |



_PureCloudPlatformClientV2 229.0.0_
