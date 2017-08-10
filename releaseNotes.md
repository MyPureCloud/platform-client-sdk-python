Platform API version: 1410


# Major Changes (4 changes)

**GET /api/v2/groups** (1 change)

* Parameter id was added

**VoicemailMessage** (1 change)

* Property retentionPolicy was removed

**Condition** (2 changes)

* Enum value LAST_RESULT_BY_COLUMN was removed from property propertyType
* Enum value LAST_RESULT_OVERALL was removed from property propertyType


# Minor Changes (22 changes)

**/api/v2/voicemail/queues/{queueId}/messages** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/conversations/emails/{conversationId}/inboundmessages** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/workforcemanagement/managementunits/{muId}/historicaladherencequery** (2 changes)

* Path was added
* Operation POST was added

**Flow** (1 change)

* Enum value SURVEYINVITE was added to property type

**VoicemailMessage** (2 changes)

* Optional property deletedDate was added
* Optional property deleteRetentionPolicy was added

**Recording** (1 change)

* Optional property users was added

**Condition** (2 changes)

* Enum value LAST_WRAPUP_BY_COLUMN was added to property propertyType
* Enum value LAST_WRAPUP_OVERALL was added to property propertyType

**Dependency** (2 changes)

* Enum value EMAILROUTE was added to property type
* Enum value SURVEYINVITEFLOW was added to property type

**DependencyObject** (2 changes)

* Enum value EMAILROUTE was added to property type
* Enum value SURVEYINVITEFLOW was added to property type

**EventLog** (1 change)

* Enum value ENTITY_LIMIT was added to property category

**EventMessage** (1 change)

* Enum value APPROACHING_ENTITY_LIMIT was added to property code

**InboundMessageRequest** (1 change)

* Model was added

**CreateEmailRequest** (1 change)

* Optional property flowId was added

**WfmHistoricalAdherenceResponse** (1 change)

* Model was added

**WfmHistoricalAdherenceQuery** (1 change)

* Model was added


# Point Changes (0 changes)
