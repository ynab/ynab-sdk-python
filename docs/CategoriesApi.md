# ynab.CategoriesApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category**](CategoriesApi.md#create_category) | **POST** /budgets/{plan_id}/categories | Create a category
[**create_category_group**](CategoriesApi.md#create_category_group) | **POST** /budgets/{plan_id}/category_groups | Create a category group
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /budgets/{plan_id}/categories | Get all categories
[**get_category_by_id**](CategoriesApi.md#get_category_by_id) | **GET** /budgets/{plan_id}/categories/{category_id} | Get a category
[**get_month_category_by_id**](CategoriesApi.md#get_month_category_by_id) | **GET** /budgets/{plan_id}/months/{month}/categories/{category_id} | Get a category for a specific plan month
[**update_category**](CategoriesApi.md#update_category) | **PATCH** /budgets/{plan_id}/categories/{category_id} | Update a category
[**update_category_group**](CategoriesApi.md#update_category_group) | **PATCH** /budgets/{plan_id}/category_groups/{category_group_id} | Update a category group
[**update_month_category**](CategoriesApi.md#update_month_category) | **PATCH** /budgets/{plan_id}/months/{month}/categories/{category_id} | Update a category for a specific month


# **create_category**
> SaveCategoryResponse create_category(plan_id, data)

Create a category

Creates a new category

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.post_category_wrapper import PostCategoryWrapper
from ynab.models.save_category_response import SaveCategoryResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan (\"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan)
    data = ynab.PostCategoryWrapper() # PostCategoryWrapper | The category to create.

    try:
        # Create a category
        api_response = api_instance.create_category(plan_id, data)
        print("The response of CategoriesApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan (\&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan) | 
 **data** | [**PostCategoryWrapper**](PostCategoryWrapper.md)| The category to create. | 

### Return type

[**SaveCategoryResponse**](SaveCategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The category was successfully created |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_category_group**
> SaveCategoryGroupResponse create_category_group(plan_id, data)

Create a category group

Creates a new category group

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.post_category_group_wrapper import PostCategoryGroupWrapper
from ynab.models.save_category_group_response import SaveCategoryGroupResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan (\"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan)
    data = ynab.PostCategoryGroupWrapper() # PostCategoryGroupWrapper | The category group to create.

    try:
        # Create a category group
        api_response = api_instance.create_category_group(plan_id, data)
        print("The response of CategoriesApi->create_category_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan (\&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan) | 
 **data** | [**PostCategoryGroupWrapper**](PostCategoryGroupWrapper.md)| The category group to create. | 

### Return type

[**SaveCategoryGroupResponse**](SaveCategoryGroupResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The category group was successfully created |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> CategoriesResponse get_categories(plan_id, last_knowledge_of_server=last_knowledge_of_server)

Get all categories

Returns all categories grouped by category group.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC).

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.categories_response import CategoriesResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all categories
        api_response = api_instance.get_categories(plan_id, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of CategoriesApi->get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The categories grouped by category group |  -  |
**404** | No categories were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_by_id**
> CategoryResponse get_category_by_id(plan_id, category_id)

Get a category

Returns a single category.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC).

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.category_response import CategoryResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    category_id = 'category_id_example' # str | The id of the category

    try:
        # Get a category
        api_response = api_instance.get_category_by_id(plan_id, category_id)
        print("The response of CategoriesApi->get_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **category_id** | **str**| The id of the category | 

### Return type

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested category |  -  |
**404** | The category was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_category_by_id**
> CategoryResponse get_month_category_by_id(plan_id, month, category_id)

Get a category for a specific plan month

Returns a single category for a specific plan month.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC).

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.category_response import CategoryResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    month = '2013-10-20' # date | The plan month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
    category_id = 'category_id_example' # str | The id of the category

    try:
        # Get a category for a specific plan month
        api_response = api_instance.get_month_category_by_id(plan_id, month, category_id)
        print("The response of CategoriesApi->get_month_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_month_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **month** | **date**| The plan month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 
 **category_id** | **str**| The id of the category | 

### Return type

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested month category |  -  |
**404** | The month category was not was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> SaveCategoryResponse update_category(plan_id, category_id, data)

Update a category

Update a category

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.patch_category_wrapper import PatchCategoryWrapper
from ynab.models.save_category_response import SaveCategoryResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    category_id = 'category_id_example' # str | The id of the category
    data = ynab.PatchCategoryWrapper() # PatchCategoryWrapper | The category to update

    try:
        # Update a category
        api_response = api_instance.update_category(plan_id, category_id, data)
        print("The response of CategoriesApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **category_id** | **str**| The id of the category | 
 **data** | [**PatchCategoryWrapper**](PatchCategoryWrapper.md)| The category to update | 

### Return type

[**SaveCategoryResponse**](SaveCategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The category was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category_group**
> SaveCategoryGroupResponse update_category_group(plan_id, category_group_id, data)

Update a category group

Update a category group

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.patch_category_group_wrapper import PatchCategoryGroupWrapper
from ynab.models.save_category_group_response import SaveCategoryGroupResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    category_group_id = 'category_group_id_example' # str | The id of the category group
    data = ynab.PatchCategoryGroupWrapper() # PatchCategoryGroupWrapper | The category group to update

    try:
        # Update a category group
        api_response = api_instance.update_category_group(plan_id, category_group_id, data)
        print("The response of CategoriesApi->update_category_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_category_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **category_group_id** | **str**| The id of the category group | 
 **data** | [**PatchCategoryGroupWrapper**](PatchCategoryGroupWrapper.md)| The category group to update | 

### Return type

[**SaveCategoryGroupResponse**](SaveCategoryGroupResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The category group was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_month_category**
> SaveCategoryResponse update_month_category(plan_id, month, category_id, data)

Update a category for a specific month

Update a category for a specific month.  Only `budgeted` (assigned) amount can be updated.

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.patch_month_category_wrapper import PatchMonthCategoryWrapper
from ynab.models.save_category_response import SaveCategoryResponse
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
    api_instance = ynab.CategoriesApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    month = '2013-10-20' # date | The plan month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
    category_id = 'category_id_example' # str | The id of the category
    data = ynab.PatchMonthCategoryWrapper() # PatchMonthCategoryWrapper | The category to update.  Only `budgeted` (assigned) amount can be updated and any other fields specified will be ignored.

    try:
        # Update a category for a specific month
        api_response = api_instance.update_month_category(plan_id, month, category_id, data)
        print("The response of CategoriesApi->update_month_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_month_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **month** | **date**| The plan month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 
 **category_id** | **str**| The id of the category | 
 **data** | [**PatchMonthCategoryWrapper**](PatchMonthCategoryWrapper.md)| The category to update.  Only &#x60;budgeted&#x60; (assigned) amount can be updated and any other fields specified will be ignored. | 

### Return type

[**SaveCategoryResponse**](SaveCategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The month category was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

