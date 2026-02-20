# HybridTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**var_date** | **date** | The transaction date in ISO format (e.g. 2016-12-01) | 
**amount** | **int** | The transaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**cleared** | [**TransactionClearedStatus**](TransactionClearedStatus.md) |  | 
**approved** | **bool** | Whether or not the transaction is approved | 
**flag_color** | [**TransactionFlagColor**](TransactionFlagColor.md) |  | [optional] 
**flag_name** | **str** | The customized name of a transaction flag | [optional] 
**account_id** | **UUID** |  | 
**payee_id** | **UUID** |  | [optional] 
**category_id** | **UUID** |  | [optional] 
**transfer_account_id** | **UUID** | If a transfer transaction, the account to which it transfers | [optional] 
**transfer_transaction_id** | **str** | If a transfer transaction, the id of transaction on the other side of the transfer | [optional] 
**matched_transaction_id** | **str** | If transaction is matched, the id of the matched transaction | [optional] 
**import_id** | **str** | If the transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: &#39;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#39;.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#39;YNAB:-294230:2015-12-30:1&#39;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#39;YNAB:-294230:2015-12-30:2&#39;. | [optional] 
**import_payee_name** | **str** | If the transaction was imported, the payee name that was used when importing and before applying any payee rename rules | [optional] 
**import_payee_name_original** | **str** | If the transaction was imported, the original payee name as it appeared on the statement | [optional] 
**debt_transaction_type** | **str** | If the transaction is a debt/loan account transaction, the type of transaction | [optional] 
**deleted** | **bool** | Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests. | 
**type** | **str** | Whether the hybrid transaction represents a regular transaction or a subtransaction | 
**parent_transaction_id** | **str** | For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null. | [optional] 
**account_name** | **str** |  | 
**payee_name** | **str** |  | [optional] 
**category_name** | **str** | The name of the category.  If a split transaction, this will be &#39;Split&#39;. | [optional] 

## Example

```python
from ynab.models.hybrid_transaction import HybridTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of HybridTransaction from a JSON string
hybrid_transaction_instance = HybridTransaction.from_json(json)
# print the JSON string representation of the object
print(HybridTransaction.to_json())

# convert the object into a dict
hybrid_transaction_dict = hybrid_transaction_instance.to_dict()
# create an instance of HybridTransaction from a dict
hybrid_transaction_from_dict = HybridTransaction.from_dict(hybrid_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


