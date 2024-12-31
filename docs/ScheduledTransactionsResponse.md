# ScheduledTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ScheduledTransactionsResponseData**](ScheduledTransactionsResponseData.md) |  | 

## Example

```python
from ynab.models.scheduled_transactions_response import ScheduledTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionsResponse from a JSON string
scheduled_transactions_response_instance = ScheduledTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionsResponse.to_json())

# convert the object into a dict
scheduled_transactions_response_dict = scheduled_transactions_response_instance.to_dict()
# create an instance of ScheduledTransactionsResponse from a dict
scheduled_transactions_response_from_dict = ScheduledTransactionsResponse.from_dict(scheduled_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


