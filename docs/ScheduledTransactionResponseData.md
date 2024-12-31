# ScheduledTransactionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_transaction** | [**ScheduledTransactionDetail**](ScheduledTransactionDetail.md) |  | 

## Example

```python
from ynab.models.scheduled_transaction_response_data import ScheduledTransactionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionResponseData from a JSON string
scheduled_transaction_response_data_instance = ScheduledTransactionResponseData.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionResponseData.to_json())

# convert the object into a dict
scheduled_transaction_response_data_dict = scheduled_transaction_response_data_instance.to_dict()
# create an instance of ScheduledTransactionResponseData from a dict
scheduled_transaction_response_data_from_dict = ScheduledTransactionResponseData.from_dict(scheduled_transaction_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


