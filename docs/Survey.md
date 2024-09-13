# Survey

## Survey

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **conversation** | [ConversationReference](ConversationReference) |  | [optional] |
| **survey_form** | [SurveyForm](SurveyForm) | Survey form used for this survey. | [optional] |
| **agent** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **status** | str |  | [optional] |
| **queue** | [QueueReference](QueueReference) |  | [optional] |
| **answers** | [SurveyScoringSet](SurveyScoringSet) |  | [optional] |
| **completed_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **survey_error_details** | [SurveyErrorDetails](SurveyErrorDetails) | Additional information about what happened when the survey is in Error status. | [optional] |
| **agent_team** | [Team](Team) | The team that the agent belongs to | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 211.0.0_
