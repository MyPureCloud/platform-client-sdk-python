---
title: CoachingAppointmentStatusDto
---
## CoachingAppointmentStatusDto

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **appointment** | [**CoachingAppointmentReference**](CoachingAppointmentReference.html) | The coaching appointment this status belongs to | [optional] |
| **created_by** | [**UserReference**](UserReference.html) | User who updated the status | [optional] |
| **date_created** | **datetime** | Creation time of the status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **status** | **str** | The status of the coaching appointment | |
{: class="table table-striped"}

