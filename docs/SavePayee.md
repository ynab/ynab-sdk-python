# SavePayee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the payee. The name must be a maximum of 500 characters. | [optional] 

## Example

```python
from ynab.models.save_payee import SavePayee

# TODO update the JSON string below
json = "{}"
# create an instance of SavePayee from a JSON string
save_payee_instance = SavePayee.from_json(json)
# print the JSON string representation of the object
print(SavePayee.to_json())

# convert the object into a dict
save_payee_dict = save_payee_instance.to_dict()
# create an instance of SavePayee from a dict
save_payee_from_dict = SavePayee.from_dict(save_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


