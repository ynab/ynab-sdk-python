# PayeeResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee** | [**Payee**](Payee.md) |  | 

## Example

```python
from ynab.models.payee_response_data import PayeeResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeResponseData from a JSON string
payee_response_data_instance = PayeeResponseData.from_json(json)
# print the JSON string representation of the object
print(PayeeResponseData.to_json())

# convert the object into a dict
payee_response_data_dict = payee_response_data_instance.to_dict()
# create an instance of PayeeResponseData from a dict
payee_response_data_from_dict = PayeeResponseData.from_dict(payee_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


