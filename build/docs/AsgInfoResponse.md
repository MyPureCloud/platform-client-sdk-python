---
title: AsgInfoResponse
---
## AsgInfoResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The full id of the asg &lt;orgId&gt;-&lt;siteId&gt;-ASG-&lt;asgVersion&gt; | [optional] |
| **site** | [**Site**](Site.html) | The site that the asg belongs to. | [optional] |
| **ami** | **str** | The version of the asg, ex &#39;003&#39; | [optional] |
| **edge_version** | **str** | The software ami of the edges in the asg. | [optional] |
| **instance_info** | [**list[InstanceInfo]**](InstanceInfo.html) | List of instances and their information that live in the ASG. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


