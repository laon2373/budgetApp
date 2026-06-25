---
name: budget-cli-development
description: Use when implementing, testing, or reviewing features in this CSV-based Python CLI budget app. Applies project workflow rules for TDD-first development, mandatory type hints, maximum 50-line functions, radon cyclomatic complexity at 10 or below, pytest/radon validation, and qa_engineer review before commits.
---

# Budget CLI Development

## Core Workflow

1. Read `AGENTS.md` before changing files.
2. Write or update a failing `pytest` test before implementation.
3. Implement the smallest change that makes the test pass.
4. Keep every Python function typed and no longer than 50 lines.
5. Keep cyclomatic complexity at 10 or below.
6. Run targeted tests first, then `pytest` before finalizing.
7. Run `radon cc .` before commit-ready handoff.
8. Ask `qa_engineer` to review quality before committing.

## Design Guidance

- Keep CSV persistence separate from CLI argument parsing and presentation.
- Handle CSV edge cases explicitly: missing files, empty files, malformed rows, invalid numeric values, and encoding issues.
- Prefer small pure functions for parsing, validation, aggregation, and formatting.
- Use clear domain names such as `transaction`, `amount`, `category`, `memo`, and `occurred_on`.
- Avoid broad exception handling unless the CLI converts the error into a clear user-facing message.

## Testing Guidance

- Cover the behavior before adding implementation.
- Prefer temporary CSV files in tests instead of shared project data files.
- Test both successful CLI flows and failure cases.
- Include regression tests for discovered bugs.

## Quality Gate

Before any commit, verify:

- `pytest`
- `radon cc .`
- `qa_engineer` review result is `Pass`

If any gate fails, fix the issue before committing or pushing.
