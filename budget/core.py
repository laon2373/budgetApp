"""Core transaction operations for the budget CLI application."""


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
