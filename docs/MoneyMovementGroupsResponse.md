# MoneyMovementGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MoneyMovementGroupsResponseData**](MoneyMovementGroupsResponseData.md) |  | 

## Example

```python
from ynab.models.money_movement_groups_response import MoneyMovementGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyMovementGroupsResponse from a JSON string
money_movement_groups_response_instance = MoneyMovementGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(MoneyMovementGroupsResponse.to_json())

# convert the object into a dict
money_movement_groups_response_dict = money_movement_groups_response_instance.to_dict()
# create an instance of MoneyMovementGroupsResponse from a dict
money_movement_groups_response_from_dict = MoneyMovementGroupsResponse.from_dict(money_movement_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


