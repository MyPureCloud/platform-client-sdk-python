---
title: ScimV2SchemaAttribute
---
## ScimV2SchemaAttribute

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The attribute&#39;s name | [optional] |
| **type** | **str** | The data type of the attribute. | [optional] |
| **sub_attributes** | [**list[ScimV2SchemaAttribute]**](ScimV2SchemaAttribute.html) | The list of subattributes for an attribute of the type \&quot;complex\&quot;. Uses the same schema as \&quot;attributes\&quot;. | [optional] |
| **multi_valued** | **bool** | Indicates whether an attribute contains multiple values. | [optional] |
| **description** | **str** | The description of the attribute. | [optional] |
| **required** | **bool** | Indicates whether an attribute is required. | [optional] |
| **canonical_values** | **list[str]** | The list of standard values that service providers may use. Service providers may ignore unsupported values. | [optional] |
| **case_exact** | **bool** | Indicates whether a string attribute is case-sensitive. If set to \&quot;true\&quot;, the server preserves case sensitivity. If set to \&quot;false\&quot;, the server may change the case. The server also uses case sensitivity when evaluating filters. See section 3.4.2.2 \&quot;Filtering\&quot; in RFC 7644 for details. | [optional] |
| **mutability** | **str** | The circumstances under which an attribute can be defined or redefined. The default is \&quot;readWrite\&quot;. | [optional] |
| **returned** | **str** | The circumstances under which an attribute and its values are returned in response to a GET, PUT, POST, or PATCH request. | [optional] |
| **uniqueness** | **str** | The method by which the service provider enforces the uniqueness of an attribute value. A server can reject a value by returning the HTTP response code 400 (Bad Request). A client can enforce uniqueness to a greater degree than the server provider enforces. For example, a client could make a value unique even though the server has \&quot;uniqueness\&quot; set to \&quot;none\&quot;. | [optional] |
| **reference_types** | **list[str]** | The list of SCIM resource types that may be referenced. Only applies when \&quot;type\&quot; is set to \&quot;reference\&quot;. | [optional] |
{: class="table table-striped"}


