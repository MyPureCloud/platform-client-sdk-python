# ExternalOrganization

## ExternalOrganization

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the company. | |
| **company_type** | str |  | [optional] |
| **industry** | str |  | [optional] |
| **primary_contact_id** | str |  | [optional] |
| **address** | [ContactAddress](ContactAddress) |  | [optional] |
| **phone_number** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **fax_number** | [PhoneNumber](PhoneNumber) |  | [optional] |
| **employee_count** | int |  | [optional] |
| **revenue** | int |  | [optional] |
| **tags** | list[str] |  | [optional] |
| **websites** | list[str] |  | [optional] |
| **tickers** | [list[Ticker]](Ticker) |  | [optional] |
| **twitter_id** | [TwitterId](TwitterId) |  | [optional] |
| **external_system_url** | str | A string that identifies an external system-of-record resource that may have more detailed information on the organization. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace. | [optional] |
| **modify_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **create_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **trustor** | [Trustor](Trustor) |  | [optional] |
| **schema** | [DataSchema](DataSchema) | The schema defining custom fields for this contact | [optional] |
| **custom_fields** | dict(str, object) | Custom fields defined in the schema referenced by schemaId and schemaVersion. | [optional] |
| **external_data_sources** | [list[ExternalDataSource]](ExternalDataSource) | Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 216.0.0_
