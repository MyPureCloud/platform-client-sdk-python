# Case

## Case

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Case. | [optional] |
| **division** | [StarrableDivision](StarrableDivision) | The division to which this entity belongs. | [optional] |
| **version** | int | The version of the Case. | [optional] |
| **reference** | str | The reference identifier of the Case. | [optional] |
| **caseplan** | [CaseplanReference](CaseplanReference) | The Caseplan the case was created from. | [optional] |
| **summary** | str | Overview information for the Case. | [optional] |
| **owner** | [UserReference](UserReference) | The owner of the Case. | [optional] |
| **status** | str | The status of the Case. | [optional] |
| **priority** | str | The priority of the Case. | [optional] |
| **date_due** | datetime | The due date of the Case. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_started** | datetime | The start time of the Case. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_closed** | datetime | The completion time of the Case. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_created** | datetime | The date the Case was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date the Case was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The id of the User who modified the Case. | [optional] |
| **external_contact** | [CaseExternalContactReference](CaseExternalContactReference) | The External Contact associated with the Case. | [optional] |
| **customer_intent** | [CustomerIntentReference](CustomerIntentReference) | The customer intent for the Case. | [optional] |
| **creation_status** | str | The creation status of the Case | [optional] |
| **ttl_seconds** | int | The time-to-live in seconds for the lifetime of the Case. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.0.0_
