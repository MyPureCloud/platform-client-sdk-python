---
title: TelephonyProvidersEdgeApi
---

## PureCloudPlatformClientV2.TelephonyProvidersEdgeApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_telephony_providers_edge**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edge) | Delete a edge.|
|[**delete_telephony_providers_edge_logicalinterface**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edge_logicalinterface) | Delete an edge logical interface|
|[**delete_telephony_providers_edge_softwareupdate**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edge_softwareupdate) | Cancels any in-progress update for this edge.|
|[**delete_telephony_providers_edges_certificateauthority**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_certificateauthority) | Delete a certificate authority.|
|[**delete_telephony_providers_edges_didpool**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_didpool) | Delete a DID Pool by ID.|
|[**delete_telephony_providers_edges_edgegroup**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_edgegroup) | Delete an edge group.|
|[**delete_telephony_providers_edges_extensionpool**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_extensionpool) | Delete an extension pool by ID|
|[**delete_telephony_providers_edges_phone**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_phone) | Delete a Phone by ID|
|[**delete_telephony_providers_edges_phonebasesetting**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_phonebasesetting) | Delete a Phone Base Settings by ID|
|[**delete_telephony_providers_edges_site**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_site) | Delete a Site by ID|
|[**delete_telephony_providers_edges_site_outboundroute**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_site_outboundroute) | Delete Outbound Route|
|[**delete_telephony_providers_edges_trunkbasesetting**](TelephonyProvidersEdgeApi.html#delete_telephony_providers_edges_trunkbasesetting) | Delete a Trunk Base Settings object by ID|
|[**get_telephony_providers_edge**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge) | Get edge.|
|[**get_telephony_providers_edge_diagnostic_nslookup**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_diagnostic_nslookup) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_diagnostic_ping**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_diagnostic_ping) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_diagnostic_route**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_diagnostic_route) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_diagnostic_tracepath**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_diagnostic_tracepath) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_logicalinterface**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_logicalinterface) | Get an edge logical interface|
|[**get_telephony_providers_edge_logicalinterfaces**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_logicalinterfaces) | Get edge logical interfaces.|
|[**get_telephony_providers_edge_logs_job**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_logs_job) | Get an Edge logs job.|
|[**get_telephony_providers_edge_metrics**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_metrics) | Get the edge metrics.|
|[**get_telephony_providers_edge_physicalinterface**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_physicalinterface) | Get edge physical interface.|
|[**get_telephony_providers_edge_physicalinterfaces**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_physicalinterfaces) | Retrieve a list of all configured physical interfaces from a specific edge.|
|[**get_telephony_providers_edge_setuppackage**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_setuppackage) | Get the setup package for a locally deployed edge device. This is needed to complete the setup process for the virtual edge.|
|[**get_telephony_providers_edge_softwareupdate**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_softwareupdate) | Gets software update status information about any edge.|
|[**get_telephony_providers_edge_softwareversions**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_softwareversions) | Gets all the available software versions for this edge.|
|[**get_telephony_providers_edge_trunks**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edge_trunks) | Get the list of available trunks for the given Edge.|
|[**get_telephony_providers_edges**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges) | Get the list of edges.|
|[**get_telephony_providers_edges_availablelanguages**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_availablelanguages) | Get the list of available languages. For never released keyword spotting feature. Deprecated, do not use.|
|[**get_telephony_providers_edges_certificateauthorities**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_certificateauthorities) | Get the list of certificate authorities.|
|[**get_telephony_providers_edges_certificateauthority**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_certificateauthority) | Get a certificate authority.|
|[**get_telephony_providers_edges_did**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_did) | Get a DID by ID.|
|[**get_telephony_providers_edges_didpool**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_didpool) | Get a DID Pool by ID.|
|[**get_telephony_providers_edges_didpools**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_didpools) | Get a listing of DID Pools|
|[**get_telephony_providers_edges_didpools_dids**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_didpools_dids) | Get a listing of unassigned and/or assigned numbers in a set of DID Pools.|
|[**get_telephony_providers_edges_dids**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_dids) | Get a listing of DIDs|
|[**get_telephony_providers_edges_edgegroup**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_edgegroup) | Get edge group.|
|[**get_telephony_providers_edges_edgegroup_edgetrunkbase**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_edgegroup_edgetrunkbase) | Gets the edge trunk base associated with the edge group|
|[**get_telephony_providers_edges_edgegroups**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_edgegroups) | Get the list of edge groups.|
|[**get_telephony_providers_edges_edgeversionreport**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_edgeversionreport) | Get the edge version report.|
|[**get_telephony_providers_edges_expired**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_expired) | List of edges more than 4 edge versions behind the latest software.|
|[**get_telephony_providers_edges_extension**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_extension) | Get an extension by ID.|
|[**get_telephony_providers_edges_extensionpool**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_extensionpool) | Get an extension pool by ID|
|[**get_telephony_providers_edges_extensionpools**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_extensionpools) | Get a listing of extension pools|
|[**get_telephony_providers_edges_extensionpools_divisionviews**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_extensionpools_divisionviews) | Get a pageable list of basic extension pool objects filterable by query parameters.|
|[**get_telephony_providers_edges_extensions**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_extensions) | Get a listing of extensions|
|[**get_telephony_providers_edges_line**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_line) | Get a Line by ID|
|[**get_telephony_providers_edges_linebasesetting**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_linebasesetting) | Get a line base settings object by ID|
|[**get_telephony_providers_edges_linebasesettings**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_linebasesettings) | Get a listing of line base settings objects|
|[**get_telephony_providers_edges_lines**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_lines) | Get a list of Lines|
|[**get_telephony_providers_edges_lines_template**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_lines_template) | Get a Line instance template based on a Line Base Settings object. This object can then be modified and saved as a new Line instance|
|[**get_telephony_providers_edges_logicalinterfaces**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_logicalinterfaces) | Get edge logical interfaces.|
|[**get_telephony_providers_edges_mediastatistics_conversation**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_mediastatistics_conversation) | Get media endpoint statistics events.|
|[**get_telephony_providers_edges_mediastatistics_conversation_communication**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_mediastatistics_conversation_communication) | Get media endpoint statistics event.|
|[**get_telephony_providers_edges_metrics**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_metrics) | Get the metrics for a list of edges.|
|[**get_telephony_providers_edges_outboundroutes**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_outboundroutes) | Get outbound routes|
|[**get_telephony_providers_edges_phone**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phone) | Get a Phone by ID|
|[**get_telephony_providers_edges_phonebasesetting**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phonebasesetting) | Get a Phone Base Settings object by ID|
|[**get_telephony_providers_edges_phonebasesettings**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phonebasesettings) | Get a list of Phone Base Settings objects|
|[**get_telephony_providers_edges_phonebasesettings_availablemetabases**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phonebasesettings_availablemetabases) | Get a list of available makes and models to create a new Phone Base Settings|
|[**get_telephony_providers_edges_phonebasesettings_template**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phonebasesettings_template) | Get a Phone Base Settings instance template from a given make and model. This object can then be modified and saved as a new Phone Base Settings instance|
|[**get_telephony_providers_edges_phones**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phones) | Get a list of Phone Instances. A maximum of 10,000 results is returned when filtering the results or sorting by a field other than the ID. Sorting by only the ID has no result limit. Each filter supports a wildcard, *, as a value to search for partial values.|
|[**get_telephony_providers_edges_phones_template**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_phones_template) | Get a Phone instance template based on a Phone Base Settings object. This object can then be modified and saved as a new Phone instance|
|[**get_telephony_providers_edges_physicalinterfaces**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_physicalinterfaces) | Get physical interfaces for edges.|
|[**get_telephony_providers_edges_site**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site) | Get a Site by ID.|
|[**get_telephony_providers_edges_site_numberplan**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site_numberplan) | Get a Number Plan by ID.|
|[**get_telephony_providers_edges_site_numberplans**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site_numberplans) | Get the list of Number Plans for this Site. Only fetches the first 200 records.|
|[**get_telephony_providers_edges_site_numberplans_classifications**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site_numberplans_classifications) | Get a list of Classifications for this Site|
|[**get_telephony_providers_edges_site_outboundroute**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site_outboundroute) | Get an outbound route|
|[**get_telephony_providers_edges_site_outboundroutes**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site_outboundroutes) | Get outbound routes|
|[**get_telephony_providers_edges_site_siteconnections**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_site_siteconnections) | Get site connections for a site.|
|[**get_telephony_providers_edges_sites**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_sites) | Get the list of Sites.|
|[**get_telephony_providers_edges_timezones**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_timezones) | Get a list of Edge-compatible time zones|
|[**get_telephony_providers_edges_trunk**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunk) | Get a Trunk by ID|
|[**get_telephony_providers_edges_trunk_metrics**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunk_metrics) | Get the trunk metrics.|
|[**get_telephony_providers_edges_trunkbasesetting**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunkbasesetting) | Get a Trunk Base Settings object by ID|
|[**get_telephony_providers_edges_trunkbasesettings**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunkbasesettings) | Get Trunk Base Settings listing|
|[**get_telephony_providers_edges_trunkbasesettings_availablemetabases**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunkbasesettings_availablemetabases) | Get a list of available makes and models to create a new Trunk Base Settings|
|[**get_telephony_providers_edges_trunkbasesettings_template**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunkbasesettings_template) | Get a Trunk Base Settings instance template from a given make and model. This object can then be modified and saved as a new Trunk Base Settings instance|
|[**get_telephony_providers_edges_trunks**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunks) | Get the list of available trunks.|
|[**get_telephony_providers_edges_trunks_metrics**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunks_metrics) | Get the metrics for a list of trunks.|
|[**get_telephony_providers_edges_trunkswithrecording**](TelephonyProvidersEdgeApi.html#get_telephony_providers_edges_trunkswithrecording) | Get Counts of trunks that have recording disabled or enabled|
|[**patch_telephony_providers_edges_site_siteconnections**](TelephonyProvidersEdgeApi.html#patch_telephony_providers_edges_site_siteconnections) | Disable site connections for a site.|
|[**post_telephony_providers_edge_diagnostic_nslookup**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_diagnostic_nslookup) | Nslookup request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_diagnostic_ping**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_diagnostic_ping) | Ping Request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_diagnostic_route**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_diagnostic_route) | Route request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_diagnostic_tracepath**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_diagnostic_tracepath) | Tracepath request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_logicalinterfaces**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_logicalinterfaces) | Create an edge logical interface.|
|[**post_telephony_providers_edge_logs_job_upload**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_logs_job_upload) | Request that the specified fileIds be uploaded from the Edge.|
|[**post_telephony_providers_edge_logs_jobs**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_logs_jobs) | Create a job to upload a list of Edge logs.|
|[**post_telephony_providers_edge_reboot**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_reboot) | Reboot an Edge|
|[**post_telephony_providers_edge_softwareupdate**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_softwareupdate) | Starts a software update for this edge.|
|[**post_telephony_providers_edge_statuscode**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_statuscode) | Take an Edge in or out of service|
|[**post_telephony_providers_edge_unpair**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edge_unpair) | Unpair an Edge|
|[**post_telephony_providers_edges**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges) | Create an edge.|
|[**post_telephony_providers_edges_addressvalidation**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_addressvalidation) | Validates a street address|
|[**post_telephony_providers_edges_certificateauthorities**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_certificateauthorities) | Create a certificate authority.|
|[**post_telephony_providers_edges_didpools**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_didpools) | Create a new DID pool|
|[**post_telephony_providers_edges_edgegroups**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_edgegroups) | Create an edge group.|
|[**post_telephony_providers_edges_extensionpools**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_extensionpools) | Create a new extension pool|
|[**post_telephony_providers_edges_phone_reboot**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_phone_reboot) | Reboot a Phone|
|[**post_telephony_providers_edges_phonebasesettings**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_phonebasesettings) | Create a new Phone Base Settings object|
|[**post_telephony_providers_edges_phones**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_phones) | Create a new Phone|
|[**post_telephony_providers_edges_phones_reboot**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_phones_reboot) | Reboot Multiple Phones|
|[**post_telephony_providers_edges_site_outboundroutes**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_site_outboundroutes) | Create outbound route|
|[**post_telephony_providers_edges_sites**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_sites) | Create a Site.|
|[**post_telephony_providers_edges_trunkbasesettings**](TelephonyProvidersEdgeApi.html#post_telephony_providers_edges_trunkbasesettings) | Create a Trunk Base Settings object|
|[**put_telephony_providers_edge**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edge) | Update a edge.|
|[**put_telephony_providers_edge_logicalinterface**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edge_logicalinterface) | Update an edge logical interface.|
|[**put_telephony_providers_edges_certificateauthority**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_certificateauthority) | Update a certificate authority.|
|[**put_telephony_providers_edges_didpool**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_didpool) | Update a DID Pool by ID.|
|[**put_telephony_providers_edges_edgegroup**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_edgegroup) | Update an edge group.|
|[**put_telephony_providers_edges_edgegroup_edgetrunkbase**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_edgegroup_edgetrunkbase) | Update the edge trunk base associated with the edge group|
|[**put_telephony_providers_edges_extensionpool**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_extensionpool) | Update an extension pool by ID|
|[**put_telephony_providers_edges_phone**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_phone) | Update a Phone by ID|
|[**put_telephony_providers_edges_phonebasesetting**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_phonebasesetting) | Update a Phone Base Settings by ID|
|[**put_telephony_providers_edges_site**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_site) | Update a Site by ID.|
|[**put_telephony_providers_edges_site_numberplans**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_site_numberplans) | Update the list of Number Plans. A user can update maximum 200 number plans at a time.|
|[**put_telephony_providers_edges_site_outboundroute**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_site_outboundroute) | Update outbound route|
|[**put_telephony_providers_edges_site_siteconnections**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_site_siteconnections) | Update site connections for a site.|
|[**put_telephony_providers_edges_trunkbasesetting**](TelephonyProvidersEdgeApi.html#put_telephony_providers_edges_trunkbasesetting) | Update a Trunk Base Settings object by ID|
{: class="table table-striped"}

<a name="delete_telephony_providers_edge"></a>

##  delete_telephony_providers_edge(edge_id)



Delete a edge.

Wraps DELETE /api/v2/telephony/providers/edges/{edgeId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID

try:
    # Delete a edge.
    api_instance.delete_telephony_providers_edge(edge_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edge_logicalinterface"></a>

##  delete_telephony_providers_edge_logicalinterface(edge_id, interface_id)



Delete an edge logical interface

Wraps DELETE /api/v2/telephony/providers/edges/{edgeId}/logicalinterfaces/{interfaceId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
interface_id = 'interface_id_example' # str | Interface ID

try:
    # Delete an edge logical interface
    api_instance.delete_telephony_providers_edge_logicalinterface(edge_id, interface_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edge_logicalinterface: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **interface_id** | **str**| Interface ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edge_softwareupdate"></a>

##  delete_telephony_providers_edge_softwareupdate(edge_id)



Cancels any in-progress update for this edge.

Wraps DELETE /api/v2/telephony/providers/edges/{edgeId}/softwareupdate 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID

try:
    # Cancels any in-progress update for this edge.
    api_instance.delete_telephony_providers_edge_softwareupdate(edge_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edge_softwareupdate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_certificateauthority"></a>

##  delete_telephony_providers_edges_certificateauthority(certificate_id)



Delete a certificate authority.

Wraps DELETE /api/v2/telephony/providers/edges/certificateauthorities/{certificateId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Delete a certificate authority.
    api_instance.delete_telephony_providers_edges_certificateauthority(certificate_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_certificateauthority: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **certificate_id** | **str**| Certificate ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_didpool"></a>

##  delete_telephony_providers_edges_didpool(did_pool_id)



Delete a DID Pool by ID.

Wraps DELETE /api/v2/telephony/providers/edges/didpools/{didPoolId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
did_pool_id = 'did_pool_id_example' # str | DID pool ID

try:
    # Delete a DID Pool by ID.
    api_instance.delete_telephony_providers_edges_didpool(did_pool_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_didpool: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **did_pool_id** | **str**| DID pool ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_edgegroup"></a>

##  delete_telephony_providers_edges_edgegroup(edge_group_id)



Delete an edge group.

Wraps DELETE /api/v2/telephony/providers/edges/edgegroups/{edgeGroupId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_group_id = 'edge_group_id_example' # str | Edge group ID

try:
    # Delete an edge group.
    api_instance.delete_telephony_providers_edges_edgegroup(edge_group_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_edgegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_group_id** | **str**| Edge group ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_extensionpool"></a>

##  delete_telephony_providers_edges_extensionpool(extension_pool_id)



Delete an extension pool by ID

Wraps DELETE /api/v2/telephony/providers/edges/extensionpools/{extensionPoolId} 

Requires ALL permissions: 

* telephony:extensionPool:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
extension_pool_id = 'extension_pool_id_example' # str | Extension pool ID

try:
    # Delete an extension pool by ID
    api_instance.delete_telephony_providers_edges_extensionpool(extension_pool_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_extensionpool: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **extension_pool_id** | **str**| Extension pool ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_phone"></a>

##  delete_telephony_providers_edges_phone(phone_id)



Delete a Phone by ID

Wraps DELETE /api/v2/telephony/providers/edges/phones/{phoneId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_id = 'phone_id_example' # str | Phone ID

try:
    # Delete a Phone by ID
    api_instance.delete_telephony_providers_edges_phone(phone_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_phone: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_id** | **str**| Phone ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_phonebasesetting"></a>

##  delete_telephony_providers_edges_phonebasesetting(phone_base_id)



Delete a Phone Base Settings by ID

Wraps DELETE /api/v2/telephony/providers/edges/phonebasesettings/{phoneBaseId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_base_id = 'phone_base_id_example' # str | Phone base ID

try:
    # Delete a Phone Base Settings by ID
    api_instance.delete_telephony_providers_edges_phonebasesetting(phone_base_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_phonebasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_base_id** | **str**| Phone base ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_site"></a>

##  delete_telephony_providers_edges_site(site_id)



Delete a Site by ID

Wraps DELETE /api/v2/telephony/providers/edges/sites/{siteId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID

try:
    # Delete a Site by ID
    api_instance.delete_telephony_providers_edges_site(site_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_site: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_site_outboundroute"></a>

##  delete_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id)



Delete Outbound Route

Wraps DELETE /api/v2/telephony/providers/edges/sites/{siteId}/outboundroutes/{outboundRouteId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
outbound_route_id = 'outbound_route_id_example' # str | Outbound route ID

try:
    # Delete Outbound Route
    api_instance.delete_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_site_outboundroute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **outbound_route_id** | **str**| Outbound route ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_telephony_providers_edges_trunkbasesetting"></a>

##  delete_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id)



Delete a Trunk Base Settings object by ID

Wraps DELETE /api/v2/telephony/providers/edges/trunkbasesettings/{trunkBaseSettingsId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_base_settings_id = 'trunk_base_settings_id_example' # str | Trunk Base ID

try:
    # Delete a Trunk Base Settings object by ID
    api_instance.delete_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_trunkbasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_base_settings_id** | **str**| Trunk Base ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_telephony_providers_edge"></a>

## [**Edge**](Edge.html) get_telephony_providers_edge(edge_id, expand=expand)



Get edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)

try:
    # Get edge.
    api_response = api_instance.get_telephony_providers_edge(edge_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: site |
{: class="table table-striped"}

### Return type

[**Edge**](Edge.html)

<a name="get_telephony_providers_edge_diagnostic_nslookup"></a>

## [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html) get_telephony_providers_edge_diagnostic_nslookup(edge_id)



Get networking-related information from an Edge for a target IP or host.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/diagnostic/nslookup 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id

try:
    # Get networking-related information from an Edge for a target IP or host.
    api_response = api_instance.get_telephony_providers_edge_diagnostic_nslookup(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_diagnostic_nslookup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html)

<a name="get_telephony_providers_edge_diagnostic_ping"></a>

## [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html) get_telephony_providers_edge_diagnostic_ping(edge_id)



Get networking-related information from an Edge for a target IP or host.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/diagnostic/ping 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id

try:
    # Get networking-related information from an Edge for a target IP or host.
    api_response = api_instance.get_telephony_providers_edge_diagnostic_ping(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_diagnostic_ping: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html)

<a name="get_telephony_providers_edge_diagnostic_route"></a>

## [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html) get_telephony_providers_edge_diagnostic_route(edge_id)



Get networking-related information from an Edge for a target IP or host.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/diagnostic/route 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id

try:
    # Get networking-related information from an Edge for a target IP or host.
    api_response = api_instance.get_telephony_providers_edge_diagnostic_route(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_diagnostic_route: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html)

<a name="get_telephony_providers_edge_diagnostic_tracepath"></a>

## [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html) get_telephony_providers_edge_diagnostic_tracepath(edge_id)



Get networking-related information from an Edge for a target IP or host.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/diagnostic/tracepath 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id

try:
    # Get networking-related information from an Edge for a target IP or host.
    api_response = api_instance.get_telephony_providers_edge_diagnostic_tracepath(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_diagnostic_tracepath: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse.html)

<a name="get_telephony_providers_edge_logicalinterface"></a>

## [**DomainLogicalInterface**](DomainLogicalInterface.html) get_telephony_providers_edge_logicalinterface(edge_id, interface_id, expand=expand)



Get an edge logical interface

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/logicalinterfaces/{interfaceId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
interface_id = 'interface_id_example' # str | Interface ID
expand = ['expand_example'] # list[str] | Field to expand in the response (optional)

try:
    # Get an edge logical interface
    api_response = api_instance.get_telephony_providers_edge_logicalinterface(edge_id, interface_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_logicalinterface: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **interface_id** | **str**| Interface ID |  |
| **expand** | [**list[str]**](str.html)| Field to expand in the response | [optional] <br />**Values**: externalTrunkBaseAssignments, phoneTrunkBaseAssignments |
{: class="table table-striped"}

### Return type

[**DomainLogicalInterface**](DomainLogicalInterface.html)

<a name="get_telephony_providers_edge_logicalinterfaces"></a>

## [**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing.html) get_telephony_providers_edge_logicalinterfaces(edge_id, expand=expand)



Get edge logical interfaces.

Retrieve a list of all configured logical interfaces from a specific edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/logicalinterfaces 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
expand = ['expand_example'] # list[str] | Field to expand in the response (optional)

try:
    # Get edge logical interfaces.
    api_response = api_instance.get_telephony_providers_edge_logicalinterfaces(edge_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_logicalinterfaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **expand** | [**list[str]**](str.html)| Field to expand in the response | [optional] <br />**Values**: externalTrunkBaseAssignments, phoneTrunkBaseAssignments |
{: class="table table-striped"}

### Return type

[**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing.html)

<a name="get_telephony_providers_edge_logs_job"></a>

## [**EdgeLogsJob**](EdgeLogsJob.html) get_telephony_providers_edge_logs_job(edge_id, job_id)



Get an Edge logs job.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/logs/jobs/{jobId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
job_id = 'job_id_example' # str | Job ID

try:
    # Get an Edge logs job.
    api_response = api_instance.get_telephony_providers_edge_logs_job(edge_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_logs_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **job_id** | **str**| Job ID |  |
{: class="table table-striped"}

### Return type

[**EdgeLogsJob**](EdgeLogsJob.html)

<a name="get_telephony_providers_edge_metrics"></a>

## [**EdgeMetrics**](EdgeMetrics.html) get_telephony_providers_edge_metrics(edge_id)



Get the edge metrics.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/metrics 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id

try:
    # Get the edge metrics.
    api_response = api_instance.get_telephony_providers_edge_metrics(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
{: class="table table-striped"}

### Return type

[**EdgeMetrics**](EdgeMetrics.html)

<a name="get_telephony_providers_edge_physicalinterface"></a>

## [**DomainPhysicalInterface**](DomainPhysicalInterface.html) get_telephony_providers_edge_physicalinterface(edge_id, interface_id)



Get edge physical interface.

Retrieve a physical interface from a specific edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/physicalinterfaces/{interfaceId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
interface_id = 'interface_id_example' # str | Interface ID

try:
    # Get edge physical interface.
    api_response = api_instance.get_telephony_providers_edge_physicalinterface(edge_id, interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_physicalinterface: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **interface_id** | **str**| Interface ID |  |
{: class="table table-striped"}

### Return type

[**DomainPhysicalInterface**](DomainPhysicalInterface.html)

<a name="get_telephony_providers_edge_physicalinterfaces"></a>

## [**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing.html) get_telephony_providers_edge_physicalinterfaces(edge_id)



Retrieve a list of all configured physical interfaces from a specific edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/physicalinterfaces 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID

try:
    # Retrieve a list of all configured physical interfaces from a specific edge.
    api_response = api_instance.get_telephony_providers_edge_physicalinterfaces(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_physicalinterfaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
{: class="table table-striped"}

### Return type

[**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing.html)

<a name="get_telephony_providers_edge_setuppackage"></a>

## [**VmPairingInfo**](VmPairingInfo.html) get_telephony_providers_edge_setuppackage(edge_id)



Get the setup package for a locally deployed edge device. This is needed to complete the setup process for the virtual edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/setuppackage 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID

try:
    # Get the setup package for a locally deployed edge device. This is needed to complete the setup process for the virtual edge.
    api_response = api_instance.get_telephony_providers_edge_setuppackage(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_setuppackage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
{: class="table table-striped"}

### Return type

[**VmPairingInfo**](VmPairingInfo.html)

<a name="get_telephony_providers_edge_softwareupdate"></a>

## [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto.html) get_telephony_providers_edge_softwareupdate(edge_id)



Gets software update status information about any edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/softwareupdate 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID

try:
    # Gets software update status information about any edge.
    api_response = api_instance.get_telephony_providers_edge_softwareupdate(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_softwareupdate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
{: class="table table-striped"}

### Return type

[**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto.html)

<a name="get_telephony_providers_edge_softwareversions"></a>

## [**DomainEdgeSoftwareVersionDtoEntityListing**](DomainEdgeSoftwareVersionDtoEntityListing.html) get_telephony_providers_edge_softwareversions(edge_id)



Gets all the available software versions for this edge.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/softwareversions 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID

try:
    # Gets all the available software versions for this edge.
    api_response = api_instance.get_telephony_providers_edge_softwareversions(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_softwareversions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
{: class="table table-striped"}

### Return type

[**DomainEdgeSoftwareVersionDtoEntityListing**](DomainEdgeSoftwareVersionDtoEntityListing.html)

<a name="get_telephony_providers_edge_trunks"></a>

## [**TrunkEntityListing**](TrunkEntityListing.html) get_telephony_providers_edge_trunks(edge_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, trunk_base_id=trunk_base_id, trunk_type=trunk_type)



Get the list of available trunks for the given Edge.

Trunks are created by assigning trunk base settings to an Edge or Edge Group.

Wraps GET /api/v2/telephony/providers/edges/{edgeId}/trunks 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = ''name'' # str | Value by which to sort (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
trunk_base_id = 'trunk_base_id_example' # str | Filter by Trunk Base Ids (optional)
trunk_type = 'trunk_type_example' # str | Filter by a Trunk type (optional)

try:
    # Get the list of available trunks for the given Edge.
    api_response = api_instance.get_telephony_providers_edge_trunks(edge_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, trunk_base_id=trunk_base_id, trunk_type=trunk_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edge_trunks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Value by which to sort | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **trunk_base_id** | **str**| Filter by Trunk Base Ids | [optional]  |
| **trunk_type** | **str**| Filter by a Trunk type | [optional] <br />**Values**: EXTERNAL, PHONE, EDGE |
{: class="table table-striped"}

### Return type

[**TrunkEntityListing**](TrunkEntityListing.html)

<a name="get_telephony_providers_edges"></a>

## [**EdgeEntityListing**](EdgeEntityListing.html) get_telephony_providers_edges(page_size=page_size, page_number=page_number, name=name, site_id=site_id, edge_group_id=edge_group_id, sort_by=sort_by, managed=managed, show_cloud_media=show_cloud_media)



Get the list of edges.

Wraps GET /api/v2/telephony/providers/edges 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
site_id = 'site_id_example' # str | Filter by site.id (optional)
edge_group_id = 'edge_group_id_example' # str | Filter by edgeGroup.id (optional)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
managed = True # bool | Filter by managed (optional)
show_cloud_media = True # bool | True to show the cloud media devices in the result. (optional) (default to True)

try:
    # Get the list of edges.
    api_response = api_instance.get_telephony_providers_edges(page_size=page_size, page_number=page_number, name=name, site_id=site_id, edge_group_id=edge_group_id, sort_by=sort_by, managed=managed, show_cloud_media=show_cloud_media)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **site_id** | **str**| Filter by site.id | [optional]  |
| **edge_group_id** | **str**| Filter by edgeGroup.id | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **managed** | **bool**| Filter by managed | [optional]  |
| **show_cloud_media** | **bool**| True to show the cloud media devices in the result. | [optional] [default to True] |
{: class="table table-striped"}

### Return type

[**EdgeEntityListing**](EdgeEntityListing.html)

<a name="get_telephony_providers_edges_availablelanguages"></a>

## [**AvailableLanguageList**](AvailableLanguageList.html) get_telephony_providers_edges_availablelanguages()

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the list of available languages. For never released keyword spotting feature. Deprecated, do not use.

Wraps GET /api/v2/telephony/providers/edges/availablelanguages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()

try:
    # Get the list of available languages. For never released keyword spotting feature. Deprecated, do not use.
    api_response = api_instance.get_telephony_providers_edges_availablelanguages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_availablelanguages: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**AvailableLanguageList**](AvailableLanguageList.html)

<a name="get_telephony_providers_edges_certificateauthorities"></a>

## [**CertificateAuthorityEntityListing**](CertificateAuthorityEntityListing.html) get_telephony_providers_edges_certificateauthorities()



Get the list of certificate authorities.

Wraps GET /api/v2/telephony/providers/edges/certificateauthorities 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()

try:
    # Get the list of certificate authorities.
    api_response = api_instance.get_telephony_providers_edges_certificateauthorities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_certificateauthorities: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**CertificateAuthorityEntityListing**](CertificateAuthorityEntityListing.html)

<a name="get_telephony_providers_edges_certificateauthority"></a>

## [**DomainCertificateAuthority**](DomainCertificateAuthority.html) get_telephony_providers_edges_certificateauthority(certificate_id)



Get a certificate authority.

Wraps GET /api/v2/telephony/providers/edges/certificateauthorities/{certificateId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Get a certificate authority.
    api_response = api_instance.get_telephony_providers_edges_certificateauthority(certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_certificateauthority: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **certificate_id** | **str**| Certificate ID |  |
{: class="table table-striped"}

### Return type

[**DomainCertificateAuthority**](DomainCertificateAuthority.html)

<a name="get_telephony_providers_edges_did"></a>

## [**DID**](DID.html) get_telephony_providers_edges_did(did_id)



Get a DID by ID.

Wraps GET /api/v2/telephony/providers/edges/dids/{didId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
did_id = 'did_id_example' # str | DID ID

try:
    # Get a DID by ID.
    api_response = api_instance.get_telephony_providers_edges_did(did_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_did: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **did_id** | **str**| DID ID |  |
{: class="table table-striped"}

### Return type

[**DID**](DID.html)

<a name="get_telephony_providers_edges_didpool"></a>

## [**DIDPool**](DIDPool.html) get_telephony_providers_edges_didpool(did_pool_id)



Get a DID Pool by ID.

Wraps GET /api/v2/telephony/providers/edges/didpools/{didPoolId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
did_pool_id = 'did_pool_id_example' # str | DID pool ID

try:
    # Get a DID Pool by ID.
    api_response = api_instance.get_telephony_providers_edges_didpool(did_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_didpool: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **did_pool_id** | **str**| DID pool ID |  |
{: class="table table-striped"}

### Return type

[**DIDPool**](DIDPool.html)

<a name="get_telephony_providers_edges_didpools"></a>

## [**DIDPoolEntityListing**](DIDPoolEntityListing.html) get_telephony_providers_edges_didpools(page_size=page_size, page_number=page_number, sort_by=sort_by, id=id)



Get a listing of DID Pools

Wraps GET /api/v2/telephony/providers/edges/didpools 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''number'' # str | Sort by (optional) (default to 'number')
id = ['id_example'] # list[str] | Filter by a specific list of ID's (optional)

try:
    # Get a listing of DID Pools
    api_response = api_instance.get_telephony_providers_edges_didpools(page_size=page_size, page_number=page_number, sort_by=sort_by, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_didpools: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;number&#39;] |
| **id** | [**list[str]**](str.html)| Filter by a specific list of ID&#39;s | [optional]  |
{: class="table table-striped"}

### Return type

[**DIDPoolEntityListing**](DIDPoolEntityListing.html)

<a name="get_telephony_providers_edges_didpools_dids"></a>

## [**DIDNumberEntityListing**](DIDNumberEntityListing.html) get_telephony_providers_edges_didpools_dids(type, id=id, number_match=number_match, page_size=page_size, page_number=page_number, sort_order=sort_order)



Get a listing of unassigned and/or assigned numbers in a set of DID Pools.

Wraps GET /api/v2/telephony/providers/edges/didpools/dids 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
type = 'type_example' # str | The type of numbers to return.
id = ['id_example'] # list[str] | Filter by a specific list of DID Pools.  If this is not provided, numbers from all DID Pools will be returned. (optional)
number_match = 'number_match_example' # str | A number to filter the results by. (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')

try:
    # Get a listing of unassigned and/or assigned numbers in a set of DID Pools.
    api_response = api_instance.get_telephony_providers_edges_didpools_dids(type, id=id, number_match=number_match, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_didpools_dids: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| The type of numbers to return. | <br />**Values**: ASSIGNED_AND_UNASSIGNED, UNASSIGNED |
| **id** | [**list[str]**](str.html)| Filter by a specific list of DID Pools.  If this is not provided, numbers from all DID Pools will be returned. | [optional]  |
| **number_match** | **str**| A number to filter the results by. | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;] |
{: class="table table-striped"}

### Return type

[**DIDNumberEntityListing**](DIDNumberEntityListing.html)

<a name="get_telephony_providers_edges_dids"></a>

## [**DIDEntityListing**](DIDEntityListing.html) get_telephony_providers_edges_dids(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, phone_number=phone_number, owner_id=owner_id, did_pool_id=did_pool_id, id=id)



Get a listing of DIDs

Wraps GET /api/v2/telephony/providers/edges/dids 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''number'' # str | Sort by (optional) (default to 'number')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
phone_number = 'phone_number_example' # str | Filter by phoneNumber (optional)
owner_id = 'owner_id_example' # str | Filter by the owner of a phone number (optional)
did_pool_id = 'did_pool_id_example' # str | Filter by the DID Pool assignment (optional)
id = ['id_example'] # list[str] | Filter by a specific list of ID's (optional)

try:
    # Get a listing of DIDs
    api_response = api_instance.get_telephony_providers_edges_dids(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, phone_number=phone_number, owner_id=owner_id, did_pool_id=did_pool_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_dids: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;number&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **phone_number** | **str**| Filter by phoneNumber | [optional]  |
| **owner_id** | **str**| Filter by the owner of a phone number | [optional]  |
| **did_pool_id** | **str**| Filter by the DID Pool assignment | [optional]  |
| **id** | [**list[str]**](str.html)| Filter by a specific list of ID&#39;s | [optional]  |
{: class="table table-striped"}

### Return type

[**DIDEntityListing**](DIDEntityListing.html)

<a name="get_telephony_providers_edges_edgegroup"></a>

## [**EdgeGroup**](EdgeGroup.html) get_telephony_providers_edges_edgegroup(edge_group_id, expand=expand)



Get edge group.

Wraps GET /api/v2/telephony/providers/edges/edgegroups/{edgeGroupId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_group_id = 'edge_group_id_example' # str | Edge group ID
expand = ['expand_example'] # list[str] | Fields to expand in the response (optional)

try:
    # Get edge group.
    api_response = api_instance.get_telephony_providers_edges_edgegroup(edge_group_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_edgegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_group_id** | **str**| Edge group ID |  |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response | [optional] <br />**Values**: phoneTrunkBases, edgeTrunkBaseAssignment |
{: class="table table-striped"}

### Return type

[**EdgeGroup**](EdgeGroup.html)

<a name="get_telephony_providers_edges_edgegroup_edgetrunkbase"></a>

## [**EdgeTrunkBase**](EdgeTrunkBase.html) get_telephony_providers_edges_edgegroup_edgetrunkbase(edgegroup_id, edgetrunkbase_id)



Gets the edge trunk base associated with the edge group

Wraps GET /api/v2/telephony/providers/edges/edgegroups/{edgegroupId}/edgetrunkbases/{edgetrunkbaseId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edgegroup_id = 'edgegroup_id_example' # str | Edge Group ID
edgetrunkbase_id = 'edgetrunkbase_id_example' # str | Edge Trunk Base ID

try:
    # Gets the edge trunk base associated with the edge group
    api_response = api_instance.get_telephony_providers_edges_edgegroup_edgetrunkbase(edgegroup_id, edgetrunkbase_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_edgegroup_edgetrunkbase: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edgegroup_id** | **str**| Edge Group ID |  |
| **edgetrunkbase_id** | **str**| Edge Trunk Base ID |  |
{: class="table table-striped"}

### Return type

[**EdgeTrunkBase**](EdgeTrunkBase.html)

<a name="get_telephony_providers_edges_edgegroups"></a>

## [**EdgeGroupEntityListing**](EdgeGroupEntityListing.html) get_telephony_providers_edges_edgegroups(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, managed=managed)



Get the list of edge groups.

Wraps GET /api/v2/telephony/providers/edges/edgegroups 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
managed = True # bool | Filter by managed (optional)

try:
    # Get the list of edge groups.
    api_response = api_instance.get_telephony_providers_edges_edgegroups(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, managed=managed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_edgegroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **managed** | **bool**| Filter by managed | [optional]  |
{: class="table table-striped"}

### Return type

[**EdgeGroupEntityListing**](EdgeGroupEntityListing.html)

<a name="get_telephony_providers_edges_edgeversionreport"></a>

## [**EdgeVersionReport**](EdgeVersionReport.html) get_telephony_providers_edges_edgeversionreport()



Get the edge version report.

The report will not have consistent data about the edge version(s) until all edges have been reset.

Wraps GET /api/v2/telephony/providers/edges/edgeversionreport 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()

try:
    # Get the edge version report.
    api_response = api_instance.get_telephony_providers_edges_edgeversionreport()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_edgeversionreport: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EdgeVersionReport**](EdgeVersionReport.html)

<a name="get_telephony_providers_edges_expired"></a>

## [**ExpiredEdgeListing**](ExpiredEdgeListing.html) get_telephony_providers_edges_expired()



List of edges more than 4 edge versions behind the latest software.

Wraps GET /api/v2/telephony/providers/edges/expired 

Requires ANY permissions: 

* telephony:plugin:all
* internal:edge:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()

try:
    # List of edges more than 4 edge versions behind the latest software.
    api_response = api_instance.get_telephony_providers_edges_expired()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_expired: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ExpiredEdgeListing**](ExpiredEdgeListing.html)

<a name="get_telephony_providers_edges_extension"></a>

## [**Extension**](Extension.html) get_telephony_providers_edges_extension(extension_id)



Get an extension by ID.

Wraps GET /api/v2/telephony/providers/edges/extensions/{extensionId} 

Requires ANY permissions: 

* telephony:extensionPool:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
extension_id = 'extension_id_example' # str | Extension ID

try:
    # Get an extension by ID.
    api_response = api_instance.get_telephony_providers_edges_extension(extension_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_extension: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **extension_id** | **str**| Extension ID |  |
{: class="table table-striped"}

### Return type

[**Extension**](Extension.html)

<a name="get_telephony_providers_edges_extensionpool"></a>

## [**ExtensionPool**](ExtensionPool.html) get_telephony_providers_edges_extensionpool(extension_pool_id)



Get an extension pool by ID

Wraps GET /api/v2/telephony/providers/edges/extensionpools/{extensionPoolId} 

Requires ALL permissions: 

* telephony:extensionPool:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
extension_pool_id = 'extension_pool_id_example' # str | Extension pool ID

try:
    # Get an extension pool by ID
    api_response = api_instance.get_telephony_providers_edges_extensionpool(extension_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_extensionpool: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **extension_pool_id** | **str**| Extension pool ID |  |
{: class="table table-striped"}

### Return type

[**ExtensionPool**](ExtensionPool.html)

<a name="get_telephony_providers_edges_extensionpools"></a>

## [**ExtensionPoolEntityListing**](ExtensionPoolEntityListing.html) get_telephony_providers_edges_extensionpools(page_size=page_size, page_number=page_number, sort_by=sort_by, number=number)



Get a listing of extension pools

Wraps GET /api/v2/telephony/providers/edges/extensionpools 

Requires ALL permissions: 

* telephony:extensionPool:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'sort_by_example' # str | Sort by (optional)
number = 'number_example' # str | Deprecated, filtering by number not supported (optional)

try:
    # Get a listing of extension pools
    api_response = api_instance.get_telephony_providers_edges_extensionpools(page_size=page_size, page_number=page_number, sort_by=sort_by, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_extensionpools: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional]  |
| **number** | **str**| Deprecated, filtering by number not supported | [optional]  |
{: class="table table-striped"}

### Return type

[**ExtensionPoolEntityListing**](ExtensionPoolEntityListing.html)

<a name="get_telephony_providers_edges_extensionpools_divisionviews"></a>

## [**ExtensionPoolDivisionViewEntityListing**](ExtensionPoolDivisionViewEntityListing.html) get_telephony_providers_edges_extensionpools_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)



Get a pageable list of basic extension pool objects filterable by query parameters.

This returns extension pools consisting of name and division. If one or more IDs are specified, the search will fetch flow outcomes that match the given ID(s) and not use any additional supplied query parameters in the search.

Wraps GET /api/v2/telephony/providers/edges/extensionpools/divisionviews 

Requires ALL permissions: 

* telephony:extensionPool:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
id = ['id_example'] # list[str] | ID of the Extension Pools to filter by. (optional)
name = 'name_example' # str | Name of the Extension Pools to filter by. (optional)
division_id = ['division_id_example'] # list[str] | List of divisionIds on which to filter. (optional)

try:
    # Get a pageable list of basic extension pool objects filterable by query parameters.
    api_response = api_instance.get_telephony_providers_edges_extensionpools_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_extensionpools_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **id** | [**list[str]**](str.html)| ID of the Extension Pools to filter by. | [optional]  |
| **name** | **str**| Name of the Extension Pools to filter by. | [optional]  |
| **division_id** | [**list[str]**](str.html)| List of divisionIds on which to filter. | [optional]  |
{: class="table table-striped"}

### Return type

[**ExtensionPoolDivisionViewEntityListing**](ExtensionPoolDivisionViewEntityListing.html)

<a name="get_telephony_providers_edges_extensions"></a>

## [**ExtensionEntityListing**](ExtensionEntityListing.html) get_telephony_providers_edges_extensions(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, number=number)



Get a listing of extensions

Wraps GET /api/v2/telephony/providers/edges/extensions 

Requires ANY permissions: 

* telephony:extensionPool:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''number'' # str | Sort by (optional) (default to 'number')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
number = 'number_example' # str | Filter by number (optional)

try:
    # Get a listing of extensions
    api_response = api_instance.get_telephony_providers_edges_extensions(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_extensions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;number&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **number** | **str**| Filter by number | [optional]  |
{: class="table table-striped"}

### Return type

[**ExtensionEntityListing**](ExtensionEntityListing.html)

<a name="get_telephony_providers_edges_line"></a>

## [**Line**](Line.html) get_telephony_providers_edges_line(line_id)



Get a Line by ID

Wraps GET /api/v2/telephony/providers/edges/lines/{lineId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
line_id = 'line_id_example' # str | Line ID

try:
    # Get a Line by ID
    api_response = api_instance.get_telephony_providers_edges_line(line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_line: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **line_id** | **str**| Line ID |  |
{: class="table table-striped"}

### Return type

[**Line**](Line.html)

<a name="get_telephony_providers_edges_linebasesetting"></a>

## [**LineBase**](LineBase.html) get_telephony_providers_edges_linebasesetting(line_base_id)



Get a line base settings object by ID

Wraps GET /api/v2/telephony/providers/edges/linebasesettings/{lineBaseId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
line_base_id = 'line_base_id_example' # str | Line base ID

try:
    # Get a line base settings object by ID
    api_response = api_instance.get_telephony_providers_edges_linebasesetting(line_base_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_linebasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **line_base_id** | **str**| Line base ID |  |
{: class="table table-striped"}

### Return type

[**LineBase**](LineBase.html)

<a name="get_telephony_providers_edges_linebasesettings"></a>

## [**LineBaseEntityListing**](LineBaseEntityListing.html) get_telephony_providers_edges_linebasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, expand=expand)



Get a listing of line base settings objects

Wraps GET /api/v2/telephony/providers/edges/linebasesettings 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = ''name'' # str | Value by which to sort (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)

try:
    # Get a listing of line base settings objects
    api_response = api_instance.get_telephony_providers_edges_linebasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_linebasesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Value by which to sort | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties |
{: class="table table-striped"}

### Return type

[**LineBaseEntityListing**](LineBaseEntityListing.html)

<a name="get_telephony_providers_edges_lines"></a>

## [**LineEntityListing**](LineEntityListing.html) get_telephony_providers_edges_lines(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, expand=expand)



Get a list of Lines

Wraps GET /api/v2/telephony/providers/edges/lines 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
sort_by = ''name'' # str | Value by which to sort (optional) (default to 'name')
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated. The edgeGroup value is deprecated. (optional)

try:
    # Get a list of Lines
    api_response = api_instance.get_telephony_providers_edges_lines(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_lines: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **sort_by** | **str**| Value by which to sort | [optional] [default to &#39;name&#39;] |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated. The edgeGroup value is deprecated. | [optional] <br />**Values**: properties, site, edgeGroup, primaryEdge, secondaryEdge, edges, assignedUser |
{: class="table table-striped"}

### Return type

[**LineEntityListing**](LineEntityListing.html)

<a name="get_telephony_providers_edges_lines_template"></a>

## [**Line**](Line.html) get_telephony_providers_edges_lines_template(line_base_settings_id)



Get a Line instance template based on a Line Base Settings object. This object can then be modified and saved as a new Line instance

Wraps GET /api/v2/telephony/providers/edges/lines/template 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
line_base_settings_id = 'line_base_settings_id_example' # str | The id of a Line Base Settings object upon which to base this Line

try:
    # Get a Line instance template based on a Line Base Settings object. This object can then be modified and saved as a new Line instance
    api_response = api_instance.get_telephony_providers_edges_lines_template(line_base_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_lines_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **line_base_settings_id** | **str**| The id of a Line Base Settings object upon which to base this Line |  |
{: class="table table-striped"}

### Return type

[**Line**](Line.html)

<a name="get_telephony_providers_edges_logicalinterfaces"></a>

## [**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing.html) get_telephony_providers_edges_logicalinterfaces(edge_ids, expand=expand)



Get edge logical interfaces.

Retrieve the configured logical interfaces for a list edges. Only 100 edges can be requested at a time.

Wraps GET /api/v2/telephony/providers/edges/logicalinterfaces 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_ids = 'edge_ids_example' # str | Comma separated list of Edge Id's
expand = ['expand_example'] # list[str] | Field to expand in the response (optional)

try:
    # Get edge logical interfaces.
    api_response = api_instance.get_telephony_providers_edges_logicalinterfaces(edge_ids, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_logicalinterfaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_ids** | **str**| Comma separated list of Edge Id&#39;s |  |
| **expand** | [**list[str]**](str.html)| Field to expand in the response | [optional] <br />**Values**: externalTrunkBaseAssignments, phoneTrunkBaseAssignments |
{: class="table table-striped"}

### Return type

[**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing.html)

<a name="get_telephony_providers_edges_mediastatistics_conversation"></a>

## [**MediaStatisticsListing**](MediaStatisticsListing.html) get_telephony_providers_edges_mediastatistics_conversation(conversation_id)



Get media endpoint statistics events.

get_telephony_providers_edges_mediastatistics_conversation is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/telephony/providers/edges/mediastatistics/conversations/{conversationId} 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
conversation_id = 'conversation_id_example' # str | Identifier of the conversation

try:
    # Get media endpoint statistics events.
    api_response = api_instance.get_telephony_providers_edges_mediastatistics_conversation(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_mediastatistics_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Identifier of the conversation |  |
{: class="table table-striped"}

### Return type

[**MediaStatisticsListing**](MediaStatisticsListing.html)

<a name="get_telephony_providers_edges_mediastatistics_conversation_communication"></a>

## [**MediaStatistics**](MediaStatistics.html) get_telephony_providers_edges_mediastatistics_conversation_communication(conversation_id, communication_id)



Get media endpoint statistics event.

get_telephony_providers_edges_mediastatistics_conversation_communication is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/telephony/providers/edges/mediastatistics/conversations/{conversationId}/communications/{communicationId} 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
conversation_id = 'conversation_id_example' # str | Identifier of the conversation
communication_id = 'communication_id_example' # str | Identifier of the media session

try:
    # Get media endpoint statistics event.
    api_response = api_instance.get_telephony_providers_edges_mediastatistics_conversation_communication(conversation_id, communication_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_mediastatistics_conversation_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Identifier of the conversation |  |
| **communication_id** | **str**| Identifier of the media session |  |
{: class="table table-striped"}

### Return type

[**MediaStatistics**](MediaStatistics.html)

<a name="get_telephony_providers_edges_metrics"></a>

## [**list[EdgeMetrics]**](EdgeMetrics.html) get_telephony_providers_edges_metrics(edge_ids)



Get the metrics for a list of edges.

Wraps GET /api/v2/telephony/providers/edges/metrics 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_ids = 'edge_ids_example' # str | Comma separated list of Edge Id's. Maximum of 100 edge ids allowed.

try:
    # Get the metrics for a list of edges.
    api_response = api_instance.get_telephony_providers_edges_metrics(edge_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_ids** | **str**| Comma separated list of Edge Id&#39;s. Maximum of 100 edge ids allowed. |  |
{: class="table table-striped"}

### Return type

[**list[EdgeMetrics]**](EdgeMetrics.html)

<a name="get_telephony_providers_edges_outboundroutes"></a>

## [**OutboundRouteEntityListing**](OutboundRouteEntityListing.html) get_telephony_providers_edges_outboundroutes(page_size=page_size, page_number=page_number, name=name, site_id=site_id, external_trunk_bases_ids=external_trunk_bases_ids, sort_by=sort_by)



Get outbound routes

Wraps GET /api/v2/telephony/providers/edges/outboundroutes 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
site_id = 'site_id_example' # str | Filter by site.id (optional)
external_trunk_bases_ids = 'external_trunk_bases_ids_example' # str | Filter by externalTrunkBases.ids (optional)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')

try:
    # Get outbound routes
    api_response = api_instance.get_telephony_providers_edges_outboundroutes(page_size=page_size, page_number=page_number, name=name, site_id=site_id, external_trunk_bases_ids=external_trunk_bases_ids, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_outboundroutes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **site_id** | **str**| Filter by site.id | [optional]  |
| **external_trunk_bases_ids** | **str**| Filter by externalTrunkBases.ids | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
{: class="table table-striped"}

### Return type

[**OutboundRouteEntityListing**](OutboundRouteEntityListing.html)

<a name="get_telephony_providers_edges_phone"></a>

## [**Phone**](Phone.html) get_telephony_providers_edges_phone(phone_id)



Get a Phone by ID

Wraps GET /api/v2/telephony/providers/edges/phones/{phoneId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_id = 'phone_id_example' # str | Phone ID

try:
    # Get a Phone by ID
    api_response = api_instance.get_telephony_providers_edges_phone(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phone: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_id** | **str**| Phone ID |  |
{: class="table table-striped"}

### Return type

[**Phone**](Phone.html)

<a name="get_telephony_providers_edges_phonebasesetting"></a>

## [**PhoneBase**](PhoneBase.html) get_telephony_providers_edges_phonebasesetting(phone_base_id)



Get a Phone Base Settings object by ID

Wraps GET /api/v2/telephony/providers/edges/phonebasesettings/{phoneBaseId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_base_id = 'phone_base_id_example' # str | Phone base ID

try:
    # Get a Phone Base Settings object by ID
    api_response = api_instance.get_telephony_providers_edges_phonebasesetting(phone_base_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phonebasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_base_id** | **str**| Phone base ID |  |
{: class="table table-striped"}

### Return type

[**PhoneBase**](PhoneBase.html)

<a name="get_telephony_providers_edges_phonebasesettings"></a>

## [**PhoneBaseEntityListing**](PhoneBaseEntityListing.html) get_telephony_providers_edges_phonebasesettings(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, expand=expand, name=name)



Get a list of Phone Base Settings objects

Wraps GET /api/v2/telephony/providers/edges/phonebasesettings 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''name'' # str | Value by which to sort (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)
name = 'name_example' # str | Name (optional)

try:
    # Get a list of Phone Base Settings objects
    api_response = api_instance.get_telephony_providers_edges_phonebasesettings(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, expand=expand, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phonebasesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Value by which to sort | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties, lines |
| **name** | **str**| Name | [optional]  |
{: class="table table-striped"}

### Return type

[**PhoneBaseEntityListing**](PhoneBaseEntityListing.html)

<a name="get_telephony_providers_edges_phonebasesettings_availablemetabases"></a>

## [**PhoneMetaBaseEntityListing**](PhoneMetaBaseEntityListing.html) get_telephony_providers_edges_phonebasesettings_availablemetabases(page_size=page_size, page_number=page_number)



Get a list of available makes and models to create a new Phone Base Settings

Wraps GET /api/v2/telephony/providers/edges/phonebasesettings/availablemetabases 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of available makes and models to create a new Phone Base Settings
    api_response = api_instance.get_telephony_providers_edges_phonebasesettings_availablemetabases(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phonebasesettings_availablemetabases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**PhoneMetaBaseEntityListing**](PhoneMetaBaseEntityListing.html)

<a name="get_telephony_providers_edges_phonebasesettings_template"></a>

## [**PhoneBase**](PhoneBase.html) get_telephony_providers_edges_phonebasesettings_template(phone_metabase_id)



Get a Phone Base Settings instance template from a given make and model. This object can then be modified and saved as a new Phone Base Settings instance

Wraps GET /api/v2/telephony/providers/edges/phonebasesettings/template 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_metabase_id = 'phone_metabase_id_example' # str | The id of a metabase object upon which to base this Phone Base Settings

try:
    # Get a Phone Base Settings instance template from a given make and model. This object can then be modified and saved as a new Phone Base Settings instance
    api_response = api_instance.get_telephony_providers_edges_phonebasesettings_template(phone_metabase_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phonebasesettings_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_metabase_id** | **str**| The id of a metabase object upon which to base this Phone Base Settings |  |
{: class="table table-striped"}

### Return type

[**PhoneBase**](PhoneBase.html)

<a name="get_telephony_providers_edges_phones"></a>

## [**PhoneEntityListing**](PhoneEntityListing.html) get_telephony_providers_edges_phones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, site_id=site_id, web_rtc_user_id=web_rtc_user_id, phone_base_settings_id=phone_base_settings_id, lines_logged_in_user_id=lines_logged_in_user_id, lines_default_for_user_id=lines_default_for_user_id, phone_hardware_id=phone_hardware_id, lines_id=lines_id, lines_name=lines_name, name=name, status_operational_status=status_operational_status, secondary_status_operational_status=secondary_status_operational_status, expand=expand, fields=fields)



Get a list of Phone Instances. A maximum of 10,000 results is returned when filtering the results or sorting by a field other than the ID. Sorting by only the ID has no result limit. Each filter supports a wildcard, *, as a value to search for partial values.

Wraps GET /api/v2/telephony/providers/edges/phones 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = ''name'' # str | The field to sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
site_id = 'site_id_example' # str | Filter by site.id (optional)
web_rtc_user_id = 'web_rtc_user_id_example' # str | Filter by webRtcUser.id (optional)
phone_base_settings_id = 'phone_base_settings_id_example' # str | Filter by phoneBaseSettings.id (optional)
lines_logged_in_user_id = 'lines_logged_in_user_id_example' # str | Filter by lines.loggedInUser.id (optional)
lines_default_for_user_id = 'lines_default_for_user_id_example' # str | Filter by lines.defaultForUser.id (optional)
phone_hardware_id = 'phone_hardware_id_example' # str | Filter by phone_hardwareId (optional)
lines_id = 'lines_id_example' # str | Filter by lines.id (optional)
lines_name = 'lines_name_example' # str | Filter by lines.name (optional)
name = 'name_example' # str | Name of the Phone to filter by, comma-separated (optional)
status_operational_status = 'status_operational_status_example' # str | The primary status to filter by (optional)
secondary_status_operational_status = 'secondary_status_operational_status_example' # str | The secondary status to filter by (optional)
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)
fields = ['fields_example'] # list[str] | Fields and properties to get, comma-separated (optional)

try:
    # Get a list of Phone Instances. A maximum of 10,000 results is returned when filtering the results or sorting by a field other than the ID. Sorting by only the ID has no result limit. Each filter supports a wildcard, *, as a value to search for partial values.
    api_response = api_instance.get_telephony_providers_edges_phones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, site_id=site_id, web_rtc_user_id=web_rtc_user_id, phone_base_settings_id=phone_base_settings_id, lines_logged_in_user_id=lines_logged_in_user_id, lines_default_for_user_id=lines_default_for_user_id, phone_hardware_id=phone_hardware_id, lines_id=lines_id, lines_name=lines_name, name=name, status_operational_status=status_operational_status, secondary_status_operational_status=secondary_status_operational_status, expand=expand, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| The field to sort by | [optional] [default to &#39;name&#39;]<br />**Values**: name, status.operationalStatus, secondaryStatus.operationalStatus |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **site_id** | **str**| Filter by site.id | [optional]  |
| **web_rtc_user_id** | **str**| Filter by webRtcUser.id | [optional]  |
| **phone_base_settings_id** | **str**| Filter by phoneBaseSettings.id | [optional]  |
| **lines_logged_in_user_id** | **str**| Filter by lines.loggedInUser.id | [optional]  |
| **lines_default_for_user_id** | **str**| Filter by lines.defaultForUser.id | [optional]  |
| **phone_hardware_id** | **str**| Filter by phone_hardwareId | [optional]  |
| **lines_id** | **str**| Filter by lines.id | [optional]  |
| **lines_name** | **str**| Filter by lines.name | [optional]  |
| **name** | **str**| Name of the Phone to filter by, comma-separated | [optional]  |
| **status_operational_status** | **str**| The primary status to filter by | [optional]  |
| **secondary_status_operational_status** | **str**| The secondary status to filter by | [optional]  |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties, site, status, status.primaryEdgesStatus, status.secondaryEdgesStatus, phoneBaseSettings, lines |
| **fields** | [**list[str]**](str.html)| Fields and properties to get, comma-separated | [optional] <br />**Values**: webRtcUser, properties.*, lines.loggedInUser, lines.defaultForUser |
{: class="table table-striped"}

### Return type

[**PhoneEntityListing**](PhoneEntityListing.html)

<a name="get_telephony_providers_edges_phones_template"></a>

## [**Phone**](Phone.html) get_telephony_providers_edges_phones_template(phone_base_settings_id)



Get a Phone instance template based on a Phone Base Settings object. This object can then be modified and saved as a new Phone instance

Wraps GET /api/v2/telephony/providers/edges/phones/template 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_base_settings_id = 'phone_base_settings_id_example' # str | The id of a Phone Base Settings object upon which to base this Phone

try:
    # Get a Phone instance template based on a Phone Base Settings object. This object can then be modified and saved as a new Phone instance
    api_response = api_instance.get_telephony_providers_edges_phones_template(phone_base_settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_phones_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_base_settings_id** | **str**| The id of a Phone Base Settings object upon which to base this Phone |  |
{: class="table table-striped"}

### Return type

[**Phone**](Phone.html)

<a name="get_telephony_providers_edges_physicalinterfaces"></a>

## [**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing.html) get_telephony_providers_edges_physicalinterfaces(edge_ids)



Get physical interfaces for edges.

Retrieves a list of all configured physical interfaces for a list of edges. Only 100 edges can be requested at a time.

Wraps GET /api/v2/telephony/providers/edges/physicalinterfaces 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_ids = 'edge_ids_example' # str | Comma separated list of Edge Id's

try:
    # Get physical interfaces for edges.
    api_response = api_instance.get_telephony_providers_edges_physicalinterfaces(edge_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_physicalinterfaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_ids** | **str**| Comma separated list of Edge Id&#39;s |  |
{: class="table table-striped"}

### Return type

[**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing.html)

<a name="get_telephony_providers_edges_site"></a>

## [**Site**](Site.html) get_telephony_providers_edges_site(site_id)



Get a Site by ID.

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId} 

Requires ANY permissions: 

* telephony:plugin:all
* telephony:sites:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID

try:
    # Get a Site by ID.
    api_response = api_instance.get_telephony_providers_edges_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
{: class="table table-striped"}

### Return type

[**Site**](Site.html)

<a name="get_telephony_providers_edges_site_numberplan"></a>

## [**NumberPlan**](NumberPlan.html) get_telephony_providers_edges_site_numberplan(site_id, number_plan_id)



Get a Number Plan by ID.

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId}/numberplans/{numberPlanId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
number_plan_id = 'number_plan_id_example' # str | Number Plan ID

try:
    # Get a Number Plan by ID.
    api_response = api_instance.get_telephony_providers_edges_site_numberplan(site_id, number_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site_numberplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **number_plan_id** | **str**| Number Plan ID |  |
{: class="table table-striped"}

### Return type

[**NumberPlan**](NumberPlan.html)

<a name="get_telephony_providers_edges_site_numberplans"></a>

## [**list[NumberPlan]**](NumberPlan.html) get_telephony_providers_edges_site_numberplans(site_id)



Get the list of Number Plans for this Site. Only fetches the first 200 records.

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId}/numberplans 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID

try:
    # Get the list of Number Plans for this Site. Only fetches the first 200 records.
    api_response = api_instance.get_telephony_providers_edges_site_numberplans(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site_numberplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
{: class="table table-striped"}

### Return type

[**list[NumberPlan]**](NumberPlan.html)

<a name="get_telephony_providers_edges_site_numberplans_classifications"></a>

## list[str]** get_telephony_providers_edges_site_numberplans_classifications(site_id, classification=classification)



Get a list of Classifications for this Site

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId}/numberplans/classifications 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
classification = 'classification_example' # str | Classification (optional)

try:
    # Get a list of Classifications for this Site
    api_response = api_instance.get_telephony_providers_edges_site_numberplans_classifications(site_id, classification=classification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site_numberplans_classifications: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **classification** | **str**| Classification | [optional]  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="get_telephony_providers_edges_site_outboundroute"></a>

## [**OutboundRouteBase**](OutboundRouteBase.html) get_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id)



Get an outbound route

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId}/outboundroutes/{outboundRouteId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
outbound_route_id = 'outbound_route_id_example' # str | Outbound route ID

try:
    # Get an outbound route
    api_response = api_instance.get_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site_outboundroute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **outbound_route_id** | **str**| Outbound route ID |  |
{: class="table table-striped"}

### Return type

[**OutboundRouteBase**](OutboundRouteBase.html)

<a name="get_telephony_providers_edges_site_outboundroutes"></a>

## [**OutboundRouteBaseEntityListing**](OutboundRouteBaseEntityListing.html) get_telephony_providers_edges_site_outboundroutes(site_id, page_size=page_size, page_number=page_number, name=name, external_trunk_bases_ids=external_trunk_bases_ids, sort_by=sort_by)



Get outbound routes

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId}/outboundroutes 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Name (optional)
external_trunk_bases_ids = 'external_trunk_bases_ids_example' # str | externalTrunkBases.ids (optional)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')

try:
    # Get outbound routes
    api_response = api_instance.get_telephony_providers_edges_site_outboundroutes(site_id, page_size=page_size, page_number=page_number, name=name, external_trunk_bases_ids=external_trunk_bases_ids, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site_outboundroutes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **name** | **str**| Name | [optional]  |
| **external_trunk_bases_ids** | **str**| externalTrunkBases.ids | [optional]  |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
{: class="table table-striped"}

### Return type

[**OutboundRouteBaseEntityListing**](OutboundRouteBaseEntityListing.html)

<a name="get_telephony_providers_edges_site_siteconnections"></a>

## [**SiteConnections**](SiteConnections.html) get_telephony_providers_edges_site_siteconnections(site_id)



Get site connections for a site.

Wraps GET /api/v2/telephony/providers/edges/sites/{siteId}/siteconnections 

Requires ANY permissions: 

* telephony:plugin:all
* telephony:sites:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID

try:
    # Get site connections for a site.
    api_response = api_instance.get_telephony_providers_edges_site_siteconnections(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_site_siteconnections: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
{: class="table table-striped"}

### Return type

[**SiteConnections**](SiteConnections.html)

<a name="get_telephony_providers_edges_sites"></a>

## [**SiteEntityListing**](SiteEntityListing.html) get_telephony_providers_edges_sites(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, location_id=location_id, managed=managed, expand=expand)



Get the list of Sites.

Wraps GET /api/v2/telephony/providers/edges/sites 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
name = 'name_example' # str | Name (optional)
location_id = 'location_id_example' # str | Location Id (optional)
managed = True # bool | Filter by managed (optional)
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)

try:
    # Get the list of Sites.
    api_response = api_instance.get_telephony_providers_edges_sites(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, location_id=location_id, managed=managed, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_sites: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **name** | **str**| Name | [optional]  |
| **location_id** | **str**| Location Id | [optional]  |
| **managed** | **bool**| Filter by managed | [optional]  |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: edges, location, primarySites, secondarySites |
{: class="table table-striped"}

### Return type

[**SiteEntityListing**](SiteEntityListing.html)

<a name="get_telephony_providers_edges_timezones"></a>

## [**TimeZoneEntityListing**](TimeZoneEntityListing.html) get_telephony_providers_edges_timezones(page_size=page_size, page_number=page_number)



Get a list of Edge-compatible time zones

Wraps GET /api/v2/telephony/providers/edges/timezones 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_size = 1000 # int | Page size (optional) (default to 1000)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Edge-compatible time zones
    api_response = api_instance.get_telephony_providers_edges_timezones(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_timezones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 1000] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TimeZoneEntityListing**](TimeZoneEntityListing.html)

<a name="get_telephony_providers_edges_trunk"></a>

## [**Trunk**](Trunk.html) get_telephony_providers_edges_trunk(trunk_id)



Get a Trunk by ID

Wraps GET /api/v2/telephony/providers/edges/trunks/{trunkId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_id = 'trunk_id_example' # str | Trunk ID

try:
    # Get a Trunk by ID
    api_response = api_instance.get_telephony_providers_edges_trunk(trunk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_id** | **str**| Trunk ID |  |
{: class="table table-striped"}

### Return type

[**Trunk**](Trunk.html)

<a name="get_telephony_providers_edges_trunk_metrics"></a>

## [**TrunkMetrics**](TrunkMetrics.html) get_telephony_providers_edges_trunk_metrics(trunk_id)



Get the trunk metrics.

Wraps GET /api/v2/telephony/providers/edges/trunks/{trunkId}/metrics 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_id = 'trunk_id_example' # str | Trunk Id

try:
    # Get the trunk metrics.
    api_response = api_instance.get_telephony_providers_edges_trunk_metrics(trunk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunk_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_id** | **str**| Trunk Id |  |
{: class="table table-striped"}

### Return type

[**TrunkMetrics**](TrunkMetrics.html)

<a name="get_telephony_providers_edges_trunkbasesetting"></a>

## [**TrunkBase**](TrunkBase.html) get_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id, ignore_hidden=ignore_hidden)



Get a Trunk Base Settings object by ID

Managed properties will not be returned unless the user is assigned the internal:trunk:edit permission.

Wraps GET /api/v2/telephony/providers/edges/trunkbasesettings/{trunkBaseSettingsId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_base_settings_id = 'trunk_base_settings_id_example' # str | Trunk Base ID
ignore_hidden = True # bool | Set this to true to not receive trunk properties that are meant to be hidden or for internal system usage only. (optional)

try:
    # Get a Trunk Base Settings object by ID
    api_response = api_instance.get_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id, ignore_hidden=ignore_hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunkbasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_base_settings_id** | **str**| Trunk Base ID |  |
| **ignore_hidden** | **bool**| Set this to true to not receive trunk properties that are meant to be hidden or for internal system usage only. | [optional]  |
{: class="table table-striped"}

### Return type

[**TrunkBase**](TrunkBase.html)

<a name="get_telephony_providers_edges_trunkbasesettings"></a>

## [**TrunkBaseEntityListing**](TrunkBaseEntityListing.html) get_telephony_providers_edges_trunkbasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, recording_enabled=recording_enabled, ignore_hidden=ignore_hidden, managed=managed, expand=expand, name=name)



Get Trunk Base Settings listing

Managed properties will not be returned unless the user is assigned the internal:trunk:edit permission.

Wraps GET /api/v2/telephony/providers/edges/trunkbasesettings 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = ''name'' # str | Value by which to sort (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
recording_enabled = True # bool | Filter trunks by recording enabled (optional)
ignore_hidden = True # bool | Set this to true to not receive trunk properties that are meant to be hidden or for internal system usage only. (optional)
managed = True # bool | Filter by managed (optional)
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)
name = 'name_example' # str | Name of the TrunkBase to filter by (optional)

try:
    # Get Trunk Base Settings listing
    api_response = api_instance.get_telephony_providers_edges_trunkbasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, recording_enabled=recording_enabled, ignore_hidden=ignore_hidden, managed=managed, expand=expand, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunkbasesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Value by which to sort | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **recording_enabled** | **bool**| Filter trunks by recording enabled | [optional]  |
| **ignore_hidden** | **bool**| Set this to true to not receive trunk properties that are meant to be hidden or for internal system usage only. | [optional]  |
| **managed** | **bool**| Filter by managed | [optional]  |
| **expand** | [**list[str]**](str.html)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties |
| **name** | **str**| Name of the TrunkBase to filter by | [optional]  |
{: class="table table-striped"}

### Return type

[**TrunkBaseEntityListing**](TrunkBaseEntityListing.html)

<a name="get_telephony_providers_edges_trunkbasesettings_availablemetabases"></a>

## [**TrunkMetabaseEntityListing**](TrunkMetabaseEntityListing.html) get_telephony_providers_edges_trunkbasesettings_availablemetabases(type=type, page_size=page_size, page_number=page_number)



Get a list of available makes and models to create a new Trunk Base Settings

Wraps GET /api/v2/telephony/providers/edges/trunkbasesettings/availablemetabases 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
type = 'type_example' # str |  (optional)
page_size = 25 # int |  (optional) (default to 25)
page_number = 1 # int |  (optional) (default to 1)

try:
    # Get a list of available makes and models to create a new Trunk Base Settings
    api_response = api_instance.get_telephony_providers_edges_trunkbasesettings_availablemetabases(type=type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunkbasesettings_availablemetabases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**|  | [optional] <br />**Values**: EXTERNAL, PHONE, EDGE |
| **page_size** | **int**|  | [optional] [default to 25] |
| **page_number** | **int**|  | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TrunkMetabaseEntityListing**](TrunkMetabaseEntityListing.html)

<a name="get_telephony_providers_edges_trunkbasesettings_template"></a>

## [**TrunkBase**](TrunkBase.html) get_telephony_providers_edges_trunkbasesettings_template(trunk_metabase_id)



Get a Trunk Base Settings instance template from a given make and model. This object can then be modified and saved as a new Trunk Base Settings instance

Wraps GET /api/v2/telephony/providers/edges/trunkbasesettings/template 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_metabase_id = 'trunk_metabase_id_example' # str | The id of a metabase object upon which to base this Trunk Base Settings

try:
    # Get a Trunk Base Settings instance template from a given make and model. This object can then be modified and saved as a new Trunk Base Settings instance
    api_response = api_instance.get_telephony_providers_edges_trunkbasesettings_template(trunk_metabase_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunkbasesettings_template: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_metabase_id** | **str**| The id of a metabase object upon which to base this Trunk Base Settings |  |
{: class="table table-striped"}

### Return type

[**TrunkBase**](TrunkBase.html)

<a name="get_telephony_providers_edges_trunks"></a>

## [**TrunkEntityListing**](TrunkEntityListing.html) get_telephony_providers_edges_trunks(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, edge_id=edge_id, trunk_base_id=trunk_base_id, trunk_type=trunk_type)



Get the list of available trunks.

Trunks are created by assigning trunk base settings to an Edge or Edge Group.

Wraps GET /api/v2/telephony/providers/edges/trunks 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = ''name'' # str | Value by which to sort (optional) (default to 'name')
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
edge_id = 'edge_id_example' # str | Filter by Edge Ids (optional)
trunk_base_id = 'trunk_base_id_example' # str | Filter by Trunk Base Ids (optional)
trunk_type = 'trunk_type_example' # str | Filter by a Trunk type (optional)

try:
    # Get the list of available trunks.
    api_response = api_instance.get_telephony_providers_edges_trunks(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, edge_id=edge_id, trunk_base_id=trunk_base_id, trunk_type=trunk_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Value by which to sort | [optional] [default to &#39;name&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **edge_id** | **str**| Filter by Edge Ids | [optional]  |
| **trunk_base_id** | **str**| Filter by Trunk Base Ids | [optional]  |
| **trunk_type** | **str**| Filter by a Trunk type | [optional] <br />**Values**: EXTERNAL, PHONE, EDGE |
{: class="table table-striped"}

### Return type

[**TrunkEntityListing**](TrunkEntityListing.html)

<a name="get_telephony_providers_edges_trunks_metrics"></a>

## [**list[TrunkMetrics]**](TrunkMetrics.html) get_telephony_providers_edges_trunks_metrics(trunk_ids)



Get the metrics for a list of trunks.

Wraps GET /api/v2/telephony/providers/edges/trunks/metrics 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_ids = 'trunk_ids_example' # str | Comma separated list of Trunk Id's

try:
    # Get the metrics for a list of trunks.
    api_response = api_instance.get_telephony_providers_edges_trunks_metrics(trunk_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunks_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_ids** | **str**| Comma separated list of Trunk Id&#39;s |  |
{: class="table table-striped"}

### Return type

[**list[TrunkMetrics]**](TrunkMetrics.html)

<a name="get_telephony_providers_edges_trunkswithrecording"></a>

## [**TrunkRecordingEnabledCount**](TrunkRecordingEnabledCount.html) get_telephony_providers_edges_trunkswithrecording(trunk_type=trunk_type)



Get Counts of trunks that have recording disabled or enabled

Wraps GET /api/v2/telephony/providers/edges/trunkswithrecording 

Requires ANY permissions: 

* recording:retentionPolicy:view
* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_type = 'trunk_type_example' # str | The type of this trunk base. (optional)

try:
    # Get Counts of trunks that have recording disabled or enabled
    api_response = api_instance.get_telephony_providers_edges_trunkswithrecording(trunk_type=trunk_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunkswithrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_type** | **str**| The type of this trunk base. | [optional] <br />**Values**: EXTERNAL, PHONE, EDGE |
{: class="table table-striped"}

### Return type

[**TrunkRecordingEnabledCount**](TrunkRecordingEnabledCount.html)

<a name="patch_telephony_providers_edges_site_siteconnections"></a>

## [**SiteConnections**](SiteConnections.html) patch_telephony_providers_edges_site_siteconnections(site_id, body)



Disable site connections for a site.

Wraps PATCH /api/v2/telephony/providers/edges/sites/{siteId}/siteconnections 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
body = PureCloudPlatformClientV2.DisableSiteConnectionsRequest() # DisableSiteConnectionsRequest | Site

try:
    # Disable site connections for a site.
    api_response = api_instance.patch_telephony_providers_edges_site_siteconnections(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->patch_telephony_providers_edges_site_siteconnections: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **body** | [**DisableSiteConnectionsRequest**](DisableSiteConnectionsRequest.html)| Site |  |
{: class="table table-striped"}

### Return type

[**SiteConnections**](SiteConnections.html)

<a name="post_telephony_providers_edge_diagnostic_nslookup"></a>

## [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html) post_telephony_providers_edge_diagnostic_nslookup(edge_id, body)



Nslookup request command to collect networking-related information from an Edge for a target IP or host.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/diagnostic/nslookup 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id
body = PureCloudPlatformClientV2.EdgeNetworkDiagnosticRequest() # EdgeNetworkDiagnosticRequest | request payload to get network diagnostic

try:
    # Nslookup request command to collect networking-related information from an Edge for a target IP or host.
    api_response = api_instance.post_telephony_providers_edge_diagnostic_nslookup(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_diagnostic_nslookup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest.html)| request payload to get network diagnostic |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html)

<a name="post_telephony_providers_edge_diagnostic_ping"></a>

## [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html) post_telephony_providers_edge_diagnostic_ping(edge_id, body)



Ping Request command to collect networking-related information from an Edge for a target IP or host.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/diagnostic/ping 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id
body = PureCloudPlatformClientV2.EdgeNetworkDiagnosticRequest() # EdgeNetworkDiagnosticRequest | request payload to get network diagnostic

try:
    # Ping Request command to collect networking-related information from an Edge for a target IP or host.
    api_response = api_instance.post_telephony_providers_edge_diagnostic_ping(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_diagnostic_ping: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest.html)| request payload to get network diagnostic |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html)

<a name="post_telephony_providers_edge_diagnostic_route"></a>

## [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html) post_telephony_providers_edge_diagnostic_route(edge_id, body)



Route request command to collect networking-related information from an Edge for a target IP or host.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/diagnostic/route 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id
body = PureCloudPlatformClientV2.EdgeNetworkDiagnosticRequest() # EdgeNetworkDiagnosticRequest | request payload to get network diagnostic

try:
    # Route request command to collect networking-related information from an Edge for a target IP or host.
    api_response = api_instance.post_telephony_providers_edge_diagnostic_route(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_diagnostic_route: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest.html)| request payload to get network diagnostic |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html)

<a name="post_telephony_providers_edge_diagnostic_tracepath"></a>

## [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html) post_telephony_providers_edge_diagnostic_tracepath(edge_id, body)



Tracepath request command to collect networking-related information from an Edge for a target IP or host.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/diagnostic/tracepath 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id
body = PureCloudPlatformClientV2.EdgeNetworkDiagnosticRequest() # EdgeNetworkDiagnosticRequest | request payload to get network diagnostic

try:
    # Tracepath request command to collect networking-related information from an Edge for a target IP or host.
    api_response = api_instance.post_telephony_providers_edge_diagnostic_tracepath(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_diagnostic_tracepath: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest.html)| request payload to get network diagnostic |  |
{: class="table table-striped"}

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic.html)

<a name="post_telephony_providers_edge_logicalinterfaces"></a>

## [**DomainLogicalInterface**](DomainLogicalInterface.html) post_telephony_providers_edge_logicalinterfaces(edge_id, body)



Create an edge logical interface.

Create

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/logicalinterfaces 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
body = PureCloudPlatformClientV2.DomainLogicalInterface() # DomainLogicalInterface | Logical interface

try:
    # Create an edge logical interface.
    api_response = api_instance.post_telephony_providers_edge_logicalinterfaces(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_logicalinterfaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **body** | [**DomainLogicalInterface**](DomainLogicalInterface.html)| Logical interface |  |
{: class="table table-striped"}

### Return type

[**DomainLogicalInterface**](DomainLogicalInterface.html)

<a name="post_telephony_providers_edge_logs_job_upload"></a>

##  post_telephony_providers_edge_logs_job_upload(edge_id, job_id, body)



Request that the specified fileIds be uploaded from the Edge.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/logs/jobs/{jobId}/upload 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
job_id = 'job_id_example' # str | Job ID
body = PureCloudPlatformClientV2.EdgeLogsJobUploadRequest() # EdgeLogsJobUploadRequest | Log upload request

try:
    # Request that the specified fileIds be uploaded from the Edge.
    api_instance.post_telephony_providers_edge_logs_job_upload(edge_id, job_id, body)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_logs_job_upload: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **job_id** | **str**| Job ID |  |
| **body** | [**EdgeLogsJobUploadRequest**](EdgeLogsJobUploadRequest.html)| Log upload request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_telephony_providers_edge_logs_jobs"></a>

## [**EdgeLogsJobResponse**](EdgeLogsJobResponse.html) post_telephony_providers_edge_logs_jobs(edge_id, body)



Create a job to upload a list of Edge logs.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/logs/jobs 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
body = PureCloudPlatformClientV2.EdgeLogsJobRequest() # EdgeLogsJobRequest | EdgeLogsJobRequest

try:
    # Create a job to upload a list of Edge logs.
    api_response = api_instance.post_telephony_providers_edge_logs_jobs(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_logs_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **body** | [**EdgeLogsJobRequest**](EdgeLogsJobRequest.html)| EdgeLogsJobRequest |  |
{: class="table table-striped"}

### Return type

[**EdgeLogsJobResponse**](EdgeLogsJobResponse.html)

<a name="post_telephony_providers_edge_reboot"></a>

## str** post_telephony_providers_edge_reboot(edge_id, body=body)



Reboot an Edge

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/reboot 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
body = PureCloudPlatformClientV2.EdgeRebootParameters() # EdgeRebootParameters | Parameters for the edge reboot (optional)

try:
    # Reboot an Edge
    api_response = api_instance.post_telephony_providers_edge_reboot(edge_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_reboot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **body** | [**EdgeRebootParameters**](EdgeRebootParameters.html)| Parameters for the edge reboot | [optional]  |
{: class="table table-striped"}

### Return type

**str**

<a name="post_telephony_providers_edge_softwareupdate"></a>

## [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto.html) post_telephony_providers_edge_softwareupdate(edge_id, body)



Starts a software update for this edge.

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/softwareupdate 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
body = PureCloudPlatformClientV2.DomainEdgeSoftwareUpdateDto() # DomainEdgeSoftwareUpdateDto | Software update request

try:
    # Starts a software update for this edge.
    api_response = api_instance.post_telephony_providers_edge_softwareupdate(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_softwareupdate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **body** | [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto.html)| Software update request |  |
{: class="table table-striped"}

### Return type

[**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto.html)

<a name="post_telephony_providers_edge_statuscode"></a>

## str** post_telephony_providers_edge_statuscode(edge_id, body=body)



Take an Edge in or out of service

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/statuscode 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
body = PureCloudPlatformClientV2.EdgeServiceStateRequest() # EdgeServiceStateRequest | Edge Service State (optional)

try:
    # Take an Edge in or out of service
    api_response = api_instance.post_telephony_providers_edge_statuscode(edge_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_statuscode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **body** | [**EdgeServiceStateRequest**](EdgeServiceStateRequest.html)| Edge Service State | [optional]  |
{: class="table table-striped"}

### Return type

**str**

<a name="post_telephony_providers_edge_unpair"></a>

## str** post_telephony_providers_edge_unpair(edge_id)



Unpair an Edge

Wraps POST /api/v2/telephony/providers/edges/{edgeId}/unpair 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge Id

try:
    # Unpair an Edge
    api_response = api_instance.post_telephony_providers_edge_unpair(edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edge_unpair: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge Id |  |
{: class="table table-striped"}

### Return type

**str**

<a name="post_telephony_providers_edges"></a>

## [**Edge**](Edge.html) post_telephony_providers_edges(body)



Create an edge.

Wraps POST /api/v2/telephony/providers/edges 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.Edge() # Edge | Edge

try:
    # Create an edge.
    api_response = api_instance.post_telephony_providers_edges(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Edge**](Edge.html)| Edge |  |
{: class="table table-striped"}

### Return type

[**Edge**](Edge.html)

<a name="post_telephony_providers_edges_addressvalidation"></a>

## [**ValidateAddressResponse**](ValidateAddressResponse.html) post_telephony_providers_edges_addressvalidation(body)



Validates a street address

Wraps POST /api/v2/telephony/providers/edges/addressvalidation 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.ValidateAddressRequest() # ValidateAddressRequest | Address

try:
    # Validates a street address
    api_response = api_instance.post_telephony_providers_edges_addressvalidation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_addressvalidation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ValidateAddressRequest**](ValidateAddressRequest.html)| Address |  |
{: class="table table-striped"}

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.html)

<a name="post_telephony_providers_edges_certificateauthorities"></a>

## [**DomainCertificateAuthority**](DomainCertificateAuthority.html) post_telephony_providers_edges_certificateauthorities(body)



Create a certificate authority.

Wraps POST /api/v2/telephony/providers/edges/certificateauthorities 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.DomainCertificateAuthority() # DomainCertificateAuthority | CertificateAuthority

try:
    # Create a certificate authority.
    api_response = api_instance.post_telephony_providers_edges_certificateauthorities(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_certificateauthorities: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DomainCertificateAuthority**](DomainCertificateAuthority.html)| CertificateAuthority |  |
{: class="table table-striped"}

### Return type

[**DomainCertificateAuthority**](DomainCertificateAuthority.html)

<a name="post_telephony_providers_edges_didpools"></a>

## [**DIDPool**](DIDPool.html) post_telephony_providers_edges_didpools(body)



Create a new DID pool

Wraps POST /api/v2/telephony/providers/edges/didpools 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.DIDPool() # DIDPool | DID pool

try:
    # Create a new DID pool
    api_response = api_instance.post_telephony_providers_edges_didpools(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_didpools: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DIDPool**](DIDPool.html)| DID pool |  |
{: class="table table-striped"}

### Return type

[**DIDPool**](DIDPool.html)

<a name="post_telephony_providers_edges_edgegroups"></a>

## [**EdgeGroup**](EdgeGroup.html) post_telephony_providers_edges_edgegroups(body)



Create an edge group.

Wraps POST /api/v2/telephony/providers/edges/edgegroups 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.EdgeGroup() # EdgeGroup | EdgeGroup

try:
    # Create an edge group.
    api_response = api_instance.post_telephony_providers_edges_edgegroups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_edgegroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EdgeGroup**](EdgeGroup.html)| EdgeGroup |  |
{: class="table table-striped"}

### Return type

[**EdgeGroup**](EdgeGroup.html)

<a name="post_telephony_providers_edges_extensionpools"></a>

## [**ExtensionPool**](ExtensionPool.html) post_telephony_providers_edges_extensionpools(body)



Create a new extension pool

Wraps POST /api/v2/telephony/providers/edges/extensionpools 

Requires ALL permissions: 

* telephony:extensionPool:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.ExtensionPool() # ExtensionPool | ExtensionPool

try:
    # Create a new extension pool
    api_response = api_instance.post_telephony_providers_edges_extensionpools(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_extensionpools: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ExtensionPool**](ExtensionPool.html)| ExtensionPool |  |
{: class="table table-striped"}

### Return type

[**ExtensionPool**](ExtensionPool.html)

<a name="post_telephony_providers_edges_phone_reboot"></a>

##  post_telephony_providers_edges_phone_reboot(phone_id)



Reboot a Phone

Wraps POST /api/v2/telephony/providers/edges/phones/{phoneId}/reboot 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_id = 'phone_id_example' # str | Phone Id

try:
    # Reboot a Phone
    api_instance.post_telephony_providers_edges_phone_reboot(phone_id)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_phone_reboot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_id** | **str**| Phone Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_telephony_providers_edges_phonebasesettings"></a>

## [**PhoneBase**](PhoneBase.html) post_telephony_providers_edges_phonebasesettings(body)



Create a new Phone Base Settings object

Wraps POST /api/v2/telephony/providers/edges/phonebasesettings 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.PhoneBase() # PhoneBase | Phone base settings

try:
    # Create a new Phone Base Settings object
    api_response = api_instance.post_telephony_providers_edges_phonebasesettings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_phonebasesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PhoneBase**](PhoneBase.html)| Phone base settings |  |
{: class="table table-striped"}

### Return type

[**PhoneBase**](PhoneBase.html)

<a name="post_telephony_providers_edges_phones"></a>

## [**Phone**](Phone.html) post_telephony_providers_edges_phones(body)



Create a new Phone

Wraps POST /api/v2/telephony/providers/edges/phones 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.Phone() # Phone | Phone

try:
    # Create a new Phone
    api_response = api_instance.post_telephony_providers_edges_phones(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_phones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Phone**](Phone.html)| Phone |  |
{: class="table table-striped"}

### Return type

[**Phone**](Phone.html)

<a name="post_telephony_providers_edges_phones_reboot"></a>

##  post_telephony_providers_edges_phones_reboot(body)



Reboot Multiple Phones

Wraps POST /api/v2/telephony/providers/edges/phones/reboot 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.PhonesReboot() # PhonesReboot | Phones

try:
    # Reboot Multiple Phones
    api_instance.post_telephony_providers_edges_phones_reboot(body)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_phones_reboot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PhonesReboot**](PhonesReboot.html)| Phones |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_telephony_providers_edges_site_outboundroutes"></a>

## [**OutboundRouteBase**](OutboundRouteBase.html) post_telephony_providers_edges_site_outboundroutes(site_id, body)



Create outbound route

Wraps POST /api/v2/telephony/providers/edges/sites/{siteId}/outboundroutes 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
body = PureCloudPlatformClientV2.OutboundRouteBase() # OutboundRouteBase | OutboundRoute

try:
    # Create outbound route
    api_response = api_instance.post_telephony_providers_edges_site_outboundroutes(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_site_outboundroutes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **body** | [**OutboundRouteBase**](OutboundRouteBase.html)| OutboundRoute |  |
{: class="table table-striped"}

### Return type

[**OutboundRouteBase**](OutboundRouteBase.html)

<a name="post_telephony_providers_edges_sites"></a>

## [**Site**](Site.html) post_telephony_providers_edges_sites(body)



Create a Site.

Wraps POST /api/v2/telephony/providers/edges/sites 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.Site() # Site | Site

try:
    # Create a Site.
    api_response = api_instance.post_telephony_providers_edges_sites(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_sites: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Site**](Site.html)| Site |  |
{: class="table table-striped"}

### Return type

[**Site**](Site.html)

<a name="post_telephony_providers_edges_trunkbasesettings"></a>

## [**TrunkBase**](TrunkBase.html) post_telephony_providers_edges_trunkbasesettings(body)



Create a Trunk Base Settings object

Wraps POST /api/v2/telephony/providers/edges/trunkbasesettings 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
body = PureCloudPlatformClientV2.TrunkBase() # TrunkBase | Trunk base settings

try:
    # Create a Trunk Base Settings object
    api_response = api_instance.post_telephony_providers_edges_trunkbasesettings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->post_telephony_providers_edges_trunkbasesettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrunkBase**](TrunkBase.html)| Trunk base settings |  |
{: class="table table-striped"}

### Return type

[**TrunkBase**](TrunkBase.html)

<a name="put_telephony_providers_edge"></a>

## [**Edge**](Edge.html) put_telephony_providers_edge(edge_id, body)



Update a edge.

Wraps PUT /api/v2/telephony/providers/edges/{edgeId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
body = PureCloudPlatformClientV2.Edge() # Edge | Edge

try:
    # Update a edge.
    api_response = api_instance.put_telephony_providers_edge(edge_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **body** | [**Edge**](Edge.html)| Edge |  |
{: class="table table-striped"}

### Return type

[**Edge**](Edge.html)

<a name="put_telephony_providers_edge_logicalinterface"></a>

## [**DomainLogicalInterface**](DomainLogicalInterface.html) put_telephony_providers_edge_logicalinterface(edge_id, interface_id, body)



Update an edge logical interface.

Wraps PUT /api/v2/telephony/providers/edges/{edgeId}/logicalinterfaces/{interfaceId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_id = 'edge_id_example' # str | Edge ID
interface_id = 'interface_id_example' # str | Interface ID
body = PureCloudPlatformClientV2.DomainLogicalInterface() # DomainLogicalInterface | Logical interface

try:
    # Update an edge logical interface.
    api_response = api_instance.put_telephony_providers_edge_logicalinterface(edge_id, interface_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edge_logicalinterface: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str**| Edge ID |  |
| **interface_id** | **str**| Interface ID |  |
| **body** | [**DomainLogicalInterface**](DomainLogicalInterface.html)| Logical interface |  |
{: class="table table-striped"}

### Return type

[**DomainLogicalInterface**](DomainLogicalInterface.html)

<a name="put_telephony_providers_edges_certificateauthority"></a>

## [**DomainCertificateAuthority**](DomainCertificateAuthority.html) put_telephony_providers_edges_certificateauthority(certificate_id, body)



Update a certificate authority.

Wraps PUT /api/v2/telephony/providers/edges/certificateauthorities/{certificateId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
certificate_id = 'certificate_id_example' # str | Certificate ID
body = PureCloudPlatformClientV2.DomainCertificateAuthority() # DomainCertificateAuthority | Certificate authority

try:
    # Update a certificate authority.
    api_response = api_instance.put_telephony_providers_edges_certificateauthority(certificate_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_certificateauthority: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **certificate_id** | **str**| Certificate ID |  |
| **body** | [**DomainCertificateAuthority**](DomainCertificateAuthority.html)| Certificate authority |  |
{: class="table table-striped"}

### Return type

[**DomainCertificateAuthority**](DomainCertificateAuthority.html)

<a name="put_telephony_providers_edges_didpool"></a>

## [**DIDPool**](DIDPool.html) put_telephony_providers_edges_didpool(did_pool_id, body)



Update a DID Pool by ID.

Wraps PUT /api/v2/telephony/providers/edges/didpools/{didPoolId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
did_pool_id = 'did_pool_id_example' # str | DID pool ID
body = PureCloudPlatformClientV2.DIDPool() # DIDPool | DID pool

try:
    # Update a DID Pool by ID.
    api_response = api_instance.put_telephony_providers_edges_didpool(did_pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_didpool: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **did_pool_id** | **str**| DID pool ID |  |
| **body** | [**DIDPool**](DIDPool.html)| DID pool |  |
{: class="table table-striped"}

### Return type

[**DIDPool**](DIDPool.html)

<a name="put_telephony_providers_edges_edgegroup"></a>

## [**EdgeGroup**](EdgeGroup.html) put_telephony_providers_edges_edgegroup(edge_group_id, body)



Update an edge group.

Wraps PUT /api/v2/telephony/providers/edges/edgegroups/{edgeGroupId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edge_group_id = 'edge_group_id_example' # str | Edge group ID
body = PureCloudPlatformClientV2.EdgeGroup() # EdgeGroup | EdgeGroup

try:
    # Update an edge group.
    api_response = api_instance.put_telephony_providers_edges_edgegroup(edge_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_edgegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edge_group_id** | **str**| Edge group ID |  |
| **body** | [**EdgeGroup**](EdgeGroup.html)| EdgeGroup |  |
{: class="table table-striped"}

### Return type

[**EdgeGroup**](EdgeGroup.html)

<a name="put_telephony_providers_edges_edgegroup_edgetrunkbase"></a>

## [**EdgeTrunkBase**](EdgeTrunkBase.html) put_telephony_providers_edges_edgegroup_edgetrunkbase(edgegroup_id, edgetrunkbase_id, body)



Update the edge trunk base associated with the edge group

Wraps PUT /api/v2/telephony/providers/edges/edgegroups/{edgegroupId}/edgetrunkbases/{edgetrunkbaseId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
edgegroup_id = 'edgegroup_id_example' # str | Edge Group ID
edgetrunkbase_id = 'edgetrunkbase_id_example' # str | Edge Trunk Base ID
body = PureCloudPlatformClientV2.EdgeTrunkBase() # EdgeTrunkBase | EdgeTrunkBase

try:
    # Update the edge trunk base associated with the edge group
    api_response = api_instance.put_telephony_providers_edges_edgegroup_edgetrunkbase(edgegroup_id, edgetrunkbase_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_edgegroup_edgetrunkbase: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **edgegroup_id** | **str**| Edge Group ID |  |
| **edgetrunkbase_id** | **str**| Edge Trunk Base ID |  |
| **body** | [**EdgeTrunkBase**](EdgeTrunkBase.html)| EdgeTrunkBase |  |
{: class="table table-striped"}

### Return type

[**EdgeTrunkBase**](EdgeTrunkBase.html)

<a name="put_telephony_providers_edges_extensionpool"></a>

## [**ExtensionPool**](ExtensionPool.html) put_telephony_providers_edges_extensionpool(extension_pool_id, body)



Update an extension pool by ID

Wraps PUT /api/v2/telephony/providers/edges/extensionpools/{extensionPoolId} 

Requires ALL permissions: 

* telephony:extensionPool:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
extension_pool_id = 'extension_pool_id_example' # str | Extension pool ID
body = PureCloudPlatformClientV2.ExtensionPool() # ExtensionPool | ExtensionPool

try:
    # Update an extension pool by ID
    api_response = api_instance.put_telephony_providers_edges_extensionpool(extension_pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_extensionpool: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **extension_pool_id** | **str**| Extension pool ID |  |
| **body** | [**ExtensionPool**](ExtensionPool.html)| ExtensionPool |  |
{: class="table table-striped"}

### Return type

[**ExtensionPool**](ExtensionPool.html)

<a name="put_telephony_providers_edges_phone"></a>

## [**Phone**](Phone.html) put_telephony_providers_edges_phone(phone_id, body)



Update a Phone by ID

Wraps PUT /api/v2/telephony/providers/edges/phones/{phoneId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_id = 'phone_id_example' # str | Phone ID
body = PureCloudPlatformClientV2.Phone() # Phone | Phone

try:
    # Update a Phone by ID
    api_response = api_instance.put_telephony_providers_edges_phone(phone_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_phone: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_id** | **str**| Phone ID |  |
| **body** | [**Phone**](Phone.html)| Phone |  |
{: class="table table-striped"}

### Return type

[**Phone**](Phone.html)

<a name="put_telephony_providers_edges_phonebasesetting"></a>

## [**PhoneBase**](PhoneBase.html) put_telephony_providers_edges_phonebasesetting(phone_base_id, body)



Update a Phone Base Settings by ID

Wraps PUT /api/v2/telephony/providers/edges/phonebasesettings/{phoneBaseId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
phone_base_id = 'phone_base_id_example' # str | Phone base ID
body = PureCloudPlatformClientV2.PhoneBase() # PhoneBase | Phone base settings

try:
    # Update a Phone Base Settings by ID
    api_response = api_instance.put_telephony_providers_edges_phonebasesetting(phone_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_phonebasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_base_id** | **str**| Phone base ID |  |
| **body** | [**PhoneBase**](PhoneBase.html)| Phone base settings |  |
{: class="table table-striped"}

### Return type

[**PhoneBase**](PhoneBase.html)

<a name="put_telephony_providers_edges_site"></a>

## [**Site**](Site.html) put_telephony_providers_edges_site(site_id, body)



Update a Site by ID.

Wraps PUT /api/v2/telephony/providers/edges/sites/{siteId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
body = PureCloudPlatformClientV2.Site() # Site | Site

try:
    # Update a Site by ID.
    api_response = api_instance.put_telephony_providers_edges_site(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_site: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **body** | [**Site**](Site.html)| Site |  |
{: class="table table-striped"}

### Return type

[**Site**](Site.html)

<a name="put_telephony_providers_edges_site_numberplans"></a>

## [**list[NumberPlan]**](NumberPlan.html) put_telephony_providers_edges_site_numberplans(site_id, body)



Update the list of Number Plans. A user can update maximum 200 number plans at a time.

Wraps PUT /api/v2/telephony/providers/edges/sites/{siteId}/numberplans 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
body = [PureCloudPlatformClientV2.NumberPlan()] # list[NumberPlan] | List of number plans

try:
    # Update the list of Number Plans. A user can update maximum 200 number plans at a time.
    api_response = api_instance.put_telephony_providers_edges_site_numberplans(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_site_numberplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **body** | [**list[NumberPlan]**](NumberPlan.html)| List of number plans |  |
{: class="table table-striped"}

### Return type

[**list[NumberPlan]**](NumberPlan.html)

<a name="put_telephony_providers_edges_site_outboundroute"></a>

## [**OutboundRouteBase**](OutboundRouteBase.html) put_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id, body)



Update outbound route

Wraps PUT /api/v2/telephony/providers/edges/sites/{siteId}/outboundroutes/{outboundRouteId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
outbound_route_id = 'outbound_route_id_example' # str | Outbound route ID
body = PureCloudPlatformClientV2.OutboundRouteBase() # OutboundRouteBase | OutboundRoute

try:
    # Update outbound route
    api_response = api_instance.put_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_site_outboundroute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **outbound_route_id** | **str**| Outbound route ID |  |
| **body** | [**OutboundRouteBase**](OutboundRouteBase.html)| OutboundRoute |  |
{: class="table table-striped"}

### Return type

[**OutboundRouteBase**](OutboundRouteBase.html)

<a name="put_telephony_providers_edges_site_siteconnections"></a>

## [**SiteConnections**](SiteConnections.html) put_telephony_providers_edges_site_siteconnections(site_id, body)



Update site connections for a site.

Wraps PUT /api/v2/telephony/providers/edges/sites/{siteId}/siteconnections 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
site_id = 'site_id_example' # str | Site ID
body = PureCloudPlatformClientV2.SiteConnections() # SiteConnections | Site

try:
    # Update site connections for a site.
    api_response = api_instance.put_telephony_providers_edges_site_siteconnections(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_site_siteconnections: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **site_id** | **str**| Site ID |  |
| **body** | [**SiteConnections**](SiteConnections.html)| Site |  |
{: class="table table-striped"}

### Return type

[**SiteConnections**](SiteConnections.html)

<a name="put_telephony_providers_edges_trunkbasesetting"></a>

## [**TrunkBase**](TrunkBase.html) put_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id, body)



Update a Trunk Base Settings object by ID

Wraps PUT /api/v2/telephony/providers/edges/trunkbasesettings/{trunkBaseSettingsId} 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi()
trunk_base_settings_id = 'trunk_base_settings_id_example' # str | Trunk Base ID
body = PureCloudPlatformClientV2.TrunkBase() # TrunkBase | Trunk base settings

try:
    # Update a Trunk Base Settings object by ID
    api_response = api_instance.put_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_trunkbasesetting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trunk_base_settings_id** | **str**| Trunk Base ID |  |
| **body** | [**TrunkBase**](TrunkBase.html)| Trunk base settings |  |
{: class="table table-striped"}

### Return type

[**TrunkBase**](TrunkBase.html)

