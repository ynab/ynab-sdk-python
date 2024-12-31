# SaveTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SaveTransactionsResponseData**](SaveTransactionsResponseData.md) |  | 

## Example

```python
from ynab.models.save_transactions_response import SaveTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTransactionsResponse from a JSON string
save_transactions_response_instance = SaveTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(SaveTransactionsResponse.to_json())

# convert the object into a dict
save_transactions_response_dict = save_transactions_response_instance.to_dict()
# create an instance of SaveTransactionsResponse from a dict
save_transactions_response_from_dict = SaveTransactionsResponse.from_dict(save_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


