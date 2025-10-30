# Top Failed Tests Analyzer

A simple Python script that analyzes log files to find the top 3 tests that failed more than **n** times.

## 🧠 How it works

The script reads through your log file, extracts lines containing the keyword `FAIL`, counts the occurrences of each failed test, and prints the top 3 that failed more than the specified threshold.

## 🚀 Usage

```bash
python top_failed_tests.py
```

Modify the `n` value in the script to set the threshold.

## 🧩 Example Output

```
Top 3 tests that failed more than 1 times:
  test_password_reset: 3 failures
  test_send_transfer: 2 failures
```
