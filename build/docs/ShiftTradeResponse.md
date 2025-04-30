# ShiftTradeResponse

## ShiftTradeResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of this shift trade | [optional] |
| **week_date** | date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **schedule** | [BuScheduleReferenceForMuRoute](BuScheduleReferenceForMuRoute) | A reference to the associated schedule | [optional] |
| **state** | str | The state of this shift trade | [optional] |
| **initiating_user** | [UserReference](UserReference) | The user who initiated this trade | [optional] |
| **initiating_shift_id** | str | The ID of the shift offered for trade by the initiating user | [optional] |
| **initiating_shift_start** | datetime | The start date/time of the shift being offered for trade. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **initiating_shift_end** | datetime | The end date/time of the shift being offered for trade. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **receiving_user** | [UserReference](UserReference) | The user matching the trade, or if the state is not &#39;Matched&#39;, the user to whom the trade request was sent | [optional] |
| **receiving_shift_id** | str | The ID of the shift being exchanged for the initiating shift, null if the receiving user is picking up a shift | [optional] |
| **receiving_shift_start** | datetime | The start date/time of the receiving shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **receiving_shift_end** | datetime | The end date/time of the receiving shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **expiration** | datetime | When this shift trade offer will expire if not matched or approved. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **one_sided** | bool | Whether this is a one-sided shift trade (e.g. the initiating user is not asking for a shift in return) | [optional] |
| **acceptable_intervals** | list[str] | Time frames when the initiating user is willing to accept trades. Empty means giving up the shift. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **reviewed_by** | [UserReference](UserReference) | The user who reviewed this shift trade. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **reviewed_date** | datetime | The timestamp when this shift trade was reviewed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version data for this trade | [optional] |



_PureCloudPlatformClientV2 227.0.0_
