# CaseAssociation

## CaseAssociation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the association. | [optional] |
| **name** | str |  | [optional] |
| **association_type** | str | Association type. | [optional] |
| **date_associated** | datetime | Interaction association date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **workitem** | [WorkitemReference](WorkitemReference) | Associated workitem ID. | [optional] |
| **conversation** | [ConversationReference](ConversationReference) | Associated conversation ID. | [optional] |
| **stage** | [StageReference](StageReference) | The stage related to this association. | [optional] |
| **step** | [StepReference](StepReference) | The step related to this association. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **case** | [CaseReference](CaseReference) | Case ID | [optional] |



_PureCloudPlatformClientV2 256.0.0_
