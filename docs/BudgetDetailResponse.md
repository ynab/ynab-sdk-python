# BudgetDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BudgetDetailResponseData**](BudgetDetailResponseData.md) |  | 

## Example

```python
from ynab.models.budget_detail_response import BudgetDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailResponse from a JSON string
budget_detail_response_instance = BudgetDetailResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailResponse.to_json())

# convert the object into a dict
budget_detail_response_dict = budget_detail_response_instance.to_dict()
# create an instance of BudgetDetailResponse from a dict
budget_detail_response_from_dict = BudgetDetailResponse.from_dict(budget_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


