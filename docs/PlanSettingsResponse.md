# PlanSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlanSettingsResponseData**](PlanSettingsResponseData.md) |  | 

## Example

```python
from ynab.models.plan_settings_response import PlanSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSettingsResponse from a JSON string
plan_settings_response_instance = PlanSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PlanSettingsResponse.to_json())

# convert the object into a dict
plan_settings_response_dict = plan_settings_response_instance.to_dict()
# create an instance of PlanSettingsResponse from a dict
plan_settings_response_from_dict = PlanSettingsResponse.from_dict(plan_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


