# WorktypeQueryRequest

## WorktypeQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] |
| **select** | str | Specify the value &#39;Count&#39; for this parameter in order to return only the record count. | [optional] |
| **filters** | [list[WorkitemFilter]](WorkitemFilter) | List of filter objects to be used in the search. Valid filter names are: &#39;divisionId&#39;, &#39;id&#39;, &#39;name&#39;, &#39;description&#39;, &#39;defaultWorkbinId&#39;, &#39;defaultDurationSeconds&#39;, &#39;defaultExpirationSeconds&#39;, &#39;defaultDueDurationSeconds&#39;, &#39;defaultPriority&#39;, &#39;defaultLanguageId&#39;, &#39;defaultTtlSeconds&#39;, &#39;assignmentEnabled&#39;, &#39;defaultQueueId&#39;, &#39;schemaId&#39;, &#39;schemaVersion&#39;, &#39;dateCreated&#39;, &#39;dateModified&#39;, &#39;modifiedBy&#39; | |
| **attributes** | list[str] | List of entity attributes to be retrieved in the result. | [optional] |
| **after** | str | The cursor that points to the end of the set of entities that has been returned. | [optional] |
| **sort** | [WorktypeQuerySort](WorktypeQuerySort) | Sort | [optional] |



_PureCloudPlatformClientV2 246.1.0_
