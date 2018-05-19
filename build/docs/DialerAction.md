---
title: DialerAction
---
## DialerAction

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | The type of this DialerAction. | |
| **action_type_name** | **str** | Additional type specification for this DialerAction. | |
| **update_option** | **str** | Specifies how a contact attribute should be updated. Required for MODIFY_CONTACT_ATTRIBUTE. | [optional] |
| **properties** | **dict(str, str)** | A map of key-value pairs pertinent to the DialerAction. Different types of DialerActions require different properties. MODIFY_CONTACT_ATTRIBUTE with an updateOption of SET takes a contact column as the key and accepts any value. SCHEDULE_CALLBACK takes a key &#39;callbackOffset&#39; that specifies how far in the future the callback should be scheduled, in minutes. SET_CALLER_ID takes two keys: &#39;callerAddress&#39;, which should be the caller id phone number, and &#39;callerName&#39;. For either key, you can also specify a column on the contact to get the value from. To do this, specify &#39;contact.Column&#39;, where &#39;Column&#39; is the name of the contact column from which to get the value. SET_SKILLS takes a key &#39;skills&#39; with an array of skill ids wrapped into a string (Example: {&#39;skills&#39;: &#39;[&#39;skillIdHere&#39;]&#39;} ). | [optional] |
{: class="table table-striped"}


