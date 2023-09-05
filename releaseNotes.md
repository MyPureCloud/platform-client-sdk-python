Platform API version: 7311


# Major Changes (13 changes)

**GET /api/v2/tokens/me** (1 change)

* Parameter preserveIdleTTL was added

**GET /api/v2/analytics/botflows/{botFlowId}/reportingturns** (1 change)

* Parameter interval was added

**GET /api/v2/externalcontacts/contacts/{contactId}/journey/sessions** (1 change)

* Tag Journey was added

**GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId}** (1 change)

* Parameter expand was added

**GET /api/v2/quality/agents/activity** (1 change)

* Parameter formContextId was added

**GET /api/v2/quality/evaluations/query** (1 change)

* Parameter formContextId was added

**GET /api/v2/routing/message/recipients** (1 change)

* Parameter name was added

**POST /api/v2/routing/skillgroups** (1 change)

* Response 200 type was changed from SkillGroup to SkillGroupWithMemberDivisions

**GET /api/v2/webdeployments/deployments/{deploymentId}** (1 change)

* Parameter expand was added

**GET /api/v2/webdeployments/deployments/{deploymentId}/configurations** (1 change)

* Parameter expand was added

**GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId}** (1 change)

* Parameter expand was added

**GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates** (1 change)

* Parameter expand was added

**POST /api/v2/workforcemanagement/adherence/historical** (1 change)

* Has been deprecated


# Minor Changes (171 changes)

