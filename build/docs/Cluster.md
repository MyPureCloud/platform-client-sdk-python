# Cluster

## Cluster

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The unique ID of this cluster within its associated scan | [optional] |
| **division** | [StarrableDivision](StarrableDivision) | The division all contacts in this cluster are associated to | [optional] |
| **cluster_scan** | [ClusterScan](ClusterScan) | The scan that this cluster belongs to | [optional] |
| **merge_info** | [MergeInfo](MergeInfo) | Information related to merge operations taken on this cluster | [optional] |
| **graph** | [Graph](Graph) | The graph of contacts and identifiers that make up this cluster | [optional] |
| **date_created** | datetime | The date this cluster was discovered. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 266.0.0_
