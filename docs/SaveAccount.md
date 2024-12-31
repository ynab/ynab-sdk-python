# SaveAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account | 
**type** | [**AccountType**](AccountType.md) |  | 
**balance** | **int** | The current balance of the account in milliunits format | 

## Example

```python
from ynab.models.save_account import SaveAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAccount from a JSON string
save_account_instance = SaveAccount.from_json(json)
# print the JSON string representation of the object
print(SaveAccount.to_json())

# convert the object into a dict
save_account_dict = save_account_instance.to_dict()
# create an instance of SaveAccount from a dict
save_account_from_dict = SaveAccount.from_dict(save_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


