---
title: ExternalContactsApi
---

## PureCloudPlatformClientV2.ExternalContactsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_externalcontacts_contact**](ExternalContactsApi.html#delete_externalcontacts_contact) | Delete an external contact|
|[**delete_externalcontacts_contact_note**](ExternalContactsApi.html#delete_externalcontacts_contact_note) | Delete a note for an external contact|
|[**delete_externalcontacts_organization**](ExternalContactsApi.html#delete_externalcontacts_organization) | Delete an external organization|
|[**delete_externalcontacts_organization_note**](ExternalContactsApi.html#delete_externalcontacts_organization_note) | Delete a note for an external organization|
|[**delete_externalcontacts_organization_trustor**](ExternalContactsApi.html#delete_externalcontacts_organization_trustor) | Unlink the Trustor for this External Organization|
|[**delete_externalcontacts_relationship**](ExternalContactsApi.html#delete_externalcontacts_relationship) | Delete a relationship|
|[**get_externalcontacts_contact**](ExternalContactsApi.html#get_externalcontacts_contact) | Fetch an external contact|
|[**get_externalcontacts_contact_note**](ExternalContactsApi.html#get_externalcontacts_contact_note) | Fetch a note for an external contact|
|[**get_externalcontacts_contact_notes**](ExternalContactsApi.html#get_externalcontacts_contact_notes) | List notes for an external contact|
|[**get_externalcontacts_contacts**](ExternalContactsApi.html#get_externalcontacts_contacts) | Search for external contacts|
|[**get_externalcontacts_organization**](ExternalContactsApi.html#get_externalcontacts_organization) | Fetch an external organization|
|[**get_externalcontacts_organization_contacts**](ExternalContactsApi.html#get_externalcontacts_organization_contacts) | Search for external contacts in an external organization|
|[**get_externalcontacts_organization_note**](ExternalContactsApi.html#get_externalcontacts_organization_note) | Fetch a note for an external organization|
|[**get_externalcontacts_organization_notes**](ExternalContactsApi.html#get_externalcontacts_organization_notes) | List notes for an external organization|
|[**get_externalcontacts_organization_relationships**](ExternalContactsApi.html#get_externalcontacts_organization_relationships) | Fetch a relationship for an external organization|
|[**get_externalcontacts_organizations**](ExternalContactsApi.html#get_externalcontacts_organizations) | Search for external organizations|
|[**get_externalcontacts_relationship**](ExternalContactsApi.html#get_externalcontacts_relationship) | Fetch a relationship|
|[**get_externalcontacts_reversewhitepageslookup**](ExternalContactsApi.html#get_externalcontacts_reversewhitepageslookup) | Lookup contacts and externalOrganizations based on an attribute|
|[**post_externalcontacts_contact_notes**](ExternalContactsApi.html#post_externalcontacts_contact_notes) | Create a note for an external contact|
|[**post_externalcontacts_contacts**](ExternalContactsApi.html#post_externalcontacts_contacts) | Create an external contact|
|[**post_externalcontacts_organization_notes**](ExternalContactsApi.html#post_externalcontacts_organization_notes) | Create a note for an external organization|
|[**post_externalcontacts_organizations**](ExternalContactsApi.html#post_externalcontacts_organizations) | Create an external organization|
|[**post_externalcontacts_relationships**](ExternalContactsApi.html#post_externalcontacts_relationships) | Create a relationship|
|[**put_externalcontacts_contact**](ExternalContactsApi.html#put_externalcontacts_contact) | Update an external contact|
|[**put_externalcontacts_contact_note**](ExternalContactsApi.html#put_externalcontacts_contact_note) | Update a note for an external contact|
|[**put_externalcontacts_conversation**](ExternalContactsApi.html#put_externalcontacts_conversation) | Associate an external contact with a conversation|
|[**put_externalcontacts_organization**](ExternalContactsApi.html#put_externalcontacts_organization) | Update an external organization|
|[**put_externalcontacts_organization_note**](ExternalContactsApi.html#put_externalcontacts_organization_note) | Update a note for an external organization|
|[**put_externalcontacts_organization_trustor_trustor_id**](ExternalContactsApi.html#put_externalcontacts_organization_trustor_trustor_id) | Links a Trustor with an External Organization|
|[**put_externalcontacts_relationship**](ExternalContactsApi.html#put_externalcontacts_relationship) | Update a relationship|
{: class="table table-striped"}

<a name="delete_externalcontacts_contact"></a>

##  delete_externalcontacts_contact(contact_id)



Delete an external contact



Wraps DELETE /api/v2/externalcontacts/contacts/{contactId} 

Requires ANY permissions: 

* externalContacts:contact:delete

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact ID

try:
    # Delete an external contact
    api_instance.delete_externalcontacts_contact(contact_id)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->delete_externalcontacts_contact: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_contact_note"></a>

##  delete_externalcontacts_contact_note(contact_id, note_id)



Delete a note for an external contact



Wraps DELETE /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

Requires ANY permissions: 

* externalContacts:contact:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
contact_id = 'contact_id_example' # str | ExternalContact Id
note_id = 'note_id_example' # str | Note Id

try:
    # Delete a note for an external contact
    api_instance.delete_externalcontacts_contact_note(contact_id, note_id)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->delete_externalcontacts_contact_note: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **note_id** | **str**| Note Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_organization"></a>

##  delete_externalcontacts_organization(external_organization_id)



Delete an external organization



Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:delete

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID

try:
    # Delete an external organization
    api_instance.delete_externalcontacts_organization(external_organization_id)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->delete_externalcontacts_organization: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_organization_note"></a>

##  delete_externalcontacts_organization_note(external_organization_id, note_id)



Delete a note for an external organization



Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes/{noteId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization Id
note_id = 'note_id_example' # str | Note Id

try:
    # Delete a note for an external organization
    api_instance.delete_externalcontacts_organization_note(external_organization_id, note_id)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->delete_externalcontacts_organization_note: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **note_id** | **str**| Note Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_organization_trustor"></a>

##  delete_externalcontacts_organization_trustor(external_organization_id)



Unlink the Trustor for this External Organization



Wraps DELETE /api/v2/externalcontacts/organizations/{externalOrganizationId}/trustor 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID

try:
    # Unlink the Trustor for this External Organization
    api_instance.delete_externalcontacts_organization_trustor(external_organization_id)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->delete_externalcontacts_organization_trustor: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_externalcontacts_relationship"></a>

##  delete_externalcontacts_relationship(relationship_id)



Delete a relationship



Wraps DELETE /api/v2/externalcontacts/relationships/{relationshipId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
relationship_id = 'relationship_id_example' # str | Relationship Id

try:
    # Delete a relationship
    api_instance.delete_externalcontacts_relationship(relationship_id)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->delete_externalcontacts_relationship: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **relationship_id** | **str**| Relationship Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_externalcontacts_contact"></a>

## [**ExternalContact**](ExternalContact.html) get_externalcontacts_contact(contact_id, expand=expand)



Fetch an external contact



Wraps GET /api/v2/externalcontacts/contacts/{contactId} 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_contact: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand (externalOrganization,externalDataSources) | [optional] <br />**Values**: externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="get_externalcontacts_contact_note"></a>

## [**Note**](Note.html) get_externalcontacts_contact_note(contact_id, note_id, expand=expand)



Fetch a note for an external contact



Wraps GET /api/v2/externalcontacts/contacts/{contactId}/notes/{noteId} 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_contact_note: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_contact_notes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: author, externalDataSources |
{: class="table table-striped"}

### Return type

[**NoteListing**](NoteListing.html)

<a name="get_externalcontacts_contacts"></a>

## [**ContactListing**](ContactListing.html) get_externalcontacts_contacts(page_size=page_size, page_number=page_number, q=q, sort_order=sort_order, expand=expand)



Search for external contacts



Wraps GET /api/v2/externalcontacts/contacts 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_contacts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 1] |
| **q** | **str**| User supplied search keywords (no special syntax is currently supported) | [optional]  |
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ContactListing**](ContactListing.html)

<a name="get_externalcontacts_organization"></a>

## [**ExternalOrganization**](ExternalOrganization.html) get_externalcontacts_organization(external_organization_id, expand=expand, include_trustors=include_trustors)



Fetch an external organization



Wraps GET /api/v2/externalcontacts/organizations/{externalOrganizationId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
external_organization_id = 'external_organization_id_example' # str | External Organization ID
expand = 'expand_example' # str | which fields, if any, to expand (externalDataSources) (optional)
include_trustors = true # bool | (true or false) whether or not to include trustor information embedded in the externalOrganization (optional)

try:
    # Fetch an external organization
    api_response = api_instance.get_externalcontacts_organization(external_organization_id, expand=expand, include_trustors=include_trustors)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->get_externalcontacts_organization: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_organization_contacts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 1] |
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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_organization_note: %s\n" % e
~~~

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

* externalContacts:externalOrganization:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_organization_notes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization Id |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 1] |
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

* externalContacts:externalOrganization:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_organization_relationships: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 1] |
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

* externalContacts:externalOrganization:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
page_size = 20 # int | Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 20)
page_number = 1 # int | Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be <= 1,000) (optional) (default to 1)
q = 'q_example' # str | Search query (optional)
trustor_id = ['trustor_id_example'] # list[str] | Search for external organizations by trustorIds (limit 25). If supplied, the 'q' parameters is ignored. Items are returned in the order requested (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)
expand = ['expand_example'] # list[str] | which fields, if any, to expand (optional)
include_trustors = true # bool | (true or false) whether or not to include trustor information embedded in the externalOrganization (optional)

try:
    # Search for external organizations
    api_response = api_instance.get_externalcontacts_organizations(page_size=page_size, page_number=page_number, q=q, trustor_id=trustor_id, sort_order=sort_order, expand=expand, include_trustors=include_trustors)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->get_externalcontacts_organizations: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 20] |
| **page_number** | **int**| Page number (limited to fetching first 1,000 records; pageNumber * pageSize must be &lt;= 1,000) | [optional] [default to 1] |
| **q** | **str**| Search query | [optional]  |
| **trustor_id** | [**list[str]**](str.html)| Search for external organizations by trustorIds (limit 25). If supplied, the &#39;q&#39; parameters is ignored. Items are returned in the order requested | [optional]  |
| **sort_order** | **str**| Sort order | [optional]  |
| **expand** | [**list[str]**](str.html)| which fields, if any, to expand | [optional] <br />**Values**: externalDataSources |
| **include_trustors** | **bool**| (true or false) whether or not to include trustor information embedded in the externalOrganization | [optional]  |
{: class="table table-striped"}

### Return type

[**ExternalOrganizationListing**](ExternalOrganizationListing.html)

<a name="get_externalcontacts_relationship"></a>

## [**Relationship**](Relationship.html) get_externalcontacts_relationship(relationship_id, expand=expand)



Fetch a relationship



Wraps GET /api/v2/externalcontacts/relationships/{relationshipId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->get_externalcontacts_relationship: %s\n" % e
~~~

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



Lookup contacts and externalOrganizations based on an attribute



Wraps GET /api/v2/externalcontacts/reversewhitepageslookup 

Requires ANY permissions: 

* externalContacts:contact:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
lookup_val = 'lookup_val_example' # str | User supplied value to lookup contacts/externalOrganizations (supports email addresses, e164 phone numbers, Twitter screen names)
expand = ['expand_example'] # list[str] | which field, if any, to expand (optional)

try:
    # Lookup contacts and externalOrganizations based on an attribute
    api_response = api_instance.get_externalcontacts_reversewhitepageslookup(lookup_val, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->get_externalcontacts_reversewhitepageslookup: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **lookup_val** | **str**| User supplied value to lookup contacts/externalOrganizations (supports email addresses, e164 phone numbers, Twitter screen names) |  |
| **expand** | [**list[str]**](str.html)| which field, if any, to expand | [optional] <br />**Values**: contacts.externalOrganization, externalDataSources |
{: class="table table-striped"}

### Return type

[**ReverseWhitepagesLookupResult**](ReverseWhitepagesLookupResult.html)

<a name="post_externalcontacts_contact_notes"></a>

## [**Note**](Note.html) post_externalcontacts_contact_notes(contact_id, body)



Create a note for an external contact



Wraps POST /api/v2/externalcontacts/contacts/{contactId}/notes 

Requires ANY permissions: 

* externalContacts:contact:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->post_externalcontacts_contact_notes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **body** | [**Note**](Note.html)| ExternalContact |  |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="post_externalcontacts_contacts"></a>

## [**ExternalContact**](ExternalContact.html) post_externalcontacts_contacts(body)



Create an external contact



Wraps POST /api/v2/externalcontacts/contacts 

Requires ANY permissions: 

* externalContacts:contact:add

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ExternalContact() # ExternalContact | ExternalContact

try:
    # Create an external contact
    api_response = api_instance.post_externalcontacts_contacts(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->post_externalcontacts_contacts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalContact**](ExternalContact.html)| ExternalContact |  |
{: class="table table-striped"}

### Return type

[**ExternalContact**](ExternalContact.html)

<a name="post_externalcontacts_organization_notes"></a>

## [**Note**](Note.html) post_externalcontacts_organization_notes(external_organization_id, body)



Create a note for an external organization



Wraps POST /api/v2/externalcontacts/organizations/{externalOrganizationId}/notes 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->post_externalcontacts_organization_notes: %s\n" % e
~~~

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

* externalContacts:externalOrganization:add

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.ExternalOrganization() # ExternalOrganization | ExternalOrganization

try:
    # Create an external organization
    api_response = api_instance.post_externalcontacts_organizations(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->post_externalcontacts_organizations: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExternalOrganization**](ExternalOrganization.html)| ExternalOrganization |  |
{: class="table table-striped"}

### Return type

[**ExternalOrganization**](ExternalOrganization.html)

<a name="post_externalcontacts_relationships"></a>

## [**Relationship**](Relationship.html) post_externalcontacts_relationships(body)



Create a relationship



Wraps POST /api/v2/externalcontacts/relationships 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
body = PureCloudPlatformClientV2.Relationship() # Relationship | Relationship

try:
    # Create a relationship
    api_response = api_instance.post_externalcontacts_relationships(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->post_externalcontacts_relationships: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->put_externalcontacts_contact: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->put_externalcontacts_contact_note: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact Id |  |
| **note_id** | **str**| Note Id |  |
| **body** | [**Note**](Note.html)| Note |  |
{: class="table table-striped"}

### Return type

[**Note**](Note.html)

<a name="put_externalcontacts_conversation"></a>

##  put_externalcontacts_conversation(conversation_id, body)



Associate an external contact with a conversation



Wraps PUT /api/v2/externalcontacts/conversations/{conversationId} 

Requires ANY permissions: 

* externalContacts:conversation:associate

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ExternalContactsApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
body = PureCloudPlatformClientV2.ConversationAssociation() # ConversationAssociation | ConversationAssociation

try:
    # Associate an external contact with a conversation
    api_instance.put_externalcontacts_conversation(conversation_id, body)
except ApiException as e:
    print "Exception when calling ExternalContactsApi->put_externalcontacts_conversation: %s\n" % e
~~~

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

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->put_externalcontacts_organization: %s\n" % e
~~~

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

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->put_externalcontacts_organization_note: %s\n" % e
~~~

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

## [**ExternalOrganization**](ExternalOrganization.html) put_externalcontacts_organization_trustor_trustor_id(external_organization_id, trustor_id)



Links a Trustor with an External Organization



Wraps PUT /api/v2/externalcontacts/organizations/{externalOrganizationId}/trustor/{trustorId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->put_externalcontacts_organization_trustor_trustor_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_organization_id** | **str**| External Organization ID |  |
| **trustor_id** | **str**| Trustor ID |  |
{: class="table table-striped"}

### Return type

[**ExternalOrganization**](ExternalOrganization.html)

<a name="put_externalcontacts_relationship"></a>

## [**Relationship**](Relationship.html) put_externalcontacts_relationship(relationship_id, body)



Update a relationship



Wraps PUT /api/v2/externalcontacts/relationships/{relationshipId} 

Requires ANY permissions: 

* externalContacts:externalOrganization:edit

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ExternalContactsApi->put_externalcontacts_relationship: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **relationship_id** | **str**| Relationship Id |  |
| **body** | [**Relationship**](Relationship.html)| Relationship |  |
{: class="table table-striped"}

### Return type

[**Relationship**](Relationship.html)

