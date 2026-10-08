# OperationalEvent

## OperationalEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_definition** | [AddressableEntityRef](AddressableEntityRef) | The event that occurred. | [optional] |
| **entity_id** | str | The unique identifier for the entity | [optional] |
| **entity_token** | str | A token representing the entity | [optional] |
| **entity_name** | str | The name for the entity | [optional] |
| **previous_value** | str | The value prior to the event | [optional] |
| **current_value** | str | The changed value following the event | [optional] |
| **error_code** | str | The error code of the entity in the providing service associated to the event | [optional] |
| **parent_entity_id** | str | The unique identifier for the parent of the entity | [optional] |
| **conversation** | [AddressableEntityRef](AddressableEntityRef) | The link to a conversation | [optional] |
| **date_created** | datetime | The date when the event created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date and time the entity affected by the event was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **entity_modified_by** | str | The unique identifier of the user who last modified the entity affected by the event. | [optional] |
| **entity_version** | str | The version of the entity in the providing service | [optional] |
| **phone_number** | str | The phone number associated with the event | [optional] |
| **external_contact_id** | str | The external contact ID associated with the event | [optional] |



_PureCloudPlatformClientV2 269.0.0_
