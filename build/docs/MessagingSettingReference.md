---
title: MessagingSettingReference
---
## MessagingSettingReference

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The messaging Setting unique identifier associated with this integration | |
| **name** | **str** | The messaging Setting profile name | [optional] |
| **self_uri** | **str** | The messaging Setting profile URI | [optional] |
| **date_created** | **datetime** | Date this messaging Setting was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date this messaging Setting was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **str** | Version number | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that created this Setting | [optional] |
| **updated_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that modified this Setting | [optional] |
| **content** | [**ContentSetting**](ContentSetting.html) | Settings relating to message contents | [optional] |
| **event** | [**EventSetting**](EventSetting.html) | Settings relating to events which may occur | [optional] |
{: class="table table-striped"}


