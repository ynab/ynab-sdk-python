# HybridTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HybridTransactionsResponseData**](HybridTransactionsResponseData.md) |  | 

## Example

```python
from ynab.models.hybrid_transactions_response import HybridTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HybridTransactionsResponse from a JSON string
hybrid_transactions_response_instance = HybridTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(HybridTransactionsResponse.to_json())

# convert the object into a dict
hybrid_transactions_response_dict = hybrid_transactions_response_instance.to_dict()
# create an instance of HybridTransactionsResponse from a dict
hybrid_transactions_response_from_dict = HybridTransactionsResponse.from_dict(hybrid_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


