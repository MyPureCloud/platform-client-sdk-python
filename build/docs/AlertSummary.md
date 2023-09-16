---
title: AlertSummary
---
## AlertSummary

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **entities** | [**list[AlertSummaryEntity]**](AlertSummaryEntity.html) | The entities who violated the rule condition over the duration of the alert. | |
| **conversation** | [**AddressableEntityRef**](AddressableEntityRef.html) | The id of the conversation that triggered the alert.  Only used for alerts based on instance-based conversation metrics. | [optional] |
| **metric_type** | **str** | The metric type that is monitored. | |
| **entities_are_team_members** | **bool** | Flag that indicated whether or not the alert is for a rule with a condition for all members of a team. | |
{: class="table table-striped"}


