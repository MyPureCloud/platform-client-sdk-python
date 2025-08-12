# CoachingApi

## PureCloudPlatformClientV2.CoachingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_coaching_appointment**](#delete_coaching_appointment) | Delete an existing appointment|
|[**delete_coaching_appointment_annotation**](#delete_coaching_appointment_annotation) | Delete an existing annotation|
|[**get_coaching_appointment**](#get_coaching_appointment) | Retrieve an appointment|
|[**get_coaching_appointment_annotation**](#get_coaching_appointment_annotation) | Retrieve an annotation.|
|[**get_coaching_appointment_annotations**](#get_coaching_appointment_annotations) | Get a list of annotations.|
|[**get_coaching_appointment_statuses**](#get_coaching_appointment_statuses) | Get the list of status changes for a coaching appointment.|
|[**get_coaching_appointments**](#get_coaching_appointments) | Get appointments for users and optional date range|
|[**get_coaching_appointments_me**](#get_coaching_appointments_me) | Get my appointments for a given date range|
|[**get_coaching_notification**](#get_coaching_notification) | Get an existing notification|
|[**get_coaching_notifications**](#get_coaching_notifications) | Retrieve the list of your notifications.|
|[**patch_coaching_appointment**](#patch_coaching_appointment) | Update an existing appointment|
|[**patch_coaching_appointment_annotation**](#patch_coaching_appointment_annotation) | Update an existing annotation.|
|[**patch_coaching_appointment_status**](#patch_coaching_appointment_status) | Update the status of a coaching appointment|
|[**patch_coaching_notification**](#patch_coaching_notification) | Update an existing notification.|
|[**post_coaching_appointment_annotations**](#post_coaching_appointment_annotations) | Create a new annotation.|
|[**post_coaching_appointment_conversations**](#post_coaching_appointment_conversations) | Add a conversation to an appointment|
|[**post_coaching_appointments**](#post_coaching_appointments) | Create a new appointment|
|[**post_coaching_appointments_aggregates_query**](#post_coaching_appointments_aggregates_query) | Retrieve aggregated appointment data|
|[**post_coaching_scheduleslots_query**](#post_coaching_scheduleslots_query) | Get list of possible slots where a coaching appointment can be scheduled.|



## delete_coaching_appointment

> [**CoachingAppointmentReference**](CoachingAppointmentReference) delete_coaching_appointment(appointment_id)


Delete an existing appointment

Permission not required if you are the creator of the appointment

Wraps DELETE /api/v2/coaching/appointments/{appointmentId} 

Requires ANY permissions: 

* coaching:appointment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.

try:
    # Delete an existing appointment
    api_response = api_instance.delete_coaching_appointment(appointment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->delete_coaching_appointment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |

### Return type

[**CoachingAppointmentReference**](CoachingAppointmentReference)


## delete_coaching_appointment_annotation

>  delete_coaching_appointment_annotation(appointment_id, annotation_id)


Delete an existing annotation

You must have the appropriate permission for the type of annotation you are updating. Permission not required if you are the creator or facilitator of the appointment

Wraps DELETE /api/v2/coaching/appointments/{appointmentId}/annotations/{annotationId} 

Requires ANY permissions: 

* coaching:annotation:delete
* coaching:privateAnnotation:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
annotation_id = 'annotation_id_example' # str | The ID of the annotation.

try:
    # Delete an existing annotation
    api_instance.delete_coaching_appointment_annotation(appointment_id, annotation_id)
except ApiException as e:
    print("Exception when calling CoachingApi->delete_coaching_appointment_annotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **annotation_id** | **str**| The ID of the annotation. |  |

### Return type

void (empty response body)


## get_coaching_appointment

> [**CoachingAppointmentResponse**](CoachingAppointmentResponse) get_coaching_appointment(appointment_id)


Retrieve an appointment

Permission not required if you are the attendee, creator or facilitator of the appointment

Wraps GET /api/v2/coaching/appointments/{appointmentId} 

Requires ANY permissions: 

* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.

try:
    # Retrieve an appointment
    api_response = api_instance.get_coaching_appointment(appointment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_appointment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |

### Return type

[**CoachingAppointmentResponse**](CoachingAppointmentResponse)


## get_coaching_appointment_annotation

> [**CoachingAnnotation**](CoachingAnnotation) get_coaching_appointment_annotation(appointment_id, annotation_id)


Retrieve an annotation.

You must have the appropriate permission for the type of annotation you are creating. Permission not required if you are related to the appointment (only the creator or facilitator can view private annotations).

Wraps GET /api/v2/coaching/appointments/{appointmentId}/annotations/{annotationId} 

Requires ANY permissions: 

* coaching:annotation:view
* coaching:privateAnnotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
annotation_id = 'annotation_id_example' # str | The ID of the annotation.

try:
    # Retrieve an annotation.
    api_response = api_instance.get_coaching_appointment_annotation(appointment_id, annotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_appointment_annotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **annotation_id** | **str**| The ID of the annotation. |  |

### Return type

[**CoachingAnnotation**](CoachingAnnotation)


## get_coaching_appointment_annotations

> [**CoachingAnnotationList**](CoachingAnnotationList) get_coaching_appointment_annotations(appointment_id, page_number=page_number, page_size=page_size)


Get a list of annotations.

You must have the appropriate permission for the type of annotation you are creating. Permission not required if you are related to the appointment (only the creator or facilitator can view private annotations).

Wraps GET /api/v2/coaching/appointments/{appointmentId}/annotations 

Requires ANY permissions: 

* coaching:annotation:view
* coaching:privateAnnotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of annotations.
    api_response = api_instance.get_coaching_appointment_annotations(appointment_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_appointment_annotations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**CoachingAnnotationList**](CoachingAnnotationList)


## get_coaching_appointment_statuses

> [**CoachingAppointmentStatusResponseList**](CoachingAppointmentStatusResponseList) get_coaching_appointment_statuses(appointment_id, page_number=page_number, page_size=page_size)


Get the list of status changes for a coaching appointment.

Permission not required if you are an attendee, creator or facilitator of the appointment

Wraps GET /api/v2/coaching/appointments/{appointmentId}/statuses 

Requires ANY permissions: 

* coaching:appointmentStatus:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get the list of status changes for a coaching appointment.
    api_response = api_instance.get_coaching_appointment_statuses(appointment_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_appointment_statuses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**CoachingAppointmentStatusResponseList**](CoachingAppointmentStatusResponseList)


## get_coaching_appointments

> [**CoachingAppointmentResponseList**](CoachingAppointmentResponseList) get_coaching_appointments(user_ids, interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order, relationships=relationships, completion_interval=completion_interval, overdue=overdue, interval_condition=interval_condition)


Get appointments for users and optional date range

Wraps GET /api/v2/coaching/appointments 

Requires ANY permissions: 

* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
user_ids = ['user_ids_example'] # list[str] | The user IDs for which to retrieve appointments
interval = 'interval_example' # str | Interval to filter data by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
statuses = ['statuses_example'] # list[str] | Appointment Statuses to filter by (optional)
facilitator_ids = ['facilitator_ids_example'] # list[str] | The facilitator IDs for which to retrieve appointments (optional)
sort_order = 'sort_order_example' # str | Sort (by due date) either Asc or Desc (optional)
relationships = ['relationships_example'] # list[str] | Relationships to filter by (optional)
completion_interval = 'completion_interval_example' # str | Appointment completion start and end to filter by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = 'overdue_example' # str | Overdue status to filter by (optional)
interval_condition = 'interval_condition_example' # str | Filter condition for interval (optional)

try:
    # Get appointments for users and optional date range
    api_response = api_instance.get_coaching_appointments(user_ids, interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order, relationships=relationships, completion_interval=completion_interval, overdue=overdue, interval_condition=interval_condition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_appointments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_ids** | [**list[str]**](str)| The user IDs for which to retrieve appointments |  |
| **interval** | **str**| Interval to filter data by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **statuses** | [**list[str]**](str)| Appointment Statuses to filter by | [optional] <br />**Values**: Scheduled, InProgress, Completed, InvalidSchedule |
| **facilitator_ids** | [**list[str]**](str)| The facilitator IDs for which to retrieve appointments | [optional]  |
| **sort_order** | **str**| Sort (by due date) either Asc or Desc | [optional] <br />**Values**: Desc, Asc |
| **relationships** | [**list[str]**](str)| Relationships to filter by | [optional] <br />**Values**: Creator, Facilitator, Attendee |
| **completion_interval** | **str**| Appointment completion start and end to filter by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Overdue status to filter by | [optional] <br />**Values**: True, False, Any |
| **interval_condition** | **str**| Filter condition for interval | [optional] <br />**Values**: StartsIn, Overlaps |

### Return type

[**CoachingAppointmentResponseList**](CoachingAppointmentResponseList)


## get_coaching_appointments_me

> [**CoachingAppointmentResponseList**](CoachingAppointmentResponseList) get_coaching_appointments_me(interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order, relationships=relationships, completion_interval=completion_interval, overdue=overdue, interval_condition=interval_condition)


Get my appointments for a given date range

Wraps GET /api/v2/coaching/appointments/me 

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
api_instance = PureCloudPlatformClientV2.CoachingApi()
interval = 'interval_example' # str | Interval to filter data by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
statuses = ['statuses_example'] # list[str] | Appointment Statuses to filter by (optional)
facilitator_ids = ['facilitator_ids_example'] # list[str] | The facilitator IDs for which to retrieve appointments (optional)
sort_order = 'sort_order_example' # str | Sort (by due date) either Asc or Desc (optional)
relationships = ['relationships_example'] # list[str] | Relationships to filter by (optional)
completion_interval = 'completion_interval_example' # str | Appointment completion start and end to filter by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = 'overdue_example' # str | Overdue status to filter by (optional)
interval_condition = 'interval_condition_example' # str | Filter condition for interval (optional)

try:
    # Get my appointments for a given date range
    api_response = api_instance.get_coaching_appointments_me(interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order, relationships=relationships, completion_interval=completion_interval, overdue=overdue, interval_condition=interval_condition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_appointments_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **interval** | **str**| Interval to filter data by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **statuses** | [**list[str]**](str)| Appointment Statuses to filter by | [optional] <br />**Values**: Scheduled, InProgress, Completed, InvalidSchedule |
| **facilitator_ids** | [**list[str]**](str)| The facilitator IDs for which to retrieve appointments | [optional]  |
| **sort_order** | **str**| Sort (by due date) either Asc or Desc | [optional] <br />**Values**: Desc, Asc |
| **relationships** | [**list[str]**](str)| Relationships to filter by | [optional] <br />**Values**: Creator, Facilitator, Attendee |
| **completion_interval** | **str**| Appointment completion start and end to filter by. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Overdue status to filter by | [optional] <br />**Values**: True, False, Any |
| **interval_condition** | **str**| Filter condition for interval | [optional] <br />**Values**: StartsIn, Overlaps |

### Return type

[**CoachingAppointmentResponseList**](CoachingAppointmentResponseList)


## get_coaching_notification

> [**CoachingNotification**](CoachingNotification) get_coaching_notification(notification_id, expand=expand)


Get an existing notification

Permission not required if you are the owner of the notification.

Wraps GET /api/v2/coaching/notifications/{notificationId} 

Requires ANY permissions: 

* coaching:notification:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
notification_id = 'notification_id_example' # str | The ID of the notification.
expand = ['expand_example'] # list[str] | Indicates a field in the response which should be expanded. (optional)

try:
    # Get an existing notification
    api_response = api_instance.get_coaching_notification(notification_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_notification: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **notification_id** | **str**| The ID of the notification. |  |
| **expand** | [**list[str]**](str)| Indicates a field in the response which should be expanded. | [optional] <br />**Values**: appointment |

### Return type

[**CoachingNotification**](CoachingNotification)


## get_coaching_notifications

> [**CoachingNotificationList**](CoachingNotificationList) get_coaching_notifications(page_number=page_number, page_size=page_size, expand=expand)


Retrieve the list of your notifications.

Wraps GET /api/v2/coaching/notifications 

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
api_instance = PureCloudPlatformClientV2.CoachingApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
expand = ['expand_example'] # list[str] | Indicates a field in the response which should be expanded. (optional)

try:
    # Retrieve the list of your notifications.
    api_response = api_instance.get_coaching_notifications(page_number=page_number, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->get_coaching_notifications: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **expand** | [**list[str]**](str)| Indicates a field in the response which should be expanded. | [optional] <br />**Values**: appointment |

### Return type

[**CoachingNotificationList**](CoachingNotificationList)


## patch_coaching_appointment

> [**CoachingAppointmentResponse**](CoachingAppointmentResponse) patch_coaching_appointment(appointment_id, body)


Update an existing appointment

Permission not required if you are the creator or facilitator of the appointment

Wraps PATCH /api/v2/coaching/appointments/{appointmentId} 

Requires ANY permissions: 

* coaching:appointment:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.UpdateCoachingAppointmentRequest() # UpdateCoachingAppointmentRequest | The new version of the appointment

try:
    # Update an existing appointment
    api_response = api_instance.patch_coaching_appointment(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->patch_coaching_appointment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**UpdateCoachingAppointmentRequest**](UpdateCoachingAppointmentRequest)| The new version of the appointment |  |

### Return type

[**CoachingAppointmentResponse**](CoachingAppointmentResponse)


## patch_coaching_appointment_annotation

> [**CoachingAnnotation**](CoachingAnnotation) patch_coaching_appointment_annotation(appointment_id, annotation_id, body)


Update an existing annotation.

You must have the appropriate permission for the type of annotation you are updating. Permission not required if you are the creator or facilitator of the appointment

Wraps PATCH /api/v2/coaching/appointments/{appointmentId}/annotations/{annotationId} 

Requires ANY permissions: 

* coaching:annotation:edit
* coaching:privateAnnotation:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
annotation_id = 'annotation_id_example' # str | The ID of the annotation.
body = PureCloudPlatformClientV2.CoachingAnnotation() # CoachingAnnotation | The new version of the annotation

try:
    # Update an existing annotation.
    api_response = api_instance.patch_coaching_appointment_annotation(appointment_id, annotation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->patch_coaching_appointment_annotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **annotation_id** | **str**| The ID of the annotation. |  |
| **body** | [**CoachingAnnotation**](CoachingAnnotation)| The new version of the annotation |  |

### Return type

[**CoachingAnnotation**](CoachingAnnotation)


## patch_coaching_appointment_status

> [**CoachingAppointmentStatusResponse**](CoachingAppointmentStatusResponse) patch_coaching_appointment_status(appointment_id, body)


Update the status of a coaching appointment

Permission not required if you are an attendee, creator or facilitator of the appointment

Wraps PATCH /api/v2/coaching/appointments/{appointmentId}/status 

Requires ANY permissions: 

* coaching:appointmentStatus:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.CoachingAppointmentStatusRequest() # CoachingAppointmentStatusRequest | Updated status of the coaching appointment

try:
    # Update the status of a coaching appointment
    api_response = api_instance.patch_coaching_appointment_status(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->patch_coaching_appointment_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**CoachingAppointmentStatusRequest**](CoachingAppointmentStatusRequest)| Updated status of the coaching appointment |  |

### Return type

[**CoachingAppointmentStatusResponse**](CoachingAppointmentStatusResponse)


## patch_coaching_notification

> [**CoachingNotification**](CoachingNotification) patch_coaching_notification(notification_id, body)


Update an existing notification.

Can only update your own notifications.

Wraps PATCH /api/v2/coaching/notifications/{notificationId} 

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
api_instance = PureCloudPlatformClientV2.CoachingApi()
notification_id = 'notification_id_example' # str | The ID of the notification.
body = PureCloudPlatformClientV2.CoachingNotification() # CoachingNotification | Change the read state of a notification

try:
    # Update an existing notification.
    api_response = api_instance.patch_coaching_notification(notification_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->patch_coaching_notification: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **notification_id** | **str**| The ID of the notification. |  |
| **body** | [**CoachingNotification**](CoachingNotification)| Change the read state of a notification |  |

### Return type

[**CoachingNotification**](CoachingNotification)


## post_coaching_appointment_annotations

> [**CoachingAnnotation**](CoachingAnnotation) post_coaching_appointment_annotations(appointment_id, body)


Create a new annotation.

You must have the appropriate permission for the type of annotation you are creating. Permission not required if you are related to the appointment (only the creator or facilitator can create private annotations).

Wraps POST /api/v2/coaching/appointments/{appointmentId}/annotations 

Requires ANY permissions: 

* coaching:annotation:add
* coaching:privateAnnotation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.CoachingAnnotationCreateRequest() # CoachingAnnotationCreateRequest | The annotation to add

try:
    # Create a new annotation.
    api_response = api_instance.post_coaching_appointment_annotations(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->post_coaching_appointment_annotations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**CoachingAnnotationCreateRequest**](CoachingAnnotationCreateRequest)| The annotation to add |  |

### Return type

[**CoachingAnnotation**](CoachingAnnotation)


## post_coaching_appointment_conversations

> [**AddConversationResponse**](AddConversationResponse) post_coaching_appointment_conversations(appointment_id, body)


Add a conversation to an appointment

Permission not required if you are the creator or facilitator of the appointment

Wraps POST /api/v2/coaching/appointments/{appointmentId}/conversations 

Requires ANY permissions: 

* coaching:appointment:edit
* coaching:appointmentConversation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.AddConversationRequest() # AddConversationRequest | body

try:
    # Add a conversation to an appointment
    api_response = api_instance.post_coaching_appointment_conversations(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->post_coaching_appointment_conversations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**AddConversationRequest**](AddConversationRequest)| body |  |

### Return type

[**AddConversationResponse**](AddConversationResponse)


## post_coaching_appointments

> [**CoachingAppointmentResponse**](CoachingAppointmentResponse) post_coaching_appointments(body)


Create a new appointment

Wraps POST /api/v2/coaching/appointments 

Requires ANY permissions: 

* coaching:appointment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
body = PureCloudPlatformClientV2.CreateCoachingAppointmentRequest() # CreateCoachingAppointmentRequest | The appointment to add

try:
    # Create a new appointment
    api_response = api_instance.post_coaching_appointments(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->post_coaching_appointments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateCoachingAppointmentRequest**](CreateCoachingAppointmentRequest)| The appointment to add |  |

### Return type

[**CoachingAppointmentResponse**](CoachingAppointmentResponse)


## post_coaching_appointments_aggregates_query

> [**CoachingAppointmentAggregateResponse**](CoachingAppointmentAggregateResponse) post_coaching_appointments_aggregates_query(body)


Retrieve aggregated appointment data

Wraps POST /api/v2/coaching/appointments/aggregates/query 

Requires ANY permissions: 

* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
body = PureCloudPlatformClientV2.CoachingAppointmentAggregateRequest() # CoachingAppointmentAggregateRequest | Aggregate Request

try:
    # Retrieve aggregated appointment data
    api_response = api_instance.post_coaching_appointments_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->post_coaching_appointments_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CoachingAppointmentAggregateRequest**](CoachingAppointmentAggregateRequest)| Aggregate Request |  |

### Return type

[**CoachingAppointmentAggregateResponse**](CoachingAppointmentAggregateResponse)


## post_coaching_scheduleslots_query

> [**CoachingSlotsResponse**](CoachingSlotsResponse) post_coaching_scheduleslots_query(body)


Get list of possible slots where a coaching appointment can be scheduled.

Wraps POST /api/v2/coaching/scheduleslots/query 

Requires ANY permissions: 

* coaching:scheduleSlot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
body = PureCloudPlatformClientV2.CoachingSlotsRequest() # CoachingSlotsRequest | The slot search request

try:
    # Get list of possible slots where a coaching appointment can be scheduled.
    api_response = api_instance.post_coaching_scheduleslots_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachingApi->post_coaching_scheduleslots_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CoachingSlotsRequest**](CoachingSlotsRequest)| The slot search request |  |

### Return type

[**CoachingSlotsResponse**](CoachingSlotsResponse)


_PureCloudPlatformClientV2 235.0.0_
