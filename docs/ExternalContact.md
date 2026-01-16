# ExternalContact

## ExternalContact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division** | [WritableStarrableDivision](WritableStarrableDivision) | The division to which this entity belongs. | [optional] |
| **first_name** | str | The first name of the contact. Max: 1000 characters. Leading and trailing whitespace stripped. | [optional] |
| **middle_name** | str | The middle name of the contact. Max: 1000 characters. Leading and trailing whitespace stripped. | [optional] |
| **last_name** | str | The last name of the contact. Max: 1000 characters. Leading and trailing whitespace stripped. | [optional] |
| **salutation** | str | The salutation of the contact. Max: 1000 characters. Leading and trailing whitespace stripped. | [optional] |
| **title** | str | The title of the contact. Max: 1000 characters. Leading and trailing whitespace stripped. | [optional] |
| **work_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **cell_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **home_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **other_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **work_email** | str | The work email of the contact. Max: 256 characters. Leading and trailing whitespace stripped. Valid email format | [optional] |
| **personal_email** | str | The personal email of the contact. Max: 256 characters. Leading and trailing whitespace stripped. Valid email format | [optional] |
| **other_email** | str | The other email of the contact. Max: 256 characters. Leading and trailing whitespace stripped. Valid email format | [optional] |
| **address** | [ContactAddress](ContactAddress) |  | [optional] |
| **twitter_id** | [TwitterId](TwitterId) | User information for a Twitter account | [optional] |
| **line_id** | [LineId](LineId) |  | [optional] |
| **whats_app_id** | [WhatsAppId](WhatsAppId) | User information for a WhatsApp account | [optional] |
| **facebook_id** | [FacebookId](FacebookId) | User information for a Facebook account | [optional] |
| **instagram_id** | [InstagramId](InstagramId) | User information for an Instagram account | [optional] |
| **apple_opaque_ids** | [list[AppleOpaqueId]](AppleOpaqueId) | User information for an Apple account. Max: 10 ids | [optional] |
| **external_ids** | [list[ExternalId]](ExternalId) | A list of external identifiers that identify this contact in an external system. Max: 10 ids | [optional] |
| **identifiers** | [list[ContactIdentifier]](ContactIdentifier) | Identifiers claimed by this contact | [optional] |
| **modify_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **create_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_organization** | [ExternalOrganization](ExternalOrganization) |  | [optional] |
| **survey_opt_out** | bool |  | [optional] |
| **external_system_url** | str | A string that identifies an external system-of-record resource that may have more detailed information on the contact. Should be a valid URL (including the http/https protocol, port, and path [if any]). Leading and trailing whitespace stripped. Max 1000 characters. | [optional] |
| **schema** | [DataSchema](DataSchema) | The schema defining custom fields for this contact | [optional] |
| **custom_fields** | dict(str, object) | Custom fields defined in the schema referenced by schemaId and schemaVersion. | [optional] |
| **external_data_sources** | [list[ExternalDataSource]](ExternalDataSource) | Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param. | [optional] |
| **type** | str | The type of contact | [optional] |
| **canonical_contact** | [ContactAddressableEntityRef](ContactAddressableEntityRef) | The contact at the head of the merge tree. If null, this contact is not a part of any merge. | [optional] |
| **merge_set** | [list[ContactAddressableEntityRef]](ContactAddressableEntityRef) | The set of all contacts that are a part of the merge tree. If null, this contact is not a part of any merge. | [optional] |
| **merged_from** | [list[ContactAddressableEntityRef]](ContactAddressableEntityRef) | The input contacts from the merge operation. | [optional] |
| **merged_to** | [ContactAddressableEntityRef](ContactAddressableEntityRef) | The output contact from the merge operation. | [optional] |
| **merge_operation** | [MergeOperation](MergeOperation) | (Deprecated: use mergedTo and mergedFrom instead) Information about the merge history of this contact. If null, this contact is not a part of any merge. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_
