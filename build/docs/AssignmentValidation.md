---
title: AssignmentValidation
---
## AssignmentValidation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **members_not_assigned** | [**list[UserReference]**](UserReference.html) | The list of users that are not assigned to any custom performance profile | [optional] |
| **members_already_assigned** | [**list[UserReference]**](UserReference.html) | The list of users that are already assigned to the requesting custom performance profile | [optional] |
| **members_already_assigned_to_other** | [**list[OtherProfileAssignment]**](OtherProfileAssignment.html) | The list of users that are already assigned to other custom performance profiles | [optional] |
| **invalid_member_assignments** | [**list[InvalidAssignment]**](InvalidAssignment.html) | The list of user id that are invalid for the gamfication service to handle | [optional] |
{: class="table table-striped"}


