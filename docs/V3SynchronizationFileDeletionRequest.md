# V3SynchronizationFileDeletionRequest

## V3SynchronizationFileDeletionRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **file_id** | str | The identifier of the file to mark for deletion. Mutually exclusive with fileName. | [optional] |
| **file_name** | str | Name of the file to mark for deletion. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%&#x60;]\&quot;&gt;[~&lt;#|. Mutually exclusive with fileId. | [optional] |



_PureCloudPlatformClientV2 265.0.0_
