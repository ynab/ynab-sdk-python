# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SubTransaction(BaseModel):
    """
    SubTransaction
    """ # noqa: E501
    id: StrictStr
    transaction_id: StrictStr
    amount: StrictInt = Field(description="The subtransaction amount in milliunits format")
    memo: Optional[StrictStr] = None
    payee_id: Optional[StrictStr] = None
    payee_name: Optional[StrictStr] = None
    category_id: Optional[StrictStr] = None
    category_name: Optional[StrictStr] = None
    transfer_account_id: Optional[StrictStr] = Field(default=None, description="If a transfer, the account_id which the subtransaction transfers to")
    transfer_transaction_id: Optional[StrictStr] = Field(default=None, description="If a transfer, the id of transaction on the other side of the transfer")
    deleted: StrictBool = Field(description="Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests.")
    __properties: ClassVar[List[str]] = ["id", "transaction_id", "amount", "memo", "payee_id", "payee_name", "category_id", "category_name", "transfer_account_id", "transfer_transaction_id", "deleted"]

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
        """Create an instance of SubTransaction from a JSON string"""
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

        # set to None if payee_id (nullable) is None
        # and model_fields_set contains the field
        if self.payee_id is None and "payee_id" in self.model_fields_set:
            _dict['payee_id'] = None

        # set to None if payee_name (nullable) is None
        # and model_fields_set contains the field
        if self.payee_name is None and "payee_name" in self.model_fields_set:
            _dict['payee_name'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if category_name (nullable) is None
        # and model_fields_set contains the field
        if self.category_name is None and "category_name" in self.model_fields_set:
            _dict['category_name'] = None

        # set to None if transfer_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_account_id is None and "transfer_account_id" in self.model_fields_set:
            _dict['transfer_account_id'] = None

        # set to None if transfer_transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_transaction_id is None and "transfer_transaction_id" in self.model_fields_set:
            _dict['transfer_transaction_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "transaction_id": obj.get("transaction_id"),
            "amount": obj.get("amount"),
            "memo": obj.get("memo"),
            "payee_id": obj.get("payee_id"),
            "payee_name": obj.get("payee_name"),
            "category_id": obj.get("category_id"),
            "category_name": obj.get("category_name"),
            "transfer_account_id": obj.get("transfer_account_id"),
            "transfer_transaction_id": obj.get("transfer_transaction_id"),
            "deleted": obj.get("deleted")
        })
        return _obj


