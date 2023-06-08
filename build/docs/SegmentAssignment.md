---
title: SegmentAssignment
---
## SegmentAssignment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique identifier for the segment assignment. | [optional] |
| **state** | **str** | State of the segment assignment. | [optional] |
| **date_assigned** | **datetime** | Date when the segment was assigned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_unassigned** | **datetime** | Date when the segment was unassigned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date when the segment assignment was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **segment** | [**SegmentAssignmentSegment**](SegmentAssignmentSegment.html) | The segment the assignment is for. | [optional] |
| **customer_id** | **str** | ID of the customer to which the segment is assigned. | [optional] |
| **customer_id_type** | **str** | Type of customer ID (e.g. cookie, email, phone). | [optional] |
| **session** | [**SegmentAssignmentSession**](SegmentAssignmentSession.html) | For session-scoped segments, the session for which the segment was assigned. | [optional] |
| **external_contact** | [**AddressableEntityRef**](AddressableEntityRef.html) | External contact of the customer to which the segment is assigned. | [optional] |
{: class="table table-striped"}


