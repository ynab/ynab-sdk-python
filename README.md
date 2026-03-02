# YNAB API Python Library

[![Build](https://github.com/ynab/ynab-sdk-python/actions/workflows/build-test.yml/badge.svg)](https://github.com/ynab/ynab-sdk-python/actions/workflows/build-test.yml) [![PyPI version](https://badge.fury.io/py/ynab.svg?icon=si%3Apython)](https://badge.fury.io/py/ynab)

This is the Python client for the YNAB API.

Please read the [YNAB API documentation](https://api.ynab.com) for an
overview of using the API and a complete list of available resources.

This client is generated using the [OpenAPI Generator](https://openapi-generator.tech/).

## Requirements

Python 3.8+

## Installation

First, install the package using pip:

```sh
pip install ynab
```

Then import the package:
```python
import ynab
```

## Usage

To use this client, you must
[obtain an access token](https://api.ynab.com/#authentication) from
the [Account Settings](https://app.ynab.com/settings) area of the YNAB web
application.

```python
import ynab

configuration = ynab.Configuration(
    access_token = "b43439eaafe2_this_is_fake_b43439eaafe2"
)

with ynab.ApiClient(configuration) as api_client:
    plans_api = ynab.PlansApi(api_client)
    plans_response = plans_api.get_plans()
    plans = plans_response.data.budgets
    
    for plan in plans:
        print(plan.name) 
```

## Methods

Class | Method | Description
------------ | ------------- | -------------
**UserApi** | [**get_user**](docs/UserApi.md#get_user) | Get user
**AccountsApi** | [**create_account**](docs/AccountsApi.md#create_account) | Create an account
&nbsp; | [**get_account_by_id**](docs/AccountsApi.md#get_account_by_id) | Get an account
&nbsp; | [**get_accounts**](docs/AccountsApi.md#get_accounts) | Get all accounts
**PlansApi** | [**get_plan_by_id**](docs/PlansApi.md#get_plan_by_id) | Get a plan
&nbsp; | [**get_plan_settings_by_id**](docs/PlansApi.md#get_plan_settings_by_id) | Get plan settings
&nbsp; | [**get_plans**](docs/PlansApi.md#get_plans) | Get all plans
**CategoriesApi** | [**create_category**](docs/CategoriesApi.md#create_category) | Create a category
&nbsp; | [**create_category_group**](docs/CategoriesApi.md#create_category_group) | Create a category group
&nbsp; | [**get_categories**](docs/CategoriesApi.md#get_categories) | Get all categories
&nbsp; | [**get_category_by_id**](docs/CategoriesApi.md#get_category_by_id) | Get a category
&nbsp; | [**get_month_category_by_id**](docs/CategoriesApi.md#get_month_category_by_id) | Get a category for a specific plan month
&nbsp; | [**update_category**](docs/CategoriesApi.md#update_category) | Update a category
&nbsp; | [**update_category_group**](docs/CategoriesApi.md#update_category_group) | Update a category group
&nbsp; | [**update_month_category**](docs/CategoriesApi.md#update_month_category) | Update a category for a specific month
**MonthsApi** | [**get_plan_month**](docs/MonthsApi.md#get_plan_month) | Get a plan month
&nbsp; | [**get_plan_months**](docs/MonthsApi.md#get_plan_months) | Get all plan months
**PayeeLocationsApi** | [**get_payee_location_by_id**](docs/PayeeLocationsApi.md#get_payee_location_by_id) | Get a payee location
&nbsp; | [**get_payee_locations**](docs/PayeeLocationsApi.md#get_payee_locations) | Get all payee locations
&nbsp; | [**get_payee_locations_by_payee**](docs/PayeeLocationsApi.md#get_payee_locations_by_payee) | Get all locations for a payee
**PayeesApi** | [**get_payee_by_id**](docs/PayeesApi.md#get_payee_by_id) | Get a payee
&nbsp; | [**get_payees**](docs/PayeesApi.md#get_payees) | Get all payees
&nbsp; | [**update_payee**](docs/PayeesApi.md#update_payee) | Update a payee
**MoneyMovementsApi** | [**get_money_movement_groups**](docs/MoneyMovementsApi.md#get_money_movement_groups) | Get all money movement groups
&nbsp; | [**get_money_movement_groups_by_month**](docs/MoneyMovementsApi.md#get_money_movement_groups_by_month) | Get money movement groups for a plan month
&nbsp; | [**get_money_movements**](docs/MoneyMovementsApi.md#get_money_movements) | Get all money movements
&nbsp; | [**get_money_movements_by_month**](docs/MoneyMovementsApi.md#get_money_movements_by_month) | Get money movements for a plan month
**TransactionsApi** | [**create_transaction**](docs/TransactionsApi.md#create_transaction) | Create a single transaction or multiple transactions
&nbsp; | [**delete_transaction**](docs/TransactionsApi.md#delete_transaction) | Delete a transaction
&nbsp; | [**get_transaction_by_id**](docs/TransactionsApi.md#get_transaction_by_id) | Get a transaction
&nbsp; | [**get_transactions**](docs/TransactionsApi.md#get_transactions) | Get all transactions
&nbsp; | [**get_transactions_by_account**](docs/TransactionsApi.md#get_transactions_by_account) | Get all account transactions
&nbsp; | [**get_transactions_by_category**](docs/TransactionsApi.md#get_transactions_by_category) | Get all category transactions
&nbsp; | [**get_transactions_by_month**](docs/TransactionsApi.md#get_transactions_by_month) | Get all plan month transactions
&nbsp; | [**get_transactions_by_payee**](docs/TransactionsApi.md#get_transactions_by_payee) | Get all payee transactions
&nbsp; | [**import_transactions**](docs/TransactionsApi.md#import_transactions) | Import transactions
&nbsp; | [**update_transaction**](docs/TransactionsApi.md#update_transaction) | Update a transaction
&nbsp; | [**update_transactions**](docs/TransactionsApi.md#update_transactions) | Update multiple transactions
**ScheduledTransactionsApi** | [**create_scheduled_transaction**](docs/ScheduledTransactionsApi.md#create_scheduled_transaction) | Create a scheduled transaction
&nbsp; | [**delete_scheduled_transaction**](docs/ScheduledTransactionsApi.md#delete_scheduled_transaction) | Delete a scheduled transaction
&nbsp; | [**get_scheduled_transaction_by_id**](docs/ScheduledTransactionsApi.md#get_scheduled_transaction_by_id) | Get a scheduled transaction
&nbsp; | [**get_scheduled_transactions**](docs/ScheduledTransactionsApi.md#get_scheduled_transactions) | Get all scheduled transactions
&nbsp; | [**update_scheduled_transaction**](docs/ScheduledTransactionsApi.md#update_scheduled_transaction) | Update a scheduled transaction

## Versioning

The version of this client is defined in the `pyproject.toml` file and follows [semantic versioning](https://semver.org/).  The version of this client is maintained independently and does not align with the the version of YNAB API itself (which is defined in the [OpenAPI spec](https://api.ynab.com/papi/open_api_spec.yaml)).  To determine which spec version of the YNAB API was used when generating this client you can refer to the "description" field in the `pyproject.toml` file.

## License

Copyright (c) 2025 YNAB

Licensed under the Apache-2.0 license
