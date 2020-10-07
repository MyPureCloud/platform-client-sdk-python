---
title: Annotation
---
## Annotation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **location** | **int** | Offset of annotation in milliseconds. | [optional] |
| **duration_ms** | **int** | Duration of annotation in milliseconds. | [optional] |
| **absolute_location** | **int** | Offset of annotation (milliseconds) from start of recording. | [optional] |
| **absolute_duration_ms** | **int** | Duration of annotation (milliseconds). | [optional] |
| **recording_location** | **int** | Offset of annotation (milliseconds) from start of recording, adjusted for any recording cuts | [optional] |
| **recording_duration_ms** | **int** | Duration of annotation (milliseconds), adjusted for any recording cuts. | [optional] |
| **user** | [**User**](User.html) | User that created this annotation (if any). | [optional] |
| **description** | **str** | Text of annotation. Maximum character limit is 300. | [optional] |
| **keyword_name** | **str** | The word or phrase which is being looked for with speech recognition. | [optional] |
| **confidence** | **float** | Actual confidence that this is an accurate match. | [optional] |
| **keyword_set_id** | **str** | A unique identifier for the keyword set to which this spotted keyword belongs. | [optional] |
| **keyword_set_name** | **str** | The keyword set to which this spotted keyword belongs. | [optional] |
| **utterance** | **str** | The phonetic spellings for the phrase and alternate spellings. | [optional] |
| **time_begin** | **str** | Beginning time offset of the keyword spot match. | [optional] |
| **time_end** | **str** | Ending time offset of the keyword spot match. | [optional] |
| **keyword_confidence_threshold** | **str** | Configured sensitivity threshold that can be increased to lower false positives or decreased to reduce false negatives. | [optional] |
| **agent_score_modifier** | **str** | A modifier to the evaluation score when the phrase is spotted in the agent channel. | |
| **customer_score_modifier** | **str** | A modifier to the evaluation score when the phrase is spotted in the customer channel. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


