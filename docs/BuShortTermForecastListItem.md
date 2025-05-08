# BuShortTermForecastListItem

## BuShortTermForecastListItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **week_date** | date | The start week date of this forecast in yyyy-MM-dd.  Must fall on the start day of week for the associated business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **week_count** | int | The number of weeks this forecast covers | [optional] |
| **creation_method** | str | The method by which this forecast was created | [optional] |
| **description** | str | The description of this forecast | [optional] |
| **legacy** | bool | Whether this forecast contains modifications on legacy metrics | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Metadata for this forecast | [optional] |
| **can_use_for_scheduling** | bool | Whether this forecast can be used for scheduling | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_
