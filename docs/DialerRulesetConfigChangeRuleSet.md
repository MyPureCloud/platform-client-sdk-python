# DialerRulesetConfigChangeRuleSet

## DialerRulesetConfigChangeRuleSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **contact_list** | [DialerRulesetConfigChangeUriReference](DialerRulesetConfigChangeUriReference) |  | [optional] |
| **queue** | [DialerRulesetConfigChangeUriReference](DialerRulesetConfigChangeUriReference) | A UriReference for a resource | [optional] |
| **rules** | [list[DialerRulesetConfigChangeRule]](DialerRulesetConfigChangeRule) |  | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **get_additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 244.0.0_
