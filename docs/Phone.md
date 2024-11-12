# Phone

## Phone

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the entity. | |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **description** | str | The resource&#39;s description. | [optional] |
| **version** | int | The current version of the resource. | [optional] |
| **date_created** | datetime | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | str | The ID of the user that last modified the resource. | [optional] |
| **created_by** | str | The ID of the user that created the resource. | [optional] |
| **state** | str | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | str | The application that last modified the resource. | [optional] |
| **created_by_app** | str | The application that created the resource. | [optional] |
| **site** | [DomainEntityRef](DomainEntityRef) | The site associated to the phone. | |
| **phone_base_settings** | [PhoneBaseSettings](PhoneBaseSettings) | Phone Base Settings | |
| **line_base_settings** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **phone_meta_base** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **lines** | [list[Line]](Line) | Lines | |
| **status** | [PhoneStatus](PhoneStatus) | The status of the phone and lines from the primary Edge. | [optional] |
| **secondary_status** | [PhoneStatus](PhoneStatus) | The status of the phone and lines from the secondary Edge. | [optional] |
| **user_agent_info** | [UserAgentInfo](UserAgentInfo) | User Agent Information for this phone. This includes model, firmware version, and manufacturer. | [optional] |
| **properties** | dict(str, object) |  | [optional] |
| **capabilities** | [PhoneCapabilities](PhoneCapabilities) |  | [optional] |
| **web_rtc_user** | [DomainEntityRef](DomainEntityRef) | This is the user associated with a WebRTC type phone.  It is required for all WebRTC phones. | [optional] |
| **primary_edge** | [Edge](Edge) |  | [optional] |
| **secondary_edge** | [Edge](Edge) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 216.0.0_
