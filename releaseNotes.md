Platform API version: 1387


# Major Changes (27 changes)

**/api/v2/alerting/routingstatus/alerts/{alertId}** (1 change)

* Path /api/v2/alerting/routingstatus/alerts/{alertId} was removed

**/api/v2/alerting/heartbeat/rules** (1 change)

* Path /api/v2/alerting/heartbeat/rules was removed

**/api/v2/alerting/heartbeat/alerts** (1 change)

* Path /api/v2/alerting/heartbeat/alerts was removed

**/api/v2/alerting/userpresence/rules** (1 change)

* Path /api/v2/alerting/userpresence/rules was removed

**/api/v2/alerting/heartbeat/alerts/{alertId}** (1 change)

* Path /api/v2/alerting/heartbeat/alerts/{alertId} was removed

**/api/v2/alerting/routingstatus/rules** (1 change)

* Path /api/v2/alerting/routingstatus/rules was removed

**/api/v2/alerting/userpresence/rules/{ruleId}** (1 change)

* Path /api/v2/alerting/userpresence/rules/{ruleId} was removed

**/api/v2/alerting/heartbeat/rules/{ruleId}** (1 change)

* Path /api/v2/alerting/heartbeat/rules/{ruleId} was removed

**/api/v2/alerting/userpresence/alerts/{alertId}** (1 change)

* Path /api/v2/alerting/userpresence/alerts/{alertId} was removed

**/api/v2/alerting/routingstatus/alerts** (1 change)

* Path /api/v2/alerting/routingstatus/alerts was removed

**/api/v2/alerting/routingstatus/rules/{ruleId}** (1 change)

* Path /api/v2/alerting/routingstatus/rules/{ruleId} was removed

**/api/v2/alerting/userpresence/alerts** (1 change)

* Path /api/v2/alerting/userpresence/alerts was removed

**GET /api/v2/authorization/roles** (1 change)

* Parameter name was added

**GET /api/v2/externalcontacts/organizations** (1 change)

* Parameter trustorId was added

**RoutingStatusAlert** (1 change)

* Model RoutingStatusAlert was removed

**HeartBeatRule** (1 change)

* Model HeartBeatRule was removed

**HeartBeatRuleContainer** (1 change)

* Model HeartBeatRuleContainer was removed

**HeartBeatAlert** (1 change)

* Model HeartBeatAlert was removed

**HeartBeatAlertContainer** (1 change)

* Model HeartBeatAlertContainer was removed

**UserPresenceRule** (1 change)

* Model UserPresenceRule was removed

**UserPresenceRuleContainer** (1 change)

* Model UserPresenceRuleContainer was removed

**RoutingStatusRule** (1 change)

* Model RoutingStatusRule was removed

**RoutingStatusRuleContainer** (1 change)

* Model RoutingStatusRuleContainer was removed

**UserPresenceAlert** (1 change)

* Model UserPresenceAlert was removed

**RoutingStatusAlertContainer** (1 change)

* Model RoutingStatusAlertContainer was removed

**UserPresenceAlertContainer** (1 change)

* Model UserPresenceAlertContainer was removed

**ScreenRecordingSession** (1 change)

* Property participantId was removed


# Minor Changes (124 changes)

