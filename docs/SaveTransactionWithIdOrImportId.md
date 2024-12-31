# SaveTransactionWithIdOrImportId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**var_date** | **date** | The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored. | [optional] 
**amount** | **int** | The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored. | [optional] 
**payee_id** | **str** | The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as &#x60;transfer_payee_id&#x60; on the account resource. | [optional] 
**payee_name** | **str** | The payee name.  If a &#x60;payee_name&#x60; value is provided and &#x60;payee_id&#x60; has a null value, the &#x60;payee_name&#x60; value will be used to resolve the payee by either (1) a matching payee rename rule (only if &#x60;import_id&#x60; is also specified) or (2) a payee with the same name or (3) creation of a new payee. | [optional] 
**category_id** | **str** | The category for the transaction.  To configure a split transaction, you can specify null for &#x60;category_id&#x60; and provide a &#x60;subtransactions&#x60; array as part of the transaction object.  If an existing transaction is a split, the &#x60;category_id&#x60; cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied. | [optional] 
**memo** | **str** |  | [optional] 
**cleared** | [**TransactionClearedStatus**](TransactionClearedStatus.md) |  | [optional] 
**approved** | **bool** | Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default. | [optional] 
**flag_color** | [**TransactionFlagColor**](TransactionFlagColor.md) |  | [optional] 
**subtransactions** | [**List[SaveSubTransaction]**](SaveSubTransaction.md) | An array of subtransactions to configure a transaction as a split. Updating &#x60;subtransactions&#x60; on an existing split transaction is not supported. | [optional] 
**id** | **str** | If specified, this id will be used to lookup a transaction by its &#x60;id&#x60; for the purpose of updating the transaction itself. If not specified, an &#x60;import_id&#x60; should be supplied. | [optional] 
**import_id** | **str** | If specified, this id will be used to lookup a transaction by its &#x60;import_id&#x60; for the purpose of updating the transaction itself. If not specified, an &#x60;id&#x60; should be supplied.  You may not provide both an &#x60;id&#x60; and an &#x60;import_id&#x60; and updating an &#x60;import_id&#x60; on an existing transaction is not allowed. | [optional] 

## Example

```python
from ynab.models.save_transaction_with_id_or_import_id import SaveTransactionWithIdOrImportId

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTransactionWithIdOrImportId from a JSON string
save_transaction_with_id_or_import_id_instance = SaveTransactionWithIdOrImportId.from_json(json)
# print the JSON string representation of the object
print(SaveTransactionWithIdOrImportId.to_json())

# convert the object into a dict
save_transaction_with_id_or_import_id_dict = save_transaction_with_id_or_import_id_instance.to_dict()
# create an instance of SaveTransactionWithIdOrImportId from a dict
save_transaction_with_id_or_import_id_from_dict = SaveTransactionWithIdOrImportId.from_dict(save_transaction_with_id_or_import_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


