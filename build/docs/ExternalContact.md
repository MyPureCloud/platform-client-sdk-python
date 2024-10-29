# ExternalContact

## ExternalContact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **first_name** | str | The first name of the contact. | [optional] |
| **middle_name** | str |  | [optional] |
| **last_name** | str | The last name of the contact. | [optional] |
| **salutation** | str |  | [optional] |
| **title** | str |  | [optional] |
| **work_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **cell_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **home_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **other_phone** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **work_email** | str |  | [optional] |
| **personal_email** | str |  | [optional] |
| **other_email** | str |  | [optional] |
| **address** | [ContactAddress](ContactAddress) |  | [optional] |
| **twitter_id** | [TwitterId](TwitterId) |  | [optional] |
| **line_id** | [LineId](LineId) |  | [optional] |
| **whats_app_id** | [WhatsAppId](WhatsAppId) |  | [optional] |
| **facebook_id** | [FacebookId](FacebookId) |  | [optional] |
| **modify_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **create_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_organization** | [ExternalOrganization](ExternalOrganization) |  | [optional] |
| **survey_opt_out** | bool |  | [optional] |
| **external_system_url** | str | A string that identifies an external system-of-record resource that may have more detailed information on the contact. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace. | [optional] |
| **schema** | [DataSchema](DataSchema) | The schema defining custom fields for this contact | [optional] |
| **custom_fields** | dict(str, object) | Custom fields defined in the schema referenced by schemaId and schemaVersion. | [optional] |
| **external_data_sources** | [list[ExternalDataSource]](ExternalDataSource) | Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param. | [optional] |
| **type** | str | The type of contact | [optional] |
| **canonical_contact** | [ContactAddressableEntityRef](ContactAddressableEntityRef) | The contact at the head of the merge tree. If null, this contact is not a part of any merge. | [optional] |
| **merge_set** | [list[ContactAddressableEntityRef]](ContactAddressableEntityRef) | The set of all contacts that are a part of the merge tree. If null, this contact is not a part of any merge. | [optional] |
| **merge_operation** | [MergeOperation](MergeOperation) | Information about the merge history of this contact. If null, this contact is not a part of any merge. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 215.0.0_
