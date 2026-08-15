# QueryOpportunityEnrollmentsResult

## QueryOpportunityEnrollmentsResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **next_start_date** | datetime | The start date to use for the next query to retrieve additional results in ISO-8601 format. Null if there are no more results | [optional] |
| **enrollments** | [list[QueryOpportunityEnrollmentResult]](QueryOpportunityEnrollmentResult) | The enrollments for the query operation | |
| **opportunities** | [list[QueryEnrollmentOpportunityResult]](QueryEnrollmentOpportunityResult) | The referenced opportunities when expand&#x3D;opportunities is specified | [optional] |



_PureCloudPlatformClientV2 264.0.0_
