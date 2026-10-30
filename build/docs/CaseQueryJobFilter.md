# CaseQueryJobFilter

## CaseQueryJobFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Attribute name. Valid filter names are: &#39;caseplanId&#39;, &#39;ownerId&#39;, &#39;status&#39;, &#39;priority&#39;, &#39;dateDue&#39;, &#39;externalContactId&#39;, &#39;customerIntentId&#39;, &#39;dateCreated&#39;, &#39;divisionId&#39;, &#39;reference&#39;, &#39;externalId&#39;. | |
| **operator** | str | Filter operator. | |
| **values** | list[str] | List of values to be used in the filter. | |
| **case_sensitive** | bool | Whether the filter matches letter case exactly. Only valid for &#39;reference&#39; and &#39;externalId&#39; filters. Defaults to true. | [optional] |



_PureCloudPlatformClientV2 270.0.0_
