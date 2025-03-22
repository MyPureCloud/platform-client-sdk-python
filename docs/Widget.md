# Widget

## Widget

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **row** | int | The row number for the specific dashboard widget configuration. | [optional] |
| **column** | int | The column number for the specific dashboard widget configuration. | [optional] |
| **title** | str | The title for the dashboard widget configuration. | [optional] |
| **type** | str | The type of dashboard widget configuration. | |
| **metrics** | list[str] | The list of metrics for the dashboard widget configuration. | [optional] |
| **display_text** | str | The display text for the dashboard widget configuration. | [optional] |
| **display_text_color** | str | The color of the display text for the dashboard widget configuration in RGB hexadecimal format (for example \&quot;#FF0000\&quot; represents red). | [optional] |
| **web_content_url** | str | The external web URL for the dashboard widget configuration. | [optional] |
| **split_filters** | bool | Indicates each filter to be displayed individually. | [optional] |
| **split_by_media_type** | bool | Indicates that data for each media type should be shown individually. | [optional] |
| **show_longest** | bool | Indicates the display be the longest time. | [optional] |
| **display_as_table** | bool | Indicates the widget to be displayed as table. | [optional] |
| **show_duration** | bool | Indicates the display to include duration. | [optional] |
| **sort_order** | str | The sort order of the table. | [optional] |
| **sort_key** | str | The sort key of the table. | [optional] |
| **entity_limit** | int | Indicates the limit of displayed entities. | [optional] |
| **display_aggregates** | bool | Indicates whether to display aggregate across all entity and media type combination. | [optional] |
| **is_full_width** | bool | Indicates whether a widget should take the full width of a dashboard or be shown only in a single slot. | [optional] |
| **show_percentage_change** | bool | Indicates whether a widget should show the percentage diff between two values. | [optional] |
| **show_profile_picture** | bool | Indicates whether a widget should show the profile picture of an agent. | [optional] |
| **filter** | [ViewFilter](ViewFilter) | The filters to be applied for dashboard widget configuration | [optional] |
| **periods** | list[str] | The list of periods for the dashboard widget configuration | [optional] |
| **media_types** | list[str] | The list of media types for the dashboard widget configuration | [optional] |
| **warnings** | [list[Warning]](Warning) | List of warnings for dashboard widget configuration | [optional] |
| **show_time_in_status** | bool | Indicates the show time in status of a widget configuration. | [optional] |
| **show_offline_agents** | bool | Indicates to show offline agent widget. | [optional] |
| **selected_statuses** | list[str] | Indicates the selected statuses used to filter the agent widget in the dashboard. | [optional] |
| **selected_segment_types** | list[str] | Indicates the selected segment types used to filter the agent activity in the dashboard. | [optional] |
| **agent_interaction_sort_order** | str | The sort order of the interactions in the agent status widget. | [optional] |



_PureCloudPlatformClientV2 224.0.0_
