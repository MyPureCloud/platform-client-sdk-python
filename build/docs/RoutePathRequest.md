# RoutePathRequest

## RoutePathRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | str | The ID of the queue to associate with the route path | |
| **media_type** | str | The media type of the given queue to associate with the route path | |
| **language_id** | str | The ID of the language to associate with the route path | [optional] |
| **skill_ids** | list[str] | The set of skill IDs to associate with the route path | [optional] |
| **source_planning_group** | [SourcePlanningGroupRequest](SourcePlanningGroupRequest) | The planning group from which to take route paths. This property is only needed if a route path already exists in another planning group.Note that taking a route path from another planning group will modify the other planning group | [optional] |



_PureCloudPlatformClientV2 245.0.0_
