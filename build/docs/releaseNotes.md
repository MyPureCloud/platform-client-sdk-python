Platform API version: 4784


# Release notes

* Forcing a major release to ensure SDKs align with API definition

# Major Changes (19 changes)

**GET /api/v2/journey/actiontemplates** (2 changes)

* Parameter queryFields was added
* Parameter queryValue was added

**GET /api/v2/journey/outcomes** (2 changes)

* Parameter queryFields was added
* Parameter queryValue was added

**GET /api/v2/journey/segments** (2 changes)

* Parameter queryFields was added
* Parameter queryValue was added

**GET /api/v2/journey/actionmaps** (2 changes)

* Parameter queryFields was added
* Parameter queryValue was added

**GET /api/v2/knowledge/knowledgebases** (1 change)

* Parameter coreLanguage was added

**GET /api/v2/architect/schedulegroups** (1 change)

* Parameter divisionId was added

**GET /api/v2/architect/schedules** (1 change)

* Parameter divisionId was added

**JourneyAggregateQueryPredicate** (4 changes)

* Enum value greaterThanCondition was removed from property dimension
* Enum value greaterThanOrEqualCondition was removed from property dimension
* Enum value lessThanCondition was removed from property dimension
* Enum value lessThanOrEqualCondition was removed from property dimension

**JourneyAggregationQuery** (4 changes)

* Enum value greaterThanCondition was removed from property groupBy
* Enum value greaterThanOrEqualCondition was removed from property groupBy
* Enum value lessThanCondition was removed from property groupBy
* Enum value lessThanOrEqualCondition was removed from property groupBy


# Minor Changes (120 changes)

