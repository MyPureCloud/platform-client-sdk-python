# AcceleratorSpecification

## AcceleratorSpecification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | name of this accelerator | [optional] |
| **description** | str | a description of the general purpose of this accelerator | [optional] |
| **origin** | str | where the accelerator originated | [optional] |
| **type** | str | type of the artifact | [optional] |
| **classification** | str | architectural classification into which the accelerator belongs | [optional] |
| **tags** | list[str] | tags | [optional] |
| **permissions** | list[str] | Genesys Cloud permissions required to install the accelerator | [optional] |
| **products** | list[str] | Genesys Cloud products required to install the accelerator | [optional] |
| **documentation** | [list[MetadataDocumentation]](MetadataDocumentation) | additional documentation about the artifact | [optional] |
| **presentation** | [list[MetadataPresentation]](MetadataPresentation) | presentation of data fields to be gathered for the accelerator | [optional] |
| **results** | [MetadataResults](MetadataResults) | resources created or modified as a result of running the accelerator | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 249.0.0_