**/api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roles** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/orgauthorization/trustor/audits** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/orgauthorization/trustees/audits** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/orgauthorization/trustors/{trustorOrgId}/users/{trusteeUserId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/voicemail/messages/{messageId}** (1 change)

* Operation patch was added. Summary: Update a voicemail message

**/api/v2/architect/schedules/{scheduleId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/orgauthorization/trustors/{trustorOrgId}/users** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/orgauthorization/trustees** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}** (3 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added

**/api/v2/orgauthorization/trustors** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/schedules** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/architect/ivrs/{ivrId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/flows/{flowId}/history/{historyId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/architect/ivrs** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/architect/schedulegroups** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/orgauthorization/pairings** (2 changes)

* Path was added
* Operation POST was added

**/api/v2/license/toggles/{featureName}** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/orgauthorization/pairings/{pairingId}** (2 changes)

* Path was added
* Operation GET was added

**/api/v2/orgauthorization/trustees/{trusteeOrgId}/users** (3 changes)

* Path was added
* Operation GET was added
* Operation POST was added

**/api/v2/orgauthorization/trustees/{trusteeOrgId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**/api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/uuidata** (2 changes)

* Path was added
* Operation PUT was added

**/api/v2/orgauthorization/trustors/{trustorOrgId}** (3 changes)

* Path was added
* Operation GET was added
* Operation DELETE was added

**/api/v2/architect/schedulegroups/{scheduleGroupId}** (4 changes)

* Path was added
* Operation GET was added
* Operation PUT was added
* Operation DELETE was added

**OutOfOffice** (1 change)

* Optional property indefinite was added

**Call** (1 change)

* Optional property uuiData was added

**ConversationChat** (1 change)

* Optional property scriptId was added

**Email** (2 changes)

* Optional property scriptId was added
* Optional property messageId was added

**Participant** (1 change)

* Optional property screenRecordingState was added

**SocialExpression** (1 change)

* Optional property scriptId was added

**Voicemail** (1 change)

* Optional property uploadStatus was added

**SearchSort** (1 change)

* Model was added

**UserSearchRequest** (1 change)

* Optional property sort was added

**Edge** (1 change)

* Optional property offlineConfigCalled was added

**AuditQueryResponse** (1 change)

* Model was added

**Facet** (1 change)

* Model was added

**Filter** (1 change)

* Model was added

**TrustorAuditQueryRequest** (1 change)

* Model was added

**TrusteeAuditQueryRequest** (1 change)

* Model was added

**OrgOAuthClient** (4 changes)

* Optional property dateCreated was added
* Optional property dateModified was added
* Optional property createdBy was added
* Optional property modifiedBy was added

**UserMe** (1 change)

* Optional property trustors was added

**OAuthClient** (4 changes)

* Optional property dateCreated was added
* Optional property dateModified was added
* Optional property createdBy was added
* Optional property modifiedBy was added

**OAuthClientListing** (4 changes)

* Optional property dateCreated was added
* Optional property dateModified was added
* Optional property createdBy was added
* Optional property modifiedBy was added

**LocationSearchRequest** (1 change)

* Optional property sort was added

**TrustUser** (1 change)

* Model was added

**TrustUserDetails** (1 change)

* Model was added

**VoicemailMessage** (1 change)

* Optional property retentionPolicy was added

**VoicemailRetentionPolicy** (1 change)

* Model was added

**CallBasic** (1 change)

* Optional property uuiData was added

**ParticipantBasic** (1 change)

* Optional property screenRecordingState was added

**Schedule** (1 change)

* Model was added

**TrustUserEntityListing** (1 change)

* Model was added

**SearchRequest** (1 change)

* Optional property sort was added

**CreateCallbackOnConversationCommand** (1 change)

* Model was added

**Trustee** (1 change)

* Model was added

**TrustCreate** (1 change)

* Model was added

**TrustUserCreate** (1 change)

* Model was added

**TrustEntityListing** (1 change)

* Model was added

**DocumentationSearchRequest** (1 change)

* Optional property sort was added

**TrustorEntityListing** (1 change)

* Model was added

**ScreenRecordingSession** (1 change)

* Optional property communicationId was added

**ScheduleEntityListing** (1 change)

* Model was added

**GroupSearchRequest** (1 change)

* Optional property sort was added

**IVR** (1 change)

* Model was added

**VoicemailSearchRequest** (1 change)

* Optional property sort was added

**HistoryListing** (1 change)

* Model was added

**IVREntityListing** (1 change)

* Model was added

**ScheduleGroup** (1 change)

* Model was added

**ScheduleGroupEntityListing** (1 change)

* Model was added

**TrustRequest** (1 change)

* Model was added

**TrustRequestCreate** (1 change)

* Model was added

**LicenseOrgToggle** (1 change)

* Model was added

**SetUuiDataRequest** (1 change)

* Model was added


# Point Changes (9 changes)

**GET /api/v2/voicemail/messages/{messageId}/media** (1 change)

* Summary was changed

**GET /api/v2/voicemail/messages/{messageId}** (1 change)

* Summary was changed

**PUT /api/v2/voicemail/messages/{messageId}** (2 changes)

* Description was changed
* Summary was changed

**DELETE /api/v2/voicemail/messages/{messageId}** (2 changes)

* Description was changed
* Summary was changed

**GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/contacts** (1 change)

* Description was changed for parameter expand

**POST /api/v2/outbound/contactlists/{contactListId}/contacts** (1 change)

* Description was changed for parameter priority

**PUT /api/v2/users/{userId}/outofoffice** (1 change)

* Description was changed for parameter body
