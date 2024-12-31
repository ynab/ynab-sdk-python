# PayeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PayeeResponseData**](PayeeResponseData.md) |  | 

## Example

```python
from ynab.models.payee_response import PayeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeResponse from a JSON string
payee_response_instance = PayeeResponse.from_json(json)
# print the JSON string representation of the object
print(PayeeResponse.to_json())

# convert the object into a dict
payee_response_dict = payee_response_instance.to_dict()
# create an instance of PayeeResponse from a dict
payee_response_from_dict = PayeeResponse.from_dict(payee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


