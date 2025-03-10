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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ynab.models.transaction_cleared_status import TransactionClearedStatus
from ynab.models.transaction_flag_color import TransactionFlagColor
from typing import Optional, Set
from typing_extensions import Self

class HybridTransaction(BaseModel):
    """
    HybridTransaction
    """ # noqa: E501
    id: StrictStr
    var_date: date = Field(description="The transaction date in ISO format (e.g. 2016-12-01)", alias="date")
    amount: StrictInt = Field(description="The transaction amount in milliunits format")
    memo: Optional[StrictStr] = None
    cleared: TransactionClearedStatus
    approved: StrictBool = Field(description="Whether or not the transaction is approved")
    flag_color: Optional[TransactionFlagColor] = None
    flag_name: Optional[StrictStr] = Field(default=None, description="The customized name of a transaction flag")
    account_id: StrictStr
    payee_id: Optional[StrictStr] = None
    category_id: Optional[StrictStr] = None
    transfer_account_id: Optional[StrictStr] = Field(default=None, description="If a transfer transaction, the account to which it transfers")
    transfer_transaction_id: Optional[StrictStr] = Field(default=None, description="If a transfer transaction, the id of transaction on the other side of the transfer")
    matched_transaction_id: Optional[StrictStr] = Field(default=None, description="If transaction is matched, the id of the matched transaction")
    import_id: Optional[StrictStr] = Field(default=None, description="If the transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.")
    import_payee_name: Optional[StrictStr] = Field(default=None, description="If the transaction was imported, the payee name that was used when importing and before applying any payee rename rules")
    import_payee_name_original: Optional[StrictStr] = Field(default=None, description="If the transaction was imported, the original payee name as it appeared on the statement")
    debt_transaction_type: Optional[StrictStr] = Field(default=None, description="If the transaction is a debt/loan account transaction, the type of transaction")
    deleted: StrictBool = Field(description="Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.")
    type: StrictStr = Field(description="Whether the hybrid transaction represents a regular transaction or a subtransaction")
    parent_transaction_id: Optional[StrictStr] = Field(default=None, description="For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.")
    account_name: StrictStr
    payee_name: Optional[StrictStr] = None
    category_name: Optional[StrictStr] = Field(default=None, description="The name of the category.  If a split transaction, this will be 'Split'.")
    __properties: ClassVar[List[str]] = ["id", "date", "amount", "memo", "cleared", "approved", "flag_color", "flag_name", "account_id", "payee_id", "category_id", "transfer_account_id", "transfer_transaction_id", "matched_transaction_id", "import_id", "import_payee_name", "import_payee_name_original", "debt_transaction_type", "deleted", "type", "parent_transaction_id", "account_name", "payee_name", "category_name"]

    @field_validator('debt_transaction_type')
    def debt_transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['payment', 'refund', 'fee', 'interest', 'escrow', 'balanceAdjustment', 'credit', 'charge']):
            raise ValueError("must be one of enum values ('payment', 'refund', 'fee', 'interest', 'escrow', 'balanceAdjustment', 'credit', 'charge')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['transaction', 'subtransaction']):
            raise ValueError("must be one of enum values ('transaction', 'subtransaction')")
        return value

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
        """Create an instance of HybridTransaction from a JSON string"""
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
        # set to None if memo (nullable) is None
        # and model_fields_set contains the field
        if self.memo is None and "memo" in self.model_fields_set:
            _dict['memo'] = None

        # set to None if flag_color (nullable) is None
        # and model_fields_set contains the field
        if self.flag_color is None and "flag_color" in self.model_fields_set:
            _dict['flag_color'] = None

        # set to None if flag_name (nullable) is None
        # and model_fields_set contains the field
        if self.flag_name is None and "flag_name" in self.model_fields_set:
            _dict['flag_name'] = None

        # set to None if payee_id (nullable) is None
        # and model_fields_set contains the field
        if self.payee_id is None and "payee_id" in self.model_fields_set:
            _dict['payee_id'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if transfer_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_account_id is None and "transfer_account_id" in self.model_fields_set:
            _dict['transfer_account_id'] = None

        # set to None if transfer_transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_transaction_id is None and "transfer_transaction_id" in self.model_fields_set:
            _dict['transfer_transaction_id'] = None

        # set to None if matched_transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.matched_transaction_id is None and "matched_transaction_id" in self.model_fields_set:
            _dict['matched_transaction_id'] = None

        # set to None if import_id (nullable) is None
        # and model_fields_set contains the field
        if self.import_id is None and "import_id" in self.model_fields_set:
            _dict['import_id'] = None

        # set to None if import_payee_name (nullable) is None
        # and model_fields_set contains the field
        if self.import_payee_name is None and "import_payee_name" in self.model_fields_set:
            _dict['import_payee_name'] = None

        # set to None if import_payee_name_original (nullable) is None
        # and model_fields_set contains the field
        if self.import_payee_name_original is None and "import_payee_name_original" in self.model_fields_set:
            _dict['import_payee_name_original'] = None

        # set to None if debt_transaction_type (nullable) is None
        # and model_fields_set contains the field
        if self.debt_transaction_type is None and "debt_transaction_type" in self.model_fields_set:
            _dict['debt_transaction_type'] = None

        # set to None if parent_transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_transaction_id is None and "parent_transaction_id" in self.model_fields_set:
            _dict['parent_transaction_id'] = None

        # set to None if payee_name (nullable) is None
        # and model_fields_set contains the field
        if self.payee_name is None and "payee_name" in self.model_fields_set:
            _dict['payee_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HybridTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "date": obj.get("date"),
            "amount": obj.get("amount"),
            "memo": obj.get("memo"),
            "cleared": obj.get("cleared"),
            "approved": obj.get("approved"),
            "flag_color": obj.get("flag_color"),
            "flag_name": obj.get("flag_name"),
            "account_id": obj.get("account_id"),
            "payee_id": obj.get("payee_id"),
            "category_id": obj.get("category_id"),
            "transfer_account_id": obj.get("transfer_account_id"),
            "transfer_transaction_id": obj.get("transfer_transaction_id"),
            "matched_transaction_id": obj.get("matched_transaction_id"),
            "import_id": obj.get("import_id"),
            "import_payee_name": obj.get("import_payee_name"),
            "import_payee_name_original": obj.get("import_payee_name_original"),
            "debt_transaction_type": obj.get("debt_transaction_type"),
            "deleted": obj.get("deleted"),
            "type": obj.get("type"),
            "parent_transaction_id": obj.get("parent_transaction_id"),
            "account_name": obj.get("account_name"),
            "payee_name": obj.get("payee_name"),
            "category_name": obj.get("category_name")
        })
        return _obj


