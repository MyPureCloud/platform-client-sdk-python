# SummarySetting

## SummarySetting

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Name of the summary setting. | |
| **language** | str | Language of the generated summary, e.g. en-US, it-IT. | |
| **summary_type** | str | Level of detail of the generated summary. | [optional] |
| **format** | str | Format of the generated summary. | [optional] |
| **mask_pii** | [SummarySettingPII](SummarySettingPII) | Displaying PII in the generated summary. | [optional] |
| **participant_labels** | [SummarySettingParticipantLabels](SummarySettingParticipantLabels) | How to refer to interaction participants in the generated summary. | [optional] |
| **predefined_insights** | list[str] | Set which insights to include in the generated summary by default. | [optional] |
| **custom_entities** | [list[SummarySettingCustomEntity]](SummarySettingCustomEntity) | Custom entity definition. | [optional] |
| **setting_type** | str | Type of the summary setting. | [optional] |
| **prompt** | str | Custom prompt of summary setting. | [optional] |
| **date_created** | datetime | The date and time the setting was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date and time the setting was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 245.0.0_
