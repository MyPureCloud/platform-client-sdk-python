---
title: Relationship
---
## Relationship

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **user** | [**User**](User.html) | The user associated with the external organization. When creating or updating a relationship, only User.id is required. User object is fully populated when expanding a note. | |
| **external_organization** | [**ExternalOrganization**](ExternalOrganization.html) | The external organization this relationship is attached to | |
| **relationship** | **str** | The relationship or role of the user to this external organization.Examples: Account Manager, Sales Engineer, Implementation Consultant | |
| **external_data_sources** | [**list[ExternalDataSource]**](ExternalDataSource.html) | Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


