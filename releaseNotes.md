Platform API version: 7251


# Major Changes (8 changes)

**PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/attributes** (1 change)

* Response 202 type was changed from _undefined_ to ParticipantAttributes

**PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/attributes** (1 change)

* Response 202 type was changed from _undefined_ to ParticipantAttributes

**PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId}/attributes** (1 change)

* Response 202 type was changed from _undefined_ to ParticipantAttributes

**PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/attributes** (1 change)

* Response 202 type was changed from _undefined_ to ParticipantAttributes

**PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId}/attributes** (1 change)

* Response 202 type was changed from _undefined_ to ParticipantAttributes

**PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/attributes** (1 change)

* Response 202 type was changed from _undefined_ to ParticipantAttributes

**LabelUtilization** (1 change)

* Property interruptingLabels was removed

**ApiUsageSimpleSearch** (1 change)

* Values are now constrained by enum members


# Minor Changes (85 changes)

**/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback/{feedbackId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/views** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/feedback** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/journey/deployments/{deploymentId}/appevents** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/architect/grammars/{grammarId}/languages/{languageCode}** (3 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added

**/api/v2/architect/grammars/{grammarId}/languages/{languageCode}/files/voice** (3 changes)

* Path was added
* Operation POST was added
* Operation DELETE was added

**/api/v2/architect/grammars/{grammarId}/languages/{languageCode}/files/dtmf** (3 changes)

* Path was added
* Operation POST was added
* Operation DELETE was added

**/api/v2/architect/grammars/{grammarId}/languages** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/architect/grammars/{grammarId}** (4 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added
* Operation PATCH was added

**/api/v2/architect/grammars** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**EvaluationAggregateQueryPredicate** (1 change)

* Enum value assigneeApplicable was added to property dimension

**EvaluationAggregationQuery** (1 change)

* Enum value assigneeApplicable was added to property groupBy

**TranscriptAggregateQueryPredicate** (1 change)

* Enum value wrapUpCode was added to property dimension

**TranscriptAggregationQuery** (7 changes)

* Enum value wrapUpCode was added to property groupBy
* Enum value oOverTalkSpeechInstances was added to property metrics
* Enum value tAgentSpeech was added to property metrics
* Enum value tCustomerSpeech was added to property metrics
* Enum value tOverTalkSpeech was added to property metrics
* Enum value tSilence was added to property metrics
* Enum value tTotalSpeechAndSilence was added to property metrics

**TranscriptAggregationView** (6 changes)

* Enum value oOverTalkSpeechInstances was added to property target
* Enum value tAgentSpeech was added to property target
* Enum value tCustomerSpeech was added to property target
* Enum value tOverTalkSpeech was added to property target
* Enum value tSilence was added to property target
* Enum value tTotalSpeechAndSilence was added to property target

**Limit** (1 change)

* Enum value learning was added to property namespace

**Device** (2 changes)

* Optional property screenDensity was added
* Optional property manufacturer was added

**Session** (3 changes)

* Optional property app was added
* Optional property sdkLibrary was added
* Optional property networkConnectivity was added

**CampaignProgress** (1 change)

* Optional property numberOfContactsSkipped was added

**DialerContact** (1 change)

* Optional property dateCreated was added

**WritableDialerContact** (1 change)

* Optional property dateCreated was added

**EntityReference** (1 change)

* Model was added

**KnowledgeDocumentFeedbackResponse** (1 change)

* Model was added

**KnowledgeDocumentVersionReference** (1 change)

* Model was added

**KnowledgeDocumentFeedback** (1 change)

* Model was added

**KnowledgeDocumentFeedbackResponseListing** (1 change)

* Model was added

**KnowledgeDocumentView** (1 change)

* Model was added

**ApprovalNamespace** (1 change)

* Enum value learning was added to property namespace

**LimitChangeRequestDetails** (1 change)

* Enum value learning was added to property namespace

**StatusChange** (1 change)

* Enum value learning was added to property namespace

**KnowledgeGuestDocumentFeedback** (1 change)

* Model was added

**KnowledgeGuestDocumentVersionReference** (1 change)

* Model was added

**KnowledgeGuestSearchClientApplication** (1 change)

* Model was added

**EvaluationAggregationQueryMe** (1 change)

* Enum value assigneeApplicable was added to property groupBy

**LabelUtilization** (1 change)

* Optional property interruptingLabelIds was added

**EvaluationAsyncAggregationQuery** (1 change)

* Enum value assigneeApplicable was added to property groupBy

**TranscriptAsyncAggregationQuery** (7 changes)

* Enum value wrapUpCode was added to property groupBy
* Enum value oOverTalkSpeechInstances was added to property metrics
* Enum value tAgentSpeech was added to property metrics
* Enum value tCustomerSpeech was added to property metrics
* Enum value tOverTalkSpeech was added to property metrics
* Enum value tSilence was added to property metrics
* Enum value tTotalSpeechAndSilence was added to property metrics

**Event** (1 change)

* Optional property appEvent was added

**AppEventRequestSession** (1 change)

* Model was added

**AppEventResponse** (1 change)

* Model was added

**AppEventResponseSession** (1 change)

* Model was added

**AppEventRequest** (1 change)

* Model was added

**GrammarLanguage** (1 change)

* Model was added

**GrammarFileUploadRequest** (1 change)

* Model was added

**Grammar** (1 change)

* Model was added

**GrammarListing** (1 change)

* Model was added


# Point Changes (12 changes)

**GET /api/v2/analytics/botflows/{botFlowId}/reportingturns** (2 changes)

* Description was changed
* Description was changed for parameter sessionId

**GET /api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapupcodes** (1 change)

* Description was changed for parameter conversationId

**PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/attributes** (1 change)

* Description was changed for parameter conversationId

**PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}** (1 change)

* Description was changed for parameter conversationId

**PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId}** (1 change)

* Description was changed for parameter conversationId

**PUT /api/v2/quality/conversations/{conversationId}/evaluations/{evaluationId}** (1 change)

* Description was changed for parameter expand

**GET /api/v2/quality/evaluations/query** (4 changes)

* Description was changed for parameter sortBy
* Description was changed for parameter nextPage
* Description was changed for parameter maximum
* Description was changed for parameter sortOrder

**GET /api/v2/telephony/providers/edges/phones** (1 change)

* Summary was changed
