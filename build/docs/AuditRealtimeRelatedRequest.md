---
title: AuditRealtimeRelatedRequest
---
## AuditRealtimeRelatedRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **audit_id** | **str** | The id of the audit of which related audits will be retrieved. | |
| **trustor_org_id** | **str** | The id of the trustor org to which the audit belongs. Used when searching for audits performed by a trustee user within a trustor org. | [optional] |
| **sort** | [**list[AuditQuerySort]**](AuditQuerySort.html) | Sort parameter for the query. | [optional] |
{: class="table table-striped"}


