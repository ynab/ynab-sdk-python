# PlanSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | [**DateFormat**](DateFormat.md) |  | 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | 

## Example

```python
from ynab.models.plan_settings import PlanSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSettings from a JSON string
plan_settings_instance = PlanSettings.from_json(json)
# print the JSON string representation of the object
print(PlanSettings.to_json())

# convert the object into a dict
plan_settings_dict = plan_settings_instance.to_dict()
# create an instance of PlanSettings from a dict
plan_settings_from_dict = PlanSettings.from_dict(plan_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


