# SavePayeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SavePayeeResponseData**](SavePayeeResponseData.md) |  | 

## Example

```python
from ynab.models.save_payee_response import SavePayeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SavePayeeResponse from a JSON string
save_payee_response_instance = SavePayeeResponse.from_json(json)
# print the JSON string representation of the object
print(SavePayeeResponse.to_json())

# convert the object into a dict
save_payee_response_dict = save_payee_response_instance.to_dict()
# create an instance of SavePayeeResponse from a dict
save_payee_response_from_dict = SavePayeeResponse.from_dict(save_payee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


