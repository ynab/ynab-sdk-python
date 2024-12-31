# PatchPayeeWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee** | [**SavePayee**](SavePayee.md) |  | 

## Example

```python
from ynab.models.patch_payee_wrapper import PatchPayeeWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPayeeWrapper from a JSON string
patch_payee_wrapper_instance = PatchPayeeWrapper.from_json(json)
# print the JSON string representation of the object
print(PatchPayeeWrapper.to_json())

# convert the object into a dict
patch_payee_wrapper_dict = patch_payee_wrapper_instance.to_dict()
# create an instance of PatchPayeeWrapper from a dict
patch_payee_wrapper_from_dict = PatchPayeeWrapper.from_dict(patch_payee_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


