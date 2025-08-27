# AlternativeShiftJobResponse

## AlternativeShiftJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str | The status of the alternative shift job | |
| **type** | str | The type of job | |
| **download_url** | str | The URL where completed results are available, only set if status &#x3D;&#x3D; &#39;Complete&#39; | [optional] |
| **error** | [ErrorBody](ErrorBody) | Any error information, only set if the status &#x3D;&#x3D; &#39;Error&#39; | [optional] |
| **view_offers_results** | [AlternativeShiftOffersViewResponseTemplate](AlternativeShiftOffersViewResponseTemplate) | Schema template for deserializing data returned from the downloadUrl. Use if type &#x3D;&#x3D; &#39;ListOffers&#39; or &#39;SearchOffers&#39; | [optional] |
| **view_trades_results** | [AlternativeShiftTradesViewResponseTemplate](AlternativeShiftTradesViewResponseTemplate) | Schema template for deserializing data returned from the downloadUrl. Use if type &#x3D;&#x3D; &#39;ListUserTrades&#39; or &#39;SearchTrades&#39; | [optional] |
| **bulk_update_trades_results** | [AlternativeShiftBulkUpdateTradesResponseTemplate](AlternativeShiftBulkUpdateTradesResponseTemplate) | Schema template for deserializing data returned from the downloadUrl. Use if type &#x3D;&#x3D; &#39;BulkUpdateTrades&#39; | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 236.0.0_
