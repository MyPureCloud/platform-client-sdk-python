---
title: LineIntegrationRequest
---
## LineIntegrationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the LINE Integration | |
| **channel_id** | **str** | The Channel Id from LINE messenger. New Official LINE account: To create a new official account, LINE requires a Webhook URL. It can be created without specifying Channel Id &amp; Channel Secret. Once the Official account is created by LINE, use the update LINE Integration API to update Channel Id and Channel Secret.  All other accounts: Channel Id is mandatory | [optional] |
| **channel_secret** | **str** | The Channel Secret from LINE messenger. New Official LINE account: To create a new official account, LINE requires a Webhook URL. It can be created without specifying Channel Id &amp; Channel Secret. Once the Official account is created by LINE, use the update LINE Integration API to update Channel Id and Channel Secret.  All other accounts: Channel Secret is mandatory | [optional] |
| **switcher_secret** | **str** | The Switcher Secret from LINE messenger. Some line official accounts are switcher functionality enabled. If the LINE account used for this integration is switcher enabled, then switcher secret is a required field. This secret can be found in your create documentation provided by LINE | [optional] |
| **channel_access_token** | **str** | The Channel Access Token from LINE messenger | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


