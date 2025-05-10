# TimeZoneMappingPreview

## TimeZoneMappingPreview

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **contact_list** | [DomainEntityRef](DomainEntityRef) | The associated ContactList | [optional] |
| **contacts_per_time_zone** | dict(str, int) | The number of contacts per time zone that mapped to only that time zone | [optional] |
| **contacts_mapped_using_zip_code** | dict(str, int) | The number of contacts per time zone that mapped to only that time zone and were mapped using the zip code column | [optional] |
| **contacts_mapped_to_a_single_zone** | int | The total number of contacts that mapped to a single time zone | [optional] |
| **contacts_mapped_to_a_single_zone_using_zip_code** | int | The total number of contacts that mapped to a single time zone and were mapped using the zip code column | [optional] |
| **contacts_mapped_to_multiple_zones** | int | The total number of contacts that mapped to multiple time zones | [optional] |
| **contacts_mapped_to_multiple_zones_using_zip_code** | int | The total number of contacts that mapped to multiple time zones and were mapped using the zip code column | [optional] |
| **contacts_in_default_window** | int | The total number of contacts that will be dialed during the default window | [optional] |
| **contact_list_size** | int | The total number of contacts in the contact list | [optional] |



_PureCloudPlatformClientV2 228.0.0_
