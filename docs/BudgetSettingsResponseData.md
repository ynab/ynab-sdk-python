# BudgetSettingsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**BudgetSettings**](BudgetSettings.md) |  | 

## Example

```python
from ynab.models.budget_settings_response_data import BudgetSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSettingsResponseData from a JSON string
budget_settings_response_data_instance = BudgetSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(BudgetSettingsResponseData.to_json())

# convert the object into a dict
budget_settings_response_data_dict = budget_settings_response_data_instance.to_dict()
# create an instance of BudgetSettingsResponseData from a dict
budget_settings_response_data_from_dict = BudgetSettingsResponseData.from_dict(budget_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


