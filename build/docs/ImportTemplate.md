# ImportTemplate

## ImportTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the import template. | [optional] |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list_template** | [DomainEntityRef](DomainEntityRef) | ContactListTemplate for this ImportTemplate. | |
| **contact_list_filter** | [DomainEntityRef](DomainEntityRef) | ContactListFilter for this ImportTemplate. | [optional] |
| **use_splitting_criteria** | bool | Whether or not to use splitting criteria. Default is false. | [optional] |
| **splitting_information** | [SplittingInformation](SplittingInformation) | How to split contact records, required if useSplittingCriteria is true. | [optional] |
| **list_name_format** | str | The list name format for target ContactLists. When Custom is provided, customListNameFormatValue is required. | [optional] |
| **custom_list_name_format_value** | str | Custom value for the list name format, at least %N is required. Any character other than the specified tokens will be used as is. Available tokens: %N: ListNamePrefix; %P: Part number; %F: Filter name; %C: Column value; YYYY: year; MM: month; DD: day; hh: hour; mm: minute; ss: second. | [optional] |
| **import_status** | [ImportStatus](ImportStatus) | The status of the import process. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_
