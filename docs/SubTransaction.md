# SubTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**amount** | **int** | The subtransaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**payee_id** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer, the account_id which the subtransaction transfers to | [optional] 
**transfer_transaction_id** | **str** | If a transfer, the id of transaction on the other side of the transfer | [optional] 
**deleted** | **bool** | Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests. | 

## Example

```python
from ynab.models.sub_transaction import SubTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SubTransaction from a JSON string
sub_transaction_instance = SubTransaction.from_json(json)
# print the JSON string representation of the object
print(SubTransaction.to_json())

# convert the object into a dict
sub_transaction_dict = sub_transaction_instance.to_dict()
# create an instance of SubTransaction from a dict
sub_transaction_from_dict = SubTransaction.from_dict(sub_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


