---
title: ContentList
---
## ContentList

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | An ID assigned to this rich message content. Each instance inside the content array has a unique ID. | [optional] |
| **list_type** | **str** | The type of list this instance represents | [optional] |
| **title** | **str** | Text to show in the title row | [optional] |
| **description** | **str** | Text to show in the description row. This is immediately below the title | [optional] |
| **submit_label** | **str** | Label for Submit button | [optional] |
| **actions** | [**ContentActions**](ContentActions.html) | User actions available on the content. All actions are optional and all actions are executed simultaneously. | [optional] |
| **components** | [**list[ListItemComponent]**](ListItemComponent.html) | An array of component objects | [optional] |
{: class="table table-striped"}


