---
title: ActivityPlanJobResponse
---
## ActivityPlanJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **activity_plan** | [**ActivityPlanReference**](ActivityPlanReference.html) | The activity plan associated with this job | |
| **status** | **str** | The status of the job | |
| **exceptions** | [**list[ActivityPlanJobException]**](ActivityPlanJobException.html) | The list of exceptions that occurred while running this activity plan job. These are exceptions that affect individual occurrences but didn&#39;t prevent the job from completing | |
| **error** | [**ErrorBody**](ErrorBody.html) | Error details if status &#x3D;&#x3D; &#39;Error&#39;. These are errors that caused the job to fail to complete | [optional] |
| **occurrence** | [**ActivityPlanOccurrenceReference**](ActivityPlanOccurrenceReference.html) | The occurrence associated with this job if type &#x3D;&#x3D; &#39;DeleteOccurrence&#39; | [optional] |
| **type** | **str** | The type of the job | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

