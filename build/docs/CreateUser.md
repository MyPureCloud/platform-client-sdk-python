# CreateUser

## CreateUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | User&#39;s full name | |
| **department** | str |  | [optional] |
| **email** | str | User&#39;s email and username | |
| **addresses** | [list[Contact]](Contact) | Email addresses and phone numbers for this user | [optional] |
| **title** | str |  | [optional] |
| **password** | str | User&#39;s password | [optional] |
| **division_id** | str | The division to which this user will belong | |
| **state** | str | Optional initialized state of the user. If not specified, state will be Active if invites are sent, otherwise Inactive. | [optional] |



_PureCloudPlatformClientV2 213.0.0_
