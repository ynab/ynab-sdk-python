# ScheduledTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ScheduledTransactionResponseData**](ScheduledTransactionResponseData.md) |  | 

## Example

```python
from ynab.models.scheduled_transaction_response import ScheduledTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionResponse from a JSON string
scheduled_transaction_response_instance = ScheduledTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionResponse.to_json())

# convert the object into a dict
scheduled_transaction_response_dict = scheduled_transaction_response_instance.to_dict()
# create an instance of ScheduledTransactionResponse from a dict
scheduled_transaction_response_from_dict = ScheduledTransactionResponse.from_dict(scheduled_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


