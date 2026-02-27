# ynab.MoneyMovementsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_money_movement_groups**](MoneyMovementsApi.md#get_money_movement_groups) | **GET** /budgets/{plan_id}/money_movement_groups | Get all money movement groups
[**get_money_movement_groups_by_month**](MoneyMovementsApi.md#get_money_movement_groups_by_month) | **GET** /budgets/{plan_id}/months/{month}/money_movement_groups | Get money movement groups for a plan month
[**get_money_movements**](MoneyMovementsApi.md#get_money_movements) | **GET** /budgets/{plan_id}/money_movements | Get all money movements
[**get_money_movements_by_month**](MoneyMovementsApi.md#get_money_movements_by_month) | **GET** /budgets/{plan_id}/months/{month}/money_movements | Get money movements for a plan month


# **get_money_movement_groups**
> MoneyMovementGroupsResponse get_money_movement_groups(plan_id)

Get all money movement groups

Returns all money movement groups

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.money_movement_groups_response import MoneyMovementGroupsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.MoneyMovementsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).

    try:
        # Get all money movement groups
        api_response = api_instance.get_money_movement_groups(plan_id)
        print("The response of MoneyMovementsApi->get_money_movement_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoneyMovementsApi->get_money_movement_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 

### Return type

[**MoneyMovementGroupsResponse**](MoneyMovementGroupsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested money movement groups |  -  |
**404** | No money movement groups were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_money_movement_groups_by_month**
> MoneyMovementGroupsResponse get_money_movement_groups_by_month(plan_id, month)

Get money movement groups for a plan month

Returns all money movement groups for a specific month

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.money_movement_groups_response import MoneyMovementGroupsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.MoneyMovementsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    month = '2013-10-20' # date | The plan month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

    try:
        # Get money movement groups for a plan month
        api_response = api_instance.get_money_movement_groups_by_month(plan_id, month)
        print("The response of MoneyMovementsApi->get_money_movement_groups_by_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoneyMovementsApi->get_money_movement_groups_by_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **month** | **date**| The plan month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 

### Return type

[**MoneyMovementGroupsResponse**](MoneyMovementGroupsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested money movement groups |  -  |
**404** | No money movement groups were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_money_movements**
> MoneyMovementsResponse get_money_movements(plan_id)

Get all money movements

Returns all money movements

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.money_movements_response import MoneyMovementsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.MoneyMovementsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).

    try:
        # Get all money movements
        api_response = api_instance.get_money_movements(plan_id)
        print("The response of MoneyMovementsApi->get_money_movements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoneyMovementsApi->get_money_movements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 

### Return type

[**MoneyMovementsResponse**](MoneyMovementsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested money movements |  -  |
**404** | No money movements were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_money_movements_by_month**
> MoneyMovementsResponse get_money_movements_by_month(plan_id, month)

Get money movements for a plan month

Returns all money movements for a specific month

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.money_movements_response import MoneyMovementsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.MoneyMovementsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    month = '2013-10-20' # date | The plan month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

    try:
        # Get money movements for a plan month
        api_response = api_instance.get_money_movements_by_month(plan_id, month)
        print("The response of MoneyMovementsApi->get_money_movements_by_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoneyMovementsApi->get_money_movements_by_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **month** | **date**| The plan month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 

### Return type

[**MoneyMovementsResponse**](MoneyMovementsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested money movements |  -  |
**404** | No money movements were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

