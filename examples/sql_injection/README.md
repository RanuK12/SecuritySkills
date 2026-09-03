# SQL Injection Example

This directory contains a before-and-after example of a SQL injection vulnerability and its fix, designed to be detected by the `sql_injection` skill in this library.

## Files

- `before.py`: Vulnerable code that concatenates user input directly into a SQL query.
- `after.py`: Fixed code using parameterized queries to prevent SQL injection.

## How to Test

1. Run the vulnerable example to see it in action (for educational purposes only):
   ```bash
   python before.py
   ```
   Provide a malicious input like `1 OR 1=1--` to see the vulnerability.

2. Run the fixed example to see the secure behavior:
   ```bash
   python after.py
   ```
   The same input will be treated as a literal string and not cause injection.

## Skill Detection

The `sql_injection` skill in this library is designed to flag the pattern in `before.py` and not flag the fixed pattern in `after.py`.

To test the skill detection:
```bash
# From the root of this repository
python tools/validate-skill.py skills/sql_injection/
```
Or use the skill with an AI agent that supports the agentskills.io standard.

## Diff

Here is the essential change made to fix the vulnerability:

```diff
-     query = "SELECT * FROM users WHERE id = " + user_id
+     query = "SELECT * FROM users WHERE id = ?"
-     cursor.execute(query)
+     cursor.execute(query, (user_id,))
```

**Explanation**: The fix replaces string concatenation with a parameterized query, which separates SQL code from data, preventing injection.