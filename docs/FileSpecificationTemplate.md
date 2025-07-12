# FileSpecificationTemplate

## FileSpecificationTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the File Specification template. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **description** | str | Description of the file specification template | [optional] |
| **format** | str | File format | |
| **number_of_heading_lines_skipped** | int | Number of heading lines to be skipped | [optional] |
| **number_of_trailing_lines_skipped** | int | Number of trailing lines to be skipped | [optional] |
| **header** | bool | If true indicates that delimited file has a header row, which can provide column names | [optional] |
| **delimiter** | str | Kind of delimiter | [optional] |
| **delimiter_value** | str | Delimiter character, used only when delimiter&#x3D;\&quot;Custom\&quot; | [optional] |
| **column_information** | [list[Column]](Column) | Columns specification | [optional] |
| **preprocessing_rules** | [list[PreprocessingRule]](PreprocessingRule) | Preprocessing rules | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 233.0.0_
