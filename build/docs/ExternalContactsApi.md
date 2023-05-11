---
title: ExternalContactsApi
---

## PureCloudPlatformClientV2.ExternalContactsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_externalcontacts_contact**](ExternalContactsApi.html#delete_externalcontacts_contact) | Delete an external contact|
|[**delete_externalcontacts_contact_note**](ExternalContactsApi.html#delete_externalcontacts_contact_note) | Delete a note for an external contact|
|[**delete_externalcontacts_contacts_schema**](ExternalContactsApi.html#delete_externalcontacts_contacts_schema) | Delete a schema|
|[**delete_externalcontacts_organization**](ExternalContactsApi.html#delete_externalcontacts_organization) | Delete an external organization|
|[**delete_externalcontacts_organization_note**](ExternalContactsApi.html#delete_externalcontacts_organization_note) | Delete a note for an external organization|
|[**delete_externalcontacts_organization_trustor**](ExternalContactsApi.html#delete_externalcontacts_organization_trustor) | Unlink the Trustor for this External Organization|
|[**delete_externalcontacts_relationship**](ExternalContactsApi.html#delete_externalcontacts_relationship) | Delete a relationship|
|[**get_externalcontacts_contact**](ExternalContactsApi.html#get_externalcontacts_contact) | Fetch an external contact|
|[**get_externalcontacts_contact_identifiers**](ExternalContactsApi.html#get_externalcontacts_contact_identifiers) | List the identifiers for a contact|
|[**get_externalcontacts_contact_journey_sessions**](ExternalContactsApi.html#get_externalcontacts_contact_journey_sessions) | Retrieve all sessions for a given external contact.|
|[**get_externalcontacts_contact_note**](ExternalContactsApi.html#get_externalcontacts_contact_note) | Fetch a note for an external contact|
|[**get_externalcontacts_contact_notes**](ExternalContactsApi.html#get_externalcontacts_contact_notes) | List notes for an external contact|
|[**get_externalcontacts_contact_unresolved**](ExternalContactsApi.html#get_externalcontacts_contact_unresolved) | Fetch an unresolved external contact|
|[**get_externalcontacts_contacts**](ExternalContactsApi.html#get_externalcontacts_contacts) | Search for external contacts|
|[**get_externalcontacts_contacts_schema**](ExternalContactsApi.html#get_externalcontacts_contacts_schema) | Get a schema|
|[**get_externalcontacts_contacts_schema_version**](ExternalContactsApi.html#get_externalcontacts_contacts_schema_version) | Get a specific version of a schema|
|[**get_externalcontacts_contacts_schema_versions**](ExternalContactsApi.html#get_externalcontacts_contacts_schema_versions) | Get all versions of an external contact&#39;s schema|
|[**get_externalcontacts_contacts_schemas**](ExternalContactsApi.html#get_externalcontacts_contacts_schemas) | Get a list of schemas.|
|[**get_externalcontacts_organization**](ExternalContactsApi.html#get_externalcontacts_organization) | Fetch an external organization|
|[**get_externalcontacts_organization_contacts**](ExternalContactsApi.html#get_externalcontacts_organization_contacts) | Search for external contacts in an external organization|
|[**get_externalcontacts_organization_note**](ExternalContactsApi.html#get_externalcontacts_organization_note) | Fetch a note for an external organization|
|[**get_externalcontacts_organization_notes**](ExternalContactsApi.html#get_externalcontacts_organization_notes) | List notes for an external organization|
|[**get_externalcontacts_organization_relationships**](ExternalContactsApi.html#get_externalcontacts_organization_relationships) | Fetch a relationship for an external organization|
|[**get_externalcontacts_organizations**](ExternalContactsApi.html#get_externalcontacts_organizations) | Search for external organizations|
|[**get_externalcontacts_organizations_schema**](ExternalContactsApi.html#get_externalcontacts_organizations_schema) | Get a schema|
|[**get_externalcontacts_organizations_schema_version**](ExternalContactsApi.html#get_externalcontacts_organizations_schema_version) | Get a specific version of a schema|
|[**get_externalcontacts_organizations_schema_versions**](ExternalContactsApi.html#get_externalcontacts_organizations_schema_versions) | Get all versions of an external organization&#39;s schema|
|[**get_externalcontacts_organizations_schemas**](ExternalContactsApi.html#get_externalcontacts_organizations_schemas) | Get a list of schemas.|
|[**get_externalcontacts_relationship**](ExternalContactsApi.html#get_externalcontacts_relationship) | Fetch a relationship|
|[**get_externalcontacts_reversewhitepageslookup**](ExternalContactsApi.html#get_externalcontacts_reversewhitepageslookup) | Look up contacts and externalOrganizations based on an attribute. Maximum of 25 values returned.|
|[**get_externalcontacts_scan_contacts**](ExternalContactsApi.html#get_externalcontacts_scan_contacts) | Scan for external contacts using paging|
|[**get_externalcontacts_scan_notes**](ExternalContactsApi.html#get_externalcontacts_scan_notes) | Scan for notes using paging|
|[**get_externalcontacts_scan_organizations**](ExternalContactsApi.html#get_externalcontacts_scan_organizations) | Scan for external organizations using paging|
|[**get_externalcontacts_scan_relationships**](ExternalContactsApi.html#get_externalcontacts_scan_relationships) | Scan for relationships|
|[**patch_externalcontacts_contact_identifiers**](ExternalContactsApi.html#patch_externalcontacts_contact_identifiers) | Claim or release identifiers for a contact|
|[**post_externalcontacts_bulk_contacts**](ExternalContactsApi.html#post_externalcontacts_bulk_contacts) | Bulk fetch contacts|
|[**post_externalcontacts_bulk_contacts_add**](ExternalContactsApi.html#post_externalcontacts_bulk_contacts_add) | Bulk add contacts|
|[**post_externalcontacts_bulk_contacts_remove**](ExternalContactsApi.html#post_externalcontacts_bulk_contacts_remove) | Bulk remove contacts|
|[**post_externalcontacts_bulk_contacts_unresolved**](ExternalContactsApi.html#post_externalcontacts_bulk_contacts_unresolved) | Bulk fetch unresolved ancestor contacts|
|[**post_externalcontacts_bulk_contacts_update**](ExternalContactsApi.html#post_externalcontacts_bulk_contacts_update) | Bulk update contacts|
|[**post_externalcontacts_bulk_notes**](ExternalContactsApi.html#post_externalcontacts_bulk_notes) | Bulk fetch notes|
|[**post_externalcontacts_bulk_notes_add**](ExternalContactsApi.html#post_externalcontacts_bulk_notes_add) | Bulk add notes|
|[**post_externalcontacts_bulk_notes_remove**](ExternalContactsApi.html#post_externalcontacts_bulk_notes_remove) | Bulk remove notes|
|[**post_externalcontacts_bulk_notes_update**](ExternalContactsApi.html#post_externalcontacts_bulk_notes_update) | Bulk update notes|
|[**post_externalcontacts_bulk_organizations**](ExternalContactsApi.html#post_externalcontacts_bulk_organizations) | Bulk fetch organizations|
|[**post_externalcontacts_bulk_organizations_add**](ExternalContactsApi.html#post_externalcontacts_bulk_organizations_add) | Bulk add organizations|
|[**post_externalcontacts_bulk_organizations_remove**](ExternalContactsApi.html#post_externalcontacts_bulk_organizations_remove) | Bulk remove organizations|
|[**post_externalcontacts_bulk_organizations_update**](ExternalContactsApi.html#post_externalcontacts_bulk_organizations_update) | Bulk update organizations|
|[**post_externalcontacts_bulk_relationships**](ExternalContactsApi.html#post_externalcontacts_bulk_relationships) | Bulk fetch relationships|
|[**post_externalcontacts_bulk_relationships_add**](ExternalContactsApi.html#post_externalcontacts_bulk_relationships_add) | Bulk add relationships|
|[**post_externalcontacts_bulk_relationships_remove**](ExternalContactsApi.html#post_externalcontacts_bulk_relationships_remove) | Bulk remove relationships|
|[**post_externalcontacts_bulk_relationships_update**](ExternalContactsApi.html#post_externalcontacts_bulk_relationships_update) | Bulk update relationships|
|[**post_externalcontacts_contact_notes**](ExternalContactsApi.html#post_externalcontacts_contact_notes) | Create a note for an external contact|
|[**post_externalcontacts_contact_promotion**](ExternalContactsApi.html#post_externalcontacts_contact_promotion) | Promote an observed contact (ephemeral or identified) to a curated contact|
|[**post_externalcontacts_contacts**](ExternalContactsApi.html#post_externalcontacts_contacts) | Create an external contact|
|[**post_externalcontacts_contacts_schemas**](ExternalContactsApi.html#post_externalcontacts_contacts_schemas) | Create a schema|
|[**post_externalcontacts_identifierlookup**](ExternalContactsApi.html#post_externalcontacts_identifierlookup) | Fetch a contact using an identifier type and value.|
|[**post_externalcontacts_merge_contacts**](ExternalContactsApi.html#post_externalcontacts_merge_contacts) | Merge two contacts into a new contact record|
|[**post_externalcontacts_organization_notes**](ExternalContactsApi.html#post_externalcontacts_organization_notes) | Create a note for an external organization|
|[**post_externalcontacts_organizations**](ExternalContactsApi.html#post_externalcontacts_organizations) | Create an external organization|
|[**post_externalcontacts_organizations_schemas**](ExternalContactsApi.html#post_externalcontacts_organizations_schemas) | Create a schema|
|[**post_externalcontacts_relationships**](ExternalContactsApi.html#post_externalcontacts_relationships) | Create a relationship|
|[**put_externalcontacts_contact**](ExternalContactsApi.html#put_externalcontacts_contact) | Update an external contact|
|[**put_externalcontacts_contact_note**](ExternalContactsApi.html#put_externalcontacts_contact_note) | Update a note for an external contact|
|[**put_externalcontacts_contacts_schema**](ExternalContactsApi.html#put_externalcontacts_contacts_schema) | Update a schema|
|[**put_externalcontacts_conversation**](ExternalContactsApi.html#put_externalcontacts_conversation) | Associate/disassociate an external contact with a conversation|
|[**put_externalcontacts_organization**](ExternalContactsApi.html#put_externalcontacts_organization) | Update an external organization|
|[**put_externalcontacts_organization_note**](ExternalContactsApi.html#put_externalcontacts_organization_note) | Update a note for an external organization|
|[**put_externalcontacts_organization_trustor_trustor_id**](ExternalContactsApi.html#put_externalcontacts_organization_trustor_trustor_id) | Links a Trustor with an External Organization|
|[**put_externalcontacts_organizations_schema**](ExternalContactsApi.html#put_externalcontacts_organizations_schema) | Update a schema|
|[**put_externalcontacts_relationship**](ExternalContactsApi.html#put_externalcontacts_relationship) | Update a relationship|
{: class="table table-striped"}

<a name="delete_externalcontacts_contact"></a>

## object** delete_externalcontacts_contact(contact_id)



Delete an external contact



Wraps DELETE /api/v2/externalcontacts/contacts/{contactId} 

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
{: class="table table-striped"}

### Return type

**object**

<a name="delete_externalcontacts_contact_note"></a>

## object** delete_externalcontacts_contact_note(contact_id, note_id)



Delete a note for an external contact



Wraps DELETE /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

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
{: class="table table-striped"}

### Return type

**object**

<a name="delete_externalcontacts_contacts_schema"></a>

##  delete_externalcontacts_contacts_schema(schema_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_organization"></a>

## object** delete_externalcontacts_organization(external_organization_id)



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
{: class="table table-striped"}

### Return type

**object**

<a name="delete_externalcontacts_organization_note"></a>

## object** delete_externalcontacts_organization_note(external_organization_id, note_id)



Delete a note for an external organization



Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

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
{: class="table table-striped"}

### Return type

**object**

<a name="delete_externalcontacts_organization_trustor"></a>

##  delete_externalcontacts_organization_trustor(external_organization_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_relationship"></a>

## object** delete_externalcontacts_relationship(relationship_id)



Delete a relationship



Wraps DELETE /api/v2/externalcontacts/relationships/{relationshipId} 

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
{: class="table table-striped"}

### Return type

**object**

<a name="get_externalcontacts_contact"></a>

## [**ExternalContact**](ExternalContact.html) get_externalcontacts_contact(contact_id, expand=expand)



Fetch an external contact



Wraps GET /api/v2/externalcontacts/contacts/{contactId} 

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
expand = ['expand_example'] # list[str] | which fields, if any, to expand (externalOrganization,externalDataSources) (optional)

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
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand (externalOrganization,externalDataSources) | [optional] <br />**Values**: externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="get_externalcontacts_contact_identifiers"></a>

## [**EntityListing**](EntityListing.html) get_externalcontacts_contact_identifiers(contact_id)



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
{: class="table table-striped"}

### Return type

[**EntityListing**](EntityListing.html)

<a name="get_externalcontacts_contact_journey_sessions"></a>

## [**SessionListing**](SessionListing.html) get_externalcontacts_contact_journey_sessions(contact_id, page_size=page_size, after=after, include_merged=include_merged)



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
{: class="table table-striped"}

### Return type

[**SessionListing**](SessionListing.html)

<a name="get_externalcontacts_contact_note"></a>

## [**Note**](Note.html) get_externalcontacts_contact_note(contact_id, note_id, expand=expand)



Fetch a note for an external contact



Wraps GET /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

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
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="get_externalcontacts_contact_notes"></a>

## [**NoteListing**](NoteListing.html) get_externalcontacts_contact_notes(contact_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)



List notes for an external contact



Wraps GET /api/v2/externalcontacts/contacts/{contactId}/notes 

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
contact_id = 'contact_id_example' # str | ExternalContact Id
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
sort_order = 'sort_order_example' # str | Sort order (optional)
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
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources |
{: class="table table-striped"}

### Return type

[**NoteListing**](NoteListing.html)

<a name="get_externalcontacts_contact_unresolved"></a>

## [**ExternalContact**](ExternalContact.html) get_externalcontacts_contact_unresolved(contact_id, expand=expand)



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
expand = ['expand_example'] # list[str] | which fields, if any, to expand (externalOrganization,externalDataSources) (optional)

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
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand (externalOrganization,externalDataSources) | [optional] <br />**Values**: externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="get_externalcontacts_contacts"></a>

## [**ContactListing**](ContactListing.html) get_externalcontacts_contacts(page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand)



Search for external contacts



Wraps GET /api/v2/externalcontacts/contacts 

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
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
q = 'q_example' # str | User supplied search keywords (no special syntax is currently supported) (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)

try:
    # Search for external contacts
    api_response = api_instance.get_externalcontacts_contacts(page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand)
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
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ContactListing**](ContactListing.html)

<a name="get_externalcontacts_contacts_schema"></a>

## [**DataSchema**](DataSchema.html) get_externalcontacts_contacts_schema(schema_id)



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
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_externalcontacts_contacts_schema_version"></a>

## [**DataSchema**](DataSchema.html) get_externalcontacts_contacts_schema_version(schema_id, version_id)



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
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_externalcontacts_contacts_schema_versions"></a>

## [**DataSchema**](DataSchema.html) get_externalcontacts_contacts_schema_versions(schema_id)



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
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_externalcontacts_contacts_schemas"></a>

## [**DataSchemaListing**](DataSchemaListing.html) get_externalcontacts_contacts_schemas()



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

[**DataSchemaListing**](DataSchemaListing.html)

<a name="get_externalcontacts_organization"></a>

## [**ExternalOrganization**](ExternalOrganization.html) get_externalcontacts_organization(external_organization_id, expand=expand, include_trustors=include_trustors)



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
expand = 'expand_example' # str | which fields, if any, to expand (externalDataSources) (optional)
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
| **expand** | **str**| which fields, if any, to expand (externalDataSources) | [optional] <br />**Values**: externalDataSources |
| **include_trustors** | **bool**| (true or false) whether or not to include trustor information embedded in the externalOrganization | [optional]  |
{: class="table table-striped"}

### Return type

[**ExternalOrganization**](ExternalOrganization.html)

<a name="get_externalcontacts_organization_contacts"></a>

## [**ContactListing**](ContactListing.html) get_externalcontacts_organization_contacts(external_organization_id, page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand)



Search for external contacts in an external organization



Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/contacts 

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
external_organization_id = 'external_organization_id_example' # str | External Organization ID
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
q = 'q_example' # str | User supplied search keywords (no special syntax is currently supported) (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)
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
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ContactListing**](ContactListing.html)

<a name="get_externalcontacts_organization_note"></a>

## [**Note**](Note.html) get_externalcontacts_organization_note(external_organization_id, note_id, expand=expand)



Fetch a note for an external organization



Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

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
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="get_externalcontacts_organization_notes"></a>

## [**NoteListing**](NoteListing.html) get_externalcontacts_organization_notes(external_organization_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)



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
sort_order = 'sort_order_example' # str | Sort order (optional)
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
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources |
{: class="table table-striped"}

### Return type

[**NoteListing**](NoteListing.html)

<a name="get_externalcontacts_organization_relationships"></a>

## [**RelationshipListing**](RelationshipListing.html) get_externalcontacts_organization_relationships(external_organization_id, page_size=page_size, page_number=page_number, expand=expand, sort_order=sort_order)



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
expand = 'expand_example' # str | which fields, if any, to expand (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)

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
| **expand** | **str**| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources |
| **sort_order** | **str**| Sort order | [optional]  |
{: class="table table-striped"}

### Return type

[**RelationshipListing**](RelationshipListing.html)

<a name="get_externalcontacts_organizations"></a>

## [**ExternalOrganizationListing**](ExternalOrganizationListing.html) get_externalcontacts_organizations(page_size=page_size, page_number=page_number, q=q, trustor_id=trustor_id, sort_order=sort_order, expand=expand, include_trustors=include_trustors)



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
sort_order = 'sort_order_example' # str | Sort order (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
include_trustors = True # bool | (true or false) whether or not to include trustor information embedded in the externalOrganization (optional)

try:
    # Search for external organizations
    api_response = api_instance.get_externalcontacts_organizations(page_size=page_size, page_number=page_number, q=q, trustor_id=trustor_id, sort_order=sort_order, expand=expand, include_trustors=include_trustors)
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
| **trustor_id** | [**list[str]**](str.html)| Search for external organizations by trustorIds (limit 25). If supplied, the &#39;q&#39; parameters is ignored. Items are returned in the order requested | [optional]  |
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources |
| **include_trustors** | **bool**| (true or false) whether or not to include trustor information embedded in the externalOrganization | [optional]  |
{: class="table table-striped"}

### Return type

[**ExternalOrganizationListing**](ExternalOrganizationListing.html)

<a name="get_externalcontacts_organizations_schema"></a>

## [**DataSchema**](DataSchema.html) get_externalcontacts_organizations_schema(schema_id)



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
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_externalcontacts_organizations_schema_version"></a>

## [**DataSchema**](DataSchema.html) get_externalcontacts_organizations_schema_version(schema_id, version_id)



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
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_externalcontacts_organizations_schema_versions"></a>

## [**DataSchema**](DataSchema.html) get_externalcontacts_organizations_schema_versions(schema_id)



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
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_externalcontacts_organizations_schemas"></a>

## [**DataSchemaListing**](DataSchemaListing.html) get_externalcontacts_organizations_schemas()



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

[**DataSchemaListing**](DataSchemaListing.html)

<a name="get_externalcontacts_relationship"></a>

## [**Relationship**](Relationship.html) get_externalcontacts_relationship(relationship_id, expand=expand)



Fetch a relationship



Wraps GET /api/v2/externalcontacts/relationships/{relationshipId} 

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
relationship_id = 'relationship_id_example' # str | Relationship Id
expand = 'expand_example' # str | which fields, if any, to expand (optional)

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
| **expand** | **str**| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources |
{: class="table table-striped"}

### Return type

[**Relationship**](Relationship.html)

<a name="get_externalcontacts_reversewhitepageslookup"></a>

## [**ReverseWhitepagesLookupResult**](ReverseWhitepagesLookupResult.html) get_externalcontacts_reversewhitepageslookup(lookup_val, expand=expand)



Look up contacts and externalOrganizations based on an attribute. Maximum of 25 values returned.



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
lookup_val = 'lookup_val_example' # str | User supplied value to lookup contacts/externalOrganizations (supports email addresses, e164 phone numbers, Twitter screen names)
expand = ['expand_example'] # list[str] | which field, if any, to expand (optional)

try:
    # Look up contacts and externalOrganizations based on an attribute. Maximum of 25 values returned.
    api_response = api_instance.get_externalcontacts_reversewhitepageslookup(lookup_val, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_reversewhitepageslookup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **lookup_val** | **str**| User supplied value to lookup contacts/externalOrganizations (supports email addresses, e164 phone numbers, Twitter screen names) |  |
| **expand** | [**list[str]**](str.html)| which field, if any, to expand | [optional] <br />**Values**: contacts.externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ReverseWhitepagesLookupResult**](ReverseWhitepagesLookupResult.html)

<a name="get_externalcontacts_scan_contacts"></a>

## [**CursorContactListing**](CursorContactListing.html) get_externalcontacts_scan_contacts(limit=limit, cursor=cursor)



Scan for external contacts using paging



Wraps GET /api/v2/externalcontacts/scan/contacts 

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
limit = 56 # int | The number of contacts per page; must be between 10 and 200, default is 100) (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for external contacts using paging
    api_response = api_instance.get_externalcontacts_scan_contacts(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_contacts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of contacts per page; must be between 10 and 200, default is 100) | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
{: class="table table-striped"}

### Return type

[**CursorContactListing**](CursorContactListing.html)

<a name="get_externalcontacts_scan_notes"></a>

## [**CursorNoteListing**](CursorNoteListing.html) get_externalcontacts_scan_notes(limit=limit, cursor=cursor)



Scan for notes using paging



Wraps GET /api/v2/externalcontacts/scan/notes 

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
limit = 56 # int | The number of notes per page; must be between 10 and 200, default is 100) (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for notes using paging
    api_response = api_instance.get_externalcontacts_scan_notes(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_notes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of notes per page; must be between 10 and 200, default is 100) | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
{: class="table table-striped"}

### Return type

[**CursorNoteListing**](CursorNoteListing.html)

<a name="get_externalcontacts_scan_organizations"></a>

## [**CursorOrganizationListing**](CursorOrganizationListing.html) get_externalcontacts_scan_organizations(limit=limit, cursor=cursor)



Scan for external organizations using paging



Wraps GET /api/v2/externalcontacts/scan/organizations 

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
limit = 56 # int | The number of organizations per page; must be between 10 and 200, default is 100) (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for external organizations using paging
    api_response = api_instance.get_externalcontacts_scan_organizations(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_organizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of organizations per page; must be between 10 and 200, default is 100) | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
{: class="table table-striped"}

### Return type

[**CursorOrganizationListing**](CursorOrganizationListing.html)

<a name="get_externalcontacts_scan_relationships"></a>

## [**CursorRelationshipListing**](CursorRelationshipListing.html) get_externalcontacts_scan_relationships(limit=limit, cursor=cursor)



Scan for relationships



Wraps GET /api/v2/externalcontacts/scan/relationships 

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
limit = 56 # int | The number of relationships per page; must be between 10 and 200, default is 100) (optional)
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL (optional)

try:
    # Scan for relationships
    api_response = api_instance.get_externalcontacts_scan_relationships(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->get_externalcontacts_scan_relationships: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | **int**| The number of relationships per page; must be between 10 and 200, default is 100) | [optional]  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page), each page returns a new cursor with a 24h TTL | [optional]  |
{: class="table table-striped"}

### Return type

[**CursorRelationshipListing**](CursorRelationshipListing.html)

<a name="patch_externalcontacts_contact_identifiers"></a>

## [**ContactIdentifier**](ContactIdentifier.html) patch_externalcontacts_contact_identifiers(contact_id, body)



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
| **body** | [**IdentifierClaimRequest**](IdentifierClaimRequest.html)| ClaimRequest |  |
{: class="table table-striped"}

### Return type

[**ContactIdentifier**](ContactIdentifier.html)

<a name="post_externalcontacts_bulk_contacts"></a>

## [**BulkFetchContactsResponse**](BulkFetchContactsResponse.html) post_externalcontacts_bulk_contacts(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Contact ids |  |
{: class="table table-striped"}

### Return type

[**BulkFetchContactsResponse**](BulkFetchContactsResponse.html)

<a name="post_externalcontacts_bulk_contacts_add"></a>

## [**BulkContactsResponse**](BulkContactsResponse.html) post_externalcontacts_bulk_contacts_add(body)



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
| **body** | [**BulkContactsRequest**](BulkContactsRequest.html)| Contacts |  |
{: class="table table-striped"}

### Return type

[**BulkContactsResponse**](BulkContactsResponse.html)

<a name="post_externalcontacts_bulk_contacts_remove"></a>

## [**BulkDeleteResponse**](BulkDeleteResponse.html) post_externalcontacts_bulk_contacts_remove(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Contact ids |  |
{: class="table table-striped"}

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.html)

<a name="post_externalcontacts_bulk_contacts_unresolved"></a>

## [**BulkFetchContactsResponse**](BulkFetchContactsResponse.html) post_externalcontacts_bulk_contacts_unresolved(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Contact ids |  |
{: class="table table-striped"}

### Return type

[**BulkFetchContactsResponse**](BulkFetchContactsResponse.html)

<a name="post_externalcontacts_bulk_contacts_update"></a>

## [**BulkContactsResponse**](BulkContactsResponse.html) post_externalcontacts_bulk_contacts_update(body)



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
| **body** | [**BulkContactsRequest**](BulkContactsRequest.html)| Contacts |  |
{: class="table table-striped"}

### Return type

[**BulkContactsResponse**](BulkContactsResponse.html)

<a name="post_externalcontacts_bulk_notes"></a>

## [**BulkFetchNotesResponse**](BulkFetchNotesResponse.html) post_externalcontacts_bulk_notes(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Note ids |  |
{: class="table table-striped"}

### Return type

[**BulkFetchNotesResponse**](BulkFetchNotesResponse.html)

<a name="post_externalcontacts_bulk_notes_add"></a>

## [**BulkNotesResponse**](BulkNotesResponse.html) post_externalcontacts_bulk_notes_add(body)



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
| **body** | [**BulkNotesRequest**](BulkNotesRequest.html)| Notes |  |
{: class="table table-striped"}

### Return type

[**BulkNotesResponse**](BulkNotesResponse.html)

<a name="post_externalcontacts_bulk_notes_remove"></a>

## [**BulkDeleteResponse**](BulkDeleteResponse.html) post_externalcontacts_bulk_notes_remove(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Note ids |  |
{: class="table table-striped"}

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.html)

<a name="post_externalcontacts_bulk_notes_update"></a>

## [**BulkNotesResponse**](BulkNotesResponse.html) post_externalcontacts_bulk_notes_update(body)



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
| **body** | [**BulkNotesRequest**](BulkNotesRequest.html)| Notes |  |
{: class="table table-striped"}

### Return type

[**BulkNotesResponse**](BulkNotesResponse.html)

<a name="post_externalcontacts_bulk_organizations"></a>

## [**BulkFetchOrganizationsResponse**](BulkFetchOrganizationsResponse.html) post_externalcontacts_bulk_organizations(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Organizations ids |  |
{: class="table table-striped"}

### Return type

[**BulkFetchOrganizationsResponse**](BulkFetchOrganizationsResponse.html)

<a name="post_externalcontacts_bulk_organizations_add"></a>

## [**BulkOrganizationsResponse**](BulkOrganizationsResponse.html) post_externalcontacts_bulk_organizations_add(body)



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
| **body** | [**BulkOrganizationsRequest**](BulkOrganizationsRequest.html)| Organizations |  |
{: class="table table-striped"}

### Return type

[**BulkOrganizationsResponse**](BulkOrganizationsResponse.html)

<a name="post_externalcontacts_bulk_organizations_remove"></a>

## [**BulkDeleteResponse**](BulkDeleteResponse.html) post_externalcontacts_bulk_organizations_remove(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Organization ids |  |
{: class="table table-striped"}

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.html)

<a name="post_externalcontacts_bulk_organizations_update"></a>

## [**BulkOrganizationsResponse**](BulkOrganizationsResponse.html) post_externalcontacts_bulk_organizations_update(body)



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
| **body** | [**BulkOrganizationsRequest**](BulkOrganizationsRequest.html)| Organizations |  |
{: class="table table-striped"}

### Return type

[**BulkOrganizationsResponse**](BulkOrganizationsResponse.html)

<a name="post_externalcontacts_bulk_relationships"></a>

## [**BulkFetchRelationshipsResponse**](BulkFetchRelationshipsResponse.html) post_externalcontacts_bulk_relationships(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Relationships ids |  |
{: class="table table-striped"}

### Return type

[**BulkFetchRelationshipsResponse**](BulkFetchRelationshipsResponse.html)

<a name="post_externalcontacts_bulk_relationships_add"></a>

## [**BulkRelationshipsResponse**](BulkRelationshipsResponse.html) post_externalcontacts_bulk_relationships_add(body)



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
| **body** | [**BulkRelationshipsRequest**](BulkRelationshipsRequest.html)| Relationships |  |
{: class="table table-striped"}

### Return type

[**BulkRelationshipsResponse**](BulkRelationshipsResponse.html)

<a name="post_externalcontacts_bulk_relationships_remove"></a>

## [**BulkDeleteResponse**](BulkDeleteResponse.html) post_externalcontacts_bulk_relationships_remove(body)



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
| **body** | [**BulkIdsRequest**](BulkIdsRequest.html)| Relationships ids |  |
{: class="table table-striped"}

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.html)

<a name="post_externalcontacts_bulk_relationships_update"></a>

## [**BulkRelationshipsResponse**](BulkRelationshipsResponse.html) post_externalcontacts_bulk_relationships_update(body)



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
| **body** | [**BulkRelationshipsRequest**](BulkRelationshipsRequest.html)| Relationships |  |
{: class="table table-striped"}

### Return type

[**BulkRelationshipsResponse**](BulkRelationshipsResponse.html)

<a name="post_externalcontacts_contact_notes"></a>

## [**Note**](Note.html) post_externalcontacts_contact_notes(contact_id, body)



Create a note for an external contact



Wraps POST /api/v2/externalcontacts/contacts/{contactId}/notes 

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
| **body** | [**Note**](Note.html)| ExternalContact |  |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="post_externalcontacts_contact_promotion"></a>

## [**ExternalContact**](ExternalContact.html) post_externalcontacts_contact_promotion(contact_id)



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
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="post_externalcontacts_contacts"></a>

## [**ExternalContact**](ExternalContact.html) post_externalcontacts_contacts(body)



Create an external contact



Wraps POST /api/v2/externalcontacts/contacts 

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
| **body** | [**ExternalContact**](ExternalContact.html)| ExternalContact |  |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="post_externalcontacts_contacts_schemas"></a>

## [**DataSchema**](DataSchema.html) post_externalcontacts_contacts_schemas(body)



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
| **body** | [**DataSchema**](DataSchema.html)| Schema |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="post_externalcontacts_identifierlookup"></a>

## [**ExternalContact**](ExternalContact.html) post_externalcontacts_identifierlookup(identifier)



Fetch a contact using an identifier type and value.

Phone number identifier values must be provided with the country code and a leading '+' symbol. Example: \"+1 704 298 4733\"



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

try:
    # Fetch a contact using an identifier type and value.
    api_response = api_instance.post_externalcontacts_identifierlookup(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalContactsApi->post_externalcontacts_identifierlookup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **identifier** | [**ContactIdentifier**](ContactIdentifier.html)|  |  |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="post_externalcontacts_merge_contacts"></a>

## [**ExternalContact**](ExternalContact.html) post_externalcontacts_merge_contacts(body)



Merge two contacts into a new contact record

Two curated contacts cannot be merged. Refer to the Contact Merging article on the Developer Center for details



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
| **body** | [**MergeRequest**](MergeRequest.html)| MergeRequest |  |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="post_externalcontacts_organization_notes"></a>

## [**Note**](Note.html) post_externalcontacts_organization_notes(external_organization_id, body)



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
| **body** | [**Note**](Note.html)| ExternalContact |  |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="post_externalcontacts_organizations"></a>

## [**ExternalOrganization**](ExternalOrganization.html) post_externalcontacts_organizations(body)



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
| **body** | [**ExternalOrganization**](ExternalOrganization.html)| ExternalOrganization |  |
{: class="table table-striped"}

### Return type

[**ExternalOrganization**](ExternalOrganization.html)

<a name="post_externalcontacts_organizations_schemas"></a>

## [**DataSchema**](DataSchema.html) post_externalcontacts_organizations_schemas(body)



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
| **body** | [**DataSchema**](DataSchema.html)| Schema |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="post_externalcontacts_relationships"></a>

## [**Relationship**](Relationship.html) post_externalcontacts_relationships(body)



Create a relationship



Wraps POST /api/v2/externalcontacts/relationships 

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
| **body** | [**Relationship**](Relationship.html)| Relationship |  |
{: class="table table-striped"}

### Return type

[**Relationship**](Relationship.html)

<a name="put_externalcontacts_contact"></a>

## [**ExternalContact**](ExternalContact.html) put_externalcontacts_contact(contact_id, body)



Update an external contact



Wraps PUT /api/v2/externalcontacts/contacts/{contactId} 

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
| **body** | [**ExternalContact**](ExternalContact.html)| ExternalContact |  |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="put_externalcontacts_contact_note"></a>

## [**Note**](Note.html) put_externalcontacts_contact_note(contact_id, note_id, body)



Update a note for an external contact



Wraps PUT /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

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
| **body** | [**Note**](Note.html)| Note |  |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="put_externalcontacts_contacts_schema"></a>

## [**DataSchema**](DataSchema.html) put_externalcontacts_contacts_schema(schema_id, body)



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
| **body** | [**DataSchema**](DataSchema.html)| Data Schema |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="put_externalcontacts_conversation"></a>

##  put_externalcontacts_conversation(conversation_id, body)



Associate/disassociate an external contact with a conversation

To associate, supply a value for the externalContactId.  To disassociate, do not include the property at all.



Wraps PUT /api/v2/externalcontacts/conversations/{conversationId} 

Requires ANY permissions: 

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
| **body** | [**ConversationAssociation**](ConversationAssociation.html)| ConversationAssociation |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="put_externalcontacts_organization"></a>

## [**ExternalOrganization**](ExternalOrganization.html) put_externalcontacts_organization(external_organization_id, body)



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
| **body** | [**ExternalOrganization**](ExternalOrganization.html)| ExternalOrganization |  |
{: class="table table-striped"}

### Return type

[**ExternalOrganization**](ExternalOrganization.html)

<a name="put_externalcontacts_organization_note"></a>

## [**Note**](Note.html) put_externalcontacts_organization_note(external_organization_id, note_id, body)



Update a note for an external organization



Wraps PUT /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

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
| **body** | [**Note**](Note.html)| Note |  |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="put_externalcontacts_organization_trustor_trustor_id"></a>

## [**ExternalOrganizationTrustorLink**](ExternalOrganizationTrustorLink.html) put_externalcontacts_organization_trustor_trustor_id(external_organization_id, trustor_id)



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
{: class="table table-striped"}

### Return type

[**ExternalOrganizationTrustorLink**](ExternalOrganizationTrustorLink.html)

<a name="put_externalcontacts_organizations_schema"></a>

## [**DataSchema**](DataSchema.html) put_externalcontacts_organizations_schema(schema_id, body)



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
| **body** | [**DataSchema**](DataSchema.html)| Data Schema |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="put_externalcontacts_relationship"></a>

## [**Relationship**](Relationship.html) put_externalcontacts_relationship(relationship_id, body)



Update a relationship



Wraps PUT /api/v2/externalcontacts/relationships/{relationshipId} 

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
| **body** | [**Relationship**](Relationship.html)| Relationship |  |
{: class="table table-striped"}

### Return type

[**Relationship**](Relationship.html)

