# SupportedContent

## SupportedContent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique supported content Id. | |
| **name** | str | The name of the supported content profile | |
| **date_created** | datetime | Date this supported content profile was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this supported content profile was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this supported content profile | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that modified this supported content profile | [optional] |
| **version** | int | Version number | [optional] |
| **media_types** | [MediaTypes](MediaTypes) | Defines the allowable media that may be accepted for an inbound message or to be sent in an outbound message. The following is an example of allowing all inbound media, and for outbound all images and only mpeg video: {   \&quot;mediaTypes\&quot;: {     \&quot;allow\&quot;: {       \&quot;inbound\&quot;: [{\&quot;type\&quot;: \&quot;*/*\&quot;}],       \&quot;outbound\&quot;: [{\&quot;type\&quot;: \&quot;image/*\&quot;}, {\&quot;type\&quot;: \&quot;video/mpeg\&quot;}]     }   } } | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 226.0.0_
