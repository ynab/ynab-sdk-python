# PayeeLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PayeeLocationResponseData**](PayeeLocationResponseData.md) |  | 

## Example

```python
from ynab.models.payee_location_response import PayeeLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeLocationResponse from a JSON string
payee_location_response_instance = PayeeLocationResponse.from_json(json)
# print the JSON string representation of the object
print(PayeeLocationResponse.to_json())

# convert the object into a dict
payee_location_response_dict = payee_location_response_instance.to_dict()
# create an instance of PayeeLocationResponse from a dict
payee_location_response_from_dict = PayeeLocationResponse.from_dict(payee_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


