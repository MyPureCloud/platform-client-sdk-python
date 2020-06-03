---
title: Schema
---
## Schema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **title** | **str** | A core type&#39;s title | [optional] |
| **description** | **str** | A core type&#39;s description | [optional] |
| **type** | **list[str]** | An array of fundamental JSON Schema primitive types on which the core type is based | [optional] |
| **items** | [**Items**](Items.html) | Denotes the type and pattern of the items in an enum core type | [optional] |
| **pattern** | **str** | For the \&quot;date\&quot; and \&quot;datetime\&quot; core types, denotes the regex prescribing the allowable date/datetime format | [optional] |
{: class="table table-striped"}


