# QuarterHourly

## QuarterHourly

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **download_urls** | list[str] | List of download URLs to fetch the result of quarter hour time series. This field is populated only if session state is Complete. The downloaded data contains Newline Delimited JSON (NDJSON): one JSON object per line | [optional] |
| **download_result** | [list[ContinuousForecastTimeSeries]](ContinuousForecastTimeSeries) | Result will always come via downloadUrls; however the schema is included for documentation | [optional] |



_PureCloudPlatformClientV2 266.0.0_
