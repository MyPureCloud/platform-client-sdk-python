# EvaluationAsyncAggregationQuery

## EvaluationAsyncAggregationQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **granularity** | str | Granularity aggregates metrics into subpartitions within the time interval specified. The default granularity is the same duration as the interval. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **time_zone** | str | Time zone context used to calculate response intervals (this allows resolving DST changes). The interval offset is used even when timeZone is specified. Default is UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London | [optional] |
| **group_by** | list[str] | Behaves like a SQL GROUPBY. Allows for multiple levels of grouping as a list of dimensions. Partitions resulting aggregate computations into distinct named subgroups rather than across the entire result set as if it were one group. | [optional] |
| **filter** | [EvaluationAggregateQueryFilter](EvaluationAggregateQueryFilter) | Behaves like a SQL WHERE clause. This is ANDed with the interval parameter. Expresses boolean logical predicates as well as dimensional filters | [optional] |
| **metrics** | list[str] | Behaves like a SQL SELECT clause. Only named metrics will be retrieved. | |
| **flatten_multivalued_dimensions** | bool | Flattens any multivalued dimensions used in response groups (e.g. [&#39;a&#39;,&#39;b&#39;,&#39;c&#39;]-&gt;&#39;a,b,c&#39;) | [optional] |
| **views** | [list[EvaluationAggregationView]](EvaluationAggregationView) | Custom derived metric views | [optional] |
| **alternate_time_dimension** | str | Dimension to use as the alternative timestamp for data in the aggregate.  Choosing \&quot;eventTime\&quot; uses the actual time of the data event. | [optional] |
| **page_size** | int | The number of results per page | [optional] |



_PureCloudPlatformClientV2 227.1.0_
