---
title: TwitterIntegration
---
## TwitterIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | A unique Integration Id | |
| **name** | **str** | The name of the Twitter Integration | |
| **access_token_key** | **str** | The Access Token Key from Twitter messenger | |
| **consumer_key** | **str** | The Consumer Key from Twitter messenger | |
| **username** | **str** | The Username from Twitter | [optional] |
| **user_id** | **str** | The UserId from Twitter | [optional] |
| **status** | **str** | The status of the Twitter Integration | [optional] |
| **tier** | **str** | The type of twitter account to be used for the integration | |
| **env_name** | **str** | The Twitter environment name, e.g.: env-beta (required for premium tier) | [optional] |
| **recipient** | [**DomainEntityRef**](DomainEntityRef.html) | The recipient associated to the Twitter Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | **datetime** | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that created this Integration | [optional] |
| **modified_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that last modified this Integration | [optional] |
| **version** | **int** | Version number required for updates. | |
| **create_status** | **str** | Status of asynchronous create operation | [optional] |
| **create_error** | [**ErrorBody**](ErrorBody.html) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


