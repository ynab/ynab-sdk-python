# ynab.PlansApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plan_by_id**](PlansApi.md#get_plan_by_id) | **GET** /budgets/{plan_id} | Get a plan
[**get_plan_settings_by_id**](PlansApi.md#get_plan_settings_by_id) | **GET** /budgets/{plan_id}/settings | Get plan settings
[**get_plans**](PlansApi.md#get_plans) | **GET** /budgets | Get all plans


# **get_plan_by_id**
> PlanDetailResponse get_plan_by_id(plan_id, last_knowledge_of_server=last_knowledge_of_server)

Get a plan

Returns a single plan with all related entities.  This resource is effectively a full plan export.

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.plan_detail_response import PlanDetailResponse
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
    api_instance = ynab.PlansApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get a plan
        api_response = api_instance.get_plan_by_id(plan_id, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of PlansApi->get_plan_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->get_plan_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**PlanDetailResponse**](PlanDetailResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested plan |  -  |
**404** | The specified plan was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_settings_by_id**
> PlanSettingsResponse get_plan_settings_by_id(plan_id)

Get plan settings

Returns settings for a plan

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.plan_settings_response import PlanSettingsResponse
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
    api_instance = ynab.PlansApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).

    try:
        # Get plan settings
        api_response = api_instance.get_plan_settings_by_id(plan_id)
        print("The response of PlansApi->get_plan_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->get_plan_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 

### Return type

[**PlanSettingsResponse**](PlanSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested plan settings |  -  |
**404** | The specified plan was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plans**
> PlanSummaryResponse get_plans(include_accounts=include_accounts)

Get all plans

Returns plans list with summary information

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.plan_summary_response import PlanSummaryResponse
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
    api_instance = ynab.PlansApi(api_client)
    include_accounts = True # bool | Whether to include the list of plan accounts (optional)

    try:
        # Get all plans
        api_response = api_instance.get_plans(include_accounts=include_accounts)
        print("The response of PlansApi->get_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->get_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_accounts** | **bool**| Whether to include the list of plan accounts | [optional] 

### Return type

[**PlanSummaryResponse**](PlanSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of plans |  -  |
**404** | No plans were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

