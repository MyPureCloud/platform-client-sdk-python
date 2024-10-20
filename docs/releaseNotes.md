Platform API version: 8554




# Major Changes (7 changes)

**GET /api/v2/authorization/roles/{roleId}/users** (1 change)

* Response 200 type was changed from UserEntityListing to UserReferenceEntityListing

**GET /api/v2/contentmanagement/shared/{sharedId}** (2 changes)

* Parameter redirect was removed
* Response 307 was removed

**POST /api/v2/conversations/{conversationId}/suggestions/feedback** (1 change)

* Has been deprecated

**ReplacementTerm** (1 change)

* Enum value FACEBOOK was removed from property type

**DocumentBodyBlockWithHighlight** (2 changes)

* Property list was changed from DocumentBodyList to DocumentBodyListWithHighlight
* Property table was changed from DocumentBodyTable to DocumentBodyTableWithHighlight


# Minor Changes (65 changes)

**/api/v2/externalcontacts/import/csv/jobs** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/externalcontacts/import/csv/settings/{settingsId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/externalcontacts/import/csv/settings** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/externalcontacts/import/csv/uploads/{uploadId}/details** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/externalcontacts/import/csv/uploads/{uploadId}/preview** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/externalcontacts/import/csv/uploads** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/orgauthorization/trustees/care** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**UserReferenceEntityListing** (1 change)

* Model was added

**ContactIdentifier** (1 change)

* Enum value SocialInstagram was added to property type

**CsvJobResponse** (1 change)

* Model was added

**CsvJobRequest** (1 change)

* Model was added

**CsvMappingEntry** (1 change)

* Model was added

**CsvSettings** (1 change)

* Model was added

**Listing** (1 change)

* Model was added

**CsvUploadDetailsResponse** (1 change)

* Model was added

**ValidationError** (1 change)

* Model was added

**ValidationResult** (1 change)

* Model was added

**CsvUploadPreviewResponse** (1 change)

* Model was added

**CsvUploadResponse** (1 change)

* Model was added

**Header** (1 change)

* Model was added

**CsvUploadRequest** (1 change)

* Model was added

**Campaign** (1 change)

* Optional property skillColumns was added

**CampaignRuleAction** (2 changes)

* Enum value setCampaignMessagesPerMinute was added to property actionType
* Enum value changeCampaignTemplate was added to property actionType

**CampaignRuleParameters** (3 changes)

* Optional property messagesPerMinute was added
* Optional property smsContentTemplate was added
* Optional property emailContentTemplate was added

**CampaignRuleWarning** (1 change)

* Model was added

**CampaignRuleWarningParameters** (1 change)

* Model was added

**DocumentBodyListBlockWithHighlight** (1 change)

* Model was added

**DocumentBodyListWithHighlight** (1 change)

* Model was added

**DocumentBodyTableCellBlockWithHighlight** (1 change)

* Model was added

**DocumentBodyTableRowBlockWithHighlight** (1 change)

* Model was added

**DocumentBodyTableWithHighlight** (1 change)

* Model was added

**DocumentListContentBlockWithHighlight** (1 change)

* Model was added

**DocumentTableContentBlockWithHighlight** (1 change)

* Model was added

**TrusteeReferenceList** (1 change)

* Model was added

**Survey** (3 changes)

* Optional property surveyType was added
* Optional property missingRequiredAnswer was added
* Optional property flow was added

**Button** (1 change)

* Model was added

**MessageFooter** (1 change)

* Model was added

**MessageHeader** (1 change)

* Model was added

**RoutePathResponse** (1 change)

* Enum value Workitem was added to property mediaType

**BuIntradayDataGroup** (1 change)

* Enum value Workitem was added to property mediaType

**RoutePathRequest** (1 change)

* Enum value Workitem was added to property mediaType

**WorkitemQueryJobCreate** (3 changes)

* Optional property queryFilters was added
* Optional property dateIntervalStart was added
* Optional property dateIntervalEnd was added

**WorkitemQueryJobQueryFilters** (1 change)

* Model was added

**WorkitemQueryJobQueryFiltersCriteria** (1 change)

* Model was added

**WorkitemQueryJobQueryFiltersPredicate** (1 change)

* Model was added

**ResolutionAggregateQueryPredicate** (1 change)

* Enum value wrapUpDate was added to property dimension

**ResolutionAsyncAggregationQuery** (1 change)

* Enum value wrapUpDate was added to property alternateTimeDimension


# Point Changes (2 changes)

**POST /api/v2/conversations/{conversationId}/suggestions/feedback** (1 change)

* Description was changed

**GET /api/v2/flows/{flowId}/versions/{versionId}/configuration** (1 change)

* Summary was changed
