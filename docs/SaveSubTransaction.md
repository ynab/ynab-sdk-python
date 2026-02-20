# SaveSubTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The subtransaction amount in milliunits format. | 
**payee_id** | **UUID** | The payee for the subtransaction. | [optional] 
**payee_name** | **str** | The payee name.  If a &#x60;payee_name&#x60; value is provided and &#x60;payee_id&#x60; has a null value, the &#x60;payee_name&#x60; value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee. | [optional] 
**category_id** | **UUID** | The category for the subtransaction.  Credit Card Payment categories are not permitted and will be ignored if supplied. | [optional] 
**memo** | **str** |  | [optional] 

## Example

```python
from ynab.models.save_sub_transaction import SaveSubTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SaveSubTransaction from a JSON string
save_sub_transaction_instance = SaveSubTransaction.from_json(json)
# print the JSON string representation of the object
print(SaveSubTransaction.to_json())

# convert the object into a dict
save_sub_transaction_dict = save_sub_transaction_instance.to_dict()
# create an instance of SaveSubTransaction from a dict
save_sub_transaction_from_dict = SaveSubTransaction.from_dict(save_sub_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


