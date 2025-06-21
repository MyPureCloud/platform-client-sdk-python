# InboundMessageRequest

## InboundMessageRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | str | The ID of the queue to use for routing the email conversation. This field is mutually exclusive with flowId | [optional] |
| **flow_id** | str | The ID of the flow to use for routing email conversation. This field is mutually exclusive with queueId | [optional] |
| **provider** | str | The name of the provider that is sourcing the email such as Oracle, Salesforce, etc. | |
| **skill_ids** | list[str] | The list of skill ID&#39;s to use for routing. | [optional] |
| **language_id** | str | The ID of the language to use for routing. | [optional] |
| **priority** | int | The priority to assign to the conversation for routing. | [optional] |
| **attributes** | dict(str, str) | The list of attributes to associate with the customer participant. | [optional] |
| **to_address** | str | The email address of the recipient of the email. | [optional] |
| **to_name** | str | The name of the recipient of the email. | [optional] |
| **from_address** | str | The email address of the sender of the email. | [optional] |
| **from_name** | str | The name of the sender of the email. | [optional] |
| **subject** | str | The subject of the email | [optional] |



_PureCloudPlatformClientV2 231.0.0_
