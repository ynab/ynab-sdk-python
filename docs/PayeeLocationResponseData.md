# PayeeLocationResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_location** | [**PayeeLocation**](PayeeLocation.md) |  | 

## Example

```python
from ynab.models.payee_location_response_data import PayeeLocationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeLocationResponseData from a JSON string
payee_location_response_data_instance = PayeeLocationResponseData.from_json(json)
# print the JSON string representation of the object
print(PayeeLocationResponseData.to_json())

# convert the object into a dict
payee_location_response_data_dict = payee_location_response_data_instance.to_dict()
# create an instance of PayeeLocationResponseData from a dict
payee_location_response_data_from_dict = PayeeLocationResponseData.from_dict(payee_location_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


