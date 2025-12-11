# WorkitemQueryPostRequest

## WorkitemQueryPostRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] |
| **select** | str | Specify the value &#39;Count&#39; for this parameter in order to return only the record count. | [optional] |
| **filters** | [list[WorkitemFilter]](WorkitemFilter) | List of filter objects to be used in the search. Valid filter names are: &#39;id&#39;, &#39;name&#39;, &#39;description&#39;, &#39;languageId&#39;, &#39;priority&#39;, &#39;dateCreated&#39;, &#39;dateModified&#39;, &#39;dateDue&#39;, &#39;dateExpires&#39;, &#39;durationInSeconds&#39;, &#39;ttl&#39;, &#39;statusId&#39;, &#39;statusCategory&#39;, &#39;dateClosed&#39;, &#39;externalContactId&#39;, &#39;reporterId&#39;, &#39;queueId&#39;, &#39;externalTag&#39;, &#39;modifiedBy&#39;, &#39;assignmentState&#39;, &#39;divisionId&#39;, &#39;customFields.&lt;custom field name&gt;&#39; | |
| **attributes** | list[str] | List of entity attributes to be retrieved in the result. | [optional] |
| **after** | str | The cursor that points to the end of the set of entities that has been returned. | [optional] |
| **sort** | [WorkitemQuerySort](WorkitemQuerySort) | Sort | [optional] |
| **expands** | list[str] | List of entity attributes to be expanded in the result. | [optional] |



_PureCloudPlatformClientV2 246.0.0_