**/api/v2/conversations/messages/cachedmedia/{cachedMediaItemId}** (3 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added

**/api/v2/conversations/messages/cachedmedia** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/conversations/messages/{integrationId}/inbound/open/event** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/conversations/messages/{integrationId}/inbound/open/message** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/conversations/messages/{integrationId}/inbound/open/receipt** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/architect/emergencygroups/divisionviews** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/ivrs/divisionviews** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/schedulegroups/divisionviews** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/schedules/divisionviews** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/workforcemanagement/timeoffrequests/estimate** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/estimate** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/integrationstatus/query** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/{timeOffRequestId}/users/{userId}/integrationstatus** (2 changes)

* Path was added
* Operation PATCH was added

**/api/v2/workforcemanagement/timeoffrequests/integrationstatus/query** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/agents/integrations/hris/query** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/agents/{agentId}/integrations/hris** (2 changes)

* Path was added
* Operation PUT was added

**/api/v2/workforcemanagement/integrations/hris/timeofftypes/jobs/{jobId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/workforcemanagement/integrations/hris** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/workforcemanagement/integrations/hris/{hrisIntegrationId}/timeofftypes/jobs** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/timeoffbalance/jobs** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/timeoffbalance/jobs/{jobId}** (2 changes)

* Path was added
* Operation GET was added

**AnalyticsConversationSegment** (2 changes)

* Enum value endpointDnd was added to property disconnectType
* Enum value transferDnd was added to property disconnectType

**ReportingExportJobResponse** (1 change)

* Enum value EXPORT_EMAIL_FILE_SIZE_EXCEEDED_LIMIT was added to property exportErrorMessagesType

**Queue** (1 change)

* Optional property scoringMethod was added

**Session** (2 changes)

* Enum value DoNotDisturbEndpoint was added to property lastUserDisconnectType
* Enum value DoNotDisturbTransfer was added to property lastUserDisconnectType

**Call** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**CallMediaParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**CallHistoryParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**CallbackMediaParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**ChatMediaParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**CobrowseMediaParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**EmailMediaParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**CachedMediaItem** (1 change)

* Model was added

**CachedMediaItemEntityListing** (1 change)

* Model was added

**MessageMediaParticipant** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**OpenEventNormalizedMessage** (1 change)

* Model was added

**OpenMessageEvent** (1 change)

* Model was added

**OpenEvent** (1 change)

* Model was added

**OpenInboundMessagingChannel** (1 change)

* Model was added

**OpenInboundNormalizedEvent** (1 change)

* Model was added

**OpenMessageNormalizedMessage** (1 change)

* Model was added

**OpenContentAttachment** (1 change)

* Model was added

**OpenInboundMessageContent** (1 change)

* Model was added

**OpenInboundMessageMessagingChannel** (1 change)

* Model was added

**OpenInboundNormalizedMessage** (1 change)

* Model was added

**OpenReceiptNormalizedMessage** (1 change)

* Model was added

**OpenInboundMessagingReceiptChannel** (1 change)

* Model was added

**OpenInboundNormalizedReceipt** (1 change)

* Model was added

**CallBasic** (2 changes)

* Enum value endpoint.donotdisturb was added to property disconnectType
* Enum value transfer.donotdisturb was added to property disconnectType

**EventMessage** (1 change)

* Enum value CAMPAIGN_FORCE_STOPPED was added to property code

**TrendData** (1 change)

* Optional property averageValue was added

**KnowledgeBaseUpdateRequest** (1 change)

* Model was added

**KnowledgeBaseCreateRequest** (1 change)

* Model was added

**KnowledgeExportJobResponse** (1 change)

* Optional property createdBy was added

**KnowledgeImportJobResponse** (3 changes)

* Optional property downloadURL was added
* Optional property failedEntitiesURL was added
* Optional property createdBy was added

**QueueRequest** (1 change)

* Optional property scoringMethod was added

**UserQueue** (1 change)

* Optional property scoringMethod was added

**CreateQueueRequest** (1 change)

* Optional property scoringMethod was added

**RecipientFlow** (1 change)

* Model was added

**RecipientRequest** (1 change)

* Model was added

**SkillGroupWithMemberDivisions** (1 change)

* Model was added

**EmpathyScore** (1 change)

* Model was added

**EmergencyGroupDivisionView** (1 change)

* Model was added

**EmergencyGroupDivisionViewEntityListing** (1 change)

* Model was added

**IVRDivisionView** (1 change)

* Model was added

**IVRDivisionViewEntityListing** (1 change)

* Model was added

**ScheduleGroupDivisionView** (1 change)

* Model was added

**ScheduleGroupDivisionViewEntityListing** (1 change)

* Model was added

**ScheduleDivisionViewEntityListing** (1 change)

* Model was added

**SchedulesDivisionView** (1 change)

* Model was added

**WebDeployment** (1 change)

* Optional property supportedContent was added

**ExpandableWebDeployment** (1 change)

* Optional property supportedContent was added

**ScheduleActivity** (1 change)

* Enum value ActivityPlan was added to property externalActivityType

**LearningSlotScheduleActivity** (1 change)

* Enum value ActivityPlan was added to property externalActivityType

**EstimateAvailableFullDayTimeOffResponse** (1 change)

* Model was added

**EstimateAvailablePartialDayTimeOffResponse** (1 change)

* Model was added

**EstimateAvailableTimeOffResponse** (1 change)

* Model was added

**EstimateAvailableFullDayTimeOffRequest** (1 change)

* Model was added

**EstimateAvailablePartialDayTimeOffRequest** (1 change)

* Model was added

**EstimateAvailableTimeOffRequest** (1 change)

* Model was added

**ForecastServiceGoalTemplateResponse** (1 change)

* Optional property impactOverride was added

**ForecastPlanningGroupsResponse** (1 change)

* Optional property businessUnitServiceGoalImpact was added

**BuSchedulingSettingsResponse** (2 changes)

* Optional property syncTimeOffProperties was added
* Optional property serviceGoalImpact was added

**BuSchedulingSettingsRequest** (2 changes)

* Optional property syncTimeOffProperties was added
* Optional property serviceGoalImpact was added

**ServiceGoalTemplate** (1 change)

* Optional property impactOverride was added

**UpdateServiceGoalTemplate** (1 change)

* Optional property impactOverride was added

**CreateServiceGoalTemplate** (1 change)

* Optional property impactOverride was added

**CreateTimeOffPlanRequest** (1 change)

* Optional property hrisTimeOffType was added

**UpdateTimeOffPlanRequest** (1 change)

* Optional property hrisTimeOffType was added

**UserTimeOffIntegrationStatusResponse** (1 change)

* Model was added

**UserTimeOffIntegrationStatusResponseListing** (1 change)

* Model was added

**QueryTimeOffIntegrationStatusRequest** (1 change)

* Model was added

**TimeOffRequestLookup** (1 change)

* Model was added

**SetTimeOffIntegrationStatusRequest** (1 change)

* Model was added

**TimeOffRequestResponse** (3 changes)

* Optional property durationMinutes was added
* Optional property payableMinutes was added
* Optional property syncVersion was added

**CreateAdminTimeOffRequest** (2 changes)

* Optional property durationMinutes was added
* Optional property payableMinutes was added

**AdminTimeOffRequestPatch** (2 changes)

* Optional property durationMinutes was added
* Optional property payableMinutes was added

**TimeOffRequest** (3 changes)

* Optional property durationMinutes was added
* Optional property payableMinutes was added
* Optional property syncVersion was added

**ShiftTradeActivityPreviewResponse** (1 change)

* Optional property payableMinutes was added

**WfmHistoricalAdherenceBulkUserResult** (1 change)

* Optional property actuals was added

**WfmHistoricalAdherenceBulkItem** (1 change)

* Optional property includeActuals was added

**CreateAgentTimeOffRequest** (2 changes)

* Optional property durationMinutes was added
* Optional property payableMinutes was added

**BuAgentScheduleActivity** (3 changes)

* Optional property payableMinutes was added
* Optional property timeOffRequestSyncVersion was added
* Enum value ActivityPlan was added to property externalActivityType

**BuFullDayTimeOffMarker** (2 changes)

* Optional property payableMinutes was added
* Optional property timeOffRequestSyncVersion was added

**TimeOffIntegrationStatusResponse** (1 change)

* Model was added

**TimeOffIntegrationStatusResponseListing** (1 change)

* Model was added

**CurrentUserTimeOffIntegrationStatusRequest** (1 change)

* Model was added

**AgentIntegrationAssociationResponse** (1 change)

* Model was added

**AgentIntegrationsResponse** (1 change)

* Model was added

**AgentsIntegrationsListing** (1 change)

* Model was added

**WfmIntegrationReference** (1 change)

* Model was added

**QueryAgentsIntegrationsRequest** (1 change)

* Model was added

**AgentIntegrationAssociationRequest** (1 change)

* Model was added

**AgentIntegrationsRequest** (1 change)

* Model was added

**HrisTimeOffTypeResponse** (1 change)

* Model was added

**HrisTimeOffTypesJobResponse** (1 change)

* Model was added

**WfmIntegrationListing** (1 change)

* Model was added

**WfmIntegrationResponse** (1 change)

* Model was added

**HrisTimeOffTypesJobReference** (1 change)

* Model was added

**HrisTimeOffTypesResponse** (1 change)

* Model was added

**TimeOffBalanceJobResponse** (1 change)

* Model was added

**GrammarLanguage** (2 changes)

* Optional property voiceFileMetadata was added
* Optional property dtmfFileMetadata was added

**GrammarLanguageFileMetadata** (1 change)

* Model was added


# Point Changes (0 changes)
