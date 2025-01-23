# CertificateDetails

## CertificateDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **issuer** | str | Information about the issuer of the certificate.  The value of this property is a comma separated key&#x3D;value format.  Each key is one of the attribute names supported by X.500. | [optional] |
| **subject** | str | Information about the subject of the certificate.  The value of this property is a comma separated key&#x3D;value format.  Each key is one of the attribute names supported by X.500. | [optional] |
| **expiration_date** | datetime | The expiration date of the certificate. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **issue_date** | datetime | The issue date of the certificate. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **expired** | bool | True if the certificate is expired, false otherwise. | [optional] |
| **signature_valid** | bool |  | [optional] |
| **valid** | bool |  | [optional] |



_PureCloudPlatformClientV2 220.0.0_
