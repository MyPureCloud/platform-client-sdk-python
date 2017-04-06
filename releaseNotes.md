
# Major Changes (4 changes)

**GET /api/v2/responsemanagement/responses/{responseId}** (1 change)

* Parameter expand was added

**PUT /api/v2/responsemanagement/responses/{responseId}** (1 change)

* Parameter expand was added

**GET /api/v2/responsemanagement/responses** (1 change)

* Parameter expand was added

**POST /api/v2/responsemanagement/responses** (1 change)

* Parameter expand was added


# Minor Changes (86 changes)

**/api/v2/architect/dependencytracking/consumedresources** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/dependencytracking/build** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/architect/dependencytracking/types** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/license/definitions/{licenseId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/dependencytracking/updatedresourceconsumers** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/flows/actions/unlock** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/flows/actions/publish** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/flows/actions/checkin** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/flows/actions/checkout** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/flows/actions/deactivate** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/flows/actions/revert** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/architect/dependencytracking/consumingresources** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/license/organization** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/license/definitions** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/dependencytracking/types/{typeId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/dependencytracking/deletedresourceconsumers** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/flows/{flowId}/versions/{versionId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/flows/{flowId}/versions/{versionId}/configuration** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/dependencytracking** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/license/users/{userId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/flows/{flowId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/flows/{flowId}/latestconfiguration** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/flows** (2 changes)

* Operation post was added. Summary: Create flow
* Operation delete was added. Summary: Batch-delete a list of flows asynchronously

**/api/v2/architect/dependencytracking/object** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/flows/{flowId}/versions** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/license/users** (2 changes)

* Path was added
* Operation POST was added

**DomainCapabilities** (1 change)

* Optional property pingEnabled was added

**ConsumedResourcesEntityListing** (1 change)

* Model was added

**Dependency** (1 change)

* Model was added

**Queue** (1 change)

* Optional property defaultScripts was added

**DependencyStatus** (1 change)

* Model was added

**FailedObject** (1 change)

* Model was added

**Campaign** (1 change)

* Optional property contactSorts was added

**DependencyType** (1 change)

* Model was added

**DependencyTypeEntityListing** (1 change)

* Model was added

**AggregationQuery** (1 change)

* Enum value segmentEnd was added to property groupBy

**AddressableLicenseDefinition** (1 change)

* Model was added

**LicenseDefinition** (1 change)

* Model was added

**Permissions** (1 change)

* Model was added

**DependencyObject** (1 change)

* Model was added

**DependencyObjectEntityListing** (1 change)

* Model was added

**JsonSchemaDocument** (1 change)

* Model was added

**ConsumingResourcesEntityListing** (1 change)

* Model was added

**AddressableEntityUser** (1 change)

* Model was added

**LicenseOrganization** (1 change)

* Model was added

**LicenseUpdateResponse** (1 change)

* Model was added

**LicenseUpdateStatus** (1 change)

* Model was added

**LicenseAssignmentRequest** (1 change)

* Model was added

**LicenseBatchAssignmentRequest** (1 change)

* Model was added

**LicenseDefinitionListing** (1 change)

* Model was added

**UserQueue** (1 change)

* Optional property defaultScripts was added

**CreateQueueRequest** (1 change)

* Optional property defaultScripts was added

**LicenseUser** (1 change)

* Model was added

**Response** (1 change)

* Optional property substitutionsSchema was added

**FlowVersionEntityListing** (1 change)

* Model was added


# Point Changes (1 change)

**GET /api/v2/architect/systemprompts/{promptId}/resources** (1 change)

* Summary was changed
