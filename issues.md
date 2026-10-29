# Lab 5: Static Code Analysis

## Issue Analysis and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Code quality / potential bug | Verify from report | A mutable list is used as a function default argument, which can lead to unintended shared state. | Use `None` as the default and initialize a new list inside the function. |
| Unsafe deserialization | Security | Verify from report | Loading data using pickle can execute malicious code if the input file is untrusted. | Use JSON for data exchange or validate and restrict the source of serialized data. |
| Shell command execution | Security | Verify from report | Constructing a shell command using input can create command-injection risks. | Avoid shell execution; use a safer subprocess approach or remove the unused helper if appropriate. |
| Naming and formatting violations | Code style | Verify from report | Some function names and formatting may not follow Python conventions. | Follow PEP 8 naming and formatting conventions. |

**Note:** The issues above are candidate findings based on the original source code. Confirm each finding against the actual Pylint, Bandit, and Flake8 reports. Update the line numbers and descriptions to match the issues you actually document.