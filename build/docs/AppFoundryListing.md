---
title: AppFoundryListing
---
## AppFoundryListing

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | [**LocalizedField**](LocalizedField.html) | Localized name | [optional] |
| **registry_info** | [**AppFoundryListingRegistryInfo**](AppFoundryListingRegistryInfo.html) | Provides information about the integration implementation | [optional] |
| **marketing_info** | [**MarketingInfo**](MarketingInfo.html) | Marketing data | [optional] |
| **tagline** | [**LocalizedField**](LocalizedField.html) | Localized tagline | [optional] |
| **brief_description** | [**LocalizedField**](LocalizedField.html) | Localized short description | [optional] |
| **full_description** | [**LocalizedField**](LocalizedField.html) | Localized full description | [optional] |
| **platform** | [**Platform**](Platform.html) | The supported platform | [optional] |
| **company_logo** | **str** | URL to the company logo to be displayed | [optional] |
| **app_logo** | **str** | URL to the app logo to be displayed | [optional] |
| **company_name** | [**LocalizedField**](LocalizedField.html) | Localized company name for the listing publisher | [optional] |
| **website** | [**LocalizedField**](LocalizedField.html) | Localized URL to the website associated with the listing | [optional] |
| **screenshots** | **list[str]** | Screenshot URLS | [optional] |
| **video_links** | **list[str]** | Usage video URLS | [optional] |
| **languages** | **list[str]** | Indicates the languages that the application supports. Supported application languages may differ from the listing localization languages | [optional] |
| **vendor_email** | **str** | Contact email for the listing publisher | [optional] |
| **terms_of_service** | **str** | URL to the terms of service | [optional] |
| **help_documentation_url** | [**LocalizedField**](LocalizedField.html) | URL to help documentation | [optional] |
| **marketing_url** | [**LocalizedField**](LocalizedField.html) | URL to external marketing page | [optional] |
| **industries** | **list[str]** | Industries targeted | [optional] |
| **categories** | **list[str]** | Indicated the categories the listing belongs to | [optional] |
| **smart_cases** | [**list[SmartCase]**](SmartCase.html) | Use cases the listing is meant to address | [optional] |
| **pricing** | [**list[PricingOption]**](PricingOption.html) | Pricing options for the listing | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


