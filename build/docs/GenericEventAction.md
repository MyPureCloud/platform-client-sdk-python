---
title: GenericEventAction
---
## GenericEventAction

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | ID of the action. | |
| **state** | **str** | Current state of the action (e.g. qualified, succeeded, errored). | [optional] |
| **media_type** | **str** | The media type used to deliver the action (e.g. email, webhook). | [optional] |
| **prompt** | **str** | Prompt of the action to be displayed/sent to the visitor. | [optional] |
| **media_address** | **str** | Address of the media type used to deliver the action (e.g. email address, webhook URL). | [optional] |
| **created_date** | **datetime** | Timestamp indicating when the action was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}

