# RuleSet

## RuleSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the RuleSet. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **contact_list** | [DomainEntityRef](DomainEntityRef) | A ContactList to provide user-interface suggestions for contact columns on relevant conditions and actions. | [optional] |
| **queue** | [DomainEntityRef](DomainEntityRef) | A Queue to provide user-interface suggestions for wrap-up codes on relevant conditions and actions. | [optional] |
| **rules** | [list[DialerRule]](DialerRule) | The list of rules. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_
