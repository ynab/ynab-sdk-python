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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Category(BaseModel):
    """
    Category
    """ # noqa: E501
    id: StrictStr
    category_group_id: StrictStr
    category_group_name: Optional[StrictStr] = None
    name: StrictStr
    hidden: StrictBool = Field(description="Whether or not the category is hidden")
    original_category_group_id: Optional[StrictStr] = Field(default=None, description="DEPRECATED: No longer used.  Value will always be null.")
    note: Optional[StrictStr] = None
    budgeted: StrictInt = Field(description="Budgeted amount in milliunits format")
    activity: StrictInt = Field(description="Activity amount in milliunits format")
    balance: StrictInt = Field(description="Balance in milliunits format")
    goal_type: Optional[StrictStr] = Field(default=None, description="The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')")
    goal_needs_whole_amount: Optional[StrictBool] = Field(default=None, description="Indicates the monthly rollover behavior for \"NEED\"-type goals. When \"true\", the goal will always ask for the target amount in the new month (\"Set Aside\"). When \"false\", previous month category funding is used (\"Refill\"). For other goal types, this field will be null.")
    goal_day: Optional[StrictInt] = Field(default=None, description="A day offset modifier for the goal's due date. When goal_cadence is 2 (Weekly), this value specifies which day of the week the goal is due (0 = Sunday, 6 = Saturday). Otherwise, this value specifies which day of the month the goal is due (1 = 1st, 31 = 31st, null = Last day of Month).")
    goal_cadence: Optional[StrictInt] = Field(default=None, description="The goal cadence. Value in range 0-14. There are two subsets of these values which behave differently. For values 0, 1, 2, and 13, the goal's due date repeats every goal_cadence * goal_cadence_frequency, where 0 = None, 1 = Monthly, 2 = Weekly, and 13 = Yearly. For example, goal_cadence 1 with goal_cadence_frequency 2 means the goal is due every other month. For values 3-12 and 14, goal_cadence_frequency is ignored and the goal's due date repeats every goal_cadence, where 3 = Every 2 Months, 4 = Every 3 Months, ..., 12 = Every 11 Months, and 14 = Every 2 Years.")
    goal_cadence_frequency: Optional[StrictInt] = Field(default=None, description="The goal cadence frequency. When goal_cadence is 0, 1, 2, or 13, a goal's due date repeats every goal_cadence * goal_cadence_frequency. For example, goal_cadence 1 with goal_cadence_frequency 2 means the goal is due every other month.  When goal_cadence is 3-12 or 14, goal_cadence_frequency is ignored.")
    goal_creation_month: Optional[date] = Field(default=None, description="The month a goal was created")
    goal_target: Optional[StrictInt] = Field(default=None, description="The goal target amount in milliunits")
    goal_target_month: Optional[date] = Field(default=None, description="The original target month for the goal to be completed.  Only some goal types specify this date.")
    goal_percentage_complete: Optional[StrictInt] = Field(default=None, description="The percentage completion of the goal")
    goal_months_to_budget: Optional[StrictInt] = Field(default=None, description="The number of months, including the current month, left in the current goal period.")
    goal_under_funded: Optional[StrictInt] = Field(default=None, description="The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period. This amount will generally correspond to the 'Underfunded' amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month.")
    goal_overall_funded: Optional[StrictInt] = Field(default=None, description="The total amount funded towards the goal within the current goal period.")
    goal_overall_left: Optional[StrictInt] = Field(default=None, description="The amount of funding still needed to complete the goal within the current goal period.")
    deleted: StrictBool = Field(description="Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.")
    __properties: ClassVar[List[str]] = ["id", "category_group_id", "category_group_name", "name", "hidden", "original_category_group_id", "note", "budgeted", "activity", "balance", "goal_type", "goal_needs_whole_amount", "goal_day", "goal_cadence", "goal_cadence_frequency", "goal_creation_month", "goal_target", "goal_target_month", "goal_percentage_complete", "goal_months_to_budget", "goal_under_funded", "goal_overall_funded", "goal_overall_left", "deleted"]

    @field_validator('goal_type')
    def goal_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TB', 'TBD', 'MF', 'NEED', 'DEBT']):
            raise ValueError("must be one of enum values ('TB', 'TBD', 'MF', 'NEED', 'DEBT')")
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
        """Create an instance of Category from a JSON string"""
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
        # set to None if original_category_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.original_category_group_id is None and "original_category_group_id" in self.model_fields_set:
            _dict['original_category_group_id'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if goal_type (nullable) is None
        # and model_fields_set contains the field
        if self.goal_type is None and "goal_type" in self.model_fields_set:
            _dict['goal_type'] = None

        # set to None if goal_needs_whole_amount (nullable) is None
        # and model_fields_set contains the field
        if self.goal_needs_whole_amount is None and "goal_needs_whole_amount" in self.model_fields_set:
            _dict['goal_needs_whole_amount'] = None

        # set to None if goal_day (nullable) is None
        # and model_fields_set contains the field
        if self.goal_day is None and "goal_day" in self.model_fields_set:
            _dict['goal_day'] = None

        # set to None if goal_cadence (nullable) is None
        # and model_fields_set contains the field
        if self.goal_cadence is None and "goal_cadence" in self.model_fields_set:
            _dict['goal_cadence'] = None

        # set to None if goal_cadence_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.goal_cadence_frequency is None and "goal_cadence_frequency" in self.model_fields_set:
            _dict['goal_cadence_frequency'] = None

        # set to None if goal_creation_month (nullable) is None
        # and model_fields_set contains the field
        if self.goal_creation_month is None and "goal_creation_month" in self.model_fields_set:
            _dict['goal_creation_month'] = None

        # set to None if goal_target (nullable) is None
        # and model_fields_set contains the field
        if self.goal_target is None and "goal_target" in self.model_fields_set:
            _dict['goal_target'] = None

        # set to None if goal_target_month (nullable) is None
        # and model_fields_set contains the field
        if self.goal_target_month is None and "goal_target_month" in self.model_fields_set:
            _dict['goal_target_month'] = None

        # set to None if goal_percentage_complete (nullable) is None
        # and model_fields_set contains the field
        if self.goal_percentage_complete is None and "goal_percentage_complete" in self.model_fields_set:
            _dict['goal_percentage_complete'] = None

        # set to None if goal_months_to_budget (nullable) is None
        # and model_fields_set contains the field
        if self.goal_months_to_budget is None and "goal_months_to_budget" in self.model_fields_set:
            _dict['goal_months_to_budget'] = None

        # set to None if goal_under_funded (nullable) is None
        # and model_fields_set contains the field
        if self.goal_under_funded is None and "goal_under_funded" in self.model_fields_set:
            _dict['goal_under_funded'] = None

        # set to None if goal_overall_funded (nullable) is None
        # and model_fields_set contains the field
        if self.goal_overall_funded is None and "goal_overall_funded" in self.model_fields_set:
            _dict['goal_overall_funded'] = None

        # set to None if goal_overall_left (nullable) is None
        # and model_fields_set contains the field
        if self.goal_overall_left is None and "goal_overall_left" in self.model_fields_set:
            _dict['goal_overall_left'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Category from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "category_group_id": obj.get("category_group_id"),
            "category_group_name": obj.get("category_group_name"),
            "name": obj.get("name"),
            "hidden": obj.get("hidden"),
            "original_category_group_id": obj.get("original_category_group_id"),
            "note": obj.get("note"),
            "budgeted": obj.get("budgeted"),
            "activity": obj.get("activity"),
            "balance": obj.get("balance"),
            "goal_type": obj.get("goal_type"),
            "goal_needs_whole_amount": obj.get("goal_needs_whole_amount"),
            "goal_day": obj.get("goal_day"),
            "goal_cadence": obj.get("goal_cadence"),
            "goal_cadence_frequency": obj.get("goal_cadence_frequency"),
            "goal_creation_month": obj.get("goal_creation_month"),
            "goal_target": obj.get("goal_target"),
            "goal_target_month": obj.get("goal_target_month"),
            "goal_percentage_complete": obj.get("goal_percentage_complete"),
            "goal_months_to_budget": obj.get("goal_months_to_budget"),
            "goal_under_funded": obj.get("goal_under_funded"),
            "goal_overall_funded": obj.get("goal_overall_funded"),
            "goal_overall_left": obj.get("goal_overall_left"),
            "deleted": obj.get("deleted")
        })
        return _obj


