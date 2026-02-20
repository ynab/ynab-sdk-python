# MoneyMovementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MoneyMovementsResponseData**](MoneyMovementsResponseData.md) |  | 

## Example

```python
from ynab.models.money_movements_response import MoneyMovementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyMovementsResponse from a JSON string
money_movements_response_instance = MoneyMovementsResponse.from_json(json)
# print the JSON string representation of the object
print(MoneyMovementsResponse.to_json())

# convert the object into a dict
money_movements_response_dict = money_movements_response_instance.to_dict()
# create an instance of MoneyMovementsResponse from a dict
money_movements_response_from_dict = MoneyMovementsResponse.from_dict(money_movements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


