# AuthorizationPolicy

## AuthorizationPolicy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **target_resource** | str | The targeted resource to which the policy should apply, in the form of domain:entity:action | [optional] |
| **subject** | [Subject](Subject) | The subject to whom the policy will apply, including type and id | |
| **effect** | str | The effect this policy should have when its conditions are met | |
| **condition** | object | The condition tree the policy will evaluate | [optional] |
| **description** | str |  | [optional] |
| **date_modified** | datetime | Date this policy was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **preset_attributes** | [dict(str, TypedAttribute)](TypedAttribute) | Map of names and values of preset attributes to use in policy evaluation | [optional] |
| **active** | bool | Flag for active enforcement. If this value is false or null, the policy will be saved but will not be checked or enforced on users. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 231.0.0_
