# MoneyMovementsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money_movements** | [**List[MoneyMovement]**](MoneyMovement.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.money_movements_response_data import MoneyMovementsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyMovementsResponseData from a JSON string
money_movements_response_data_instance = MoneyMovementsResponseData.from_json(json)
# print the JSON string representation of the object
print(MoneyMovementsResponseData.to_json())

# convert the object into a dict
money_movements_response_data_dict = money_movements_response_data_instance.to_dict()
# create an instance of MoneyMovementsResponseData from a dict
money_movements_response_data_from_dict = MoneyMovementsResponseData.from_dict(money_movements_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


