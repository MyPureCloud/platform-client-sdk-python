# CaseAssociation

## CaseAssociation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the association. | [optional] |
| **name** | str |  | [optional] |
| **association_type** | str | The association type. | [optional] |
| **date_associated** | datetime | The date of the interaction association. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **workitem** | [WorkitemReference](WorkitemReference) | The associated Workitem. | [optional] |
| **conversation** | [ConversationReference](ConversationReference) | The associated Conversation. | [optional] |
| **stage** | [StageReference](StageReference) | The Stage related to this association. | [optional] |
| **step** | [StepReference](StepReference) | The Step related to this association. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **case** | [CaseReference](CaseReference) | The Case for this association. | [optional] |



_PureCloudPlatformClientV2 263.0.0_
