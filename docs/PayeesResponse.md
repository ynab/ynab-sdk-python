# PayeesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PayeesResponseData**](PayeesResponseData.md) |  | 

## Example

```python
from ynab.models.payees_response import PayeesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayeesResponse from a JSON string
payees_response_instance = PayeesResponse.from_json(json)
# print the JSON string representation of the object
print(PayeesResponse.to_json())

# convert the object into a dict
payees_response_dict = payees_response_instance.to_dict()
# create an instance of PayeesResponse from a dict
payees_response_from_dict = PayeesResponse.from_dict(payees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


