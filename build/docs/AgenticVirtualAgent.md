# AgenticVirtualAgent

## AgenticVirtualAgent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **date_created** | datetime | The date and time the virtual agent was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date and time the virtual agent was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str | The status of the virtual agent. | [optional] |
| **latest_saved_version** | [AgenticVersionAddressableEntity](AgenticVersionAddressableEntity) | The latest saved version of the virtual agent. | [optional] |
| **latest_production_ready_version** | [AgenticVersionAddressableEntity](AgenticVersionAddressableEntity) | The latest production ready version of the virtual agent. | [optional] |
| **image_uri** | str | The URI of the image for the virtual agent. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 264.0.0_
