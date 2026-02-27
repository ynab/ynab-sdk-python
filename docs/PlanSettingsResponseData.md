# PlanSettingsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**PlanSettings**](PlanSettings.md) |  | 

## Example

```python
from ynab.models.plan_settings_response_data import PlanSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSettingsResponseData from a JSON string
plan_settings_response_data_instance = PlanSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(PlanSettingsResponseData.to_json())

# convert the object into a dict
plan_settings_response_data_dict = plan_settings_response_data_instance.to_dict()
# create an instance of PlanSettingsResponseData from a dict
plan_settings_response_data_from_dict = PlanSettingsResponseData.from_dict(plan_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


