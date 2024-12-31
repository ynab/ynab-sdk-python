# PayeesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payees** | [**List[Payee]**](Payee.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.payees_response_data import PayeesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PayeesResponseData from a JSON string
payees_response_data_instance = PayeesResponseData.from_json(json)
# print the JSON string representation of the object
print(PayeesResponseData.to_json())

# convert the object into a dict
payees_response_data_dict = payees_response_data_instance.to_dict()
# create an instance of PayeesResponseData from a dict
payees_response_data_from_dict = PayeesResponseData.from_dict(payees_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


