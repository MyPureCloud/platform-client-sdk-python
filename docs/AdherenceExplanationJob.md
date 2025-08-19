# AdherenceExplanationJob

## AdherenceExplanationJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **type** | str | The type of the adherence explanation job | [optional] |
| **status** | str | The status of the adherence explanation job | [optional] |
| **adherence_explanation** | [AdherenceExplanationResponse](AdherenceExplanationResponse) | The adherence explanation added or modified by the job once complete; may be null if status &#x3D;&#x3D; &#39;Error&#39;. Used if type is in [ &#39;AddExplanation&#39;, &#39;UpdateExplanation&#39; ] | [optional] |
| **download_url** | str | A URL to fetch results of the job. Only set if status &#x3D;&#x3D; &#39;Complete&#39; and type is in [ &#39;QueryAgentExplanations&#39;, &#39;QueryBuExplanations&#39; ] | [optional] |
| **error** | [ErrorBody](ErrorBody) | Error details if status &#x3D;&#x3D; &#39;Error&#39; | [optional] |
| **agent_query_response_template** | [AdherenceExplanationListingAgentQueryResponse](AdherenceExplanationListingAgentQueryResponse) | Schema template for deserializing data returned from the downloadUrl. Use if type &#x3D;&#x3D; &#39;QueryAgentExplanations&#39; | [optional] |
| **bu_query_response_template** | [AdherenceExplanationListingBuQueryResponse](AdherenceExplanationListingBuQueryResponse) | Schema template for deserializing data returned from the downloadUrl. Use if type &#x3D;&#x3D; &#39;QueryBuExplanations&#39; | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
