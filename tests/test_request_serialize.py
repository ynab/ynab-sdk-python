from ynab.models.existing_transaction import ExistingTransaction


def test_from_dict_omits_missing_nullable_fields():
    transaction = ExistingTransaction.from_dict({"amount": -5000})

    assert transaction.to_dict() == {"amount": -5000}


def test_from_dict_keeps_explicit_null():
    transaction = ExistingTransaction.from_dict({"amount": -5000, "memo": None})

    assert transaction.to_dict() == {"amount": -5000, "memo": None}
