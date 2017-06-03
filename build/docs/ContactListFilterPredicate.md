---
title: ContactListFilterPredicate
---
## ContactListFilterPredicate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **column** | **str** | Contact List column that must match a contact list column in the ContactListFilter&#39;s contactList object | [optional] |
| **column_type** | **str** | Whether the contact column contains numeric or alphabetic data | [optional] |
| **operator** | **str** |  | [optional] |
| **value** | **str** | Contact List value to operate on. This could be text, a number, or a relative time. A value for relative time should follow the format PxxDTyyHzzM, where xx, yy, and zz specify the days, hours and minutes. For example, a value of P01DT08H30M corresponds to 1 day, 8 hours, and 30 minutes from now. To specify a time in the past, include a negative sign before each numeric value. For example, a value of P-01DT-08H-30M corresponds to 1 day, 8 hours, and 30 minutes in the past. You can also do things like P01DT00H-30M, which would correspond to 23 hours and 30 minutes from now (1 day - 30 minutes). | [optional] |
| **range** | [**ContactListFilterRange**](ContactListFilterRange.html) | Range is only required for ContactListFilterComparisonOperator&#39;s BETWEEN and IN | [optional] |
| **inverted** | **bool** | Inverts the result of the predicate (i.e., if the predicate returns true, inverting it will return false). | [optional] |
{: class="table table-striped"}


