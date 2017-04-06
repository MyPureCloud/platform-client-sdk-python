---
title: Keyword
---
## Keyword

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **phrase** | **str** | The word or phrase which is being looked for with speech recognition. | |
| **confidence** | **int** | A sensitivity threshold that can be increased to lower false positives or decreased to reduce false negatives. | |
| **agent_score_modifier** | **int** | A modifier to the evaluation score when the phrase is spotted in the agent channel | |
| **customer_score_modifier** | **int** | A modifier to the evaluation score when the phrase is spotted in the customer channel | |
| **alternate_spellings** | **list[str]** | Other spellings of the phrase that can be added to reduce missed spots (false negatives). | [optional] |
| **pronunciations** | **list[str]** | The phonetic spellings for the phrase and alternate spellings. | [optional] |
| **anti_words** | **list[str]** | Words that are similar to the phrase but not desired. Added to reduce incorrect spots (false positives). | [optional] |
| **anti_pronunciations** | **list[str]** | The phonetic spellings for the antiWords. | [optional] |
| **spotability_index** | **float** | A prediction of how easy it is to unambiguously spot the keyword within its language based on spelling. | [optional] |
| **margin_of_error** | **float** |  | [optional] |
| **pronunciation** | **str** |  | [optional] |
{: class="table table-striped"}


