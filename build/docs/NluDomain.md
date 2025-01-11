# NluDomain

## NluDomain

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the NLU domain. | |
| **language** | str | The language culture of the NLU domain, e.g. &#x60;en-us&#x60;, &#x60;de-de&#x60;. | [optional] |
| **draft_version** | [NluDomainVersion](NluDomainVersion) | The draft version of that NLU domain. | [optional] |
| **last_published_version** | [NluDomainVersion](NluDomainVersion) | The last published version of that NLU domain. | [optional] |
| **date_created** | datetime | The date when the NLU domain was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date when the NLU domain was updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **engine_version** | str | The version of the NLU engine to use. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 219.1.0_
