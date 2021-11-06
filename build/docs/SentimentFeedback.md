---
title: SentimentFeedback
---
## SentimentFeedback

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **phrase** | **str** | The phrase for which sentiment feedback is provided | |
| **dialect** | **str** | The dialect for the given phrase, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | |
| **feedback_value** | **str** | The sentiment feedback value for the given phrase | |
| **date_created** | **datetime** | The Timestamp when sentiment feedback created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**AddressableEntityRef**](AddressableEntityRef.html) | The Id of user who created the sentiment feedback | [optional] |
{: class="table table-striped"}


