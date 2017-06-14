
# Major Changes (8 changes)

**GET /api/v2/externalcontacts/organizations** (2 changes)

* Parameter expand was changed from string to array
* Parameter includeTrustors was added

**POST /api/v2/license/organization** (1 change)

* Response 200 type was changed from LicenseUpdateResponse to LicenseUpdateStatus[]

**GET /api/v2/externalcontacts/organizations/{externalOrganizationId}** (2 changes)

* Parameter expand was changed from array to string
* Parameter includeTrustors was added

**GET /api/v2/license/definitions** (1 change)

* Response 200 type was changed from LicenseDefinitionListing to LicenseDefinition[]

**LicenseUpdateResponse** (1 change)

* Model LicenseUpdateResponse was removed

**LicenseDefinitionListing** (1 change)

* Model LicenseDefinitionListing was removed


# Minor Changes (7 changes)

**/api/v2/externalcontacts/organizations/{externalOrganizationId}/trustor/{trustorId}** (2 changes)

* Path was added
* Operation PUT was added

**/api/v2/externalcontacts/organizations/{externalOrganizationId}/trustor** (2 changes)

* Path was added
* Operation DELETE was added

**OrgUser** (1 change)

* Model was added

**Trustor** (1 change)

* Model was added

**ExternalOrganization** (1 change)

* Optional property trustor was added


# Point Changes (0 changes)
