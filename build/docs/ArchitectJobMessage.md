# ArchitectJobMessage

## ArchitectJobMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_time** | datetime | The DateTime when the message was generated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **type** | str | The message type. | [optional] |
| **text** | str | The text of the message. | [optional] |
| **details** | [list[ArchitectJobMessageDetail]](ArchitectJobMessageDetail) | Structured information about the message, absent from the large majority of messages. Populated only by publish jobs, and only on errors raised when a Genesys Cloud entity reference in the flow definition could not be resolved. Export and validate jobs resolve an existing flow by id rather than processing a flow definition, so they never return it. Holds one entry per request captured within the failing lookup, ordered oldest request first, and more than one entry is normal. Entries for requests that succeeded are included alongside the request that failed. A lookup failure usually also produces a separate message with similar text and no details. | [optional] |



_PureCloudPlatformClientV2 264.0.0_
