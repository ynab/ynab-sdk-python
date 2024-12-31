# Payee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**transfer_account_id** | **str** | If a transfer payee, the &#x60;account_id&#x60; to which this payee transfers to | [optional] 
**deleted** | **bool** | Whether or not the payee has been deleted.  Deleted payees will only be included in delta requests. | 

## Example

```python
from ynab.models.payee import Payee

# TODO update the JSON string below
json = "{}"
# create an instance of Payee from a JSON string
payee_instance = Payee.from_json(json)
# print the JSON string representation of the object
print(Payee.to_json())

# convert the object into a dict
payee_dict = payee_instance.to_dict()
# create an instance of Payee from a dict
payee_from_dict = Payee.from_dict(payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


