# DmarcResult

## DmarcResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | The DMARC status of this domain | |
| **detected_policy** | str | The DMARC policy that was detected in the associated DNS record, if one is present | [optional] |
| **date_checked** | datetime | The date of the most recent check of the domain&#39;s DMARC DNS record. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **records** | [list[Record]](Record) | The minimum DMARC DNS record that Genesys Cloud recommends | |



_PureCloudPlatformClientV2 256.0.0_
