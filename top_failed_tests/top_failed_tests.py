from collections import Counter
import re

def top_failed_tests(logs, n):
    """
    Displays the top 3 tests that failed more than n times, based on log entries.
    Log format expected: 'timestamp | STATUS | test_name,'
    """

    failed_tests = []

    # Split the logs into individual lines
    for line in logs.strip().splitlines():
        # Normalize and clean line
        line = line.strip()
        if not line:
            continue  # skip empty lines

        # Use regex to safely extract status and test name
        match = re.search(r"\|\s*(PASS|FAIL)\s*\|\s*([\w\d_]+),?", line)
        if match:
            status, test_name = match.groups()
            if status == "FAIL":
                failed_tests.append(test_name)

    # Count failures
    fail_count = Counter(failed_tests)

    # Filter only tests that failed more than n times
    filtered = {test: count for test, count in fail_count.items() if count > n}

    # Sort by number of failures (descending) and select top 3
    top_3 = sorted(filtered.items(), key=lambda x: x[1], reverse=True)[:3]

    # Print results
    if not top_3:
        print(f"No tests failed more than {n} times.")
    else:
        print(f"Top 3 tests that failed more than {n} times:")
        for test, count in top_3:
            print(f"  {test}: {count} failures")


if __name__ == "__main__":
    test_logs = """
    2026-01-01 14:23:01| PASS |test_login_valid_credentials,
    2026-01-01 14:23:02| FAIL |test_login_invalid_credentials,
    2026-01-01 14:23:14| PASS |test_send_transfer,
    2026-01-01 14:23:15| FAIL |test_password_reset,
    2026-01-01 14:23:16| FAIL |test_send_transfer,
    2026-01-01 14:23:18| PASS |test_send_transfer,
    2026-01-01 14:23:19| FAIL |test_send_transfer,
    2026-01-01 14:23:21| FAIL |test_account_deletion,
    2026-01-01 14:23:25| FAIL |test_profile_update,
    2026-01-01 14:23:31| FAIL |test_password_reset,
    2026-01-01 14:23:34| FAIL |test_password_reset,
    2026-01-01 14:23:45| FAIL |test_notification_settings,
    2026-01-01 14:23:51| FAIL |test_email_verification,
    """

    top_failed_tests(test_logs, n=1)
