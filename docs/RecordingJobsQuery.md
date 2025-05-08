# RecordingJobsQuery

## RecordingJobsQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **action** | str | Operation to perform bulk task. If the operation will cause the delete date of a recording to be older than the export date, the export date will be adjusted to the delete date. | |
| **action_date** | datetime | The date when the action will be performed. If screenRecordingActionDate is also provided, this value is only used for non-screen recordings. Otherwise this value is used for all recordings. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **action_age** | int | The number of days after each recording&#39;s creation date when the action will be performed. If screenRecordingActionAge is also provided, this value is only used for non-screen recordings. Otherwise this value is used for all recordings. | [optional] |
| **screen_recording_action_date** | datetime | The date when the action will be performed for screen recordings. If this is provided then includeScreenRecordings must be true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **screen_recording_action_age** | int | The number of days after each screen recording&#39;s creation date when the action will be performed. If this is provided then includeScreenRecordings must be true. | [optional] |
| **integration_id** | str | IntegrationId to Access AWS S3 bucket for bulk recording exports. This field is required and used only for EXPORT action. | [optional] |
| **include_recordings_with_sensitive_data** | bool | Whether to include recordings with PCI DSS and/or PII data, default value &#x3D; false  | [optional] |
| **include_screen_recordings** | bool | Whether to include Screen recordings for the action, default value &#x3D; true  | [optional] |
| **clear_export** | bool | For DELETE action, setting this to true will clear any pending exports for recordings. This field is only used for DELETE action. Default value &#x3D; false | [optional] |
| **conversation_query** | [AsyncConversationQuery](AsyncConversationQuery) | Conversation Query. Note: After the recording is created, it might take up to 48 hours for the recording to be included in the submitted job query.  This result depends on the analytics data lake job completion. See also: https://developer.genesys.cloud/analyticsdatamanagement/analytics/jobs/conversation-details-job#data-availability.This is supported only when querying for conversations up to and including 5 years old. | [optional] |
| **aged_conversation_interval** | str | As an alternative to conversationQuery, specify the date and time range of conversations that are older than 5 years to query.Results will include all conversations that had activity during the interval. This is supported only when querying for conversations older than 5 years;conversationQuery must not be provided when this is provided. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss.Interval duration must not exceed 6 months. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |



_PureCloudPlatformClientV2 227.1.0_
