# HybridTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[HybridTransaction]**](HybridTransaction.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | [optional] 

## Example

```python
from ynab.models.hybrid_transactions_response_data import HybridTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of HybridTransactionsResponseData from a JSON string
hybrid_transactions_response_data_instance = HybridTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(HybridTransactionsResponseData.to_json())

# convert the object into a dict
hybrid_transactions_response_data_dict = hybrid_transactions_response_data_instance.to_dict()
# create an instance of HybridTransactionsResponseData from a dict
hybrid_transactions_response_data_from_dict = HybridTransactionsResponseData.from_dict(hybrid_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


