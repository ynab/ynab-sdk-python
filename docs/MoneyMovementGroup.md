# MoneyMovementGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**group_created_at** | **datetime** | When the money movement group was created | 
**month** | **date** | The month of the money movement group in ISO format (e.g. 2024-01-01) | 
**note** | **str** |  | [optional] 
**performed_by_user_id** | **UUID** | The id of the user who performed the money movement group | [optional] 

## Example

```python
from ynab.models.money_movement_group import MoneyMovementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyMovementGroup from a JSON string
money_movement_group_instance = MoneyMovementGroup.from_json(json)
# print the JSON string representation of the object
print(MoneyMovementGroup.to_json())

# convert the object into a dict
money_movement_group_dict = money_movement_group_instance.to_dict()
# create an instance of MoneyMovementGroup from a dict
money_movement_group_from_dict = MoneyMovementGroup.from_dict(money_movement_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


