from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    transactions: list[dict[str, object]] = []
    transaction: dict[str, object] = {
        "date": "2026-01-05",
        "type": "\uc9c0\ucd9c",
        "category": "\uc2dd\ube44",
        "description": "\uc810\uc2ec\uc2dd\uc0ac",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 1


def test_add_transaction_stores_negative_expense_amount() -> None:
    transactions: list[dict[str, object]] = []
    transaction: dict[str, object] = {
        "date": "2026-01-10",
        "type": "\uc9c0\ucd9c",
        "category": "\uad50\ud1b5",
        "description": "\uc9c0\ud558\ucca0",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["amount"] == -1500


def test_add_transaction_stores_positive_income_amount() -> None:
    transactions: list[dict[str, object]] = []
    transaction: dict[str, object] = {
        "date": "2026-01-07",
        "type": "\uc218\uc785",
        "category": "\uae09\uc5ec",
        "description": "\uc6d4\uae09",
        "amount": 3500000,
        "memo": "1\uc6d4\uae09\uc5ec",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["amount"] == 3500000


def test_add_transaction_accepts_empty_description() -> None:
    transactions: list[dict[str, object]] = []
    transaction: dict[str, object] = {
        "date": "2026-01-28",
        "type": "\uae30\ud0c0\uc218\uc785",
        "category": "\uae30\ud0c0\uc218\uc785",
        "description": "",
        "amount": 25000,
        "memo": "\uc911\uace0\ub9c8\ucf13",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["description"] == ""
