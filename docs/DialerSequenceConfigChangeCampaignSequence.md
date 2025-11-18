# DialerSequenceConfigChangeCampaignSequence

## DialerSequenceConfigChangeCampaignSequence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaigns** | [list[DialerSequenceConfigChangeUriReference]](DialerSequenceConfigChangeUriReference) | the ordered list of campaign identifiers | [optional] |
| **current_campaign** | int | the zero-based index of the current campaign in the campaigns list | [optional] |
| **status** | str |  | [optional] |
| **stop_message** | str | if a sequence has unexpectedly stopped, this message provides the reason | [optional] |
| **repeat** | bool | indicates if a sequence is to repeat from the beginning after the last campaign completes; default is false | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **get_additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 243.0.0_
