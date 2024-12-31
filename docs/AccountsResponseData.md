# AccountsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[Account]**](Account.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.accounts_response_data import AccountsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsResponseData from a JSON string
accounts_response_data_instance = AccountsResponseData.from_json(json)
# print the JSON string representation of the object
print(AccountsResponseData.to_json())

# convert the object into a dict
accounts_response_data_dict = accounts_response_data_instance.to_dict()
# create an instance of AccountsResponseData from a dict
accounts_response_data_from_dict = AccountsResponseData.from_dict(accounts_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


