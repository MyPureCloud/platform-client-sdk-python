# ActionEventRequest

## ActionEventRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **session_id** | str | UUID of the customer session for this action. | |
| **action_id** | str | UUID for the action, as returned by the Ping endpoint when the action was qualified. | |
| **action_state** | str | State the action is transitioning to. | |
| **error_code** | str | Client defined error code (when state transitions to errored) | [optional] |
| **error_message** | str | Message of the error returned when the action fails (when state transitions to errored) | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
