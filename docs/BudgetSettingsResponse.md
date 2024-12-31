# BudgetSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BudgetSettingsResponseData**](BudgetSettingsResponseData.md) |  | 

## Example

```python
from ynab.models.budget_settings_response import BudgetSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSettingsResponse from a JSON string
budget_settings_response_instance = BudgetSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetSettingsResponse.to_json())

# convert the object into a dict
budget_settings_response_dict = budget_settings_response_instance.to_dict()
# create an instance of BudgetSettingsResponse from a dict
budget_settings_response_from_dict = BudgetSettingsResponse.from_dict(budget_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


