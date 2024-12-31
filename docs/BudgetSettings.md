# BudgetSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | [**DateFormat**](DateFormat.md) |  | 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | 

## Example

```python
from ynab.models.budget_settings import BudgetSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSettings from a JSON string
budget_settings_instance = BudgetSettings.from_json(json)
# print the JSON string representation of the object
print(BudgetSettings.to_json())

# convert the object into a dict
budget_settings_dict = budget_settings_instance.to_dict()
# create an instance of BudgetSettings from a dict
budget_settings_from_dict = BudgetSettings.from_dict(budget_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


