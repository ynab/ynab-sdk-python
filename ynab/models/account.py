# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.74.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ynab.models.account_type import AccountType
from typing import Optional, Set
from typing_extensions import Self

class Account(BaseModel):
    """
    Account
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    type: AccountType
    on_budget: StrictBool = Field(description="Whether this account is on budget or not")
    closed: StrictBool = Field(description="Whether this account is closed or not")
    note: Optional[StrictStr] = None
    balance: StrictInt = Field(description="The current balance of the account in milliunits format")
    cleared_balance: StrictInt = Field(description="The current cleared balance of the account in milliunits format")
    uncleared_balance: StrictInt = Field(description="The current uncleared balance of the account in milliunits format")
    transfer_payee_id: Optional[StrictStr] = Field(description="The payee id which should be used when transferring to this account")
    direct_import_linked: Optional[StrictBool] = Field(default=None, description="Whether or not the account is linked to a financial institution for automatic transaction import.")
    direct_import_in_error: Optional[StrictBool] = Field(default=None, description="If an account linked to a financial institution (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.")
    last_reconciled_at: Optional[datetime] = Field(default=None, description="A date/time specifying when the account was last reconciled.")
    debt_original_balance: Optional[StrictInt] = Field(default=None, description="The original debt/loan account balance, specified in milliunits format.")
    debt_interest_rates: Optional[Dict[str, StrictInt]] = None
    debt_minimum_payments: Optional[Dict[str, StrictInt]] = None
    debt_escrow_amounts: Optional[Dict[str, StrictInt]] = None
    deleted: StrictBool = Field(description="Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests.")
    __properties: ClassVar[List[str]] = ["id", "name", "type", "on_budget", "closed", "note", "balance", "cleared_balance", "uncleared_balance", "transfer_payee_id", "direct_import_linked", "direct_import_in_error", "last_reconciled_at", "debt_original_balance", "debt_interest_rates", "debt_minimum_payments", "debt_escrow_amounts", "deleted"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if transfer_payee_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_payee_id is None and "transfer_payee_id" in self.model_fields_set:
            _dict['transfer_payee_id'] = None

        # set to None if last_reconciled_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_reconciled_at is None and "last_reconciled_at" in self.model_fields_set:
            _dict['last_reconciled_at'] = None

        # set to None if debt_original_balance (nullable) is None
        # and model_fields_set contains the field
        if self.debt_original_balance is None and "debt_original_balance" in self.model_fields_set:
            _dict['debt_original_balance'] = None

        # set to None if debt_interest_rates (nullable) is None
        # and model_fields_set contains the field
        if self.debt_interest_rates is None and "debt_interest_rates" in self.model_fields_set:
            _dict['debt_interest_rates'] = None

        # set to None if debt_minimum_payments (nullable) is None
        # and model_fields_set contains the field
        if self.debt_minimum_payments is None and "debt_minimum_payments" in self.model_fields_set:
            _dict['debt_minimum_payments'] = None

        # set to None if debt_escrow_amounts (nullable) is None
        # and model_fields_set contains the field
        if self.debt_escrow_amounts is None and "debt_escrow_amounts" in self.model_fields_set:
            _dict['debt_escrow_amounts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "on_budget": obj.get("on_budget"),
            "closed": obj.get("closed"),
            "note": obj.get("note"),
            "balance": obj.get("balance"),
            "cleared_balance": obj.get("cleared_balance"),
            "uncleared_balance": obj.get("uncleared_balance"),
            "transfer_payee_id": obj.get("transfer_payee_id"),
            "direct_import_linked": obj.get("direct_import_linked"),
            "direct_import_in_error": obj.get("direct_import_in_error"),
            "last_reconciled_at": obj.get("last_reconciled_at"),
            "debt_original_balance": obj.get("debt_original_balance"),
            "debt_interest_rates": obj.get("debt_interest_rates"),
            "debt_minimum_payments": obj.get("debt_minimum_payments"),
            "debt_escrow_amounts": obj.get("debt_escrow_amounts"),
            "deleted": obj.get("deleted")
        })
        return _obj


