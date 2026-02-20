# MoneyMovement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**month** | **date** | The month of the money movement in ISO format (e.g. 2024-01-01) | [optional] 
**moved_at** | **datetime** | The date/time the money movement was processed on the server in ISO format (e.g. 2024-01-01T12:00:00Z) | [optional] 
**note** | **str** |  | [optional] 
**money_movement_group_id** | **UUID** | The id of the money movement group this movement belongs to | [optional] 
**performed_by_user_id** | **UUID** | The id of the user who performed the money movement | [optional] 
**from_category_id** | **UUID** | The id of the category the money was moved from | [optional] 
**to_category_id** | **UUID** | The id of the category the money was moved to | [optional] 
**amount** | **int** | The amount of the money movement in milliunits format | 

## Example

```python
from ynab.models.money_movement import MoneyMovement

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyMovement from a JSON string
money_movement_instance = MoneyMovement.from_json(json)
# print the JSON string representation of the object
print(MoneyMovement.to_json())

# convert the object into a dict
money_movement_dict = money_movement_instance.to_dict()
# create an instance of MoneyMovement from a dict
money_movement_from_dict = MoneyMovement.from_dict(money_movement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


