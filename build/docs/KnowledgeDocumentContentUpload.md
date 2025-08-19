# KnowledgeDocumentContentUpload

## KnowledgeDocumentContentUpload

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **content_type** | str | Type of Article Content. | |
| **file_name** | str | Name of the file to upload. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%&#x60;]\&quot;&gt;[~&lt;#| | |
| **status** | str | Status of the upload operation | [optional] |
| **upload_key** | str | Key that identifies the file in the storage including the file name | [optional] |
| **url** | str | Presigned URL to PUT the file to | [optional] |
| **headers** | dict(str, str) | Required headers when uploading a file through PUT request to the URL | [optional] |
| **document** | [AddressableEntityRef](AddressableEntityRef) | ID of the document for which article content is to be uploaded | [optional] |
| **error_message** | str | Error message when upload fails | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
