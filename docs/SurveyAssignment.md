# SurveyAssignment

## SurveyAssignment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **survey_form** | [PublishedSurveyFormReference](PublishedSurveyFormReference) | The survey form used for this survey. | [optional] |
| **flow** | [DomainEntityRef](DomainEntityRef) | The URI reference to the flow associated with this survey. | [optional] |
| **invite_time_interval** | str | An ISO 8601 repeated interval consisting of the number of repetitions, the start datetime, and the interval (e.g. R2/2018-03-01T13:00:00Z/P1M10DT2H30M). Total duration must not exceed 90 days. | [optional] |
| **sending_user** | str | User together with sendingDomain used to send email, null to use no-reply | [optional] |
| **sending_domain** | str | Validated email domain, required | |
| **use_threading_timeline_for_send_time** | bool | If true, the survey invitation send time will be calculated using the threading timeline. If false or unspecified, a fixed 72-hour delay will be used. Default is false for new policies. | [optional] |



_PureCloudPlatformClientV2 267.0.0_
