# ExternalOrganizationTrustorLink

## ExternalOrganizationTrustorLink

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **division** | [WritableStarrableDivision](WritableStarrableDivision) | The division to which this entity belongs. | [optional] |
| **external_organization_id** | str | The id of a PureCloud External Organization entity in the External Contacts system that will be used to represent the trustor org | [optional] |
| **trustor_org_id** | str | The id of a PureCloud organization that has granted trust to this PureCloud organization | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **external_organization_uri** | str | The URI for the External Organization that is linked to the trustor org | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
