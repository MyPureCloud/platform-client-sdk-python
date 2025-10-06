# GuideVersion

## GuideVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **self_uri** | str |  | [optional] |
| **guide** | [AddressableEntityRef](AddressableEntityRef) | The guide this version belongs to. | [optional] |
| **version** | str | Guide version. | [optional] |
| **instruction** | str | The instruction given to this version of the guide, for how it should behave when interacting with a User. | [optional] |
| **state** | str | The current state of the guide version. | [optional] |
| **date_created** | datetime | The date and time the guide version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date and time the guide version was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **variables** | [list[Variable]](Variable) | The variables associated with this version of the guide. Includes input variables (provided) and output variables (captured during execution). | [optional] |
| **resources** | [GuideVersionResources](GuideVersionResources) | The resources associated with this version of the guide. | [optional] |



_PureCloudPlatformClientV2 240.0.0_