**/api/v2/routing/predictors** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/routing/assessments/jobs/{jobId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/routing/queues/{queueId}/comparisonperiods/{comparisonPeriodId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/routing/predictors/{predictorId}** (4 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added
* Operation PATCH was added

**/api/v2/routing/predictors/keyperformanceindicators** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/routing/assessments/{assessmentId}** (3 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added

**/api/v2/routing/assessments/jobs** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/routing/assessments** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/routing/queues/{queueId}/comparisonperiods** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/workforcemanagement/agents/{agentId}/managementunit** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/workforcemanagement/agents/me/managementunit** (2 changes)

* Path was added
* Operation GET was added

**Team** (1 change)

* Optional property division was added

**FlowVersion** (2 changes)

* Enum value INQUEUEEMAIL was added to property compatibleFlowTypes
* Enum value INQUEUESHORTMESSAGE was added to property compatibleFlowTypes

**AnalyticsFlow** (2 changes)

* Enum value INQUEUEEMAIL was added to property flowType
* Enum value INQUEUESHORTMESSAGE was added to property flowType

**Predictor** (1 change)

* Model was added

**PredictorListing** (1 change)

* Model was added

**PredictorSchedule** (1 change)

* Model was added

**PredictorWorkloadBalancing** (1 change)

* Model was added

**CreatePredictorRequest** (1 change)

* Model was added

**ViewFilter** (3 changes)

* Enum value instagram was added to property messageTypes
* Enum value inqueueshortmessage was added to property flowTypes
* Enum value inqueueemail was added to property flowTypes

**EventMessage** (3 changes)

* Enum value IMPORT_INVALID_EMAIL_ADDRESSES was added to property code
* Enum value IMPORT_INVALID_EXPIRATION_DATE was added to property code
* Enum value IMPORT_EXPIRATION_DATE_EXCEEDS_MAX_DAYS was added to property code

**DevelopmentActivity** (1 change)

* Enum value Assessment was added to property type

**BenefitAssessmentJob** (1 change)

* Model was added

**Flow** (4 changes)

* Enum value INQUEUEEMAIL was added to property type
* Enum value INQUEUESHORTMESSAGE was added to property type
* Enum value INQUEUEEMAIL was added to property compatibleFlowTypes
* Enum value INQUEUESHORTMESSAGE was added to property compatibleFlowTypes

**ComparisonPeriod** (1 change)

* Model was added

**CreateCallbackCommand** (2 changes)

* Optional property callerId was added
* Optional property callerIdName was added

**Dependency** (2 changes)

* Enum value INQUEUEEMAILFLOW was added to property type
* Enum value INQUEUESHORTMESSAGEFLOW was added to property type

**VoicemailGroupPolicy** (1 change)

* Optional property disableEmailPii was added

**DependencyObject** (2 changes)

* Enum value INQUEUEEMAILFLOW was added to property type
* Enum value INQUEUESHORTMESSAGEFLOW was added to property type

**PatchPredictorRequest** (1 change)

* Model was added

**KeyPerformanceIndicator** (1 change)

* Model was added

**TrustUpdate** (1 change)

* Model was added

**CrossPlatformPolicyUpdate** (1 change)

* Model was added

**JourneyAggregateQueryPredicate** (1 change)

* Enum value journeyBlockingEmergencyScheduleGroupId was added to property dimension

**JourneyAggregationQuery** (1 change)

* Enum value journeyBlockingEmergencyScheduleGroupId was added to property groupBy

**BenefitAssessment** (1 change)

* Model was added

**Check** (1 change)

* Model was added

**KeyPerformanceIndicatorAssessment** (1 change)

* Model was added

**AssessmentJobListing** (1 change)

* Model was added

**CreateBenefitAssessmentJobRequest** (1 change)

* Model was added

**AssessmentListing** (1 change)

* Model was added

**CreateBenefitAssessmentRequest** (1 change)

* Model was added

**PolicyUpdate** (1 change)

* Model was added

**CreateCallbackOnConversationCommand** (2 changes)

* Optional property callerId was added
* Optional property callerIdName was added

**VoicemailOrganizationPolicy** (1 change)

* Optional property disableEmailPii was added

**ComparisonPeriodListing** (1 change)

* Model was added

**FlowDivisionView** (2 changes)

* Enum value INQUEUEEMAIL was added to property type
* Enum value INQUEUESHORTMESSAGE was added to property type

**AgentManagementUnitReference** (1 change)

* Model was added

**AuditQueryExecutionStatusResponse** (3 changes)

* Enum value Coaching was added to property serviceName
* Enum value Datatables was added to property serviceName
* Enum value Gamification was added to property serviceName

**AuditQueryRequest** (3 changes)

* Enum value Coaching was added to property serviceName
* Enum value Datatables was added to property serviceName
* Enum value Gamification was added to property serviceName

**AuditLogMessage** (16 changes)

* Enum value Coaching was added to property serviceName
* Enum value Datatables was added to property serviceName
* Enum value Gamification was added to property serviceName
* Enum value Write was added to property action
* Enum value Purge was added to property action
* Enum value Processed was added to property action
* Enum value Annotation was added to property entityType
* Enum value Appointment was added to property entityType
* Enum value Bulk was added to property entityType
* Enum value ExternalMetricData was added to property entityType
* Enum value HistoricalData was added to property entityType
* Enum value Metric was added to property entityType
* Enum value Row was added to property entityType
* Enum value Schema was added to property entityType
* Enum value Status was added to property entityType
* Enum value SupportedContent was added to property entityType

**AuditRealtimeQueryRequest** (3 changes)

* Enum value Coaching was added to property serviceName
* Enum value Datatables was added to property serviceName
* Enum value Gamification was added to property serviceName

**AuditQueryEntity** (13 changes)

* Enum value Annotation was added to property name
* Enum value Appointment was added to property name
* Enum value Bulk was added to property name
* Enum value ExternalMetricData was added to property name
* Enum value HistoricalData was added to property name
* Enum value Metric was added to property name
* Enum value Row was added to property name
* Enum value Schema was added to property name
* Enum value Status was added to property name
* Enum value SupportedContent was added to property name
* Enum value Write was added to property actions
* Enum value Purge was added to property actions
* Enum value Processed was added to property actions

**AuditQueryService** (3 changes)

* Enum value Coaching was added to property name
* Enum value Datatables was added to property name
* Enum value Gamification was added to property name


# Point Changes (4 changes)

**GET /api/v2/journey/actiontemplates** (1 change)

* Description was changed for parameter state

**GET /api/v2/journey/outcomes** (1 change)

* Description was changed for parameter outcomeIds

**GET /api/v2/journey/segments** (1 change)

* Description was changed for parameter segmentIds

**GET /api/v2/journey/actionmaps** (1 change)

* Description was changed for parameter actionMapIds
