---
title: ContentGeneric
---
## ContentGeneric

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | An ID assigned to this rich message content. Each instance inside the content array has a unique ID. | [optional] |
| **title** | **str** | Text to show in the title row | [optional] |
| **description** | **str** | Text to show in the description row. This is immediately below the title | [optional] |
| **image** | **str** | Path or URI to an image file | [optional] |
| **video** | **str** | Path or URI to a video file | [optional] |
| **actions** | [**ContentActions**](ContentActions.html) | User actions available on the content. All actions are optional and all actions are executed simultaneously. | [optional] |
| **components** | [**list[ButtonComponent]**](ButtonComponent.html) | An array of component objects | [optional] |
{: class="table table-striped"}


