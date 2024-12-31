# DateFormat

The date format setting for the budget.  In some cases the format will not be available and will be specified as null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 

## Example

```python
from ynab.models.date_format import DateFormat

# TODO update the JSON string below
json = "{}"
# create an instance of DateFormat from a JSON string
date_format_instance = DateFormat.from_json(json)
# print the JSON string representation of the object
print(DateFormat.to_json())

# convert the object into a dict
date_format_dict = date_format_instance.to_dict()
# create an instance of DateFormat from a dict
date_format_from_dict = DateFormat.from_dict(date_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


