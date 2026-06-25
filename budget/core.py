"""Core transaction operations for the budget CLI application."""

from csv import DictReader
from pathlib import Path


def add_transaction(transactions: list[dict[str, object]], transaction: dict[str, object]) -> list[dict[str, object]]:
    """Append a transaction and return the updated transaction list."""
    transactions.append(transaction)
    return transactions


def get_balance(transactions: list[dict[str, object]]) -> float:
    """Return the sum of transaction amounts."""
    return float(sum(float(transaction["amount"]) for transaction in transactions))


def filter_by_category(transactions: list[dict[str, object]], category: str) -> list[dict[str, object]]:
    """Return transactions that match the given category, case-insensitively."""
    matched_transactions = [
        transaction
        for transaction in transactions
        if str(transaction["category"]).lower() == category.lower()
    ]
    return list(matched_transactions)


def load_transactions_from_csv(csv_path: str | Path) -> list[dict[str, object]]:
    """Load transactions from a UTF-8-sig CSV file."""
    path = Path(csv_path)
    with path.open(encoding="utf-8-sig", newline="") as file_handle:
        reader = DictReader(file_handle)
        return [
            {
                "date": row["date"],
                "type": row["type"],
                "category": row["category"],
                "description": row["description"],
                "amount": int(row["amount"]),
                "memo": row["memo"],
            }
            for row in reader
        ]
