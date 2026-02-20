# MoneyMovementGroupsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money_movement_groups** | [**List[MoneyMovementGroup]**](MoneyMovementGroup.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.money_movement_groups_response_data import MoneyMovementGroupsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyMovementGroupsResponseData from a JSON string
money_movement_groups_response_data_instance = MoneyMovementGroupsResponseData.from_json(json)
# print the JSON string representation of the object
print(MoneyMovementGroupsResponseData.to_json())

# convert the object into a dict
money_movement_groups_response_data_dict = money_movement_groups_response_data_instance.to_dict()
# create an instance of MoneyMovementGroupsResponseData from a dict
money_movement_groups_response_data_from_dict = MoneyMovementGroupsResponseData.from_dict(money_movement_groups_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


