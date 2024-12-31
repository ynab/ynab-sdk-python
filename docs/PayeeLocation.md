# PayeeLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**payee_id** | **str** |  | 
**latitude** | **str** |  | 
**longitude** | **str** |  | 
**deleted** | **bool** | Whether or not the payee location has been deleted.  Deleted payee locations will only be included in delta requests. | 

## Example

```python
from ynab.models.payee_location import PayeeLocation

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeLocation from a JSON string
payee_location_instance = PayeeLocation.from_json(json)
# print the JSON string representation of the object
print(PayeeLocation.to_json())

# convert the object into a dict
payee_location_dict = payee_location_instance.to_dict()
# create an instance of PayeeLocation from a dict
payee_location_from_dict = PayeeLocation.from_dict(payee_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


