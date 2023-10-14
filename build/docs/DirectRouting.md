---
title: DirectRouting
---
## DirectRouting

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **call_media_settings** | [**DirectRoutingMediaSettings**](DirectRoutingMediaSettings.html) | Direct Routing Settings specific to Call media. | [optional] |
| **email_media_settings** | [**DirectRoutingMediaSettings**](DirectRoutingMediaSettings.html) | Direct Routing Settings specific to Email media. | [optional] |
| **message_media_settings** | [**DirectRoutingMediaSettings**](DirectRoutingMediaSettings.html) | Direct Routing Settings specific to Message media. | [optional] |
| **backup_queue_id** | **str** | ID of queue to be used as the default backup if an agent does not have their Backup Settings configured. | [optional] |
| **wait_for_agent** | **bool** | Flag indicating if Direct Routing interactions should wait for Direct Routing agent or go immediately to selected backup. | [optional] |
| **agent_wait_seconds** | **int** | Time (in seconds) that a Direct Routing interaction will wait for Direct Routing agent before going to selected backup. Valid range [60, 864000]. | [optional] |
{: class="table table-striped"}


