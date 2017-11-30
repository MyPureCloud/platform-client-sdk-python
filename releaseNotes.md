Platform API version: 1704


# Major Changes (4 changes)

**GET /api/v2/quality/evaluations/query** (1 change)

* Parameter sortOrder was added

**GET /api/v2/architect/prompts** (2 changes)

* Parameter sortBy was added
* Parameter sortOrder was added

**UpdateUser** (1 change)

* primaryContactInfo has been made readonly


# Minor Changes (70 changes)

**/api/v2/workforcemanagement/agents/managementunits** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/signeddata** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/scripts/uploads/{uploadId}/status** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions/{secureSessionId}** (2 changes)

* Path was added
* Operation GET was added

**InboundRoute** (1 change)

* Optional property replyRoute was added

**UserQueue** (2 changes)

* Optional property whisper was added
* Optional property autoAnswerOnly was added

**ExternalContact** (1 change)

* Optional property surveyOptOut was added

**Message** (3 changes)

* Optional property type was added
* Optional property recipientCountry was added
* Optional property recipientType was added

**MessageDetails** (2 changes)

* Optional property messageStatus was added
* Optional property messageSegmentCount was added

**Participant** (1 change)

* Enum value timeout was added to property screenRecordingState

**Queue** (2 changes)

* Optional property whisper was added
* Optional property autoAnswerOnly was added

**CreateEmailRequest** (2 changes)

* Optional property htmlBody was added
* Optional property textBody was added

**AdherenceSettings** (1 change)

* Model was added

**ManagementUnit** (2 changes)

* Optional property settings was added
* Optional property modifiedBy was added

**ManagementUnitSettings** (1 change)

* Model was added

**SchedulingSettings** (1 change)

* Model was added

**ShortTermForecastingSettings** (1 change)

* Model was added

**TimeOffRequestSettings** (1 change)

* Model was added

**Dependency** (2 changes)

* Enum value LEXBOT was added to property type
* Enum value LEXBOTALIAS was added to property type

**DependencyObject** (2 changes)

* Enum value LEXBOT was added to property type
* Enum value LEXBOTALIAS was added to property type

**CallForwarding** (2 changes)

* Optional property calls was added
* Optional property voicemail was added

**CallRoute** (1 change)

* Model was added

**CallTarget** (1 change)

* Model was added

**AgentManagementUnitReference** (1 change)

* Model was added

**ManagementUnitReference** (1 change)

* Model was added

**UserReference** (1 change)

* Model was added

**SecureSession** (1 change)

* Model was added

**SecureSessionEntityListing** (1 change)

* Model was added

**CreateSecureSession** (1 change)

* Model was added

**SignedData** (1 change)

* Model was added

**IntradayQueue** (1 change)

* Enum value Message was added to property mediaTypes

**IntradayDataGroup** (1 change)

* Enum value Message was added to property mediaType

**EventMessage** (2 changes)

* Enum value APPROACHING_CONTACT_LIMIT was added to property code
* Enum value EXCEEDED_CONTACT_LIMIT was added to property code

**ParticipantBasic** (1 change)

* Enum value timeout was added to property screenRecordingState

**AggregateMetricData** (1 change)

* Enum value tFlowOut was added to property metric

**AggregationQuery** (2 changes)

* Enum value messageType was added to property groupBy
* Enum value tFlowOut was added to property metrics

**AnalyticsQueryPredicate** (2 changes)

* Enum value messageType was added to property dimension
* Enum value tFlowOut was added to property metric

**AnalyticsConversationSegment** (5 changes)

* Enum value contacting was added to property segmentType
* Enum value transmitting was added to property segmentType
* Enum value converting was added to property segmentType
* Enum value uploading was added to property segmentType
* Enum value sharing was added to property segmentType

**AnalyticsSession** (1 change)

* Optional property messageType was added

**InteractionStatsAlert** (1 change)

* Enum value message was added to property mediaType

**CreateQueueRequest** (2 changes)

* Optional property whisper was added
* Optional property autoAnswerOnly was added

**CallMediaParticipant** (1 change)

* Optional property uuiData was added

**InteractionStatsRule** (1 change)

* Enum value message was added to property mediaType

**ImportScriptStatusResponse** (1 change)

* Model was added

**ObservationQuery** (1 change)

* Enum value tFlowOut was added to property metrics


# Point Changes (0 changes)
