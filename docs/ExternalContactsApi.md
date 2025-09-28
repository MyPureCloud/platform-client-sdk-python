# ExternalContactsApi

## PureCloudPlatformClientV2.ExternalContactsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_externalcontacts_contact**](#delete_externalcontacts_contact) | Delete an external contact|
|[**delete_externalcontacts_contact_note**](#delete_externalcontacts_contact_note) | Delete a note for an external contact|
|[**delete_externalcontacts_contacts_schema**](#delete_externalcontacts_contacts_schema) | Delete a schema|
|[**delete_externalcontacts_externalsource**](#delete_externalcontacts_externalsource) | Delete an External Source. WARNING: Any records that reference this External Source will not be automatically cleaned up. Those records will still be editable, but their External IDs may not be fully viewable.|
|[**delete_externalcontacts_import_csv_setting**](#delete_externalcontacts_import_csv_setting) | Delete settings for CSV import|
|[**delete_externalcontacts_import_setting**](#delete_externalcontacts_import_setting) | Delete Settings|
|[**delete_externalcontacts_organization**](#delete_externalcontacts_organization) | Delete an external organization|
|[**delete_externalcontacts_organization_note**](#delete_externalcontacts_organization_note) | Delete a note for an external organization|
|[**delete_externalcontacts_organization_trustor**](#delete_externalcontacts_organization_trustor) | Unlink the Trustor for this External Organization|
|[**delete_externalcontacts_relationship**](#delete_externalcontacts_relationship) | Delete a relationship|
|[**get_externalcontacts_contact**](#get_externalcontacts_contact) | Fetch an external contact|
|[**get_externalcontacts_contact_identifiers**](#get_externalcontacts_contact_identifiers) | List the identifiers for a contact|
|[**get_externalcontacts_contact_journey_segments**](#get_externalcontacts_contact_journey_segments) | Retrieve segment assignments by external contact ID.|
|[**get_externalcontacts_contact_journey_sessions**](#get_externalcontacts_contact_journey_sessions) | Retrieve all sessions for a given external contact.|
|[**get_externalcontacts_contact_note**](#get_externalcontacts_contact_note) | Fetch a note for an external contact|
|[**get_externalcontacts_contact_notes**](#get_externalcontacts_contact_notes) | List notes for an external contact|
|[**get_externalcontacts_contact_unresolved**](#get_externalcontacts_contact_unresolved) | Fetch an unresolved external contact|
|[**get_externalcontacts_contacts**](#get_externalcontacts_contacts) | Search for external contacts|
|[**get_externalcontacts_contacts_export**](#get_externalcontacts_contacts_export) | Get export for exportId|
|[**get_externalcontacts_contacts_exports**](#get_externalcontacts_contacts_exports) | List exports for organization|
|[**get_externalcontacts_contacts_schema**](#get_externalcontacts_contacts_schema) | Get a schema|
|[**get_externalcontacts_contacts_schema_version**](#get_externalcontacts_contacts_schema_version) | Get a specific version of a schema|
|[**get_externalcontacts_contacts_schema_versions**](#get_externalcontacts_contacts_schema_versions) | Get all versions of an external contact&#39;s schema|
|[**get_externalcontacts_contacts_schemas**](#get_externalcontacts_contacts_schemas) | Get a list of schemas.|
|[**get_externalcontacts_contacts_schemas_coretype**](#get_externalcontacts_contacts_schemas_coretype) | Get a specific named core type.|
|[**get_externalcontacts_contacts_schemas_coretypes**](#get_externalcontacts_contacts_schemas_coretypes) | Get the core types from which all schemas are built.|
|[**get_externalcontacts_contacts_schemas_limits**](#get_externalcontacts_contacts_schemas_limits) | Get quantitative limits on schemas|
|[**get_externalcontacts_externalsource**](#get_externalcontacts_externalsource) | Fetch an External Source|
|[**get_externalcontacts_externalsources**](#get_externalcontacts_externalsources) | Fetch a list of External Sources|
|[**get_externalcontacts_import_csv_setting**](#get_externalcontacts_import_csv_setting) | Get settings for CSV import|
|[**get_externalcontacts_import_csv_settings**](#get_externalcontacts_import_csv_settings) | Retrieve all settings for organization filtered by externalSettingsId if provided|
|[**get_externalcontacts_import_csv_upload_details**](#get_externalcontacts_import_csv_upload_details) | Get details for CSV upload|
|[**get_externalcontacts_import_csv_upload_preview**](#get_externalcontacts_import_csv_upload_preview) | Get preview for CSV upload|
|[**get_externalcontacts_import_job**](#get_externalcontacts_import_job) | Get job based on id|
|[**get_externalcontacts_import_jobs**](#get_externalcontacts_import_jobs) | List jobs for organization|
|[**get_externalcontacts_import_setting**](#get_externalcontacts_import_setting) | Get setting based on id|
|[**get_externalcontacts_import_settings**](#get_externalcontacts_import_settings) | List settings for organization|
|[**get_externalcontacts_organization**](#get_externalcontacts_organization) | Fetch an external organization|
|[**get_externalcontacts_organization_contacts**](#get_externalcontacts_organization_contacts) | Search for external contacts in an external organization|
|[**get_externalcontacts_organization_identifiers**](#get_externalcontacts_organization_identifiers) | List the identifiers for an external organization|
|[**get_externalcontacts_organization_note**](#get_externalcontacts_organization_note) | Fetch a note for an external organization|
|[**get_externalcontacts_organization_notes**](#get_externalcontacts_organization_notes) | List notes for an external organization|
|[**get_externalcontacts_organization_relationships**](#get_externalcontacts_organization_relationships) | Fetch a relationship for an external organization|
|[**get_externalcontacts_organizations**](#get_externalcontacts_organizations) | Search for external organizations|
|[**get_externalcontacts_organizations_schema**](#get_externalcontacts_organizations_schema) | Get a schema|
|[**get_externalcontacts_organizations_schema_version**](#get_externalcontacts_organizations_schema_version) | Get a specific version of a schema|
|[**get_externalcontacts_organizations_schema_versions**](#get_externalcontacts_organizations_schema_versions) | Get all versions of an external organization&#39;s schema|
|[**get_externalcontacts_organizations_schemas**](#get_externalcontacts_organizations_schemas) | Get a list of schemas.|
|[**get_externalcontacts_organizations_schemas_coretype**](#get_externalcontacts_organizations_schemas_coretype) | Get a specific named core type.|
|[**get_externalcontacts_organizations_schemas_coretypes**](#get_externalcontacts_organizations_schemas_coretypes) | Get the core types from which all schemas are built.|
|[**get_externalcontacts_organizations_schemas_limits**](#get_externalcontacts_organizations_schemas_limits) | Get quantitative limits on schemas|
|[**get_externalcontacts_relationship**](#get_externalcontacts_relationship) | Fetch a relationship|
|[**get_externalcontacts_reversewhitepageslookup**](#get_externalcontacts_reversewhitepageslookup) | Look up contacts based on an attribute. Maximum of 25 values returned.|
|[**get_externalcontacts_scan_contacts**](#get_externalcontacts_scan_contacts) | Scan for external contacts using paging|
|[**get_externalcontacts_scan_contacts_divisionviews_all**](#get_externalcontacts_scan_contacts_divisionviews_all) | Scan for external contacts using paging|
|[**get_externalcontacts_scan_notes**](#get_externalcontacts_scan_notes) | Scan for notes using paging|
|[**get_externalcontacts_scan_notes_divisionviews_all**](#get_externalcontacts_scan_notes_divisionviews_all) | Scan for notes using paging|
|[**get_externalcontacts_scan_organizations**](#get_externalcontacts_scan_organizations) | Scan for external organizations using paging|
|[**get_externalcontacts_scan_organizations_divisionviews_all**](#get_externalcontacts_scan_organizations_divisionviews_all) | Scan for external organizations using paging|
|[**get_externalcontacts_scan_relationships**](#get_externalcontacts_scan_relationships) | Scan for relationships|
|[**get_externalcontacts_scan_relationships_divisionviews_all**](#get_externalcontacts_scan_relationships_divisionviews_all) | Scan for relationships|
|[**patch_externalcontacts_contact_identifiers**](#patch_externalcontacts_contact_identifiers) | Claim or release identifiers for a contact|
|[**patch_externalcontacts_organization_identifiers**](#patch_externalcontacts_organization_identifiers) | Claim or release identifiers for an external organization|
|[**post_externalcontacts_bulk_contacts**](#post_externalcontacts_bulk_contacts) | Bulk fetch contacts|
|[**post_externalcontacts_bulk_contacts_add**](#post_externalcontacts_bulk_contacts_add) | Bulk add contacts|
|[**post_externalcontacts_bulk_contacts_divisionviews**](#post_externalcontacts_bulk_contacts_divisionviews) | Bulk fetch contacts across divisions|
|[**post_externalcontacts_bulk_contacts_enrich**](#post_externalcontacts_bulk_contacts_enrich) | Bulk Enrich Contacts - Run up to 10 Enrich operations per request|
|[**post_externalcontacts_bulk_contacts_remove**](#post_externalcontacts_bulk_contacts_remove) | Bulk remove contacts|
|[**post_externalcontacts_bulk_contacts_unresolved**](#post_externalcontacts_bulk_contacts_unresolved) | Bulk fetch unresolved ancestor contacts|
|[**post_externalcontacts_bulk_contacts_update**](#post_externalcontacts_bulk_contacts_update) | Bulk update contacts|
|[**post_externalcontacts_bulk_notes**](#post_externalcontacts_bulk_notes) | Bulk fetch notes|
|[**post_externalcontacts_bulk_notes_add**](#post_externalcontacts_bulk_notes_add) | Bulk add notes|
|[**post_externalcontacts_bulk_notes_remove**](#post_externalcontacts_bulk_notes_remove) | Bulk remove notes|
|[**post_externalcontacts_bulk_notes_update**](#post_externalcontacts_bulk_notes_update) | Bulk update notes|
|[**post_externalcontacts_bulk_organizations**](#post_externalcontacts_bulk_organizations) | Bulk fetch organizations|
|[**post_externalcontacts_bulk_organizations_add**](#post_externalcontacts_bulk_organizations_add) | Bulk add organizations|
|[**post_externalcontacts_bulk_organizations_divisionviews**](#post_externalcontacts_bulk_organizations_divisionviews) | Bulk fetch organizations across divisions|
|[**post_externalcontacts_bulk_organizations_enrich**](#post_externalcontacts_bulk_organizations_enrich) | Bulk enrich external organizations - Run up to 10 Enrich operations per request|
|[**post_externalcontacts_bulk_organizations_remove**](#post_externalcontacts_bulk_organizations_remove) | Bulk remove organizations|
|[**post_externalcontacts_bulk_organizations_update**](#post_externalcontacts_bulk_organizations_update) | Bulk update organizations|
|[**post_externalcontacts_bulk_relationships**](#post_externalcontacts_bulk_relationships) | Bulk fetch relationships|
|[**post_externalcontacts_bulk_relationships_add**](#post_externalcontacts_bulk_relationships_add) | Bulk add relationships|
|[**post_externalcontacts_bulk_relationships_remove**](#post_externalcontacts_bulk_relationships_remove) | Bulk remove relationships|
|[**post_externalcontacts_bulk_relationships_update**](#post_externalcontacts_bulk_relationships_update) | Bulk update relationships|
|[**post_externalcontacts_contact_journey_segments**](#post_externalcontacts_contact_journey_segments) | Assign/Unassign up to 10 segments to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment. Any unprocessed segment assignments are returned in the body for the client to retry, in the event of a partial success.|
|[**post_externalcontacts_contact_notes**](#post_externalcontacts_contact_notes) | Create a note for an external contact|
|[**post_externalcontacts_contact_promotion**](#post_externalcontacts_contact_promotion) | Promote an observed contact (ephemeral or identified) to a curated contact|
|[**post_externalcontacts_contacts**](#post_externalcontacts_contacts) | Create an external contact|
|[**post_externalcontacts_contacts_enrich**](#post_externalcontacts_contacts_enrich) | Modify or create an External Contact, with powerful behaviors for finding and combining data with pre-existing Contacts.|
|[**post_externalcontacts_contacts_exports**](#post_externalcontacts_contacts_exports) | Create bulk export|
|[**post_externalcontacts_contacts_merge**](#post_externalcontacts_contacts_merge) | Merge up to 25 contacts into a new contact record|
|[**post_externalcontacts_contacts_schemas**](#post_externalcontacts_contacts_schemas) | Create a schema|
|[**post_externalcontacts_externalsources**](#post_externalcontacts_externalsources) | Create an External Source|
|[**post_externalcontacts_identifierlookup**](#post_externalcontacts_identifierlookup) | Fetch a contact using an identifier type and value.|
|[**post_externalcontacts_identifierlookup_contacts**](#post_externalcontacts_identifierlookup_contacts) | Fetch a contact using an identifier type and value.|
|[**post_externalcontacts_identifierlookup_organizations**](#post_externalcontacts_identifierlookup_organizations) | Fetch an external organization using an identifier type and value.|
|[**post_externalcontacts_import_csv_jobs**](#post_externalcontacts_import_csv_jobs) | Create CSV import job|
|[**post_externalcontacts_import_csv_settings**](#post_externalcontacts_import_csv_settings) | Create settings for CSV import|
|[**post_externalcontacts_import_csv_uploads**](#post_externalcontacts_import_csv_uploads) | Get url for CSV upload|
|[**post_externalcontacts_import_jobs**](#post_externalcontacts_import_jobs) | Create a new job|
|[**post_externalcontacts_import_settings**](#post_externalcontacts_import_settings) | Create a new settings|
|[**post_externalcontacts_merge_contacts**](#post_externalcontacts_merge_contacts) | Merge two contacts into a new contact record|
|[**post_externalcontacts_organization_notes**](#post_externalcontacts_organization_notes) | Create a note for an external organization|
|[**post_externalcontacts_organizations**](#post_externalcontacts_organizations) | Create an external organization|
|[**post_externalcontacts_organizations_enrich**](#post_externalcontacts_organizations_enrich) | Modify or create an External Org, with powerful behaviors for finding and combining data with pre-existing External Orgs.|
|[**post_externalcontacts_organizations_schemas**](#post_externalcontacts_organizations_schemas) | Create a schema|
|[**post_externalcontacts_relationships**](#post_externalcontacts_relationships) | Create a relationship|
|[**put_externalcontacts_contact**](#put_externalcontacts_contact) | Update an external contact|
|[**put_externalcontacts_contact_note**](#put_externalcontacts_contact_note) | Update a note for an external contact|
|[**put_externalcontacts_contacts_schema**](#put_externalcontacts_contacts_schema) | Update a schema|
|[**put_externalcontacts_conversation**](#put_externalcontacts_conversation) | Associate/disassociate an external contact with a conversation|
|[**put_externalcontacts_externalsource**](#put_externalcontacts_externalsource) | Update an External Source|
|[**put_externalcontacts_import_csv_setting**](#put_externalcontacts_import_csv_setting) | Update settings for CSV import|
|[**put_externalcontacts_import_job**](#put_externalcontacts_import_job) | Update Job&#39;s workflow status|
|[**put_externalcontacts_import_setting**](#put_externalcontacts_import_setting) | Update settings|
|[**put_externalcontacts_organization**](#put_externalcontacts_organization) | Update an external organization|
|[**put_externalcontacts_organization_note**](#put_externalcontacts_organization_note) | Update a note for an external organization|
|[**put_externalcontacts_organization_trustor_trustor_id**](#put_externalcontacts_organization_trustor_trustor_id) | Links a Trustor with an External Organization|
|[**put_externalcontacts_organizations_schema**](#put_externalcontacts_organizations_schema) | Update a schema|
|[**put_externalcontacts_relationship**](#put_externalcontacts_relationship) | Update a relationship|



## delete_externalcontacts_contact

> object** delete_externalcontacts_contact(contact_id)


Delete an external contact

Wraps DELETE /api/v2/externalcontacts/contacts/{contactId} 

Requires ANY permissions: 

* relate:contact:delete
* externalContacts:contact:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID

try:
    # Delete an external contact
    api_response = api_instance.delete_externalcontacts_contact(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_contact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |

### Return type

**object**


## delete_externalcontacts_contact_note

> object** delete_externalcontacts_contact_note(contact_id, note_id)


Delete a note for an external contact

Wraps DELETE /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

Requires ANY permissions: 

* relate:contact:edit
* externalContacts:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact Id
note_id = 'note_id_example' # str | Note Id

try:
    # Delete a note for an external contact
    api_response = api_instance.delete_externalcontacts_contact_note(contact_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_contact_note: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **note_id** | **str**| Note Id |  |

### Return type

**object**


## delete_externalcontacts_contacts_schema

>  delete_externalcontacts_contacts_schema(schema_id)


Delete a schema

Wraps DELETE /api/v2/externalcontacts/contacts/schemas/{schemaId} 

Requires ANY permissions: 

* externalContacts:customFields:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Delete a schema
    api_instance.delete_externalcontacts_contacts_schema(schema_id)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_contacts_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

void (empty response body)


## delete_externalcontacts_externalsource

> object** delete_externalcontacts_externalsource(external_source_id)


Delete an External Source. WARNING: Any records that reference this External Source will not be automatically cleaned up. Those records will still be editable, but their External IDs may not be fully viewable.

Wraps DELETE /api/v2/externalcontacts/externalsources/{externalSourceId} 

Requires ANY permissions: 

* externalContacts:externalSource:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_source_id = 'external_source_id_example' # str | External Source ID

try:
    # Delete an External Source. WARNING: Any records that reference this External Source will not be automatically cleaned up. Those records will still be editable, but their External IDs may not be fully viewable.
    api_response = api_instance.delete_externalcontacts_externalsource(external_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_externalsource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_source_id** | **str**| External Source ID |  |

### Return type

**object**


## delete_externalcontacts_import_csv_setting

>  delete_externalcontacts_import_csv_setting(settings_id)


Delete settings for CSV import

Wraps DELETE /api/v2/externalcontacts/import/csv/settings/{settingsId} 

Requires ANY permissions: 

* externalContacts:importCsvSettings:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
settings_id = 'settings_id_example' # str | Settings id

try:
    # Delete settings for CSV import
    api_instance.delete_externalcontacts_import_csv_setting(settings_id)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_import_csv_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings id |  |

### Return type

void (empty response body)


## delete_externalcontacts_import_setting

>  delete_externalcontacts_import_setting(settings_id)


Delete Settings

Wraps DELETE /api/v2/externalcontacts/import/settings/{settingsId} 

Requires ANY permissions: 

* externalContacts:importSettings:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
settings_id = 'settings_id_example' # str | Settings id

try:
    # Delete Settings
    api_instance.delete_externalcontacts_import_setting(settings_id)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_import_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings id |  |

### Return type

void (empty response body)


## delete_externalcontacts_organization

> object** delete_externalcontacts_organization(external_organization_id)


Delete an external organization

Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId} 

Requires ANY permissions: 

* relate:externalOrganization:delete
* externalContacts:externalOrganization:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID

try:
    # Delete an external organization
    api_response = api_instance.delete_externalcontacts_organization(external_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_organization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |

### Return type

**object**


## delete_externalcontacts_organization_note

> object** delete_externalcontacts_organization_note(external_organization_id, note_id)


Delete a note for an external organization

Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization Id
note_id = 'note_id_example' # str | Note Id

try:
    # Delete a note for an external organization
    api_response = api_instance.delete_externalcontacts_organization_note(external_organization_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_organization_note: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **note_id** | **str**| Note Id |  |

### Return type

**object**


## delete_externalcontacts_organization_trustor

>  delete_externalcontacts_organization_trustor(external_organization_id)


Unlink the Trustor for this External Organization

Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId}/trustor 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID

try:
    # Unlink the Trustor for this External Organization
    api_instance.delete_externalcontacts_organization_trustor(external_organization_id)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_organization_trustor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |

### Return type

void (empty response body)


## delete_externalcontacts_relationship

> object** delete_externalcontacts_relationship(relationship_id)


Delete a relationship

Wraps DELETE /api/v2/externalcontacts/relationships/{relationshipId} 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
relationship_id = 'relationship_id_example' # str | Relationship Id

try:
    # Delete a relationship
    api_response = api_instance.delete_externalcontacts_relationship(relationship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->delete_externalcontacts_relationship: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **relationship_id** | **str**| Relationship Id |  |

### Return type

**object**


## get_externalcontacts_contact

> [**ExternalContact**](ExternalContact) get_externalcontacts_contact(contact_id, expand=expand)


Fetch an external contact

Wraps GET /api/v2/externalcontacts/contacts/{contactId} 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Fetch an external contact
    api_response = api_instance.get_externalcontacts_contact(contact_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources, identifiers, externalSources, division |

### Return type

[**ExternalContact**](ExternalContact)


## get_externalcontacts_contact_identifiers

> [**ContactIdentifierListing**](ContactIdentifierListing) get_externalcontacts_contact_identifiers(contact_id)


List the identifiers for a contact

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/identifiers 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID

try:
    # List the identifiers for a contact
    api_response = api_instance.get_externalcontacts_contact_identifiers(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact_identifiers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |

### Return type

[**ContactIdentifierListing**](ContactIdentifierListing)


## get_externalcontacts_contact_journey_segments

> [**SegmentAssignmentListing**](SegmentAssignmentListing) get_externalcontacts_contact_journey_segments(contact_id, include_merged=include_merged, limit=limit)


Retrieve segment assignments by external contact ID.

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/journey/segments 

Requires ANY permissions: 

* externalContacts:segmentAssignment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
include_merged = True # bool | Indicates whether to return segment assignments from all external contacts in the merge-set of the given one. (optional)
limit = 56 # int | Number of entities to return. Default of 25, maximum of 500. (optional)

try:
    # Retrieve segment assignments by external contact ID.
    api_response = api_instance.get_externalcontacts_contact_journey_segments(contact_id, include_merged=include_merged, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **include_merged** | **bool**| Indicates whether to return segment assignments from all external contacts in the merge-set of the given one. | [optional]  |
| **limit** | **int**| Number of entities to return. Default of 25, maximum of 500. | [optional]  |

### Return type

[**SegmentAssignmentListing**](SegmentAssignmentListing)


## get_externalcontacts_contact_journey_sessions

> [**SessionListing**](SessionListing) get_externalcontacts_contact_journey_sessions(contact_id, page_size=page_size, after=after, include_merged=include_merged)


Retrieve all sessions for a given external contact.

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/journey/sessions 

Requires ANY permissions: 

* externalContacts:session:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
include_merged = True # bool | Indicates whether to return sessions from all external contacts in the merge-set of the given one. (optional)

try:
    # Retrieve all sessions for a given external contact.
    api_response = api_instance.get_externalcontacts_contact_journey_sessions(contact_id, page_size=page_size, after=after, include_merged=include_merged)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact_journey_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **include_merged** | **bool**| Indicates whether to return sessions from all external contacts in the merge-set of the given one. | [optional]  |

### Return type

[**SessionListing**](SessionListing)


## get_externalcontacts_contact_note

> [**Note**](Note) get_externalcontacts_contact_note(contact_id, note_id, expand=expand)


Fetch a note for an external contact

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact Id
note_id = 'note_id_example' # str | Note Id
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Fetch a note for an external contact
    api_response = api_instance.get_externalcontacts_contact_note(contact_id, note_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact_note: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **note_id** | **str**| Note Id |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources, division |

### Return type

[**Note**](Note)


## get_externalcontacts_contact_notes

> [**NoteListing**](NoteListing) get_externalcontacts_contact_notes(contact_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)


List notes for an external contact

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/notes 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact Id
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
sort_order = 'sort_order_example' # str | The Note field to sort by. Any of: [createDate]. Direction: [asc, desc].  e.g. \"createDate:asc\", \"createDate:desc\" (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # List notes for an external contact
    api_response = api_instance.get_externalcontacts_contact_notes(contact_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 1] |
| **sort_order** | **str**| The Note field to sort by. Any of: [createDate]. Direction: [asc, desc].  e.g. \&quot;createDate:asc\&quot;, \&quot;createDate:desc\&quot; | [optional]  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources, division |

### Return type

[**NoteListing**](NoteListing)


## get_externalcontacts_contact_unresolved

> [**ExternalContact**](ExternalContact) get_externalcontacts_contact_unresolved(contact_id, expand=expand)


Fetch an unresolved external contact

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/unresolved 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Fetch an unresolved external contact
    api_response = api_instance.get_externalcontacts_contact_unresolved(contact_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contact_unresolved: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources, identifiers, division |

### Return type

[**ExternalContact**](ExternalContact)


## get_externalcontacts_contacts

> [**ContactListing**](ContactListing) get_externalcontacts_contacts(page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand, division_ids=division_ids)


Search for external contacts

Wraps GET /api/v2/externalcontacts/contacts 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
q = 'q_example' # str | User supplied search keywords (no special syntax is currently supported) (optional)
sort_order = 'sort_order_example' # str | The External Contact field to sort by. Any of: [firstName, lastName, middleName, title]. Direction: [asc, desc]. e.g. \"firstName:asc\", \"title:desc\" (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
division_ids = ['division_ids_example'] # list[str] | which divisions to search, up to 50 (optional)

try:
    # Search for external contacts
    api_response = api_instance.get_externalcontacts_contacts(page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 1] |
| **q** | **str**| User supplied search keywords (no special syntax is currently supported) | [optional]  |
| **sort_order** | **str**| The External Contact field to sort by. Any of: [firstName, lastName, middleName, title]. Direction: [asc, desc]. e.g. \&quot;firstName:asc\&quot;, \&quot;title:desc\&quot; | [optional]  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources, identifiers, externalSources, division |
| **division_ids** | [**list[str]**](str)| which divisions to search, up to 50 | [optional]  |

### Return type

[**ContactListing**](ContactListing)


## get_externalcontacts_contacts_export

> [**ContactsExport**](ContactsExport) get_externalcontacts_contacts_export(export_id)


Get export for exportId

Wraps GET /api/v2/externalcontacts/contacts/exports/{exportId} 

Requires ALL permissions: 

* externalContacts:export:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
export_id = 'export_id_example' # str | Export id

try:
    # Get export for exportId
    api_response = api_instance.get_externalcontacts_contacts_export(export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **export_id** | **str**| Export id |  |

### Return type

[**ContactsExport**](ContactsExport)


## get_externalcontacts_contacts_exports

> [**ExportListing**](ExportListing) get_externalcontacts_contacts_exports(division_ids=division_ids, after=after, page_size=page_size)


List exports for organization

Wraps GET /api/v2/externalcontacts/contacts/exports 

Requires ALL permissions: 

* externalContacts:export:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
division_ids = ['division_ids_example'] # list[str] | Division IDs of entities (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities (optional)
page_size = 56 # int | Number of entities to return (optional)

try:
    # List exports for organization
    api_response = api_instance.get_externalcontacts_contacts_exports(division_ids=division_ids, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_exports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_ids** | [**list[str]**](str)| Division IDs of entities | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities | [optional]  |
| **page_size** | **int**| Number of entities to return | [optional]  |

### Return type

[**ExportListing**](ExportListing)


## get_externalcontacts_contacts_schema

> [**DataSchema**](DataSchema) get_externalcontacts_contacts_schema(schema_id)


Get a schema

Wraps GET /api/v2/externalcontacts/contacts/schemas/{schemaId} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get a schema
    api_response = api_instance.get_externalcontacts_contacts_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**DataSchema**](DataSchema)


## get_externalcontacts_contacts_schema_version

> [**DataSchema**](DataSchema) get_externalcontacts_contacts_schema_version(schema_id, version_id)


Get a specific version of a schema

Wraps GET /api/v2/externalcontacts/contacts/schemas/{schemaId}/versions/{versionId} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID
version_id = 'version_id_example' # str | Schema version

try:
    # Get a specific version of a schema
    api_response = api_instance.get_externalcontacts_contacts_schema_version(schema_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schema_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **version_id** | **str**| Schema version |  |

### Return type

[**DataSchema**](DataSchema)


## get_externalcontacts_contacts_schema_versions

> [**DataSchemaListing**](DataSchemaListing) get_externalcontacts_contacts_schema_versions(schema_id)


Get all versions of an external contact's schema

Wraps GET /api/v2/externalcontacts/contacts/schemas/{schemaId}/versions 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get all versions of an external contact's schema
    api_response = api_instance.get_externalcontacts_contacts_schema_versions(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schema_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**DataSchemaListing**](DataSchemaListing)


## get_externalcontacts_contacts_schemas

> [**DataSchemaListing**](DataSchemaListing) get_externalcontacts_contacts_schemas()


Get a list of schemas.

Wraps GET /api/v2/externalcontacts/contacts/schemas 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()

try:
    # Get a list of schemas.
    api_response = api_instance.get_externalcontacts_contacts_schemas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schemas: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataSchemaListing**](DataSchemaListing)


## get_externalcontacts_contacts_schemas_coretype

> [**Coretype**](Coretype) get_externalcontacts_contacts_schemas_coretype(core_type_name)


Get a specific named core type.

Wraps GET /api/v2/externalcontacts/contacts/schemas/coretypes/{coreTypeName} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
core_type_name = 'core_type_name_example' # str | Name of the core type

try:
    # Get a specific named core type.
    api_response = api_instance.get_externalcontacts_contacts_schemas_coretype(core_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schemas_coretype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **core_type_name** | **str**| Name of the core type |  |

### Return type

[**Coretype**](Coretype)


## get_externalcontacts_contacts_schemas_coretypes

> [**CoretypeListing**](CoretypeListing) get_externalcontacts_contacts_schemas_coretypes()


Get the core types from which all schemas are built.

Wraps GET /api/v2/externalcontacts/contacts/schemas/coretypes 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()

try:
    # Get the core types from which all schemas are built.
    api_response = api_instance.get_externalcontacts_contacts_schemas_coretypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schemas_coretypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CoretypeListing**](CoretypeListing)


## get_externalcontacts_contacts_schemas_limits

> [**SchemaQuantityLimits**](SchemaQuantityLimits) get_externalcontacts_contacts_schemas_limits()


Get quantitative limits on schemas

Wraps GET /api/v2/externalcontacts/contacts/schemas/limits 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()

try:
    # Get quantitative limits on schemas
    api_response = api_instance.get_externalcontacts_contacts_schemas_limits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_contacts_schemas_limits: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SchemaQuantityLimits**](SchemaQuantityLimits)


## get_externalcontacts_externalsource

> [**ExternalSource**](ExternalSource) get_externalcontacts_externalsource(external_source_id)


Fetch an External Source

Wraps GET /api/v2/externalcontacts/externalsources/{externalSourceId} 

Requires ANY permissions: 

* externalContacts:externalSource:view
* externalContacts:contact:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_source_id = 'external_source_id_example' # str | External Source ID

try:
    # Fetch an External Source
    api_response = api_instance.get_externalcontacts_externalsource(external_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_externalsource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_source_id** | **str**| External Source ID |  |

### Return type

[**ExternalSource**](ExternalSource)


## get_externalcontacts_externalsources

> [**CursorExternalSourceListing**](CursorExternalSourceListing) get_externalcontacts_externalsources(cursor=cursor, limit=limit, name=name, active=active)


Fetch a list of External Sources

Wraps GET /api/v2/externalcontacts/externalsources 

Requires ANY permissions: 

* externalContacts:externalSource:view
* externalContacts:contact:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)
limit = 56 # int | The number of ExternalSources per page; must be between 10 and 200, default is 100 (optional)
name = 'name_example' # str | Filter by external source name. Filtering is prefix filtering and not an exact match (optional)
active = True # bool | Filter by active status of external source (optional)

try:
    # Fetch a list of External Sources
    api_response = api_instance.get_externalcontacts_externalsources(cursor=cursor, limit=limit, name=name, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_externalsources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
| **limit** | **int**| The number of ExternalSources per page; must be between 10 and 200, default is 100 | [optional]  |
| **name** | **str**| Filter by external source name. Filtering is prefix filtering and not an exact match | [optional]  |
| **active** | **bool**| Filter by active status of external source | [optional]  |

### Return type

[**CursorExternalSourceListing**](CursorExternalSourceListing)


## get_externalcontacts_import_csv_setting

> [**CsvSettings**](CsvSettings) get_externalcontacts_import_csv_setting(settings_id)


Get settings for CSV import

Wraps GET /api/v2/externalcontacts/import/csv/settings/{settingsId} 

Requires ANY permissions: 

* externalContacts:importCsvSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
settings_id = 'settings_id_example' # str | Settings id

try:
    # Get settings for CSV import
    api_response = api_instance.get_externalcontacts_import_csv_setting(settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_csv_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings id |  |

### Return type

[**CsvSettings**](CsvSettings)


## get_externalcontacts_import_csv_settings

> [**Listing**](Listing) get_externalcontacts_import_csv_settings(after=after, page_size=page_size, external_settings_id=external_settings_id)


Retrieve all settings for organization filtered by externalSettingsId if provided

Wraps GET /api/v2/externalcontacts/import/csv/settings 

Requires ANY permissions: 

* externalContacts:importCsvSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
external_settings_id = 'external_settings_id_example' # str | External Settings Id to filter the list. (optional)

try:
    # Retrieve all settings for organization filtered by externalSettingsId if provided
    api_response = api_instance.get_externalcontacts_import_csv_settings(after=after, page_size=page_size, external_settings_id=external_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_csv_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **external_settings_id** | **str**| External Settings Id to filter the list. | [optional]  |

### Return type

[**Listing**](Listing)


## get_externalcontacts_import_csv_upload_details

> [**CsvUploadDetailsResponse**](CsvUploadDetailsResponse) get_externalcontacts_import_csv_upload_details(upload_id)


Get details for CSV upload

Wraps GET /api/v2/externalcontacts/import/csv/uploads/{uploadId}/details 

Requires ANY permissions: 

* externalContacts:importCsvUpload:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
upload_id = 'upload_id_example' # str | Upload id

try:
    # Get details for CSV upload
    api_response = api_instance.get_externalcontacts_import_csv_upload_details(upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_csv_upload_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **upload_id** | **str**| Upload id |  |

### Return type

[**CsvUploadDetailsResponse**](CsvUploadDetailsResponse)


## get_externalcontacts_import_csv_upload_preview

> [**CsvUploadPreviewResponse**](CsvUploadPreviewResponse) get_externalcontacts_import_csv_upload_preview(upload_id)


Get preview for CSV upload

Wraps GET /api/v2/externalcontacts/import/csv/uploads/{uploadId}/preview 

Requires ANY permissions: 

* externalContacts:importCsvUpload:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
upload_id = 'upload_id_example' # str | Upload id

try:
    # Get preview for CSV upload
    api_response = api_instance.get_externalcontacts_import_csv_upload_preview(upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_csv_upload_preview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **upload_id** | **str**| Upload id |  |

### Return type

[**CsvUploadPreviewResponse**](CsvUploadPreviewResponse)


## get_externalcontacts_import_job

> [**ContactImportJobResponse**](ContactImportJobResponse) get_externalcontacts_import_job(job_id, expand=expand)


Get job based on id

Wraps GET /api/v2/externalcontacts/import/jobs/{jobId} 

Requires ANY permissions: 

* externalContacts:importJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
job_id = 'job_id_example' # str | Job id
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Get job based on id
    api_response = api_instance.get_externalcontacts_import_job(job_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Job id |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: division |

### Return type

[**ContactImportJobResponse**](ContactImportJobResponse)


## get_externalcontacts_import_jobs

> [**ContactImportJobEntityListing**](ContactImportJobEntityListing) get_externalcontacts_import_jobs(expand=expand, after=after, page_size=page_size, sort_order=sort_order, job_status=job_status)


List jobs for organization

Wraps GET /api/v2/externalcontacts/import/jobs 

Requires ANY permissions: 

* externalContacts:importJob:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = ''25'' # str | Number of entities to return. Maximum of 100. (optional) (default to '25')
sort_order = ''Ascending'' # str | Direction of sorting. (optional) (default to 'Ascending')
job_status = 'job_status_example' # str | Search term to filter by jobStatus (optional)

try:
    # List jobs for organization
    api_response = api_instance.get_externalcontacts_import_jobs(expand=expand, after=after, page_size=page_size, sort_order=sort_order, job_status=job_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: division |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. | [optional] [default to &#39;25&#39;] |
| **sort_order** | **str**| Direction of sorting. | [optional] [default to &#39;Ascending&#39;]<br />**Values**: Ascending, Descending |
| **job_status** | **str**| Search term to filter by jobStatus | [optional] <br />**Values**: Created, Running, Completed, Failed, Cancelled |

### Return type

[**ContactImportJobEntityListing**](ContactImportJobEntityListing)


## get_externalcontacts_import_setting

> [**ContactImportSettings**](ContactImportSettings) get_externalcontacts_import_setting(settings_id)


Get setting based on id

Wraps GET /api/v2/externalcontacts/import/settings/{settingsId} 

Requires ANY permissions: 

* externalContacts:importSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
settings_id = 'settings_id_example' # str | Settings id

try:
    # Get setting based on id
    api_response = api_instance.get_externalcontacts_import_setting(settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings id |  |

### Return type

[**ContactImportSettings**](ContactImportSettings)


## get_externalcontacts_import_settings

> [**ContactImportSettingsEntityListing**](ContactImportSettingsEntityListing) get_externalcontacts_import_settings(after=after, page_size=page_size, sort_order=sort_order, name=name)


List settings for organization

Wraps GET /api/v2/externalcontacts/import/settings 

Requires ANY permissions: 

* externalContacts:importSettings:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = ''25'' # str | Number of entities to return. Maximum of 100. (optional) (default to '25')
sort_order = ''Ascending'' # str | Direction of sorting. (optional) (default to 'Ascending')
name = 'name_example' # str | Search term to filter by settings name (optional)

try:
    # List settings for organization
    api_response = api_instance.get_externalcontacts_import_settings(after=after, page_size=page_size, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_import_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. | [optional] [default to &#39;25&#39;] |
| **sort_order** | **str**| Direction of sorting. | [optional] [default to &#39;Ascending&#39;]<br />**Values**: Ascending, Descending |
| **name** | **str**| Search term to filter by settings name | [optional]  |

### Return type

[**ContactImportSettingsEntityListing**](ContactImportSettingsEntityListing)


## get_externalcontacts_organization

> [**ExternalOrganization**](ExternalOrganization) get_externalcontacts_organization(external_organization_id, expand=expand, include_trustors=include_trustors)


Fetch an external organization

Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId} 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
include_trustors = True # bool | (true or false) whether or not to include trustor information embedded in the externalOrganization (optional)

try:
    # Fetch an external organization
    api_response = api_instance.get_externalcontacts_organization(external_organization_id, expand=expand, include_trustors=include_trustors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources, division, identifiers, externalSources |
| **include_trustors** | **bool**| (true or false) whether or not to include trustor information embedded in the externalOrganization | [optional]  |

### Return type

[**ExternalOrganization**](ExternalOrganization)


## get_externalcontacts_organization_contacts

> [**ContactListing**](ContactListing) get_externalcontacts_organization_contacts(external_organization_id, page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand)


Search for external contacts in an external organization

Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/contacts 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
q = 'q_example' # str | User supplied search keywords (no special syntax is currently supported) (optional)
sort_order = 'sort_order_example' # str | The External Contact field to sort by. Any of: [firstName, lastName, middleName, title]. Direction: [asc, desc]. e.g. \"firstName:asc\", \"title:desc\" (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Search for external contacts in an external organization
    api_response = api_instance.get_externalcontacts_organization_contacts(external_organization_id, page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organization_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 1] |
| **q** | **str**| User supplied search keywords (no special syntax is currently supported) | [optional]  |
| **sort_order** | **str**| The External Contact field to sort by. Any of: [firstName, lastName, middleName, title]. Direction: [asc, desc]. e.g. \&quot;firstName:asc\&quot;, \&quot;title:desc\&quot; | [optional]  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources, identifiers, externalSources, division |

### Return type

[**ContactListing**](ContactListing)


## get_externalcontacts_organization_identifiers

> [**ExternalOrganizationIdentifierListing**](ExternalOrganizationIdentifierListing) get_externalcontacts_organization_identifiers(external_organization_id)


List the identifiers for an external organization

Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/identifiers 

Requires ANY permissions: 

* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID

try:
    # List the identifiers for an external organization
    api_response = api_instance.get_externalcontacts_organization_identifiers(external_organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organization_identifiers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |

### Return type

[**ExternalOrganizationIdentifierListing**](ExternalOrganizationIdentifierListing)


## get_externalcontacts_organization_note

> [**Note**](Note) get_externalcontacts_organization_note(external_organization_id, note_id, expand=expand)


Fetch a note for an external organization

Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization Id
note_id = 'note_id_example' # str | Note Id
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Fetch a note for an external organization
    api_response = api_instance.get_externalcontacts_organization_note(external_organization_id, note_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organization_note: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **note_id** | **str**| Note Id |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources, division |

### Return type

[**Note**](Note)


## get_externalcontacts_organization_notes

> [**NoteListing**](NoteListing) get_externalcontacts_organization_notes(external_organization_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)


List notes for an external organization

Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization Id
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
sort_order = 'sort_order_example' # str | The Note field to sort by. Any of: [createDate]. Direction: [asc, desc]. e.g. \"createDate:asc\", \"createDate:desc\" (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # List notes for an external organization
    api_response = api_instance.get_externalcontacts_organization_notes(external_organization_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organization_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 1] |
| **sort_order** | **str**| The Note field to sort by. Any of: [createDate]. Direction: [asc, desc]. e.g. \&quot;createDate:asc\&quot;, \&quot;createDate:desc\&quot; | [optional]  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources, division |

### Return type

[**NoteListing**](NoteListing)


## get_externalcontacts_organization_relationships

> [**RelationshipListing**](RelationshipListing) get_externalcontacts_organization_relationships(external_organization_id, page_size=page_size, page_number=page_number, expand=expand, sort_order=sort_order)


Fetch a relationship for an external organization

Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/relationships 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
sort_order = 'sort_order_example' # str | The Relationship field to sort by. Any of: [createDate, relationship]. Direction: [asc, desc]. e.g. \"createDate:asc\", \"relationship:desc\" (optional)

try:
    # Fetch a relationship for an external organization
    api_response = api_instance.get_externalcontacts_organization_relationships(external_organization_id, page_size=page_size, page_number=page_number, expand=expand, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organization_relationships: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 1] |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources, division |
| **sort_order** | **str**| The Relationship field to sort by. Any of: [createDate, relationship]. Direction: [asc, desc]. e.g. \&quot;createDate:asc\&quot;, \&quot;relationship:desc\&quot; | [optional]  |

### Return type

[**RelationshipListing**](RelationshipListing)


## get_externalcontacts_organizations

> [**ExternalOrganizationListing**](ExternalOrganizationListing) get_externalcontacts_organizations(page_size=page_size, page_number=page_number, q=q, trustor_id=trustor_id, sort_order=sort_order, expand=expand, include_trustors=include_trustors, division_ids=division_ids)


Search for external organizations

Wraps GET /api/v2/externalcontacts/organizations 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
q = 'q_example' # str | Search query (optional)
trustor_id = ['trustor_id_example'] # list[str] | Search for external organizations by trustorIds (limit 25). If supplied, the 'q' parameters is ignored. Items are returned in the order requested (optional)
sort_order = 'sort_order_example' # str | The Organization field to sort by. Any of: [companyType, industry, name]. Direction: [asc, desc]. e.g. \"companyType:asc\", \"industry:desc\" (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
include_trustors = True # bool | (true or false) whether or not to include trustor information embedded in the externalOrganization (optional)
division_ids = ['division_ids_example'] # list[str] | which divisions to search, up to 50 (optional)

try:
    # Search for external organizations
    api_response = api_instance.get_externalcontacts_organizations(page_size=page_size, page_number=page_number, q=q, trustor_id=trustor_id, sort_order=sort_order, expand=expand, include_trustors=include_trustors, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;&#x3D; 1,000) | [optional] [default to 1] |
| **q** | **str**| Search query | [optional]  |
| **trustor_id** | [**list[str]**](str)| Search for external organizations by trustorIds (limit 25). If supplied, the &#39;q&#39; parameters is ignored. Items are returned in the order requested | [optional]  |
| **sort_order** | **str**| The Organization field to sort by. Any of: [companyType, industry, name]. Direction: [asc, desc]. e.g. \&quot;companyType:asc\&quot;, \&quot;industry:desc\&quot; | [optional]  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources, division, identifiers, externalSources |
| **include_trustors** | **bool**| (true or false) whether or not to include trustor information embedded in the externalOrganization | [optional]  |
| **division_ids** | [**list[str]**](str)| which divisions to search, up to 50 | [optional]  |

### Return type

[**ExternalOrganizationListing**](ExternalOrganizationListing)


## get_externalcontacts_organizations_schema

> [**DataSchema**](DataSchema) get_externalcontacts_organizations_schema(schema_id)


Get a schema

Wraps GET /api/v2/externalcontacts/organizations/schemas/{schemaId} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get a schema
    api_response = api_instance.get_externalcontacts_organizations_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**DataSchema**](DataSchema)


## get_externalcontacts_organizations_schema_version

> [**DataSchema**](DataSchema) get_externalcontacts_organizations_schema_version(schema_id, version_id)


Get a specific version of a schema

Wraps GET /api/v2/externalcontacts/organizations/schemas/{schemaId}/versions/{versionId} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID
version_id = 'version_id_example' # str | Schema version

try:
    # Get a specific version of a schema
    api_response = api_instance.get_externalcontacts_organizations_schema_version(schema_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schema_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **version_id** | **str**| Schema version |  |

### Return type

[**DataSchema**](DataSchema)


## get_externalcontacts_organizations_schema_versions

> [**DataSchemaListing**](DataSchemaListing) get_externalcontacts_organizations_schema_versions(schema_id)


Get all versions of an external organization's schema

Wraps GET /api/v2/externalcontacts/organizations/schemas/{schemaId}/versions 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get all versions of an external organization's schema
    api_response = api_instance.get_externalcontacts_organizations_schema_versions(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schema_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |

### Return type

[**DataSchemaListing**](DataSchemaListing)


## get_externalcontacts_organizations_schemas

> [**DataSchemaListing**](DataSchemaListing) get_externalcontacts_organizations_schemas()


Get a list of schemas.

Wraps GET /api/v2/externalcontacts/organizations/schemas 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()

try:
    # Get a list of schemas.
    api_response = api_instance.get_externalcontacts_organizations_schemas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schemas: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataSchemaListing**](DataSchemaListing)


## get_externalcontacts_organizations_schemas_coretype

> [**Coretype**](Coretype) get_externalcontacts_organizations_schemas_coretype(core_type_name)


Get a specific named core type.

Wraps GET /api/v2/externalcontacts/organizations/schemas/coretypes/{coreTypeName} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
core_type_name = 'core_type_name_example' # str | Name of the core type

try:
    # Get a specific named core type.
    api_response = api_instance.get_externalcontacts_organizations_schemas_coretype(core_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schemas_coretype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **core_type_name** | **str**| Name of the core type |  |

### Return type

[**Coretype**](Coretype)


## get_externalcontacts_organizations_schemas_coretypes

> [**CoretypeListing**](CoretypeListing) get_externalcontacts_organizations_schemas_coretypes()


Get the core types from which all schemas are built.

Wraps GET /api/v2/externalcontacts/organizations/schemas/coretypes 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()

try:
    # Get the core types from which all schemas are built.
    api_response = api_instance.get_externalcontacts_organizations_schemas_coretypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schemas_coretypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CoretypeListing**](CoretypeListing)


## get_externalcontacts_organizations_schemas_limits

> [**SchemaQuantityLimits**](SchemaQuantityLimits) get_externalcontacts_organizations_schemas_limits()


Get quantitative limits on schemas

Wraps GET /api/v2/externalcontacts/organizations/schemas/limits 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()

try:
    # Get quantitative limits on schemas
    api_response = api_instance.get_externalcontacts_organizations_schemas_limits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_organizations_schemas_limits: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SchemaQuantityLimits**](SchemaQuantityLimits)


## get_externalcontacts_relationship

> [**Relationship**](Relationship) get_externalcontacts_relationship(relationship_id, expand=expand)


Fetch a relationship

Wraps GET /api/v2/externalcontacts/relationships/{relationshipId} 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
relationship_id = 'relationship_id_example' # str | Relationship Id
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Fetch a relationship
    api_response = api_instance.get_externalcontacts_relationship(relationship_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_relationship: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **relationship_id** | **str**| Relationship Id |  |
| **expand** | [**list[str]**](str)| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources, division |

### Return type

[**Relationship**](Relationship)


## get_externalcontacts_reversewhitepageslookup

> [**ReverseWhitepagesLookupResult**](ReverseWhitepagesLookupResult) get_externalcontacts_reversewhitepageslookup(lookup_val, expand=expand, division_id=division_id)


Look up contacts based on an attribute. Maximum of 25 values returned.

Wraps GET /api/v2/externalcontacts/reversewhitepageslookup 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
lookup_val = 'lookup_val_example' # str | User supplied value to lookup contacts (supports email addresses, e164 phone numbers, Twitter screen names)
expand = ['expand_example'] # list[str] | which field, if any, to expand (optional)
division_id = ''*'' # str | Specifies which division to lookup contacts in, for the given lookup value (optional) (default to '*')

try:
    # Look up contacts based on an attribute. Maximum of 25 values returned.
    api_response = api_instance.get_externalcontacts_reversewhitepageslookup(lookup_val, expand=expand, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_reversewhitepageslookup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **lookup_val** | **str**| User supplied value to lookup contacts (supports email addresses, e164 phone numbers, Twitter screen names) |  |
| **expand** | [**list[str]**](str)| which field, if any, to expand | [optional] <br />**Values**: contacts.externalOrganization, externalDataSources, division |
| **division_id** | **str**| Specifies which division to lookup contacts in, for the given lookup value | [optional] [default to &#39;*&#39;] |

### Return type

[**ReverseWhitepagesLookupResult**](ReverseWhitepagesLookupResult)


## get_externalcontacts_scan_contacts

> [**CursorContactListing**](CursorContactListing) get_externalcontacts_scan_contacts(limit=limit, cursor=cursor, division_id=division_id)


Scan for external contacts using paging

Wraps GET /api/v2/externalcontacts/scan/contacts 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of contacts per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)
division_id = ''*'' # str | The division to scan over (optional) (default to '*')

try:
    # Scan for external contacts using paging
    api_response = api_instance.get_externalcontacts_scan_contacts(limit=limit, cursor=cursor, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of contacts per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
| **division_id** | **str**| The division to scan over | [optional] [default to &#39;*&#39;] |

### Return type

[**CursorContactListing**](CursorContactListing)


## get_externalcontacts_scan_contacts_divisionviews_all

> [**CursorContactListing**](CursorContactListing) get_externalcontacts_scan_contacts_divisionviews_all(limit=limit, cursor=cursor)


Scan for external contacts using paging

Wraps GET /api/v2/externalcontacts/scan/contacts/divisionviews/all 

Requires ALL permissions: 

* externalContacts:contact:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of contacts per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for external contacts using paging
    api_response = api_instance.get_externalcontacts_scan_contacts_divisionviews_all(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_contacts_divisionviews_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of contacts per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |

### Return type

[**CursorContactListing**](CursorContactListing)


## get_externalcontacts_scan_notes

> [**CursorNoteListing**](CursorNoteListing) get_externalcontacts_scan_notes(limit=limit, cursor=cursor, division_id=division_id)


Scan for notes using paging

Wraps GET /api/v2/externalcontacts/scan/notes 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of notes per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)
division_id = ''*'' # str | The division to scan over (optional) (default to '*')

try:
    # Scan for notes using paging
    api_response = api_instance.get_externalcontacts_scan_notes(limit=limit, cursor=cursor, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of notes per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
| **division_id** | **str**| The division to scan over | [optional] [default to &#39;*&#39;] |

### Return type

[**CursorNoteListing**](CursorNoteListing)


## get_externalcontacts_scan_notes_divisionviews_all

> [**CursorNoteListing**](CursorNoteListing) get_externalcontacts_scan_notes_divisionviews_all(limit=limit, cursor=cursor)


Scan for notes using paging

Wraps GET /api/v2/externalcontacts/scan/notes/divisionviews/all 

Requires ALL permissions: 

* externalContacts:contact:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of notes per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for notes using paging
    api_response = api_instance.get_externalcontacts_scan_notes_divisionviews_all(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_notes_divisionviews_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of notes per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |

### Return type

[**CursorNoteListing**](CursorNoteListing)


## get_externalcontacts_scan_organizations

> [**CursorOrganizationListing**](CursorOrganizationListing) get_externalcontacts_scan_organizations(limit=limit, cursor=cursor, division_id=division_id)


Scan for external organizations using paging

Wraps GET /api/v2/externalcontacts/scan/organizations 

Requires ANY permissions: 

* relate:externalOrganization:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of organizations per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)
division_id = ''*'' # str | The division to scan over (optional) (default to '*')

try:
    # Scan for external organizations using paging
    api_response = api_instance.get_externalcontacts_scan_organizations(limit=limit, cursor=cursor, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_organizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of organizations per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
| **division_id** | **str**| The division to scan over | [optional] [default to &#39;*&#39;] |

### Return type

[**CursorOrganizationListing**](CursorOrganizationListing)


## get_externalcontacts_scan_organizations_divisionviews_all

> [**CursorOrganizationListing**](CursorOrganizationListing) get_externalcontacts_scan_organizations_divisionviews_all(limit=limit, cursor=cursor)


Scan for external organizations using paging

Wraps GET /api/v2/externalcontacts/scan/organizations/divisionviews/all 

Requires ALL permissions: 

* externalContacts:externalOrganization:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of organizations per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for external organizations using paging
    api_response = api_instance.get_externalcontacts_scan_organizations_divisionviews_all(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_organizations_divisionviews_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of organizations per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |

### Return type

[**CursorOrganizationListing**](CursorOrganizationListing)


## get_externalcontacts_scan_relationships

> [**CursorRelationshipListing**](CursorRelationshipListing) get_externalcontacts_scan_relationships(limit=limit, cursor=cursor, division_id=division_id)


Scan for relationships

Wraps GET /api/v2/externalcontacts/scan/relationships 

Requires ANY permissions: 

* relate:contact:view
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of relationships per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)
division_id = ''*'' # str | The division to scan over (optional) (default to '*')

try:
    # Scan for relationships
    api_response = api_instance.get_externalcontacts_scan_relationships(limit=limit, cursor=cursor, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_relationships: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of relationships per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
| **division_id** | **str**| The division to scan over | [optional] [default to &#39;*&#39;] |

### Return type

[**CursorRelationshipListing**](CursorRelationshipListing)


## get_externalcontacts_scan_relationships_divisionviews_all

> [**CursorRelationshipListing**](CursorRelationshipListing) get_externalcontacts_scan_relationships_divisionviews_all(limit=limit, cursor=cursor)


Scan for relationships

Wraps GET /api/v2/externalcontacts/scan/relationships/divisionviews/all 

Requires ALL permissions: 

* externalContacts:contact:viewAll

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
limit = 56 # int | The number of relationships per page; must be between 10 and 200, default is 100 (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for relationships
    api_response = api_instance.get_externalcontacts_scan_relationships_divisionviews_all(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_relationships_divisionviews_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of relationships per page; must be between 10 and 200, default is 100 | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |

### Return type

[**CursorRelationshipListing**](CursorRelationshipListing)


## patch_externalcontacts_contact_identifiers

> [**ContactIdentifier**](ContactIdentifier) patch_externalcontacts_contact_identifiers(contact_id, body)


Claim or release identifiers for a contact

Wraps PATCH /api/v2/externalcontacts/contacts/{contactId}/identifiers 

Requires ANY permissions: 

* externalContacts:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
body = PureCloudPlatformClientV2.IdentifierClaimRequest() # IdentifierClaimRequest | ClaimRequest

try:
    # Claim or release identifiers for a contact
    api_response = api_instance.patch_externalcontacts_contact_identifiers(contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->patch_externalcontacts_contact_identifiers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **body** | [**IdentifierClaimRequest**](IdentifierClaimRequest)| ClaimRequest |  |

### Return type

[**ContactIdentifier**](ContactIdentifier)


## patch_externalcontacts_organization_identifiers

> [**ExternalOrganizationIdentifier**](ExternalOrganizationIdentifier) patch_externalcontacts_organization_identifiers(external_organization_id, body)


Claim or release identifiers for an external organization

Wraps PATCH /api/v2/externalcontacts/organizations/{externalOrganizationId}/identifiers 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
body = PureCloudPlatformClientV2.ExternalOrganizationIdentifierClaimRequest() # ExternalOrganizationIdentifierClaimRequest | ClaimRequest

try:
    # Claim or release identifiers for an external organization
    api_response = api_instance.patch_externalcontacts_organization_identifiers(external_organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->patch_externalcontacts_organization_identifiers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **body** | [**ExternalOrganizationIdentifierClaimRequest**](ExternalOrganizationIdentifierClaimRequest)| ClaimRequest |  |

### Return type

[**ExternalOrganizationIdentifier**](ExternalOrganizationIdentifier)


## post_externalcontacts_bulk_contacts

> [**BulkFetchContactsResponse**](BulkFetchContactsResponse) post_externalcontacts_bulk_contacts(body)


Bulk fetch contacts

Wraps POST /api/v2/externalcontacts/bulk/contacts 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Contact ids

try:
    # Bulk fetch contacts
    api_response = api_instance.post_externalcontacts_bulk_contacts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Contact ids |  |

### Return type

[**BulkFetchContactsResponse**](BulkFetchContactsResponse)


## post_externalcontacts_bulk_contacts_add

> [**BulkContactsResponse**](BulkContactsResponse) post_externalcontacts_bulk_contacts_add(body)


Bulk add contacts

Wraps POST /api/v2/externalcontacts/bulk/contacts/add 

Requires ANY permissions: 

* externalContacts:contact:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkContactsRequest() # BulkContactsRequest | Contacts

try:
    # Bulk add contacts
    api_response = api_instance.post_externalcontacts_bulk_contacts_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkContactsRequest**](BulkContactsRequest)| Contacts |  |

### Return type

[**BulkContactsResponse**](BulkContactsResponse)


## post_externalcontacts_bulk_contacts_divisionviews

> [**BulkFetchContactsResponse**](BulkFetchContactsResponse) post_externalcontacts_bulk_contacts_divisionviews(body)


Bulk fetch contacts across divisions

Wraps POST /api/v2/externalcontacts/bulk/contacts/divisionviews 

Requires ANY permissions: 

* externalContacts:contact:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Contact ids

try:
    # Bulk fetch contacts across divisions
    api_response = api_instance.post_externalcontacts_bulk_contacts_divisionviews(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Contact ids |  |

### Return type

[**BulkFetchContactsResponse**](BulkFetchContactsResponse)


## post_externalcontacts_bulk_contacts_enrich

> [**BulkContactsEnrichResponse**](BulkContactsEnrichResponse) post_externalcontacts_bulk_contacts_enrich(body, dry_run=dry_run)


Bulk Enrich Contacts - Run up to 10 Enrich operations per request

See the API endpoint /externalcontacts/contacts/enrich for docs on individual Enrich operations.

Wraps POST /api/v2/externalcontacts/bulk/contacts/enrich 

Requires ANY permissions: 

* externalContacts:contact:enrich

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkContactsEnrichRequest() # BulkContactsEnrichRequest | Contact Enrich Requests
dry_run = True # bool | If true, the request will not make any modifications, but will show you what the end result *would* be. (optional)

try:
    # Bulk Enrich Contacts - Run up to 10 Enrich operations per request
    api_response = api_instance.post_externalcontacts_bulk_contacts_enrich(body, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts_enrich: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkContactsEnrichRequest**](BulkContactsEnrichRequest)| Contact Enrich Requests |  |
| **dry_run** | **bool**| If true, the request will not make any modifications, but will show you what the end result *would* be. | [optional]  |

### Return type

[**BulkContactsEnrichResponse**](BulkContactsEnrichResponse)


## post_externalcontacts_bulk_contacts_remove

> [**BulkDeleteResponse**](BulkDeleteResponse) post_externalcontacts_bulk_contacts_remove(body)


Bulk remove contacts

Wraps POST /api/v2/externalcontacts/bulk/contacts/remove 

Requires ANY permissions: 

* externalContacts:contact:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Contact ids

try:
    # Bulk remove contacts
    api_response = api_instance.post_externalcontacts_bulk_contacts_remove(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Contact ids |  |

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse)


## post_externalcontacts_bulk_contacts_unresolved

> [**BulkFetchContactsResponse**](BulkFetchContactsResponse) post_externalcontacts_bulk_contacts_unresolved(body)


Bulk fetch unresolved ancestor contacts

Wraps POST /api/v2/externalcontacts/bulk/contacts/unresolved 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Contact ids

try:
    # Bulk fetch unresolved ancestor contacts
    api_response = api_instance.post_externalcontacts_bulk_contacts_unresolved(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts_unresolved: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Contact ids |  |

### Return type

[**BulkFetchContactsResponse**](BulkFetchContactsResponse)


## post_externalcontacts_bulk_contacts_update

> [**BulkContactsResponse**](BulkContactsResponse) post_externalcontacts_bulk_contacts_update(body)


Bulk update contacts

Wraps POST /api/v2/externalcontacts/bulk/contacts/update 

Requires ANY permissions: 

* externalContacts:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkContactsRequest() # BulkContactsRequest | Contacts

try:
    # Bulk update contacts
    api_response = api_instance.post_externalcontacts_bulk_contacts_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_contacts_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkContactsRequest**](BulkContactsRequest)| Contacts |  |

### Return type

[**BulkContactsResponse**](BulkContactsResponse)


## post_externalcontacts_bulk_notes

> [**BulkFetchNotesResponse**](BulkFetchNotesResponse) post_externalcontacts_bulk_notes(body)


Bulk fetch notes

Wraps POST /api/v2/externalcontacts/bulk/notes 

Requires ALL permissions: 

* externalContacts:contact:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Note ids

try:
    # Bulk fetch notes
    api_response = api_instance.post_externalcontacts_bulk_notes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Note ids |  |

### Return type

[**BulkFetchNotesResponse**](BulkFetchNotesResponse)


## post_externalcontacts_bulk_notes_add

> [**BulkNotesResponse**](BulkNotesResponse) post_externalcontacts_bulk_notes_add(body)


Bulk add notes

Wraps POST /api/v2/externalcontacts/bulk/notes/add 

Requires ALL permissions: 

* externalContacts:contact:add
* externalContacts:externalOrganization:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkNotesRequest() # BulkNotesRequest | Notes

try:
    # Bulk add notes
    api_response = api_instance.post_externalcontacts_bulk_notes_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_notes_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkNotesRequest**](BulkNotesRequest)| Notes |  |

### Return type

[**BulkNotesResponse**](BulkNotesResponse)


## post_externalcontacts_bulk_notes_remove

> [**BulkDeleteResponse**](BulkDeleteResponse) post_externalcontacts_bulk_notes_remove(body)


Bulk remove notes

Wraps POST /api/v2/externalcontacts/bulk/notes/remove 

Requires ALL permissions: 

* externalContacts:contact:delete
* externalContacts:externalOrganization:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Note ids

try:
    # Bulk remove notes
    api_response = api_instance.post_externalcontacts_bulk_notes_remove(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_notes_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Note ids |  |

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse)


## post_externalcontacts_bulk_notes_update

> [**BulkNotesResponse**](BulkNotesResponse) post_externalcontacts_bulk_notes_update(body)


Bulk update notes

Wraps POST /api/v2/externalcontacts/bulk/notes/update 

Requires ALL permissions: 

* externalContacts:contact:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkNotesRequest() # BulkNotesRequest | Notes

try:
    # Bulk update notes
    api_response = api_instance.post_externalcontacts_bulk_notes_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_notes_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkNotesRequest**](BulkNotesRequest)| Notes |  |

### Return type

[**BulkNotesResponse**](BulkNotesResponse)


## post_externalcontacts_bulk_organizations

> [**BulkFetchOrganizationsResponse**](BulkFetchOrganizationsResponse) post_externalcontacts_bulk_organizations(body)


Bulk fetch organizations

Wraps POST /api/v2/externalcontacts/bulk/organizations 

Requires ANY permissions: 

* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Organizations ids

try:
    # Bulk fetch organizations
    api_response = api_instance.post_externalcontacts_bulk_organizations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_organizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Organizations ids |  |

### Return type

[**BulkFetchOrganizationsResponse**](BulkFetchOrganizationsResponse)


## post_externalcontacts_bulk_organizations_add

> [**BulkOrganizationsResponse**](BulkOrganizationsResponse) post_externalcontacts_bulk_organizations_add(body)


Bulk add organizations

Wraps POST /api/v2/externalcontacts/bulk/organizations/add 

Requires ANY permissions: 

* externalContacts:externalOrganization:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkOrganizationsRequest() # BulkOrganizationsRequest | Organizations

try:
    # Bulk add organizations
    api_response = api_instance.post_externalcontacts_bulk_organizations_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_organizations_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkOrganizationsRequest**](BulkOrganizationsRequest)| Organizations |  |

### Return type

[**BulkOrganizationsResponse**](BulkOrganizationsResponse)


## post_externalcontacts_bulk_organizations_divisionviews

> [**BulkFetchOrganizationsResponse**](BulkFetchOrganizationsResponse) post_externalcontacts_bulk_organizations_divisionviews(body)


Bulk fetch organizations across divisions

Wraps POST /api/v2/externalcontacts/bulk/organizations/divisionviews 

Requires ANY permissions: 

* externalContacts:externalOrganization:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Organizations ids

try:
    # Bulk fetch organizations across divisions
    api_response = api_instance.post_externalcontacts_bulk_organizations_divisionviews(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_organizations_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Organizations ids |  |

### Return type

[**BulkFetchOrganizationsResponse**](BulkFetchOrganizationsResponse)


## post_externalcontacts_bulk_organizations_enrich

> [**BulkOrganizationsEnrichResponse**](BulkOrganizationsEnrichResponse) post_externalcontacts_bulk_organizations_enrich(body, dry_run=dry_run)


Bulk enrich external organizations - Run up to 10 Enrich operations per request

See the API endpoint /externalcontacts/organizations/enrich for docs on individual Enrich operations.

Wraps POST /api/v2/externalcontacts/bulk/organizations/enrich 

Requires ANY permissions: 

* externalContacts:externalOrganization:enrich

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkOrganizationsEnrichRequest() # BulkOrganizationsEnrichRequest | External Organization Enrich Requests
dry_run = True # bool | If true, the request will not make any modifications, but will show you what the end result *would* be. (optional)

try:
    # Bulk enrich external organizations - Run up to 10 Enrich operations per request
    api_response = api_instance.post_externalcontacts_bulk_organizations_enrich(body, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_organizations_enrich: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkOrganizationsEnrichRequest**](BulkOrganizationsEnrichRequest)| External Organization Enrich Requests |  |
| **dry_run** | **bool**| If true, the request will not make any modifications, but will show you what the end result *would* be. | [optional]  |

### Return type

[**BulkOrganizationsEnrichResponse**](BulkOrganizationsEnrichResponse)


## post_externalcontacts_bulk_organizations_remove

> [**BulkDeleteResponse**](BulkDeleteResponse) post_externalcontacts_bulk_organizations_remove(body)


Bulk remove organizations

Wraps POST /api/v2/externalcontacts/bulk/organizations/remove 

Requires ANY permissions: 

* externalContacts:externalOrganization:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Organization ids

try:
    # Bulk remove organizations
    api_response = api_instance.post_externalcontacts_bulk_organizations_remove(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_organizations_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Organization ids |  |

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse)


## post_externalcontacts_bulk_organizations_update

> [**BulkOrganizationsResponse**](BulkOrganizationsResponse) post_externalcontacts_bulk_organizations_update(body)


Bulk update organizations

Wraps POST /api/v2/externalcontacts/bulk/organizations/update 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkOrganizationsRequest() # BulkOrganizationsRequest | Organizations

try:
    # Bulk update organizations
    api_response = api_instance.post_externalcontacts_bulk_organizations_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_organizations_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkOrganizationsRequest**](BulkOrganizationsRequest)| Organizations |  |

### Return type

[**BulkOrganizationsResponse**](BulkOrganizationsResponse)


## post_externalcontacts_bulk_relationships

> [**BulkFetchRelationshipsResponse**](BulkFetchRelationshipsResponse) post_externalcontacts_bulk_relationships(body)


Bulk fetch relationships

Wraps POST /api/v2/externalcontacts/bulk/relationships 

Requires ALL permissions: 

* externalContacts:contact:view
* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Relationships ids

try:
    # Bulk fetch relationships
    api_response = api_instance.post_externalcontacts_bulk_relationships(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_relationships: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Relationships ids |  |

### Return type

[**BulkFetchRelationshipsResponse**](BulkFetchRelationshipsResponse)


## post_externalcontacts_bulk_relationships_add

> [**BulkRelationshipsResponse**](BulkRelationshipsResponse) post_externalcontacts_bulk_relationships_add(body)


Bulk add relationships

Wraps POST /api/v2/externalcontacts/bulk/relationships/add 

Requires ALL permissions: 

* externalContacts:contact:add
* externalContacts:externalOrganization:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkRelationshipsRequest() # BulkRelationshipsRequest | Relationships

try:
    # Bulk add relationships
    api_response = api_instance.post_externalcontacts_bulk_relationships_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_relationships_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkRelationshipsRequest**](BulkRelationshipsRequest)| Relationships |  |

### Return type

[**BulkRelationshipsResponse**](BulkRelationshipsResponse)


## post_externalcontacts_bulk_relationships_remove

> [**BulkDeleteResponse**](BulkDeleteResponse) post_externalcontacts_bulk_relationships_remove(body)


Bulk remove relationships

Wraps POST /api/v2/externalcontacts/bulk/relationships/remove 

Requires ALL permissions: 

* externalContacts:contact:delete
* externalContacts:externalOrganization:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkIdsRequest() # BulkIdsRequest | Relationships ids

try:
    # Bulk remove relationships
    api_response = api_instance.post_externalcontacts_bulk_relationships_remove(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_relationships_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkIdsRequest**](BulkIdsRequest)| Relationships ids |  |

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse)


## post_externalcontacts_bulk_relationships_update

> [**BulkRelationshipsResponse**](BulkRelationshipsResponse) post_externalcontacts_bulk_relationships_update(body)


Bulk update relationships

Wraps POST /api/v2/externalcontacts/bulk/relationships/update 

Requires ALL permissions: 

* externalContacts:contact:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.BulkRelationshipsRequest() # BulkRelationshipsRequest | Relationships

try:
    # Bulk update relationships
    api_response = api_instance.post_externalcontacts_bulk_relationships_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_bulk_relationships_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkRelationshipsRequest**](BulkRelationshipsRequest)| Relationships |  |

### Return type

[**BulkRelationshipsResponse**](BulkRelationshipsResponse)


## post_externalcontacts_contact_journey_segments

> [**UpdateSegmentAssignmentResponse**](UpdateSegmentAssignmentResponse) post_externalcontacts_contact_journey_segments(contact_id, body=body)


Assign/Unassign up to 10 segments to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment. Any unprocessed segment assignments are returned in the body for the client to retry, in the event of a partial success.

Wraps POST /api/v2/externalcontacts/contacts/{contactId}/journey/segments 

Requires ANY permissions: 

* externalContacts:segmentAssignment:add
* externalContacts:segmentAssignment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
body = PureCloudPlatformClientV2.UpdateSegmentAssignmentRequest() # UpdateSegmentAssignmentRequest |  (optional)

try:
    # Assign/Unassign up to 10 segments to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment. Any unprocessed segment assignments are returned in the body for the client to retry, in the event of a partial success.
    api_response = api_instance.post_externalcontacts_contact_journey_segments(contact_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contact_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **body** | [**UpdateSegmentAssignmentRequest**](UpdateSegmentAssignmentRequest)|  | [optional]  |

### Return type

[**UpdateSegmentAssignmentResponse**](UpdateSegmentAssignmentResponse)


## post_externalcontacts_contact_notes

> [**Note**](Note) post_externalcontacts_contact_notes(contact_id, body)


Create a note for an external contact

Wraps POST /api/v2/externalcontacts/contacts/{contactId}/notes 

Requires ANY permissions: 

* relate:contact:edit
* externalContacts:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact Id
body = PureCloudPlatformClientV2.Note() # Note | ExternalContact

try:
    # Create a note for an external contact
    api_response = api_instance.post_externalcontacts_contact_notes(contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contact_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **body** | [**Note**](Note)| ExternalContact |  |

### Return type

[**Note**](Note)


## post_externalcontacts_contact_promotion

> [**ExternalContact**](ExternalContact) post_externalcontacts_contact_promotion(contact_id)


Promote an observed contact (ephemeral or identified) to a curated contact

Wraps POST /api/v2/externalcontacts/contacts/{contactId}/promotion 

Requires ANY permissions: 

* externalContacts:identity:promote

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID

try:
    # Promote an observed contact (ephemeral or identified) to a curated contact
    api_response = api_instance.post_externalcontacts_contact_promotion(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contact_promotion: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_contacts

> [**ExternalContact**](ExternalContact) post_externalcontacts_contacts(body)


Create an external contact

Wraps POST /api/v2/externalcontacts/contacts 

Requires ANY permissions: 

* relate:contact:add
* externalContacts:contact:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ExternalContact() # ExternalContact | ExternalContact

try:
    # Create an external contact
    api_response = api_instance.post_externalcontacts_contacts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalContact**](ExternalContact)| ExternalContact |  |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_contacts_enrich

> [**ExternalContact**](ExternalContact) post_externalcontacts_contacts_enrich(body, dry_run=dry_run)


Modify or create an External Contact, with powerful behaviors for finding and combining data with pre-existing Contacts.

You may also submit multiple Enrich operations in one request via the Bulk Enrich API at /externalcontacts/bulk/contacts. A 201 response status indicates that a new Contact was created, whereas a 200 status indicates that a Contact was updated or a merge occurred.

Wraps POST /api/v2/externalcontacts/contacts/enrich 

Requires ANY permissions: 

* externalContacts:contact:enrich

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ContactEnrichRequest() # ContactEnrichRequest | ContactEnrichRequest
dry_run = True # bool | If true, the request will not make any modifications, but will show you what the end result *would* be. (optional)

try:
    # Modify or create an External Contact, with powerful behaviors for finding and combining data with pre-existing Contacts.
    api_response = api_instance.post_externalcontacts_contacts_enrich(body, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contacts_enrich: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactEnrichRequest**](ContactEnrichRequest)| ContactEnrichRequest |  |
| **dry_run** | **bool**| If true, the request will not make any modifications, but will show you what the end result *would* be. | [optional]  |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_contacts_exports

> [**ContactsExport**](ContactsExport) post_externalcontacts_contacts_exports(body)


Create bulk export

Wraps POST /api/v2/externalcontacts/contacts/exports 

Requires ALL permissions: 

* externalContacts:export:add
* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ContactsExport() # ContactsExport | Export

try:
    # Create bulk export
    api_response = api_instance.post_externalcontacts_contacts_exports(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contacts_exports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactsExport**](ContactsExport)| Export |  |

### Return type

[**ContactsExport**](ContactsExport)


## post_externalcontacts_contacts_merge

> [**ExternalContact**](ExternalContact) post_externalcontacts_contacts_merge(body)


Merge up to 25 contacts into a new contact record

Merge operation may fail if the resulting mergeset exceeds our default limit of 52. The valueOverride field lets you override any of the Contact fields post-merge. If any Contact field is left null in `valueOverride`, it will be taken from the most recently-modified contact in the merge set. Exception for *phone/*email fields: Conflicting data will be moved to any other available phone/email fields in the merged contact.

Wraps POST /api/v2/externalcontacts/contacts/merge 

Requires ANY permissions: 

* externalContacts:identity:merge

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.MergeContactsRequest() # MergeContactsRequest | MergeRequest

try:
    # Merge up to 25 contacts into a new contact record
    api_response = api_instance.post_externalcontacts_contacts_merge(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contacts_merge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MergeContactsRequest**](MergeContactsRequest)| MergeRequest |  |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_contacts_schemas

> [**DataSchema**](DataSchema) post_externalcontacts_contacts_schemas(body)


Create a schema

Wraps POST /api/v2/externalcontacts/contacts/schemas 

Requires ANY permissions: 

* externalContacts:customFields:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Schema

try:
    # Create a schema
    api_response = api_instance.post_externalcontacts_contacts_schemas(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_contacts_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DataSchema**](DataSchema)| Schema |  |

### Return type

[**DataSchema**](DataSchema)


## post_externalcontacts_externalsources

> [**ExternalSource**](ExternalSource) post_externalcontacts_externalsources(body)


Create an External Source

Wraps POST /api/v2/externalcontacts/externalsources 

Requires ANY permissions: 

* externalContacts:externalSource:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ExternalSource() # ExternalSource | External Source

try:
    # Create an External Source
    api_response = api_instance.post_externalcontacts_externalsources(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_externalsources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalSource**](ExternalSource)| External Source |  |

### Return type

[**ExternalSource**](ExternalSource)


## post_externalcontacts_identifierlookup

> [**ExternalContact**](ExternalContact) post_externalcontacts_identifierlookup(identifier, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Fetch a contact using an identifier type and value.

NOTE: Deprecated. Please use /api/v2/externalcontacts/identifierlookup/contacts as an alternative endpoint instead. Phone number identifier values must be provided with the country code and a leading '+' symbol. Example: \"+1 704 298 4733\"

Wraps POST /api/v2/externalcontacts/identifierlookup 

Requires ANY permissions: 

* externalContacts:contact:view
* relate:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
identifier = PureCloudPlatformClientV2.ContactIdentifier() # ContactIdentifier | 
expand = ['expand_example'] # list[str] | which field, if any, to expand (optional)

try:
    # Fetch a contact using an identifier type and value.
    api_response = api_instance.post_externalcontacts_identifierlookup(identifier, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_identifierlookup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **identifier** | [**ContactIdentifier**](ContactIdentifier)|  |  |
| **expand** | [**list[str]**](str)| which field, if any, to expand | [optional] <br />**Values**: externalOrganization, identifiers, externalSources, division |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_identifierlookup_contacts

> [**ExternalContact**](ExternalContact) post_externalcontacts_identifierlookup_contacts(identifier, expand=expand)


Fetch a contact using an identifier type and value.

Phone number identifier values must be provided with the country code and a leading '+' symbol. Example: \"+1 704 298 4733\"

Wraps POST /api/v2/externalcontacts/identifierlookup/contacts 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
identifier = PureCloudPlatformClientV2.ContactIdentifier() # ContactIdentifier | 
expand = ['expand_example'] # list[str] | which field, if any, to expand (optional)

try:
    # Fetch a contact using an identifier type and value.
    api_response = api_instance.post_externalcontacts_identifierlookup_contacts(identifier, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_identifierlookup_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **identifier** | [**ContactIdentifier**](ContactIdentifier)|  |  |
| **expand** | [**list[str]**](str)| which field, if any, to expand | [optional] <br />**Values**: externalOrganization, identifiers, externalSources, division |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_identifierlookup_organizations

> [**ExternalOrganization**](ExternalOrganization) post_externalcontacts_identifierlookup_organizations(identifier, expand=expand)


Fetch an external organization using an identifier type and value.

This endpoint will only accept ExternalId type identifiers.

Wraps POST /api/v2/externalcontacts/identifierlookup/organizations 

Requires ANY permissions: 

* externalContacts:externalOrganization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
identifier = PureCloudPlatformClientV2.ExternalOrganizationIdentifier() # ExternalOrganizationIdentifier | 
expand = ['expand_example'] # list[str] | which field, if any, to expand (optional)

try:
    # Fetch an external organization using an identifier type and value.
    api_response = api_instance.post_externalcontacts_identifierlookup_organizations(identifier, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_identifierlookup_organizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **identifier** | [**ExternalOrganizationIdentifier**](ExternalOrganizationIdentifier)|  |  |
| **expand** | [**list[str]**](str)| which field, if any, to expand | [optional] <br />**Values**: identifiers, externalSources, division |

### Return type

[**ExternalOrganization**](ExternalOrganization)


## post_externalcontacts_import_csv_jobs

> [**CsvJobResponse**](CsvJobResponse) post_externalcontacts_import_csv_jobs(body)


Create CSV import job

Wraps POST /api/v2/externalcontacts/import/csv/jobs 

Requires ANY permissions: 

* externalContacts:importCsvJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.CsvJobRequest() # CsvJobRequest | ImportRequest

try:
    # Create CSV import job
    api_response = api_instance.post_externalcontacts_import_csv_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_import_csv_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CsvJobRequest**](CsvJobRequest)| ImportRequest |  |

### Return type

[**CsvJobResponse**](CsvJobResponse)


## post_externalcontacts_import_csv_settings

> [**CsvSettings**](CsvSettings) post_externalcontacts_import_csv_settings(body)


Create settings for CSV import

Wraps POST /api/v2/externalcontacts/import/csv/settings 

Requires ANY permissions: 

* externalContacts:importCsvSettings:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.CsvSettings() # CsvSettings | Settings

try:
    # Create settings for CSV import
    api_response = api_instance.post_externalcontacts_import_csv_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_import_csv_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CsvSettings**](CsvSettings)| Settings |  |

### Return type

[**CsvSettings**](CsvSettings)


## post_externalcontacts_import_csv_uploads

> [**CsvUploadResponse**](CsvUploadResponse) post_externalcontacts_import_csv_uploads(body)


Get url for CSV upload

Wraps POST /api/v2/externalcontacts/import/csv/uploads 

Requires ANY permissions: 

* externalContacts:importCsvUpload:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.CsvUploadRequest() # CsvUploadRequest | UploadRequest

try:
    # Get url for CSV upload
    api_response = api_instance.post_externalcontacts_import_csv_uploads(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_import_csv_uploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CsvUploadRequest**](CsvUploadRequest)| UploadRequest |  |

### Return type

[**CsvUploadResponse**](CsvUploadResponse)


## post_externalcontacts_import_jobs

> [**ContactImportJobResponse**](ContactImportJobResponse) post_externalcontacts_import_jobs(body)


Create a new job

Wraps POST /api/v2/externalcontacts/import/jobs 

Requires ANY permissions: 

* externalContacts:importJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ContactImportJobRequest() # ContactImportJobRequest | Job

try:
    # Create a new job
    api_response = api_instance.post_externalcontacts_import_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_import_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactImportJobRequest**](ContactImportJobRequest)| Job |  |

### Return type

[**ContactImportJobResponse**](ContactImportJobResponse)


## post_externalcontacts_import_settings

> [**ContactImportSettings**](ContactImportSettings) post_externalcontacts_import_settings(body)


Create a new settings

Wraps POST /api/v2/externalcontacts/import/settings 

Requires ANY permissions: 

* externalContacts:importSettings:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ContactImportSettings() # ContactImportSettings | Setting

try:
    # Create a new settings
    api_response = api_instance.post_externalcontacts_import_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_import_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ContactImportSettings**](ContactImportSettings)| Setting |  |

### Return type

[**ContactImportSettings**](ContactImportSettings)


## post_externalcontacts_merge_contacts

> [**ExternalContact**](ExternalContact) post_externalcontacts_merge_contacts(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Merge two contacts into a new contact record

Two curated contacts cannot be merged. Refer to the Contact Merging article on the Developer Center for details. Deprecated: This API has been superseded by a new merge API. You are encouraged to instead use /api/v2/externalcontacts/contacts/merge, which supports merging up to 25 Contacts of any type, and overriding specific fields in the resulting Contact.

Wraps POST /api/v2/externalcontacts/merge/contacts 

Requires ANY permissions: 

* externalContacts:identity:merge

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.MergeRequest() # MergeRequest | MergeRequest

try:
    # Merge two contacts into a new contact record
    api_response = api_instance.post_externalcontacts_merge_contacts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_merge_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MergeRequest**](MergeRequest)| MergeRequest |  |

### Return type

[**ExternalContact**](ExternalContact)


## post_externalcontacts_organization_notes

> [**Note**](Note) post_externalcontacts_organization_notes(external_organization_id, body)


Create a note for an external organization

Wraps POST /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization Id
body = PureCloudPlatformClientV2.Note() # Note | ExternalContact

try:
    # Create a note for an external organization
    api_response = api_instance.post_externalcontacts_organization_notes(external_organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_organization_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **body** | [**Note**](Note)| ExternalContact |  |

### Return type

[**Note**](Note)


## post_externalcontacts_organizations

> [**ExternalOrganization**](ExternalOrganization) post_externalcontacts_organizations(body)


Create an external organization

Wraps POST /api/v2/externalcontacts/organizations 

Requires ANY permissions: 

* relate:externalOrganization:add
* externalContacts:externalOrganization:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ExternalOrganization() # ExternalOrganization | ExternalOrganization

try:
    # Create an external organization
    api_response = api_instance.post_externalcontacts_organizations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_organizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalOrganization**](ExternalOrganization)| ExternalOrganization |  |

### Return type

[**ExternalOrganization**](ExternalOrganization)


## post_externalcontacts_organizations_enrich

> [**ExternalOrganization**](ExternalOrganization) post_externalcontacts_organizations_enrich(body, dry_run=dry_run)


Modify or create an External Org, with powerful behaviors for finding and combining data with pre-existing External Orgs.

You may also submit multiple Enrich operations in one request via the Bulk Enrich API at /externalcontacts/bulk/organizations. A 201 response status indicates that a new External Organization was created, whereas a 200 status indicates that an External Organization was updated

Wraps POST /api/v2/externalcontacts/organizations/enrich 

Requires ANY permissions: 

* externalContacts:externalOrganization:enrich

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ExternalOrganizationEnrichRequest() # ExternalOrganizationEnrichRequest | ExternalOrgEnrichRequest
dry_run = True # bool | If true, the request will not make any modifications, but will show you what the end result *would* be. (optional)

try:
    # Modify or create an External Org, with powerful behaviors for finding and combining data with pre-existing External Orgs.
    api_response = api_instance.post_externalcontacts_organizations_enrich(body, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_organizations_enrich: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalOrganizationEnrichRequest**](ExternalOrganizationEnrichRequest)| ExternalOrgEnrichRequest |  |
| **dry_run** | **bool**| If true, the request will not make any modifications, but will show you what the end result *would* be. | [optional]  |

### Return type

[**ExternalOrganization**](ExternalOrganization)


## post_externalcontacts_organizations_schemas

> [**DataSchema**](DataSchema) post_externalcontacts_organizations_schemas(body)


Create a schema

Wraps POST /api/v2/externalcontacts/organizations/schemas 

Requires ANY permissions: 

* externalContacts:customFields:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Schema

try:
    # Create a schema
    api_response = api_instance.post_externalcontacts_organizations_schemas(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_organizations_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DataSchema**](DataSchema)| Schema |  |

### Return type

[**DataSchema**](DataSchema)


## post_externalcontacts_relationships

> [**Relationship**](Relationship) post_externalcontacts_relationships(body)


Create a relationship

Wraps POST /api/v2/externalcontacts/relationships 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.Relationship() # Relationship | Relationship

try:
    # Create a relationship
    api_response = api_instance.post_externalcontacts_relationships(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_relationships: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Relationship**](Relationship)| Relationship |  |

### Return type

[**Relationship**](Relationship)


## put_externalcontacts_contact

> [**ExternalContact**](ExternalContact) put_externalcontacts_contact(contact_id, body)


Update an external contact

Wraps PUT /api/v2/externalcontacts/contacts/{contactId} 

Requires ANY permissions: 

* relate:contact:edit
* externalContacts:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID
body = PureCloudPlatformClientV2.ExternalContact() # ExternalContact | ExternalContact

try:
    # Update an external contact
    api_response = api_instance.put_externalcontacts_contact(contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_contact: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **body** | [**ExternalContact**](ExternalContact)| ExternalContact |  |

### Return type

[**ExternalContact**](ExternalContact)


## put_externalcontacts_contact_note

> [**Note**](Note) put_externalcontacts_contact_note(contact_id, note_id, body)


Update a note for an external contact

Wraps PUT /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

Requires ANY permissions: 

* relate:contact:edit
* externalContacts:contact:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact Id
note_id = 'note_id_example' # str | Note Id
body = PureCloudPlatformClientV2.Note() # Note | Note

try:
    # Update a note for an external contact
    api_response = api_instance.put_externalcontacts_contact_note(contact_id, note_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_contact_note: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **note_id** | **str**| Note Id |  |
| **body** | [**Note**](Note)| Note |  |

### Return type

[**Note**](Note)


## put_externalcontacts_contacts_schema

> [**DataSchema**](DataSchema) put_externalcontacts_contacts_schema(schema_id, body)


Update a schema

Wraps PUT /api/v2/externalcontacts/contacts/schemas/{schemaId} 

Requires ANY permissions: 

* externalContacts:customFields:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Data Schema

try:
    # Update a schema
    api_response = api_instance.put_externalcontacts_contacts_schema(schema_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_contacts_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **body** | [**DataSchema**](DataSchema)| Data Schema |  |

### Return type

[**DataSchema**](DataSchema)


## put_externalcontacts_conversation

>  put_externalcontacts_conversation(conversation_id, body)


Associate/disassociate an external contact with a conversation

To associate, supply a value for the externalContactId.  To disassociate, do not include the property at all.

Wraps PUT /api/v2/externalcontacts/conversations/{conversationId} 

Requires ANY permissions: 

* relate:conversation:associate
* externalContacts:conversation:associate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
body = PureCloudPlatformClientV2.ConversationAssociation() # ConversationAssociation | ConversationAssociation

try:
    # Associate/disassociate an external contact with a conversation
    api_instance.put_externalcontacts_conversation(conversation_id, body)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **body** | [**ConversationAssociation**](ConversationAssociation)| ConversationAssociation |  |

### Return type

void (empty response body)


## put_externalcontacts_externalsource

> [**ExternalSource**](ExternalSource) put_externalcontacts_externalsource(external_source_id, body)


Update an External Source

Wraps PUT /api/v2/externalcontacts/externalsources/{externalSourceId} 

Requires ANY permissions: 

* externalContacts:externalSource:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_source_id = 'external_source_id_example' # str | External Source ID
body = PureCloudPlatformClientV2.ExternalSource() # ExternalSource | External Source

try:
    # Update an External Source
    api_response = api_instance.put_externalcontacts_externalsource(external_source_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_externalsource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_source_id** | **str**| External Source ID |  |
| **body** | [**ExternalSource**](ExternalSource)| External Source |  |

### Return type

[**ExternalSource**](ExternalSource)


## put_externalcontacts_import_csv_setting

> [**CsvSettings**](CsvSettings) put_externalcontacts_import_csv_setting(settings_id, body)


Update settings for CSV import

Wraps PUT /api/v2/externalcontacts/import/csv/settings/{settingsId} 

Requires ANY permissions: 

* externalContacts:importCsvSettings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
settings_id = 'settings_id_example' # str | Settings id
body = PureCloudPlatformClientV2.CsvSettings() # CsvSettings | Settings

try:
    # Update settings for CSV import
    api_response = api_instance.put_externalcontacts_import_csv_setting(settings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_import_csv_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings id |  |
| **body** | [**CsvSettings**](CsvSettings)| Settings |  |

### Return type

[**CsvSettings**](CsvSettings)


## put_externalcontacts_import_job

> [**ContactImportJobStatusUpdateResponse**](ContactImportJobStatusUpdateResponse) put_externalcontacts_import_job(job_id, body)


Update Job's workflow status

Wraps PUT /api/v2/externalcontacts/import/jobs/{jobId} 

Requires ANY permissions: 

* externalContacts:importJob:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
job_id = 'job_id_example' # str | Job id
body = PureCloudPlatformClientV2.ContactImportJobStatusUpdateRequest() # ContactImportJobStatusUpdateRequest | Status of the Job's workflow

try:
    # Update Job's workflow status
    api_response = api_instance.put_externalcontacts_import_job(job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_import_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Job id |  |
| **body** | [**ContactImportJobStatusUpdateRequest**](ContactImportJobStatusUpdateRequest)| Status of the Job&#39;s workflow |  |

### Return type

[**ContactImportJobStatusUpdateResponse**](ContactImportJobStatusUpdateResponse)


## put_externalcontacts_import_setting

> [**ContactImportSettings**](ContactImportSettings) put_externalcontacts_import_setting(settings_id, body)


Update settings

Wraps PUT /api/v2/externalcontacts/import/settings/{settingsId} 

Requires ANY permissions: 

* externalContacts:importSettings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
settings_id = 'settings_id_example' # str | Settings id
body = PureCloudPlatformClientV2.ContactImportSettings() # ContactImportSettings | Setting

try:
    # Update settings
    api_response = api_instance.put_externalcontacts_import_setting(settings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_import_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **settings_id** | **str**| Settings id |  |
| **body** | [**ContactImportSettings**](ContactImportSettings)| Setting |  |

### Return type

[**ContactImportSettings**](ContactImportSettings)


## put_externalcontacts_organization

> [**ExternalOrganization**](ExternalOrganization) put_externalcontacts_organization(external_organization_id, body)


Update an external organization

Wraps PUT /api/v2/externalcontacts/organizations/{externalOrganizationId} 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
body = PureCloudPlatformClientV2.ExternalOrganization() # ExternalOrganization | ExternalOrganization

try:
    # Update an external organization
    api_response = api_instance.put_externalcontacts_organization(external_organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_organization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **body** | [**ExternalOrganization**](ExternalOrganization)| ExternalOrganization |  |

### Return type

[**ExternalOrganization**](ExternalOrganization)


## put_externalcontacts_organization_note

> [**Note**](Note) put_externalcontacts_organization_note(external_organization_id, note_id, body)


Update a note for an external organization

Wraps PUT /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization Id
note_id = 'note_id_example' # str | Note Id
body = PureCloudPlatformClientV2.Note() # Note | Note

try:
    # Update a note for an external organization
    api_response = api_instance.put_externalcontacts_organization_note(external_organization_id, note_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_organization_note: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **note_id** | **str**| Note Id |  |
| **body** | [**Note**](Note)| Note |  |

### Return type

[**Note**](Note)


## put_externalcontacts_organization_trustor_trustor_id

> [**ExternalOrganizationTrustorLink**](ExternalOrganizationTrustorLink) put_externalcontacts_organization_trustor_trustor_id(external_organization_id, trustor_id)


Links a Trustor with an External Organization

Wraps PUT /api/v2/externalcontacts/organizations/{externalOrganizationId}/trustor/{trustorId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
trustor_id = 'trustor_id_example' # str | Trustor ID

try:
    # Links a Trustor with an External Organization
    api_response = api_instance.put_externalcontacts_organization_trustor_trustor_id(external_organization_id, trustor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_organization_trustor_trustor_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **trustor_id** | **str**| Trustor ID |  |

### Return type

[**ExternalOrganizationTrustorLink**](ExternalOrganizationTrustorLink)


## put_externalcontacts_organizations_schema

> [**DataSchema**](DataSchema) put_externalcontacts_organizations_schema(schema_id, body)


Update a schema

Wraps PUT /api/v2/externalcontacts/organizations/schemas/{schemaId} 

Requires ANY permissions: 

* externalContacts:customFields:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
schema_id = 'schema_id_example' # str | Schema ID
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Data Schema

try:
    # Update a schema
    api_response = api_instance.put_externalcontacts_organizations_schema(schema_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_organizations_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **body** | [**DataSchema**](DataSchema)| Data Schema |  |

### Return type

[**DataSchema**](DataSchema)


## put_externalcontacts_relationship

> [**Relationship**](Relationship) put_externalcontacts_relationship(relationship_id, body)


Update a relationship

Wraps PUT /api/v2/externalcontacts/relationships/{relationshipId} 

Requires ANY permissions: 

* relate:externalOrganization:edit
* externalContacts:externalOrganization:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
relationship_id = 'relationship_id_example' # str | Relationship Id
body = PureCloudPlatformClientV2.Relationship() # Relationship | Relationship

try:
    # Update a relationship
    api_response = api_instance.put_externalcontacts_relationship(relationship_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->put_externalcontacts_relationship: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **relationship_id** | **str**| Relationship Id |  |
| **body** | [**Relationship**](Relationship)| Relationship |  |

### Return type

[**Relationship**](Relationship)


_PureCloudPlatformClientV2 238.0.0_
