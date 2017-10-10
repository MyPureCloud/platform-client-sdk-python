---
title: CreateAsgRequest
---
## CreateAsgRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **asg_owner_email** | **str** | Email address of the individual starting the ASG | |
| **edge_group_id** | **str** | Edge group that the user wants the asg edges to be assigned to. | [optional] |
| **external_trunk_base_id** | **str** | Trunk base that the user wants the asg edges to be assigned to | [optional] |
| **asg_logical_iam_instance_profile** | **str** | Overrides the default logical IAM Instance Profile | [optional] |
| **asg_ami** | **bool** | Overrides the default EDGE AMI used with the ASG | [optional] |
| **asg_type** | **str** | Overrides the type of ASG being created.  By default we always create a &#39;standard&#39; asg. | [optional] |
| **asg_instance_count** | **int** | Overrides the default number of Edge instances to start in the ASG | [optional] |
| **asg_network_space** | **str** | Overrides the network space the ASG will start in.  The default will always be mediaservices | [optional] |
| **asg_chaos_exempt** | **bool** | Optional parameter that exempts this ASG from chaos monkey killing one of its instances. | [optional] |
| **asg_recovery_shutdown_minutes** | **int** | Number of minutes a recovery ASG will stay active before it is torn down | [optional] |
{: class="table table-striped"}


