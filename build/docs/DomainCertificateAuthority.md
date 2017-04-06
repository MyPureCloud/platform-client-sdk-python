---
title: DomainCertificateAuthority
---
## DomainCertificateAuthority

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** |  | [optional] |
| **created_by** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **modified_by_app** | **str** |  | [optional] |
| **created_by_app** | **str** |  | [optional] |
| **certificate** | **str** | The authorities signed X509 PEM encoded certificate. | |
| **type** | **str** | The certificate authorities type.  Managed certificate authorities are generated and maintained by Interactive Intelligence.  These are read-only and not modifiable by clients.  Remote authorities are customer managed. | |
| **services** | **list[str]** | The service(s) that the authority can be used to authenticate. | |
| **certificate_details** | [**list[CertificateDetails]**](CertificateDetails.html) | The details of the parsed certificate(s). | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


