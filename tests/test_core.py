from pathlib import Path
import csv

from budget.core import add_transaction, filter_by_category, get_balance, load_transactions_from_csv


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


def test_get_balance_returns_zero_for_empty_list() -> None:
    assert get_balance([]) == 0.0


def test_get_balance_matches_step2_transactions() -> None:
    data_path = Path("data/step2_transactions.csv")
    with data_path.open(encoding="utf-8-sig", newline="") as file_handle:
        rows = list(csv.DictReader(file_handle))

    transactions = [
        {
            "date": row["date"],
            "type": row["type"],
            "category": row["category"],
            "description": row["description"],
            "amount": float(row["amount"]),
            "memo": row["memo"],
        }
        for row in rows
    ]

    assert get_balance(transactions) == 24285027.0


def test_filter_by_category_matches_step2_transactions_case_insensitive() -> None:
    data_path = Path("data/step2_transactions.csv")
    with data_path.open(encoding="utf-8-sig", newline="") as file_handle:
        rows = list(csv.DictReader(file_handle))

    transactions = [
        {
            "date": row["date"],
            "type": row["type"],
            "category": row["category"],
            "description": row["description"],
            "amount": float(row["amount"]),
            "memo": row["memo"],
        }
        for row in rows
    ]

    filtered_transactions = filter_by_category(transactions, "여행")
    uppercased_transactions = filter_by_category(transactions, "여행".upper())

    assert len(filtered_transactions) == 6
    assert len(uppercased_transactions) == 6
    assert filtered_transactions == uppercased_transactions


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    transactions: list[dict[str, object]] = []

    result = filter_by_category(transactions, "없는카테고리")

    assert result == []


def test_filter_by_category_returns_independent_list() -> None:
    transactions: list[dict[str, object]] = [
        {
            "date": "2026-01-04",
            "type": "\uc9c0\ucd9c",
            "category": "\uc5ec\ud589",
            "description": "\ud56d\uacf5\uad8c",
            "amount": -979796,
            "memo": "\uba54\ubaa8_3",
        }
    ]

    result = filter_by_category(transactions, "여행")
    result.append(
        {
            "date": "2026-01-05",
            "type": "\uc9c0\ucd9c",
            "category": "\uc5ec\ud589",
            "description": "\uc5ec\ud589 \uacbd\ube44",
            "amount": -1000,
            "memo": "",
        }
    )

    assert len(transactions) == 1


def test_load_transactions_from_csv_loads_step1_transactions() -> None:
    transactions = load_transactions_from_csv("data/step1_transactions.csv")

    assert len(transactions) == 10
    assert transactions[0]["date"] == "2026-01-05"
    assert transactions[0]["amount"] == -12000
    assert isinstance(transactions[0]["amount"], int)
    assert transactions[-1]["amount"] == 25000
    assert isinstance(transactions[-1]["amount"], int)


def test_load_transactions_from_csv_handles_step4_large_file() -> None:
    transactions = load_transactions_from_csv("data/step4_large_transactions.csv")

    assert len(transactions) == 5000
    assert transactions[0]["amount"] == -64372
    assert isinstance(transactions[0]["amount"], int)
    assert transactions[-1]["amount"] == 445320
    assert isinstance(transactions[-1]["amount"], int)
