# ScheduledTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_transactions** | [**List[ScheduledTransactionDetail]**](ScheduledTransactionDetail.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.scheduled_transactions_response_data import ScheduledTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionsResponseData from a JSON string
scheduled_transactions_response_data_instance = ScheduledTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionsResponseData.to_json())

# convert the object into a dict
scheduled_transactions_response_data_dict = scheduled_transactions_response_data_instance.to_dict()
# create an instance of ScheduledTransactionsResponseData from a dict
scheduled_transactions_response_data_from_dict = ScheduledTransactionsResponseData.from_dict(scheduled_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


