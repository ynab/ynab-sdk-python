# ynab.MonthsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plan_month**](MonthsApi.md#get_plan_month) | **GET** /budgets/{plan_id}/months/{month} | Get a plan month
[**get_plan_months**](MonthsApi.md#get_plan_months) | **GET** /budgets/{plan_id}/months | Get all plan months


# **get_plan_month**
> MonthDetailResponse get_plan_month(plan_id, month)

Get a plan month

Returns a single plan month

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.month_detail_response import MonthDetailResponse
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
    api_instance = ynab.MonthsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    month = '2013-10-20' # date | The plan month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

    try:
        # Get a plan month
        api_response = api_instance.get_plan_month(plan_id, month)
        print("The response of MonthsApi->get_plan_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonthsApi->get_plan_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **month** | **date**| The plan month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 

### Return type

[**MonthDetailResponse**](MonthDetailResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The plan month detail |  -  |
**404** | The plan month was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_months**
> MonthSummariesResponse get_plan_months(plan_id, last_knowledge_of_server=last_knowledge_of_server)

Get all plan months

Returns all plan months

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.month_summaries_response import MonthSummariesResponse
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
    api_instance = ynab.MonthsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all plan months
        api_response = api_instance.get_plan_months(plan_id, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of MonthsApi->get_plan_months:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonthsApi->get_plan_months: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**MonthSummariesResponse**](MonthSummariesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of plan months |  -  |
**404** | No plan months were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

