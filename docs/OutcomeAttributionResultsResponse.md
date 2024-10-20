# OutcomeAttributionResultsResponse

## OutcomeAttributionResultsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outcome_id** | str | ID of Outcome. | [optional] |
| **index** | int | The index/position of the OutcomeAttribution in the original POST request. | [optional] |
| **external_contact_id** | str | The external contact ID of the customer who achieved the outcome. | [optional] |
| **associated_value** | float | The total value associated with the customer&#39;s outcome. | [optional] |
| **state** | str | State of the Outcome Attribution entity. | |
| **message** | str | Additional information on the state of the Outcome Attribution entity. | |
| **touchpoints** | [list[TouchpointResponse]](TouchpointResponse) | List of interactions that led to this outcome being achieved. | [optional] |
| **created_date** | datetime | Date outcome was achieved. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 214.0.0_
