# TelephonyProvidersEdgeApi

## PureCloudPlatformClientV2.TelephonyProvidersEdgeApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_telephony_providers_edge**](#delete_telephony_providers_edge) | Delete a edge.|
|[**delete_telephony_providers_edge_logicalinterface**](#delete_telephony_providers_edge_logicalinterface) | Delete an edge logical interface|
|[**delete_telephony_providers_edge_softwareupdate**](#delete_telephony_providers_edge_softwareupdate) | Cancels any in-progress update for this edge.|
|[**delete_telephony_providers_edges_alertablepresences**](#delete_telephony_providers_edges_alertablepresences) | Deletes alertable presences overrides.|
|[**delete_telephony_providers_edges_certificateauthority**](#delete_telephony_providers_edges_certificateauthority) | Delete a certificate authority.|
|[**delete_telephony_providers_edges_didpool**](#delete_telephony_providers_edges_didpool) | Delete a DID Pool by ID.|
|[**delete_telephony_providers_edges_edgegroup**](#delete_telephony_providers_edges_edgegroup) | Delete an edge group.|
|[**delete_telephony_providers_edges_extensionpool**](#delete_telephony_providers_edges_extensionpool) | Delete an extension pool by ID|
|[**delete_telephony_providers_edges_phone**](#delete_telephony_providers_edges_phone) | Delete a Phone by ID|
|[**delete_telephony_providers_edges_phonebasesetting**](#delete_telephony_providers_edges_phonebasesetting) | Delete a Phone Base Settings by ID|
|[**delete_telephony_providers_edges_site**](#delete_telephony_providers_edges_site) | Delete a Site by ID|
|[**delete_telephony_providers_edges_site_outboundroute**](#delete_telephony_providers_edges_site_outboundroute) | Delete Outbound Route|
|[**delete_telephony_providers_edges_trunkbasesetting**](#delete_telephony_providers_edges_trunkbasesetting) | Delete a Trunk Base Settings object by ID|
|[**get_telephony_providers_edge**](#get_telephony_providers_edge) | Get edge.|
|[**get_telephony_providers_edge_diagnostic_nslookup**](#get_telephony_providers_edge_diagnostic_nslookup) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_diagnostic_ping**](#get_telephony_providers_edge_diagnostic_ping) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_diagnostic_route**](#get_telephony_providers_edge_diagnostic_route) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_diagnostic_tracepath**](#get_telephony_providers_edge_diagnostic_tracepath) | Get networking-related information from an Edge for a target IP or host.|
|[**get_telephony_providers_edge_logicalinterface**](#get_telephony_providers_edge_logicalinterface) | Get an edge logical interface|
|[**get_telephony_providers_edge_logicalinterfaces**](#get_telephony_providers_edge_logicalinterfaces) | Get edge logical interfaces.|
|[**get_telephony_providers_edge_logs_job**](#get_telephony_providers_edge_logs_job) | Get an Edge logs job.|
|[**get_telephony_providers_edge_metrics**](#get_telephony_providers_edge_metrics) | Get the edge metrics.|
|[**get_telephony_providers_edge_physicalinterface**](#get_telephony_providers_edge_physicalinterface) | Get edge physical interface.|
|[**get_telephony_providers_edge_physicalinterfaces**](#get_telephony_providers_edge_physicalinterfaces) | Retrieve a list of all configured physical interfaces from a specific edge.|
|[**get_telephony_providers_edge_setuppackage**](#get_telephony_providers_edge_setuppackage) | Get the setup package for a locally deployed edge device. This is needed to complete the setup process for the virtual edge.|
|[**get_telephony_providers_edge_softwareupdate**](#get_telephony_providers_edge_softwareupdate) | Gets software update status information about any edge.|
|[**get_telephony_providers_edge_softwareversions**](#get_telephony_providers_edge_softwareversions) | Gets all the available software versions for this edge.|
|[**get_telephony_providers_edge_trunks**](#get_telephony_providers_edge_trunks) | Get the list of available trunks for the given Edge.|
|[**get_telephony_providers_edges**](#get_telephony_providers_edges) | Get the list of edges.|
|[**get_telephony_providers_edges_alertablepresences**](#get_telephony_providers_edges_alertablepresences) | Get the list alertable presences. The &#39;type&#39; query parameter can be used to If there are any overrides, this is the list of overrides; if there are no overrides, it is the default list.|
|[**get_telephony_providers_edges_certificateauthorities**](#get_telephony_providers_edges_certificateauthorities) | Get the list of certificate authorities.|
|[**get_telephony_providers_edges_certificateauthority**](#get_telephony_providers_edges_certificateauthority) | Get a certificate authority.|
|[**get_telephony_providers_edges_did**](#get_telephony_providers_edges_did) | Get a DID by ID.|
|[**get_telephony_providers_edges_didpool**](#get_telephony_providers_edges_didpool) | Get a DID Pool by ID.|
|[**get_telephony_providers_edges_didpools**](#get_telephony_providers_edges_didpools) | Get a listing of DID Pools|
|[**get_telephony_providers_edges_didpools_dids**](#get_telephony_providers_edges_didpools_dids) | Get a listing of unassigned and/or assigned numbers in a set of DID Pools.|
|[**get_telephony_providers_edges_dids**](#get_telephony_providers_edges_dids) | Get a listing of DIDs|
|[**get_telephony_providers_edges_edgegroup**](#get_telephony_providers_edges_edgegroup) | Get edge group.|
|[**get_telephony_providers_edges_edgegroup_edgetrunkbase**](#get_telephony_providers_edges_edgegroup_edgetrunkbase) | Gets the edge trunk base associated with the edge group|
|[**get_telephony_providers_edges_edgegroups**](#get_telephony_providers_edges_edgegroups) | Get the list of edge groups.|
|[**get_telephony_providers_edges_edgeversionreport**](#get_telephony_providers_edges_edgeversionreport) | Get the edge version report.|
|[**get_telephony_providers_edges_expired**](#get_telephony_providers_edges_expired) | List of edges more than 4 edge versions behind the latest software.|
|[**get_telephony_providers_edges_extension**](#get_telephony_providers_edges_extension) | Get an extension by ID.|
|[**get_telephony_providers_edges_extensionpool**](#get_telephony_providers_edges_extensionpool) | Get an extension pool by ID|
|[**get_telephony_providers_edges_extensionpools**](#get_telephony_providers_edges_extensionpools) | Get a listing of extension pools|
|[**get_telephony_providers_edges_extensionpools_divisionviews**](#get_telephony_providers_edges_extensionpools_divisionviews) | Get a pageable list of basic extension pool objects filterable by query parameters.|
|[**get_telephony_providers_edges_extensions**](#get_telephony_providers_edges_extensions) | Get a listing of extensions|
|[**get_telephony_providers_edges_line**](#get_telephony_providers_edges_line) | Get a Line by ID|
|[**get_telephony_providers_edges_linebasesetting**](#get_telephony_providers_edges_linebasesetting) | Get a line base settings object by ID|
|[**get_telephony_providers_edges_linebasesettings**](#get_telephony_providers_edges_linebasesettings) | Get a listing of line base settings objects|
|[**get_telephony_providers_edges_lines**](#get_telephony_providers_edges_lines) | Get a list of Lines|
|[**get_telephony_providers_edges_lines_template**](#get_telephony_providers_edges_lines_template) | Get a Line instance template based on a Line Base Settings object. This object can then be modified and saved as a new Line instance|
|[**get_telephony_providers_edges_logicalinterfaces**](#get_telephony_providers_edges_logicalinterfaces) | Get edge logical interfaces.|
|[**get_telephony_providers_edges_mediastatistics_conversation**](#get_telephony_providers_edges_mediastatistics_conversation) | Get media endpoint statistics events.|
|[**get_telephony_providers_edges_mediastatistics_conversation_communication**](#get_telephony_providers_edges_mediastatistics_conversation_communication) | Get media endpoint statistics event.|
|[**get_telephony_providers_edges_metrics**](#get_telephony_providers_edges_metrics) | Get the metrics for a list of edges.|
|[**get_telephony_providers_edges_outboundroutes**](#get_telephony_providers_edges_outboundroutes) | Get outbound routes|
|[**get_telephony_providers_edges_phone**](#get_telephony_providers_edges_phone) | Get a Phone by ID|
|[**get_telephony_providers_edges_phonebasesetting**](#get_telephony_providers_edges_phonebasesetting) | Get a Phone Base Settings object by ID|
|[**get_telephony_providers_edges_phonebasesettings**](#get_telephony_providers_edges_phonebasesettings) | Get a list of Phone Base Settings objects|
|[**get_telephony_providers_edges_phonebasesettings_availablemetabases**](#get_telephony_providers_edges_phonebasesettings_availablemetabases) | Get a list of available makes and models to create a new Phone Base Settings|
|[**get_telephony_providers_edges_phonebasesettings_template**](#get_telephony_providers_edges_phonebasesettings_template) | Get a Phone Base Settings instance template from a given make and model. This object can then be modified and saved as a new Phone Base Settings instance|
|[**get_telephony_providers_edges_phones**](#get_telephony_providers_edges_phones) | Get a list of Phone Instances. A maximum of 10,000 results is returned when filtering the results or sorting by a field other than the ID. Sorting by only the ID has no result limit. Each filter supports a wildcard, *, as a value to search for partial values.|
|[**get_telephony_providers_edges_phones_template**](#get_telephony_providers_edges_phones_template) | Get a Phone instance template based on a Phone Base Settings object. This object can then be modified and saved as a new Phone instance|
|[**get_telephony_providers_edges_physicalinterfaces**](#get_telephony_providers_edges_physicalinterfaces) | Get physical interfaces for edges.|
|[**get_telephony_providers_edges_site**](#get_telephony_providers_edges_site) | Get a Site by ID.|
|[**get_telephony_providers_edges_site_numberplan**](#get_telephony_providers_edges_site_numberplan) | Get a Number Plan by ID.|
|[**get_telephony_providers_edges_site_numberplans**](#get_telephony_providers_edges_site_numberplans) | Get the list of Number Plans for this Site. Only fetches the first 200 records.|
|[**get_telephony_providers_edges_site_numberplans_classifications**](#get_telephony_providers_edges_site_numberplans_classifications) | Get a list of Classifications for this Site|
|[**get_telephony_providers_edges_site_outboundroute**](#get_telephony_providers_edges_site_outboundroute) | Get an outbound route|
|[**get_telephony_providers_edges_site_outboundroutes**](#get_telephony_providers_edges_site_outboundroutes) | Get outbound routes|
|[**get_telephony_providers_edges_site_siteconnections**](#get_telephony_providers_edges_site_siteconnections) | Get site connections for a site.|
|[**get_telephony_providers_edges_sites**](#get_telephony_providers_edges_sites) | Get the list of Sites.|
|[**get_telephony_providers_edges_timezones**](#get_telephony_providers_edges_timezones) | Get a list of Edge-compatible time zones|
|[**get_telephony_providers_edges_trunk**](#get_telephony_providers_edges_trunk) | Get a Trunk by ID|
|[**get_telephony_providers_edges_trunk_metrics**](#get_telephony_providers_edges_trunk_metrics) | Get the trunk metrics.|
|[**get_telephony_providers_edges_trunkbasesetting**](#get_telephony_providers_edges_trunkbasesetting) | Get a Trunk Base Settings object by ID|
|[**get_telephony_providers_edges_trunkbasesettings**](#get_telephony_providers_edges_trunkbasesettings) | Get Trunk Base Settings listing|
|[**get_telephony_providers_edges_trunkbasesettings_availablemetabases**](#get_telephony_providers_edges_trunkbasesettings_availablemetabases) | Get a list of available makes and models to create a new Trunk Base Settings|
|[**get_telephony_providers_edges_trunkbasesettings_template**](#get_telephony_providers_edges_trunkbasesettings_template) | Get a Trunk Base Settings instance template from a given make and model. This object can then be modified and saved as a new Trunk Base Settings instance|
|[**get_telephony_providers_edges_trunks**](#get_telephony_providers_edges_trunks) | Get the list of available trunks.|
|[**get_telephony_providers_edges_trunks_metrics**](#get_telephony_providers_edges_trunks_metrics) | Get the metrics for a list of trunks.|
|[**get_telephony_providers_edges_trunkswithrecording**](#get_telephony_providers_edges_trunkswithrecording) | Get Counts of trunks that have recording disabled or enabled|
|[**patch_telephony_providers_edges_site_siteconnections**](#patch_telephony_providers_edges_site_siteconnections) | Disable site connections for a site.|
|[**post_telephony_providers_edge_diagnostic_nslookup**](#post_telephony_providers_edge_diagnostic_nslookup) | Nslookup request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_diagnostic_ping**](#post_telephony_providers_edge_diagnostic_ping) | Ping Request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_diagnostic_route**](#post_telephony_providers_edge_diagnostic_route) | Route request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_diagnostic_tracepath**](#post_telephony_providers_edge_diagnostic_tracepath) | Tracepath request command to collect networking-related information from an Edge for a target IP or host.|
|[**post_telephony_providers_edge_logicalinterfaces**](#post_telephony_providers_edge_logicalinterfaces) | Create an edge logical interface.|
|[**post_telephony_providers_edge_logs_job_upload**](#post_telephony_providers_edge_logs_job_upload) | Request that the specified fileIds be uploaded from the Edge.|
|[**post_telephony_providers_edge_logs_jobs**](#post_telephony_providers_edge_logs_jobs) | Create a job to upload a list of Edge logs.|
|[**post_telephony_providers_edge_reboot**](#post_telephony_providers_edge_reboot) | Reboot an Edge|
|[**post_telephony_providers_edge_softwareupdate**](#post_telephony_providers_edge_softwareupdate) | Starts a software update for this edge.|
|[**post_telephony_providers_edge_statuscode**](#post_telephony_providers_edge_statuscode) | Take an Edge in or out of service|
|[**post_telephony_providers_edge_unpair**](#post_telephony_providers_edge_unpair) | Unpair an Edge|
|[**post_telephony_providers_edges**](#post_telephony_providers_edges) | Create an edge.|
|[**post_telephony_providers_edges_addressvalidation**](#post_telephony_providers_edges_addressvalidation) | Validates a street address|
|[**post_telephony_providers_edges_certificateauthorities**](#post_telephony_providers_edges_certificateauthorities) | Create a certificate authority.|
|[**post_telephony_providers_edges_didpools**](#post_telephony_providers_edges_didpools) | Create a new DID pool|
|[**post_telephony_providers_edges_edgegroups**](#post_telephony_providers_edges_edgegroups) | Create an edge group.|
|[**post_telephony_providers_edges_extensionpools**](#post_telephony_providers_edges_extensionpools) | Create a new extension pool|
|[**post_telephony_providers_edges_phone_reboot**](#post_telephony_providers_edges_phone_reboot) | Reboot a Phone|
|[**post_telephony_providers_edges_phonebasesettings**](#post_telephony_providers_edges_phonebasesettings) | Create a new Phone Base Settings object|
|[**post_telephony_providers_edges_phones**](#post_telephony_providers_edges_phones) | Create a new Phone|
|[**post_telephony_providers_edges_phones_reboot**](#post_telephony_providers_edges_phones_reboot) | Reboot Multiple Phones|
|[**post_telephony_providers_edges_site_outboundroutes**](#post_telephony_providers_edges_site_outboundroutes) | Create outbound route|
|[**post_telephony_providers_edges_sites**](#post_telephony_providers_edges_sites) | Create a Site.|
|[**post_telephony_providers_edges_trunkbasesettings**](#post_telephony_providers_edges_trunkbasesettings) | Create a Trunk Base Settings object|
|[**put_telephony_providers_edge**](#put_telephony_providers_edge) | Update a edge.|
|[**put_telephony_providers_edge_logicalinterface**](#put_telephony_providers_edge_logicalinterface) | Update an edge logical interface.|
|[**put_telephony_providers_edges_alertablepresences**](#put_telephony_providers_edges_alertablepresences) | Creates or updates alertable presences overrides.|
|[**put_telephony_providers_edges_certificateauthority**](#put_telephony_providers_edges_certificateauthority) | Update a certificate authority.|
|[**put_telephony_providers_edges_didpool**](#put_telephony_providers_edges_didpool) | Update a DID Pool by ID.|
|[**put_telephony_providers_edges_edgegroup**](#put_telephony_providers_edges_edgegroup) | Update an edge group.|
|[**put_telephony_providers_edges_edgegroup_edgetrunkbase**](#put_telephony_providers_edges_edgegroup_edgetrunkbase) | Update the edge trunk base associated with the edge group|
|[**put_telephony_providers_edges_extensionpool**](#put_telephony_providers_edges_extensionpool) | Update an extension pool by ID|
|[**put_telephony_providers_edges_phone**](#put_telephony_providers_edges_phone) | Update a Phone by ID|
|[**put_telephony_providers_edges_phonebasesetting**](#put_telephony_providers_edges_phonebasesetting) | Update a Phone Base Settings by ID|
|[**put_telephony_providers_edges_site**](#put_telephony_providers_edges_site) | Update a Site by ID.|
|[**put_telephony_providers_edges_site_numberplans**](#put_telephony_providers_edges_site_numberplans) | Update the list of Number Plans. A user can update maximum 200 number plans at a time.|
|[**put_telephony_providers_edges_site_outboundroute**](#put_telephony_providers_edges_site_outboundroute) | Update outbound route|
|[**put_telephony_providers_edges_site_siteconnections**](#put_telephony_providers_edges_site_siteconnections) | Update site connections for a site.|
|[**put_telephony_providers_edges_trunkbasesetting**](#put_telephony_providers_edges_trunkbasesetting) | Update a Trunk Base Settings object by ID|



## delete_telephony_providers_edge

>  delete_telephony_providers_edge(edge_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edge_logicalinterface

>  delete_telephony_providers_edge_logicalinterface(edge_id, interface_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edge_softwareupdate

>  delete_telephony_providers_edge_softwareupdate(edge_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_alertablepresences

>  delete_telephony_providers_edges_alertablepresences()


Deletes alertable presences overrides.

Wraps DELETE /api/v2/telephony/providers/edges/alertablepresences 

Requires ANY permissions: 

* telephony:alertablePresences:delete

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
    # Deletes alertable presences overrides.
    api_instance.delete_telephony_providers_edges_alertablepresences()
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->delete_telephony_providers_edges_alertablepresences: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_telephony_providers_edges_certificateauthority

>  delete_telephony_providers_edges_certificateauthority(certificate_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_didpool

>  delete_telephony_providers_edges_didpool(did_pool_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_edgegroup

>  delete_telephony_providers_edges_edgegroup(edge_group_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_extensionpool

>  delete_telephony_providers_edges_extensionpool(extension_pool_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_phone

>  delete_telephony_providers_edges_phone(phone_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_phonebasesetting

>  delete_telephony_providers_edges_phonebasesetting(phone_base_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_site

>  delete_telephony_providers_edges_site(site_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_site_outboundroute

>  delete_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id)


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

### Return type

void (empty response body)


## delete_telephony_providers_edges_trunkbasesetting

>  delete_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id)


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

### Return type

void (empty response body)


## get_telephony_providers_edge

> [**Edge**](Edge) get_telephony_providers_edge(edge_id, expand=expand)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: site |

### Return type

[**Edge**](Edge)


## get_telephony_providers_edge_diagnostic_nslookup

> [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse) get_telephony_providers_edge_diagnostic_nslookup(edge_id)


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

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse)


## get_telephony_providers_edge_diagnostic_ping

> [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse) get_telephony_providers_edge_diagnostic_ping(edge_id)


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

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse)


## get_telephony_providers_edge_diagnostic_route

> [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse) get_telephony_providers_edge_diagnostic_route(edge_id)


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

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse)


## get_telephony_providers_edge_diagnostic_tracepath

> [**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse) get_telephony_providers_edge_diagnostic_tracepath(edge_id)


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

### Return type

[**EdgeNetworkDiagnosticResponse**](EdgeNetworkDiagnosticResponse)


## get_telephony_providers_edge_logicalinterface

> [**DomainLogicalInterface**](DomainLogicalInterface) get_telephony_providers_edge_logicalinterface(edge_id, interface_id, expand=expand)


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
| **expand** | [**list[str]**](str)| Field to expand in the response | [optional] <br />**Values**: externalTrunkBaseAssignments, phoneTrunkBaseAssignments |

### Return type

[**DomainLogicalInterface**](DomainLogicalInterface)


## get_telephony_providers_edge_logicalinterfaces

> [**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing) get_telephony_providers_edge_logicalinterfaces(edge_id, expand=expand)


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
| **expand** | [**list[str]**](str)| Field to expand in the response | [optional] <br />**Values**: externalTrunkBaseAssignments, phoneTrunkBaseAssignments |

### Return type

[**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing)


## get_telephony_providers_edge_logs_job

> [**EdgeLogsJob**](EdgeLogsJob) get_telephony_providers_edge_logs_job(edge_id, job_id)


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

### Return type

[**EdgeLogsJob**](EdgeLogsJob)


## get_telephony_providers_edge_metrics

> [**EdgeMetrics**](EdgeMetrics) get_telephony_providers_edge_metrics(edge_id)


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

### Return type

[**EdgeMetrics**](EdgeMetrics)


## get_telephony_providers_edge_physicalinterface

> [**DomainPhysicalInterface**](DomainPhysicalInterface) get_telephony_providers_edge_physicalinterface(edge_id, interface_id)


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

### Return type

[**DomainPhysicalInterface**](DomainPhysicalInterface)


## get_telephony_providers_edge_physicalinterfaces

> [**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing) get_telephony_providers_edge_physicalinterfaces(edge_id)


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

### Return type

[**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing)


## get_telephony_providers_edge_setuppackage

> [**VmPairingInfo**](VmPairingInfo) get_telephony_providers_edge_setuppackage(edge_id)


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

### Return type

[**VmPairingInfo**](VmPairingInfo)


## get_telephony_providers_edge_softwareupdate

> [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto) get_telephony_providers_edge_softwareupdate(edge_id)


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

### Return type

[**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto)


## get_telephony_providers_edge_softwareversions

> [**DomainEdgeSoftwareVersionDtoEntityListing**](DomainEdgeSoftwareVersionDtoEntityListing) get_telephony_providers_edge_softwareversions(edge_id)


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

### Return type

[**DomainEdgeSoftwareVersionDtoEntityListing**](DomainEdgeSoftwareVersionDtoEntityListing)


## get_telephony_providers_edge_trunks

> [**TrunkEntityListing**](TrunkEntityListing) get_telephony_providers_edge_trunks(edge_id, page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, trunk_base_id=trunk_base_id, trunk_type=trunk_type)


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

### Return type

[**TrunkEntityListing**](TrunkEntityListing)


## get_telephony_providers_edges

> [**EdgeEntityListing**](EdgeEntityListing) get_telephony_providers_edges(page_size=page_size, page_number=page_number, name=name, site_id=site_id, edge_group_id=edge_group_id, sort_by=sort_by, managed=managed, show_cloud_media=show_cloud_media)


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

### Return type

[**EdgeEntityListing**](EdgeEntityListing)


## get_telephony_providers_edges_alertablepresences

> [**AlertablePresences**](AlertablePresences) get_telephony_providers_edges_alertablepresences(type=type)


Get the list alertable presences. The 'type' query parameter can be used to If there are any overrides, this is the list of overrides; if there are no overrides, it is the default list.

Wraps GET /api/v2/telephony/providers/edges/alertablepresences 

Requires ANY permissions: 

* telephony:alertablePresences:view

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

try:
    # Get the list alertable presences. The 'type' query parameter can be used to If there are any overrides, this is the list of overrides; if there are no overrides, it is the default list.
    api_response = api_instance.get_telephony_providers_edges_alertablepresences(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_alertablepresences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**|  | [optional] <br />**Values**: defaults, overrides |

### Return type

[**AlertablePresences**](AlertablePresences)


## get_telephony_providers_edges_certificateauthorities

> [**CertificateAuthorityEntityListing**](CertificateAuthorityEntityListing) get_telephony_providers_edges_certificateauthorities()


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

[**CertificateAuthorityEntityListing**](CertificateAuthorityEntityListing)


## get_telephony_providers_edges_certificateauthority

> [**DomainCertificateAuthority**](DomainCertificateAuthority) get_telephony_providers_edges_certificateauthority(certificate_id)


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

### Return type

[**DomainCertificateAuthority**](DomainCertificateAuthority)


## get_telephony_providers_edges_did

> [**DID**](DID) get_telephony_providers_edges_did(did_id)


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

### Return type

[**DID**](DID)


## get_telephony_providers_edges_didpool

> [**DIDPool**](DIDPool) get_telephony_providers_edges_didpool(did_pool_id)


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

### Return type

[**DIDPool**](DIDPool)


## get_telephony_providers_edges_didpools

> [**DIDPoolEntityListing**](DIDPoolEntityListing) get_telephony_providers_edges_didpools(page_size=page_size, page_number=page_number, sort_by=sort_by, id=id)


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
| **id** | [**list[str]**](str)| Filter by a specific list of ID&#39;s | [optional]  |

### Return type

[**DIDPoolEntityListing**](DIDPoolEntityListing)


## get_telephony_providers_edges_didpools_dids

> [**DIDNumberEntityListing**](DIDNumberEntityListing) get_telephony_providers_edges_didpools_dids(type, id=id, number_match=number_match, page_size=page_size, page_number=page_number, sort_order=sort_order)


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
| **id** | [**list[str]**](str)| Filter by a specific list of DID Pools.  If this is not provided, numbers from all DID Pools will be returned. | [optional]  |
| **number_match** | **str**| A number to filter the results by. | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;] |

### Return type

[**DIDNumberEntityListing**](DIDNumberEntityListing)


## get_telephony_providers_edges_dids

> [**DIDEntityListing**](DIDEntityListing) get_telephony_providers_edges_dids(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, phone_number=phone_number, owner_id=owner_id, did_pool_id=did_pool_id, id=id)


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
| **id** | [**list[str]**](str)| Filter by a specific list of ID&#39;s | [optional]  |

### Return type

[**DIDEntityListing**](DIDEntityListing)


## get_telephony_providers_edges_edgegroup

> [**EdgeGroup**](EdgeGroup) get_telephony_providers_edges_edgegroup(edge_group_id, expand=expand)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response | [optional] <br />**Values**: phoneTrunkBases, edgeTrunkBaseAssignment |

### Return type

[**EdgeGroup**](EdgeGroup)


## get_telephony_providers_edges_edgegroup_edgetrunkbase

> [**EdgeTrunkBase**](EdgeTrunkBase) get_telephony_providers_edges_edgegroup_edgetrunkbase(edgegroup_id, edgetrunkbase_id)


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

### Return type

[**EdgeTrunkBase**](EdgeTrunkBase)


## get_telephony_providers_edges_edgegroups

> [**EdgeGroupEntityListing**](EdgeGroupEntityListing) get_telephony_providers_edges_edgegroups(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, managed=managed)


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

### Return type

[**EdgeGroupEntityListing**](EdgeGroupEntityListing)


## get_telephony_providers_edges_edgeversionreport

> [**EdgeVersionReport**](EdgeVersionReport) get_telephony_providers_edges_edgeversionreport()


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

[**EdgeVersionReport**](EdgeVersionReport)


## get_telephony_providers_edges_expired

> [**ExpiredEdgeListing**](ExpiredEdgeListing) get_telephony_providers_edges_expired()


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

[**ExpiredEdgeListing**](ExpiredEdgeListing)


## get_telephony_providers_edges_extension

> [**Extension**](Extension) get_telephony_providers_edges_extension(extension_id)


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

### Return type

[**Extension**](Extension)


## get_telephony_providers_edges_extensionpool

> [**ExtensionPool**](ExtensionPool) get_telephony_providers_edges_extensionpool(extension_pool_id)


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

### Return type

[**ExtensionPool**](ExtensionPool)


## get_telephony_providers_edges_extensionpools

> [**ExtensionPoolEntityListing**](ExtensionPoolEntityListing) get_telephony_providers_edges_extensionpools(page_size=page_size, page_number=page_number, sort_by=sort_by, number=number)


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

### Return type

[**ExtensionPoolEntityListing**](ExtensionPoolEntityListing)


## get_telephony_providers_edges_extensionpools_divisionviews

> [**ExtensionPoolDivisionViewEntityListing**](ExtensionPoolDivisionViewEntityListing) get_telephony_providers_edges_extensionpools_divisionviews(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, id=id, name=name, division_id=division_id)


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
| **id** | [**list[str]**](str)| ID of the Extension Pools to filter by. | [optional]  |
| **name** | **str**| Name of the Extension Pools to filter by. | [optional]  |
| **division_id** | [**list[str]**](str)| List of divisionIds on which to filter. | [optional]  |

### Return type

[**ExtensionPoolDivisionViewEntityListing**](ExtensionPoolDivisionViewEntityListing)


## get_telephony_providers_edges_extensions

> [**ExtensionEntityListing**](ExtensionEntityListing) get_telephony_providers_edges_extensions(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, number=number)


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

### Return type

[**ExtensionEntityListing**](ExtensionEntityListing)


## get_telephony_providers_edges_line

> [**Line**](Line) get_telephony_providers_edges_line(line_id)


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

### Return type

[**Line**](Line)


## get_telephony_providers_edges_linebasesetting

> [**LineBase**](LineBase) get_telephony_providers_edges_linebasesetting(line_base_id)


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

### Return type

[**LineBase**](LineBase)


## get_telephony_providers_edges_linebasesettings

> [**LineBaseEntityListing**](LineBaseEntityListing) get_telephony_providers_edges_linebasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, expand=expand)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties |

### Return type

[**LineBaseEntityListing**](LineBaseEntityListing)


## get_telephony_providers_edges_lines

> [**LineEntityListing**](LineEntityListing) get_telephony_providers_edges_lines(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, expand=expand)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated. The edgeGroup value is deprecated. | [optional] <br />**Values**: properties, site, edgeGroup, primaryEdge, secondaryEdge, edges, assignedUser |

### Return type

[**LineEntityListing**](LineEntityListing)


## get_telephony_providers_edges_lines_template

> [**Line**](Line) get_telephony_providers_edges_lines_template(line_base_settings_id)


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

### Return type

[**Line**](Line)


## get_telephony_providers_edges_logicalinterfaces

> [**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing) get_telephony_providers_edges_logicalinterfaces(edge_ids, expand=expand)


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
| **expand** | [**list[str]**](str)| Field to expand in the response | [optional] <br />**Values**: externalTrunkBaseAssignments, phoneTrunkBaseAssignments |

### Return type

[**LogicalInterfaceEntityListing**](LogicalInterfaceEntityListing)


## get_telephony_providers_edges_mediastatistics_conversation

> [**MediaStatisticsListing**](MediaStatisticsListing) get_telephony_providers_edges_mediastatistics_conversation(conversation_id)


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

### Return type

[**MediaStatisticsListing**](MediaStatisticsListing)


## get_telephony_providers_edges_mediastatistics_conversation_communication

> [**MediaStatistics**](MediaStatistics) get_telephony_providers_edges_mediastatistics_conversation_communication(conversation_id, communication_id)


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

### Return type

[**MediaStatistics**](MediaStatistics)


## get_telephony_providers_edges_metrics

> [**list[EdgeMetrics]**](EdgeMetrics) get_telephony_providers_edges_metrics(edge_ids)


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

### Return type

[**list[EdgeMetrics]**](EdgeMetrics)


## get_telephony_providers_edges_outboundroutes

> [**OutboundRouteEntityListing**](OutboundRouteEntityListing) get_telephony_providers_edges_outboundroutes(page_size=page_size, page_number=page_number, name=name, site_id=site_id, external_trunk_bases_ids=external_trunk_bases_ids, sort_by=sort_by)


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

### Return type

[**OutboundRouteEntityListing**](OutboundRouteEntityListing)


## get_telephony_providers_edges_phone

> [**Phone**](Phone) get_telephony_providers_edges_phone(phone_id)


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

### Return type

[**Phone**](Phone)


## get_telephony_providers_edges_phonebasesetting

> [**PhoneBase**](PhoneBase) get_telephony_providers_edges_phonebasesetting(phone_base_id)


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

### Return type

[**PhoneBase**](PhoneBase)


## get_telephony_providers_edges_phonebasesettings

> [**PhoneBaseEntityListing**](PhoneBaseEntityListing) get_telephony_providers_edges_phonebasesettings(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, expand=expand, name=name)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties, lines |
| **name** | **str**| Name | [optional]  |

### Return type

[**PhoneBaseEntityListing**](PhoneBaseEntityListing)


## get_telephony_providers_edges_phonebasesettings_availablemetabases

> [**PhoneMetaBaseEntityListing**](PhoneMetaBaseEntityListing) get_telephony_providers_edges_phonebasesettings_availablemetabases(page_size=page_size, page_number=page_number)


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

### Return type

[**PhoneMetaBaseEntityListing**](PhoneMetaBaseEntityListing)


## get_telephony_providers_edges_phonebasesettings_template

> [**PhoneBase**](PhoneBase) get_telephony_providers_edges_phonebasesettings_template(phone_metabase_id)


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

### Return type

[**PhoneBase**](PhoneBase)


## get_telephony_providers_edges_phones

> [**PhoneEntityListing**](PhoneEntityListing) get_telephony_providers_edges_phones(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, site_id=site_id, web_rtc_user_id=web_rtc_user_id, phone_base_settings_id=phone_base_settings_id, lines_logged_in_user_id=lines_logged_in_user_id, lines_default_for_user_id=lines_default_for_user_id, phone_hardware_id=phone_hardware_id, lines_id=lines_id, lines_name=lines_name, name=name, status_operational_status=status_operational_status, secondary_status_operational_status=secondary_status_operational_status, expand=expand, fields=fields)


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
| **sort_by** | **str**| The field to sort by | [optional] [default to &#39;name&#39;]<br />**Values**: id, name, status.operationalStatus, secondaryStatus.operationalStatus |
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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties, site, status, status.primaryEdgesStatus, status.secondaryEdgesStatus, phoneBaseSettings, lines |
| **fields** | [**list[str]**](str)| Fields and properties to get, comma-separated | [optional] <br />**Values**: webRtcUser, properties.*, lines.loggedInUser, lines.defaultForUser |

### Return type

[**PhoneEntityListing**](PhoneEntityListing)


## get_telephony_providers_edges_phones_template

> [**Phone**](Phone) get_telephony_providers_edges_phones_template(phone_base_settings_id)


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

### Return type

[**Phone**](Phone)


## get_telephony_providers_edges_physicalinterfaces

> [**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing) get_telephony_providers_edges_physicalinterfaces(edge_ids)


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

### Return type

[**PhysicalInterfaceEntityListing**](PhysicalInterfaceEntityListing)


## get_telephony_providers_edges_site

> [**Site**](Site) get_telephony_providers_edges_site(site_id)


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

### Return type

[**Site**](Site)


## get_telephony_providers_edges_site_numberplan

> [**NumberPlan**](NumberPlan) get_telephony_providers_edges_site_numberplan(site_id, number_plan_id)


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

### Return type

[**NumberPlan**](NumberPlan)


## get_telephony_providers_edges_site_numberplans

> [**list[NumberPlan]**](NumberPlan) get_telephony_providers_edges_site_numberplans(site_id)


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

### Return type

[**list[NumberPlan]**](NumberPlan)


## get_telephony_providers_edges_site_numberplans_classifications

> list[str]** get_telephony_providers_edges_site_numberplans_classifications(site_id, classification=classification)


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

### Return type

**list[str]**


## get_telephony_providers_edges_site_outboundroute

> [**OutboundRouteBase**](OutboundRouteBase) get_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id)


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

### Return type

[**OutboundRouteBase**](OutboundRouteBase)


## get_telephony_providers_edges_site_outboundroutes

> [**OutboundRouteBaseEntityListing**](OutboundRouteBaseEntityListing) get_telephony_providers_edges_site_outboundroutes(site_id, page_size=page_size, page_number=page_number, name=name, external_trunk_bases_ids=external_trunk_bases_ids, sort_by=sort_by)


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

### Return type

[**OutboundRouteBaseEntityListing**](OutboundRouteBaseEntityListing)


## get_telephony_providers_edges_site_siteconnections

> [**SiteConnections**](SiteConnections) get_telephony_providers_edges_site_siteconnections(site_id)


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

### Return type

[**SiteConnections**](SiteConnections)


## get_telephony_providers_edges_sites

> [**SiteEntityListing**](SiteEntityListing) get_telephony_providers_edges_sites(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, location_id=location_id, managed=managed, expand=expand)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: edges, location, primarySites, secondarySites |

### Return type

[**SiteEntityListing**](SiteEntityListing)


## get_telephony_providers_edges_timezones

> [**TimeZoneEntityListing**](TimeZoneEntityListing) get_telephony_providers_edges_timezones(page_size=page_size, page_number=page_number)


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

### Return type

[**TimeZoneEntityListing**](TimeZoneEntityListing)


## get_telephony_providers_edges_trunk

> [**Trunk**](Trunk) get_telephony_providers_edges_trunk(trunk_id)


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

### Return type

[**Trunk**](Trunk)


## get_telephony_providers_edges_trunk_metrics

> [**TrunkMetrics**](TrunkMetrics) get_telephony_providers_edges_trunk_metrics(trunk_id)


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

### Return type

[**TrunkMetrics**](TrunkMetrics)


## get_telephony_providers_edges_trunkbasesetting

> [**TrunkBase**](TrunkBase) get_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id, ignore_hidden=ignore_hidden)


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

### Return type

[**TrunkBase**](TrunkBase)


## get_telephony_providers_edges_trunkbasesettings

> [**TrunkBaseEntityListing**](TrunkBaseEntityListing) get_telephony_providers_edges_trunkbasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, recording_enabled=recording_enabled, ignore_hidden=ignore_hidden, managed=managed, expand=expand, name=name)


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
| **expand** | [**list[str]**](str)| Fields to expand in the response, comma-separated | [optional] <br />**Values**: properties |
| **name** | **str**| Name of the TrunkBase to filter by | [optional]  |

### Return type

[**TrunkBaseEntityListing**](TrunkBaseEntityListing)


## get_telephony_providers_edges_trunkbasesettings_availablemetabases

> [**TrunkMetabaseEntityListing**](TrunkMetabaseEntityListing) get_telephony_providers_edges_trunkbasesettings_availablemetabases(type=type, page_size=page_size, page_number=page_number)


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

### Return type

[**TrunkMetabaseEntityListing**](TrunkMetabaseEntityListing)


## get_telephony_providers_edges_trunkbasesettings_template

> [**TrunkBase**](TrunkBase) get_telephony_providers_edges_trunkbasesettings_template(trunk_metabase_id)


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

### Return type

[**TrunkBase**](TrunkBase)


## get_telephony_providers_edges_trunks

> [**TrunkEntityListing**](TrunkEntityListing) get_telephony_providers_edges_trunks(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, edge_id=edge_id, trunk_base_id=trunk_base_id, trunk_type=trunk_type)


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

### Return type

[**TrunkEntityListing**](TrunkEntityListing)


## get_telephony_providers_edges_trunks_metrics

> [**list[TrunkMetrics]**](TrunkMetrics) get_telephony_providers_edges_trunks_metrics(trunk_ids)


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

### Return type

[**list[TrunkMetrics]**](TrunkMetrics)


## get_telephony_providers_edges_trunkswithrecording

> [**TrunkRecordingEnabledCount**](TrunkRecordingEnabledCount) get_telephony_providers_edges_trunkswithrecording(trunk_type=trunk_type)


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

### Return type

[**TrunkRecordingEnabledCount**](TrunkRecordingEnabledCount)


## patch_telephony_providers_edges_site_siteconnections

> [**SiteConnections**](SiteConnections) patch_telephony_providers_edges_site_siteconnections(site_id, body)


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
| **body** | [**DisableSiteConnectionsRequest**](DisableSiteConnectionsRequest)| Site |  |

### Return type

[**SiteConnections**](SiteConnections)


## post_telephony_providers_edge_diagnostic_nslookup

> [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic) post_telephony_providers_edge_diagnostic_nslookup(edge_id, body)


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
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest)| request payload to get network diagnostic |  |

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic)


## post_telephony_providers_edge_diagnostic_ping

> [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic) post_telephony_providers_edge_diagnostic_ping(edge_id, body)


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
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest)| request payload to get network diagnostic |  |

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic)


## post_telephony_providers_edge_diagnostic_route

> [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic) post_telephony_providers_edge_diagnostic_route(edge_id, body)


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
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest)| request payload to get network diagnostic |  |

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic)


## post_telephony_providers_edge_diagnostic_tracepath

> [**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic) post_telephony_providers_edge_diagnostic_tracepath(edge_id, body)


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
| **body** | [**EdgeNetworkDiagnosticRequest**](EdgeNetworkDiagnosticRequest)| request payload to get network diagnostic |  |

### Return type

[**EdgeNetworkDiagnostic**](EdgeNetworkDiagnostic)


## post_telephony_providers_edge_logicalinterfaces

> [**DomainLogicalInterface**](DomainLogicalInterface) post_telephony_providers_edge_logicalinterfaces(edge_id, body)


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
| **body** | [**DomainLogicalInterface**](DomainLogicalInterface)| Logical interface |  |

### Return type

[**DomainLogicalInterface**](DomainLogicalInterface)


## post_telephony_providers_edge_logs_job_upload

>  post_telephony_providers_edge_logs_job_upload(edge_id, job_id, body)


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
| **body** | [**EdgeLogsJobUploadRequest**](EdgeLogsJobUploadRequest)| Log upload request |  |

### Return type

void (empty response body)


## post_telephony_providers_edge_logs_jobs

> [**EdgeLogsJobResponse**](EdgeLogsJobResponse) post_telephony_providers_edge_logs_jobs(edge_id, body)


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
| **body** | [**EdgeLogsJobRequest**](EdgeLogsJobRequest)| EdgeLogsJobRequest |  |

### Return type

[**EdgeLogsJobResponse**](EdgeLogsJobResponse)


## post_telephony_providers_edge_reboot

> str** post_telephony_providers_edge_reboot(edge_id, body=body)


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
| **body** | [**EdgeRebootParameters**](EdgeRebootParameters)| Parameters for the edge reboot | [optional]  |

### Return type

**str**


## post_telephony_providers_edge_softwareupdate

> [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto) post_telephony_providers_edge_softwareupdate(edge_id, body)


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
| **body** | [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto)| Software update request |  |

### Return type

[**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto)


## post_telephony_providers_edge_statuscode

> str** post_telephony_providers_edge_statuscode(edge_id, body=body)


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
| **body** | [**EdgeServiceStateRequest**](EdgeServiceStateRequest)| Edge Service State | [optional]  |

### Return type

**str**


## post_telephony_providers_edge_unpair

> str** post_telephony_providers_edge_unpair(edge_id)


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

### Return type

**str**


## post_telephony_providers_edges

> [**Edge**](Edge) post_telephony_providers_edges(body)


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
| **body** | [**Edge**](Edge)| Edge |  |

### Return type

[**Edge**](Edge)


## post_telephony_providers_edges_addressvalidation

> [**ValidateAddressResponse**](ValidateAddressResponse) post_telephony_providers_edges_addressvalidation(body)


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
| **body** | [**ValidateAddressRequest**](ValidateAddressRequest)| Address |  |

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse)


## post_telephony_providers_edges_certificateauthorities

> [**DomainCertificateAuthority**](DomainCertificateAuthority) post_telephony_providers_edges_certificateauthorities(body)


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
| **body** | [**DomainCertificateAuthority**](DomainCertificateAuthority)| CertificateAuthority |  |

### Return type

[**DomainCertificateAuthority**](DomainCertificateAuthority)


## post_telephony_providers_edges_didpools

> [**DIDPool**](DIDPool) post_telephony_providers_edges_didpools(body)


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
| **body** | [**DIDPool**](DIDPool)| DID pool |  |

### Return type

[**DIDPool**](DIDPool)


## post_telephony_providers_edges_edgegroups

> [**EdgeGroup**](EdgeGroup) post_telephony_providers_edges_edgegroups(body)


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
| **body** | [**EdgeGroup**](EdgeGroup)| EdgeGroup |  |

### Return type

[**EdgeGroup**](EdgeGroup)


## post_telephony_providers_edges_extensionpools

> [**ExtensionPool**](ExtensionPool) post_telephony_providers_edges_extensionpools(body)


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
| **body** | [**ExtensionPool**](ExtensionPool)| ExtensionPool |  |

### Return type

[**ExtensionPool**](ExtensionPool)


## post_telephony_providers_edges_phone_reboot

>  post_telephony_providers_edges_phone_reboot(phone_id)


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

### Return type

void (empty response body)


## post_telephony_providers_edges_phonebasesettings

> [**PhoneBase**](PhoneBase) post_telephony_providers_edges_phonebasesettings(body)


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
| **body** | [**PhoneBase**](PhoneBase)| Phone base settings |  |

### Return type

[**PhoneBase**](PhoneBase)


## post_telephony_providers_edges_phones

> [**Phone**](Phone) post_telephony_providers_edges_phones(body)


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
| **body** | [**Phone**](Phone)| Phone |  |

### Return type

[**Phone**](Phone)


## post_telephony_providers_edges_phones_reboot

>  post_telephony_providers_edges_phones_reboot(body)


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
| **body** | [**PhonesReboot**](PhonesReboot)| Phones |  |

### Return type

void (empty response body)


## post_telephony_providers_edges_site_outboundroutes

> [**OutboundRouteBase**](OutboundRouteBase) post_telephony_providers_edges_site_outboundroutes(site_id, body)


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
| **body** | [**OutboundRouteBase**](OutboundRouteBase)| OutboundRoute |  |

### Return type

[**OutboundRouteBase**](OutboundRouteBase)


## post_telephony_providers_edges_sites

> [**Site**](Site) post_telephony_providers_edges_sites(body)


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
| **body** | [**Site**](Site)| Site |  |

### Return type

[**Site**](Site)


## post_telephony_providers_edges_trunkbasesettings

> [**TrunkBase**](TrunkBase) post_telephony_providers_edges_trunkbasesettings(body)


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
| **body** | [**TrunkBase**](TrunkBase)| Trunk base settings |  |

### Return type

[**TrunkBase**](TrunkBase)


## put_telephony_providers_edge

> [**Edge**](Edge) put_telephony_providers_edge(edge_id, body)


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
| **body** | [**Edge**](Edge)| Edge |  |

### Return type

[**Edge**](Edge)


## put_telephony_providers_edge_logicalinterface

> [**DomainLogicalInterface**](DomainLogicalInterface) put_telephony_providers_edge_logicalinterface(edge_id, interface_id, body)


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
| **body** | [**DomainLogicalInterface**](DomainLogicalInterface)| Logical interface |  |

### Return type

[**DomainLogicalInterface**](DomainLogicalInterface)


## put_telephony_providers_edges_alertablepresences

>  put_telephony_providers_edges_alertablepresences(body)


Creates or updates alertable presences overrides.

Wraps PUT /api/v2/telephony/providers/edges/alertablepresences 

Requires ANY permissions: 

* telephony:alertablePresences:edit

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
body = PureCloudPlatformClientV2.AlertablePresences() # AlertablePresences | Alertable Presences Overrides

try:
    # Creates or updates alertable presences overrides.
    api_instance.put_telephony_providers_edges_alertablepresences(body)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->put_telephony_providers_edges_alertablepresences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AlertablePresences**](AlertablePresences)| Alertable Presences Overrides |  |

### Return type

void (empty response body)


## put_telephony_providers_edges_certificateauthority

> [**DomainCertificateAuthority**](DomainCertificateAuthority) put_telephony_providers_edges_certificateauthority(certificate_id, body)


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
| **body** | [**DomainCertificateAuthority**](DomainCertificateAuthority)| Certificate authority |  |

### Return type

[**DomainCertificateAuthority**](DomainCertificateAuthority)


## put_telephony_providers_edges_didpool

> [**DIDPool**](DIDPool) put_telephony_providers_edges_didpool(did_pool_id, body)


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
| **body** | [**DIDPool**](DIDPool)| DID pool |  |

### Return type

[**DIDPool**](DIDPool)


## put_telephony_providers_edges_edgegroup

> [**EdgeGroup**](EdgeGroup) put_telephony_providers_edges_edgegroup(edge_group_id, body)


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
| **body** | [**EdgeGroup**](EdgeGroup)| EdgeGroup |  |

### Return type

[**EdgeGroup**](EdgeGroup)


## put_telephony_providers_edges_edgegroup_edgetrunkbase

> [**EdgeTrunkBase**](EdgeTrunkBase) put_telephony_providers_edges_edgegroup_edgetrunkbase(edgegroup_id, edgetrunkbase_id, body)


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
| **body** | [**EdgeTrunkBase**](EdgeTrunkBase)| EdgeTrunkBase |  |

### Return type

[**EdgeTrunkBase**](EdgeTrunkBase)


## put_telephony_providers_edges_extensionpool

> [**ExtensionPool**](ExtensionPool) put_telephony_providers_edges_extensionpool(extension_pool_id, body)


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
| **body** | [**ExtensionPool**](ExtensionPool)| ExtensionPool |  |

### Return type

[**ExtensionPool**](ExtensionPool)


## put_telephony_providers_edges_phone

> [**Phone**](Phone) put_telephony_providers_edges_phone(phone_id, body)


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
| **body** | [**Phone**](Phone)| Phone |  |

### Return type

[**Phone**](Phone)


## put_telephony_providers_edges_phonebasesetting

> [**PhoneBase**](PhoneBase) put_telephony_providers_edges_phonebasesetting(phone_base_id, body)


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
| **body** | [**PhoneBase**](PhoneBase)| Phone base settings |  |

### Return type

[**PhoneBase**](PhoneBase)


## put_telephony_providers_edges_site

> [**Site**](Site) put_telephony_providers_edges_site(site_id, body)


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
| **body** | [**Site**](Site)| Site |  |

### Return type

[**Site**](Site)


## put_telephony_providers_edges_site_numberplans

> [**list[NumberPlan]**](NumberPlan) put_telephony_providers_edges_site_numberplans(site_id, body)


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
| **body** | [**list[NumberPlan]**](NumberPlan)| List of number plans |  |

### Return type

[**list[NumberPlan]**](NumberPlan)


## put_telephony_providers_edges_site_outboundroute

> [**OutboundRouteBase**](OutboundRouteBase) put_telephony_providers_edges_site_outboundroute(site_id, outbound_route_id, body)


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
| **body** | [**OutboundRouteBase**](OutboundRouteBase)| OutboundRoute |  |

### Return type

[**OutboundRouteBase**](OutboundRouteBase)


## put_telephony_providers_edges_site_siteconnections

> [**SiteConnections**](SiteConnections) put_telephony_providers_edges_site_siteconnections(site_id, body)


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
| **body** | [**SiteConnections**](SiteConnections)| Site |  |

### Return type

[**SiteConnections**](SiteConnections)


## put_telephony_providers_edges_trunkbasesetting

> [**TrunkBase**](TrunkBase) put_telephony_providers_edges_trunkbasesetting(trunk_base_settings_id, body)


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
| **body** | [**TrunkBase**](TrunkBase)| Trunk base settings |  |

### Return type

[**TrunkBase**](TrunkBase)


_PureCloudPlatformClientV2 213.0.0_
