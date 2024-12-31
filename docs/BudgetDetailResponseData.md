# BudgetDetailResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**BudgetDetail**](BudgetDetail.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.budget_detail_response_data import BudgetDetailResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailResponseData from a JSON string
budget_detail_response_data_instance = BudgetDetailResponseData.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailResponseData.to_json())

# convert the object into a dict
budget_detail_response_data_dict = budget_detail_response_data_instance.to_dict()
# create an instance of BudgetDetailResponseData from a dict
budget_detail_response_data_from_dict = BudgetDetailResponseData.from_dict(budget_detail_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


