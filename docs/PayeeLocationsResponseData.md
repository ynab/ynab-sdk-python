# PayeeLocationsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_locations** | [**List[PayeeLocation]**](PayeeLocation.md) |  | 

## Example

```python
from ynab.models.payee_locations_response_data import PayeeLocationsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeLocationsResponseData from a JSON string
payee_locations_response_data_instance = PayeeLocationsResponseData.from_json(json)
# print the JSON string representation of the object
print(PayeeLocationsResponseData.to_json())

# convert the object into a dict
payee_locations_response_data_dict = payee_locations_response_data_instance.to_dict()
# create an instance of PayeeLocationsResponseData from a dict
payee_locations_response_data_from_dict = PayeeLocationsResponseData.from_dict(payee_locations_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


