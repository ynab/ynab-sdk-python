# SubTransactionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**amount** | **int** | The subtransaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**payee_id** | **UUID** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**category_id** | **UUID** |  | [optional] 
**category_name** | **str** |  | [optional] 
**transfer_account_id** | **UUID** | If a transfer, the account_id which the subtransaction transfers to | [optional] 
**transfer_transaction_id** | **str** | If a transfer, the id of transaction on the other side of the transfer | [optional] 
**deleted** | **bool** | Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests. | 

## Example

```python
from ynab.models.sub_transaction_base import SubTransactionBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubTransactionBase from a JSON string
sub_transaction_base_instance = SubTransactionBase.from_json(json)
# print the JSON string representation of the object
print(SubTransactionBase.to_json())

# convert the object into a dict
sub_transaction_base_dict = sub_transaction_base_instance.to_dict()
# create an instance of SubTransactionBase from a dict
sub_transaction_base_from_dict = SubTransactionBase.from_dict(sub_transaction_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


