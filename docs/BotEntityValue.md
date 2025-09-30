# BotEntityValue

## BotEntityValue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the entity. | |
| **type** | str | The data type of the entity. Valid types include: String, Integer, Decimal, Boolean, Duration, Datetime, Currency, StringCollection, IntegerCollection, DecimalCollection, BooleanCollection, DurationCollection, DatetimeCollection, CurrencyCollection. | |
| **value** | str | The string value of the entity for simple types. Required when using non-collection types. Format depends on the &#39;type&#39; field: String: \&quot;any text\&quot;; Integer: whole number (e.g., \&quot;42\&quot;); Decimal: number with optional decimal point (e.g., \&quot;42.5\&quot;); Boolean: \&quot;true\&quot; or \&quot;false\&quot;; Duration: ISO-8601 duration format (e.g., \&quot;PT1H30M\&quot; for 1 hour and 30 minutes); Datetime: ISO-8601 datetime format (e.g., \&quot;2023-04-15T14:30:00Z\&quot;); Currency: JSON object with &#39;amount&#39; and &#39;code&#39; fields as an escaped JSON string (e.g., \&quot;{\\\&quot;amount\\\&quot;:10.50,\\\&quot;code\\\&quot;:\\\&quot;USD\\\&quot;}\&quot; - note the escaped quotes). | [optional] |
| **values** | list[str] | The collection values for collection types. Required when using collection types. Each value must follow the format of its base type: StringCollection: array of strings; IntegerCollection: array of integer strings (e.g., [\&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot;]); DecimalCollection: array of decimal strings (e.g., [\&quot;1.5\&quot;, \&quot;2.0\&quot;, \&quot;3.75\&quot;]); BooleanCollection: array of boolean strings (e.g., [\&quot;true\&quot;, \&quot;false\&quot;]); DurationCollection: array of ISO-8601 duration strings; DatetimeCollection: array of ISO-8601 datetime strings; CurrencyCollection: array of escaped JSON currency object strings (e.g., [\&quot;{\\\&quot;amount\\\&quot;:10.50,\\\&quot;code\\\&quot;:\\\&quot;USD\\\&quot;}\&quot;, \&quot;{\\\&quot;amount\\\&quot;:25.00,\\\&quot;code\\\&quot;:\\\&quot;EUR\\\&quot;}\&quot;] - note the escaped quotes). | [optional] |



_PureCloudPlatformClientV2 239.0.0_
