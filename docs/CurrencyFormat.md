# CurrencyFormat

The currency format setting for the budget.  In some cases the format will not be available and will be specified as null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_code** | **str** |  | 
**example_format** | **str** |  | 
**decimal_digits** | **int** |  | 
**decimal_separator** | **str** |  | 
**symbol_first** | **bool** |  | 
**group_separator** | **str** |  | 
**currency_symbol** | **str** |  | 
**display_symbol** | **bool** |  | 

## Example

```python
from ynab.models.currency_format import CurrencyFormat

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyFormat from a JSON string
currency_format_instance = CurrencyFormat.from_json(json)
# print the JSON string representation of the object
print(CurrencyFormat.to_json())

# convert the object into a dict
currency_format_dict = currency_format_instance.to_dict()
# create an instance of CurrencyFormat from a dict
currency_format_from_dict = CurrencyFormat.from_dict(currency_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


