# SaveTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** | The transaction ids that were saved | 
**transaction** | [**TransactionDetail**](TransactionDetail.md) |  | [optional] 
**transactions** | [**List[TransactionDetail]**](TransactionDetail.md) | If multiple transactions were specified, the transactions that were saved | [optional] 
**duplicate_import_ids** | **List[str]** | If multiple transactions were specified, a list of import_ids that were not created because of an existing &#x60;import_id&#x60; found on the same account | [optional] 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.save_transactions_response_data import SaveTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTransactionsResponseData from a JSON string
save_transactions_response_data_instance = SaveTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(SaveTransactionsResponseData.to_json())

# convert the object into a dict
save_transactions_response_data_dict = save_transactions_response_data_instance.to_dict()
# create an instance of SaveTransactionsResponseData from a dict
save_transactions_response_data_from_dict = SaveTransactionsResponseData.from_dict(save_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


