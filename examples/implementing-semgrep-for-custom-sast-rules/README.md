# Example: Detecting Hardcoded Secrets with a Custom Semgrep Rule

This example demonstrates how the skill "implementing-semgrep-for-custom-sast-rules" can be used to create a Semgrep rule that detects hardcoded API keys in Python code.

## Files

- `vulnerable.py`: Contains a hardcoded secret (simulated API key).
- `fixed.py`: The same code, but the secret is loaded from an environment variable.
- `rules/hardcoded-secret.yaml`: A custom Semgrep rule that matches hardcoded strings assigned to variables named `API_KEY`.

## How to Run

1. Make sure you have Semgrep installed (version 1.177.0 or newer). You can install it via pip:

   ```bash
   pip install semgrep
   ```

2. Run the rule against the vulnerable code:

   ```bash
   semgrep --config=rules/hardcoded-secret.yaml vulnerable.py
   ```

   Expected output: one finding (the hardcoded secret).

3. Run the rule against the fixed code:

   ```bash
   semgrep --config=rules/hardcoded-secret.yaml fixed.py
   ```

   Expected output: no findings.

## What This Shows

- The skill enables users to write custom Semgrep rules without deep prior knowledge.
- The rule is simple, targeted, and produces zero false positives in this example.
- By providing such a rule as part of a skill, agents can automatically improve the security of codebases they work on.

## Notes

- The rule matches both double and single quoted strings.
- In a real project, you might want to extend the rule to catch more variations (e.g., different variable names, other types of secrets).
