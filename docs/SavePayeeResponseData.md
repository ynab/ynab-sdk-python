# SavePayeeResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee** | [**Payee**](Payee.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.save_payee_response_data import SavePayeeResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SavePayeeResponseData from a JSON string
save_payee_response_data_instance = SavePayeeResponseData.from_json(json)
# print the JSON string representation of the object
print(SavePayeeResponseData.to_json())

# convert the object into a dict
save_payee_response_data_dict = save_payee_response_data_instance.to_dict()
# create an instance of SavePayeeResponseData from a dict
save_payee_response_data_from_dict = SavePayeeResponseData.from_dict(save_payee_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


