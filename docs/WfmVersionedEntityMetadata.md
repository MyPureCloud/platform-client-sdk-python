# WfmVersionedEntityMetadata

## WfmVersionedEntityMetadata

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **version** | int | The version of the associated entity.  Used to prevent conflicts on concurrent edits | |
| **modified_by** | [UserReference](UserReference) | The user who last modified the associated entity. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **date_modified** | datetime | The date the associated entity was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the associated entity, if available. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **date_created** | datetime | The date the associated entity was created, if available. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 244.0.0_
