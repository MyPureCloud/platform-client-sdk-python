# DomainCertificateAuthority

## DomainCertificateAuthority

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the entity. | |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **description** | str | The resource&#39;s description. | [optional] |
| **version** | int | The current version of the resource. | [optional] |
| **date_created** | datetime | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | str | The ID of the user that last modified the resource. | [optional] |
| **created_by** | str | The ID of the user that created the resource. | [optional] |
| **state** | str | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | str | The application that last modified the resource. | [optional] |
| **created_by_app** | str | The application that created the resource. | [optional] |
| **certificate** | str | The authorities signed X509 PEM encoded certificate. | |
| **type** | str | The certificate authorities type.  Managed certificate authorities are generated and maintained by Interactive Intelligence.  These are read-only and not modifiable by clients.  Remote authorities are customer managed. | |
| **services** | list[str] | The service(s) that the authority can be used to authenticate. | |
| **certificate_details** | [list[CertificateDetails]](CertificateDetails) | The details of the parsed certificate(s). | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 220.0.0_
