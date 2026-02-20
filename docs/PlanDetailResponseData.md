# PlanDetailResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**PlanDetail**](PlanDetail.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.plan_detail_response_data import PlanDetailResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PlanDetailResponseData from a JSON string
plan_detail_response_data_instance = PlanDetailResponseData.from_json(json)
# print the JSON string representation of the object
print(PlanDetailResponseData.to_json())

# convert the object into a dict
plan_detail_response_data_dict = plan_detail_response_data_instance.to_dict()
# create an instance of PlanDetailResponseData from a dict
plan_detail_response_data_from_dict = PlanDetailResponseData.from_dict(plan_detail_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


