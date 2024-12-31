# AccountResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | 

## Example

```python
from ynab.models.account_response_data import AccountResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponseData from a JSON string
account_response_data_instance = AccountResponseData.from_json(json)
# print the JSON string representation of the object
print(AccountResponseData.to_json())

# convert the object into a dict
account_response_data_dict = account_response_data_instance.to_dict()
# create an instance of AccountResponseData from a dict
account_response_data_from_dict = AccountResponseData.from_dict(account_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


