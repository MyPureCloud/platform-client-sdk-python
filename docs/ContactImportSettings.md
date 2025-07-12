# ContactImportSettings

## ContactImportSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Display name for the settings | |
| **matching_criteria** | list[str] | Which fields you want to identity resolution based on. (e.g.: Email, Phone). It can be empty, populated only one of them or it can be both for now. The order of the items is important for identity resolution | [optional] |
| **merge_contacts** | bool | Decides what happens when a record already found in the system. Action will be Upsert or Merge | |
| **external_source_id** | str | Define the corresponding source system by the customer, the customer can have different externalId source, they can collect this id from contact service | |
| **import_fields** | [list[ContactImportField]](ContactImportField) | Decides which field we need to send towards contact service | |
| **date_created** | datetime | Creation date for the settings. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
