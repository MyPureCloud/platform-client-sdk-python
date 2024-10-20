# CreateShareRequest

## CreateShareRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **shared_entity_type** | str | The share entity type | |
| **shared_entity** | [SharedEntity](SharedEntity) | The entity that will be shared | |
| **member_type** | str |  | [optional] |
| **member** | [SharedEntity](SharedEntity) | The member that will have access to this share. Only required if a list of members is not provided. | [optional] |
| **members** | [list[CreateShareRequestMember]](CreateShareRequestMember) |  | [optional] |



_PureCloudPlatformClientV2 214.0.0_
