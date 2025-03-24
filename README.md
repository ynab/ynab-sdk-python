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
    budgets_api = ynab.BudgetsApi(api_client)
    budgets_response = budgets_api.get_budgets()
    budgets = budgets_response.data.budgets
    
    for budget in budgets:
        print(budget.name) 
```

## Methods

Class | Method | Description
------------ | ------------- | -------------
**UserApi** | [**get_user**](docs/UserApi.md#get_user) | User info
**AccountsApi** | [**create_account**](docs/AccountsApi.md#create_account) | Create a new account
&nbsp; | [**get_account_by_id**](docs/AccountsApi.md#get_account_by_id) | Single account
&nbsp; | [**get_accounts**](docs/AccountsApi.md#get_accounts) | Account list
**BudgetsApi** | [**get_budget_by_id**](docs/BudgetsApi.md#get_budget_by_id) | Single budget
&nbsp; | [**get_budget_settings_by_id**](docs/BudgetsApi.md#get_budget_settings_by_id) | Budget Settings
&nbsp; | [**get_budgets**](docs/BudgetsApi.md#get_budgets) | List budgets
**CategoriesApi** | [**get_categories**](docs/CategoriesApi.md#get_categories) | List categories
&nbsp; | [**get_category_by_id**](docs/CategoriesApi.md#get_category_by_id) | Single category
&nbsp; | [**get_month_category_by_id**](docs/CategoriesApi.md#get_month_category_by_id) | Single category for a specific budget month
&nbsp; | [**update_category**](docs/CategoriesApi.md#update_category) | Update a category
&nbsp; | [**update_month_category**](docs/CategoriesApi.md#update_month_category) | Update a category for a specific month
**MonthsApi** | [**get_budget_month**](docs/MonthsApi.md#get_budget_month) | Single budget month
&nbsp; | [**get_budget_months**](docs/MonthsApi.md#get_budget_months) | List budget months
**PayeeLocationsApi** | [**get_payee_location_by_id**](docs/PayeeLocationsApi.md#get_payee_location_by_id) | Single payee location
&nbsp; | [**get_payee_locations**](docs/PayeeLocationsApi.md#get_payee_locations) | List payee locations
&nbsp; | [**get_payee_locations_by_payee**](docs/PayeeLocationsApi.md#get_payee_locations_by_payee) | List locations for a payee
**PayeesApi** | [**get_payee_by_id**](docs/PayeesApi.md#get_payee_by_id) | Single payee
&nbsp; | [**get_payees**](docs/PayeesApi.md#get_payees) | List payees
&nbsp; | [**update_payee**](docs/PayeesApi.md#update_payee) | Update a payee
**ScheduledTransactionsApi** | [**create_scheduled_transaction**](docs/ScheduledTransactionsApi.md#create_scheduled_transaction) | Create a single scheduled transaction
&nbsp; | [**get_scheduled_transaction_by_id**](docs/ScheduledTransactionsApi.md#get_scheduled_transaction_by_id) | Single scheduled transaction
&nbsp; | [**get_scheduled_transactions**](docs/ScheduledTransactionsApi.md#get_scheduled_transactions) | List scheduled transactions
&nbsp; | [**update_scheduled_transaction**](docs/ScheduledTransactionsApi.md#update_scheduled_transaction) | Update an existing scheduled transactions
&nbsp; | [**delete_scheduled_transaction**](docs/ScheduledTransactionsApi.md#delete_scheduled_transaction) | Delete an existing scheduled transaction
**TransactionsApi** | [**create_transaction**](docs/TransactionsApi.md#create_transaction) | Create a single transaction or multiple transactions
&nbsp; | [**delete_transaction**](docs/TransactionsApi.md#delete_transaction) | Deletes an existing transaction
&nbsp; | [**get_transaction_by_id**](docs/TransactionsApi.md#get_transaction_by_id) | Single transaction
&nbsp; | [**get_transactions**](docs/TransactionsApi.md#get_transactions) | List transactions
&nbsp; | [**get_transactions_by_account**](docs/TransactionsApi.md#get_transactions_by_account) | List account transactions
&nbsp; | [**get_transactions_by_category**](docs/TransactionsApi.md#get_transactions_by_category) | List category transactions, excluding any pending transactions
&nbsp; | [**get_transactions_by_month**](docs/TransactionsApi.md#get_transactions_by_month) | List transactions in month, excluding any pending transactions
&nbsp; | [**get_transactions_by_payee**](docs/TransactionsApi.md#get_transactions_by_payee) | List payee transactions, excluding any pending transactions
&nbsp; | [**import_transactions**](docs/TransactionsApi.md#import_transactions) | Import transactions
&nbsp; | [**update_transaction**](docs/TransactionsApi.md#update_transaction) | Updates an existing transaction
&nbsp; | [**update_transactions**](docs/TransactionsApi.md#update_transactions) | Update multiple transactions

## Versioning

The version of this client is defined in the `pyproject.toml` file and follows [semantic versioning](https://semver.org/).  The version of this client is maintained independently and does not align with the the version of YNAB API itself (which is defined in the [OpenAPI spec](https://api.ynab.com/papi/open_api_spec.yaml)).  To determine which spec version of the YNAB API was used when generating this client you can refer to the "description" field in the `pyproject.toml` file.

## License

Copyright (c) 2025 You Need A Budget, LLC

Licensed under the Apache-2.0 license
