# AccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccountsResponseData**](AccountsResponseData.md) |  | 

## Example

```python
from ynab.models.accounts_response import AccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsResponse from a JSON string
accounts_response_instance = AccountsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsResponse.to_json())

# convert the object into a dict
accounts_response_dict = accounts_response_instance.to_dict()
# create an instance of AccountsResponse from a dict
accounts_response_from_dict = AccountsResponse.from_dict(accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


