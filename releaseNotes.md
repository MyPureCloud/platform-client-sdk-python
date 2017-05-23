
# Major Changes (5 changes)

**GET /api/v2/locations** (1 change)

* Response 200 type was changed from LocationDefinition[] to LocationEntityListing

**GET /api/v2/users** (1 change)

* Parameter state was added

**Flow** (2 changes)

* Property lockedUser was changed from UriReference to User
* Property publishedBy was changed from UriReference to User

**FlowVersion** (1 change)

* Property createdBy was changed from UriReference to User


# Minor Changes (27 changes)

**/api/v2/telephony/providers/edges/{edgeId}/trunks** (2 changes)

* Path was added
* Operation GET was added

**Call** (1 change)

* Optional property peerId was added

**CallBasic** (1 change)

* Optional property peerId was added

**Callback** (2 changes)

* Optional property voicemail was added
* Optional property peerId was added

**CallbackBasic** (2 changes)

* Optional property voicemail was added
* Optional property peerId was added

**Cobrowsesession** (1 change)

* Optional property peerId was added

**Contact** (1 change)

* Optional property extension was added

**ConversationChat** (1 change)

* Optional property peerId was added

**Email** (1 change)

* Optional property peerId was added

**Screenshare** (1 change)

* Optional property peerId was added

**SocialExpression** (1 change)

* Optional property peerId was added

**Video** (1 change)

* Optional property peerId was added

**Voicemail** (1 change)

* Model was added

**VoicemailMediaInfo** (1 change)

* Optional property waveformData was added

**EncryptionKey** (1 change)

* Optional property localEncryptionConfiguration was added

**ManagementUnit** (1 change)

* Optional property dateModified was added

**CallMediaParticipant** (1 change)

* Optional property peer was added

**EmailMediaParticipant** (1 change)

* Optional property peer was added

**LocationEntityListing** (1 change)

* Model was added

**CobrowseMediaParticipant** (1 change)

* Optional property peer was added

**ChatMediaParticipant** (1 change)

* Optional property peer was added

**UpdateUser** (1 change)

* Optional property state was added

**CallbackMediaParticipant** (2 changes)

* Optional property peer was added
* Optional property voicemail was added


# Point Changes (7 changes)

**GET /api/v2/workforcemanagement/managementunits/{muId}/intraday/queues** (1 change)

* Description was changed for parameter muId

**POST /api/v2/workforcemanagement/managementunits/{muId}/intraday** (1 change)

* Description was changed for parameter muId

**GET /api/v2/workforcemanagement/managementunits/{muId}/users** (1 change)

* Description was changed for parameter muId

**GET /api/v2/workforcemanagement/managementunits/{muId}/activitycodes** (1 change)

* Description was changed for parameter muId

**POST /api/v2/workforcemanagement/managementunits/{muId}/schedules/search** (1 change)

* Description was changed for parameter muId

**GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests/{timeOffRequestId}** (1 change)

* Description was changed for parameter muId

**GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests** (1 change)

* Description was changed for parameter muId
