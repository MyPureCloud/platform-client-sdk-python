---
title: MediaEndpointStatistics
---
## MediaEndpointStatistics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **trunk** | [**NamedEntity**](NamedEntity.html) | Trunk information utilized when creating the media endpoint | [optional] |
| **station** | [**NamedEntity**](NamedEntity.html) | Station information associated with media endpoint | [optional] |
| **user** | [**NamedEntity**](NamedEntity.html) | User information associated media endpoint | [optional] |
| **ice** | [**MediaIceStatistics**](MediaIceStatistics.html) | The ICE protocol statistics and details. Reference: https://www.rfc-editor.org/rfc/rfc5245 | [optional] |
| **rtp** | [**MediaRtpStatistics**](MediaRtpStatistics.html) | Statistics of sent and received RTP. Reference: https://www.rfc-editor.org/rfc/rfc3550 | [optional] |
{: class="table table-striped"}


