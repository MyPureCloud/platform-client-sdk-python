# DictionaryFeedback

## DictionaryFeedback

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **term** | str | The dictionary term which needs to be added to dictionary feedback system | |
| **dialect** | str | The dialect for the given term, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | |
| **boost_value** | float | A weighted value assigned to a phrase. The higher the value, the higher the likelihood that the system will choose the word or phrase from the possible alternatives. Boost range is from 1.0 to 10.0. Default is 2.0 | [optional] |
| **source** | str | The source of the given dictionary feedback | [optional] |
| **date_created** | datetime | The Timestamp when dictionary feedback created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The Id of the user who created the dictionary feedback | [optional] |
| **date_modified** | datetime | The Timestamp when dictionary feedback modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The Id of the user who modified the dictionary feedback | [optional] |
| **example_phrases** | [list[DictionaryFeedbackExamplePhrase]](DictionaryFeedbackExamplePhrase) | A list of at least 3 and up to 20 unique phrases that are example usage of the term | |
| **sounds_like** | list[str] | A list of up to 10 terms that give examples of how the term sounds | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.0.0_
