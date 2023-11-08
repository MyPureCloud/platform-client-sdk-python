---
title: SearchShiftTradesResponse
---
## SearchShiftTradesResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **trades** | [**list[SearchShiftTradeResponse]**](SearchShiftTradeResponse.html) | The shift trades that match the search criteria | [optional] |
| **download_url** | **str** | URL from which to fetch results for requests with a large result set. If populated, the downloaded data will conform to the same schema as would normally be returned, excepting downloaded data will never itself contain a downloadUrl | [optional] |
{: class="table table-striped"}


