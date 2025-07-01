# TransactionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**TransactionDetail**](TransactionDetail.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.transaction_response_data import TransactionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseData from a JSON string
transaction_response_data_instance = TransactionResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionResponseData.to_json())

# convert the object into a dict
transaction_response_data_dict = transaction_response_data_instance.to_dict()
# create an instance of TransactionResponseData from a dict
transaction_response_data_from_dict = TransactionResponseData.from_dict(transaction_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


