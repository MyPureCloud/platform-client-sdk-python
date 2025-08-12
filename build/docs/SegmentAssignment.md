# SegmentAssignment

## SegmentAssignment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_assigned** | datetime | Date when the segment was assigned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_for_unassignment** | datetime | Date indicating when a segment is scheduled to be unassigned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **segment** | [SegmentAssignmentSegment](SegmentAssignmentSegment) | The segment the assignment is for. | |
| **session** | [SegmentAssignmentSession](SegmentAssignmentSession) | For session-scoped segments, the session for which the segment was assigned. | [optional] |
| **external_contact** | [AddressableEntityRef](AddressableEntityRef) | External contact of the customer to which the segment is assigned. | |



_PureCloudPlatformClientV2 235.0.0_
