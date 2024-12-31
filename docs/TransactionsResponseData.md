# TransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionDetail]**](TransactionDetail.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.transactions_response_data import TransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsResponseData from a JSON string
transactions_response_data_instance = TransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionsResponseData.to_json())

# convert the object into a dict
transactions_response_data_dict = transactions_response_data_instance.to_dict()
# create an instance of TransactionsResponseData from a dict
transactions_response_data_from_dict = TransactionsResponseData.from_dict(transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


