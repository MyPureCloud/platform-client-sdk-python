# Disposition

## Disposition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Name of the disposition. Either a platform predefined value, or the name of the disposition in the disposition table.. | |
| **analyzer** | str | The final media analyzer result that triggered the disposition result, if any. | [optional] |
| **disposition_parameters** | [DispositionParameters](DispositionParameters) | Contains various parameters related to call analysis. | [optional] |
| **detected_speech_start** | datetime | Absolute time when the speech started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **detected_speech_end** | datetime | Absolute time when the speech ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 220.0.0_
