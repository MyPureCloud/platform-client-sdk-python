---
title: OutboundDomain
---
## OutboundDomain

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique Id of the domain such as: example.com | |
| **name** | **str** |  | [optional] |
| **cname_verification_result** | [**VerificationResult**](VerificationResult.html) | CNAME registration Status | [optional] |
| **dkim_verification_result** | [**VerificationResult**](VerificationResult.html) | DKIM registration Status | [optional] |
| **from_email** | [**EmailAddress**](EmailAddress.html) | The email that is used to display sender informations | [optional] |
| **reply_to_email** | [**EmailAddress**](EmailAddress.html) | The email that is used if replies are expected | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


