# PayeeLocationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PayeeLocationsResponseData**](PayeeLocationsResponseData.md) |  | 

## Example

```python
from ynab.models.payee_locations_response import PayeeLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeLocationsResponse from a JSON string
payee_locations_response_instance = PayeeLocationsResponse.from_json(json)
# print the JSON string representation of the object
print(PayeeLocationsResponse.to_json())

# convert the object into a dict
payee_locations_response_dict = payee_locations_response_instance.to_dict()
# create an instance of PayeeLocationsResponse from a dict
payee_locations_response_from_dict = PayeeLocationsResponse.from_dict(payee_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


