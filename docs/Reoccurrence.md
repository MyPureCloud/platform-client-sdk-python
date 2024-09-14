# Reoccurrence

## Reoccurrence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **start** | str | The start date time of the initial occurrence as an ISO-8601 string in the format YYYY-MM-DDThh:mm:ss | |
| **end** | str | The end date time of the initial occurrence as an ISO-8601 string in the format YYYY-MM-DDThh:mm:ss | |
| **time_zone** | str | The time zone for the recurrence. The time zone of the recurrence is determined by prioritizing the recurrence&#39;s time zone if specified, then the schedule&#39;s time zone if set, and finally defaulting to UTC if neither defines a time zone. | |
| **pattern** | [Pattern](Pattern) | The schedule pattern e.g.: Daily/Weekly | |
| **range** | [Range](Range) | The schedule range e.g.: EndDate/NoEnd/Numbered | |
| **alterations** | [list[Alteration]](Alteration) | Modifications to the original recurrence schedule (Exclusions/Inclusions) | [optional] |
| **next_occurrence_details** | [NextOccurrenceDetails](NextOccurrenceDetails) | The next occurrence details for the next start and end occurrences for the recurrence | [optional] |



_PureCloudPlatformClientV2 211.1.0_
