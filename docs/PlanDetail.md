# PlanDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**last_modified_on** | **datetime** | The last time any changes were made to the plan from either a web or mobile client | [optional] 
**first_month** | **date** | The earliest plan month | [optional] 
**last_month** | **date** | The latest plan month | [optional] 
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | [optional] 
**accounts** | [**List[Account]**](Account.md) |  | [optional] 
**payees** | [**List[Payee]**](Payee.md) |  | [optional] 
**payee_locations** | [**List[PayeeLocation]**](PayeeLocation.md) |  | [optional] 
**category_groups** | [**List[CategoryGroup]**](CategoryGroup.md) |  | [optional] 
**categories** | [**List[Category]**](Category.md) |  | [optional] 
**months** | [**List[MonthDetail]**](MonthDetail.md) |  | [optional] 
**transactions** | [**List[TransactionSummary]**](TransactionSummary.md) |  | [optional] 
**subtransactions** | [**List[SubTransaction]**](SubTransaction.md) |  | [optional] 
**scheduled_transactions** | [**List[ScheduledTransactionSummary]**](ScheduledTransactionSummary.md) |  | [optional] 
**scheduled_subtransactions** | [**List[ScheduledSubTransaction]**](ScheduledSubTransaction.md) |  | [optional] 

## Example

```python
from ynab.models.plan_detail import PlanDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PlanDetail from a JSON string
plan_detail_instance = PlanDetail.from_json(json)
# print the JSON string representation of the object
print(PlanDetail.to_json())

# convert the object into a dict
plan_detail_dict = plan_detail_instance.to_dict()
# create an instance of PlanDetail from a dict
plan_detail_from_dict = PlanDetail.from_dict(plan_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


