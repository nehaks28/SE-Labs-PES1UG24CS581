# Lab 5: Static Code Analysis

**Name:** Neha
**SRN:** PES1UG24CS581
**Program analysed:** Personal Expense Tracker (`expense_tracker.py`)

## Forked Repository

https://github.com/nehaks28/L5_32_expense_tracker

The fork contains the cleaned `expense_tracker.py` and the three fix commits (one each for Bandit, Pylint and Flake8).

| Commit | Message |
|--------|---------|
| [2e3ff53](https://github.com/nehaks28/L5_32_expense_tracker/commit/2e3ff53) | Fix Bandit issues (B105, B108, B306, B605) |
| [4d623aa](https://github.com/nehaks28/L5_32_expense_tracker/commit/4d623aa) | Fix Pylint issues (docstrings, naming, global, broad except, enumerate, main guard) |
| [18af269](https://github.com/nehaks28/L5_32_expense_tracker/commit/18af269) | Fix Flake8 formatting issues (E203, E302, E261, E501) |

## Tools and Environment

| Tool | Version | Purpose |
|------|---------|---------|
| Pylint | 4.1.3 | Code quality and logic issues |
| Bandit | 1.9.4 | Security vulnerabilities |
| Flake8 | 7.4.1 | PEP 8 style and formatting |

Python 3.14.6, run inside a virtual environment (`venv`) on macOS.

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.27/10 | 10.00/10 |
| Bandit | 1 High, 2 Medium, 1 Low | 0 issues |
| Flake8 | 4 issues | 0 issues |

The program output is identical before and after the fixes, so behaviour was preserved.

## Issues Fixed

### Bandit (security)
- **B605 (High):** `os.system("xdg-open " + path)` allowed command injection. Replaced with `subprocess.run(["xdg-open", path], check=True)`.
- **B306 (Medium):** `tempfile.mktemp` has a race condition. Replaced with `tempfile.mkstemp`.
- **B108 (Medium):** hardcoded `/tmp` path. Replaced with `tempfile.gettempdir()`.
- **B105 (Low):** hardcoded password in source. Now read from the `BANK_SYNC_PASSWORD` environment variable and compared with `hmac.compare_digest`.

### Pylint (quality)
- Added module and function docstrings.
- Renamed camelCase names to snake_case.
- Removed the `global` statement by keeping the budget in a `settings` dict.
- Replaced the broad `except Exception` with `max(..., default=None)`.
- Replaced `range(len(...))` with `enumerate`.
- Added an `if __name__ == "__main__":` guard.

### Flake8 (formatting)
- E203 whitespace before `:`, E302 expected 2 blank lines, E261 two spaces before inline comment, E501 line too long.

## Note on `# nosec`

After switching to `subprocess.run` with a fixed argument list and no shell, Bandit still raises informational Low notes (B404, B603, B607). The injection risk is gone, so these were suppressed with specific `# nosec` codes instead of removing the feature.

## Files in this folder

- `README.md`: this file
- `Lab5_Issue_Table.docx`: issue table, results and reflection
- `pylint_before.txt`, `bandit_before.txt`, `flake8_before.txt`: tool reports before the fixes
- `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt`: tool reports after the fixes
