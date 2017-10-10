---
title: AsgInfoResponse
---
## AsgInfoResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **site** | [**Site**](Site.html) | The site that the asg belongs to. | [optional] |
| **ami** | **str** | The ami ami of the asg. | [optional] |
| **edge_version** | **str** | The software ami of the edges in the asg. | [optional] |
| **instance_info** | [**list[InstanceInfo]**](InstanceInfo.html) | List of instances and their information that live in the ASG. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


