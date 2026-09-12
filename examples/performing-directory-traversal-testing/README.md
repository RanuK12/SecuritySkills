# Directory Traversal Example

This example demonstrates a classic directory traversal (path traversal) vulnerability and how to fix it.

## Vulnerable Code (`vulnerable.py`)

The vulnerable code takes a `file` query parameter and directly uses it to open a file without any validation.
An attacker can traverse directories by providing sequences like `../../../etc/passwd`.

### How to test the vulnerability

Create a test file in a safe location (or use an existing one) and run:

```bash
# Assuming you have a file at /etc/passwd (Linux) or C:\Windows\win.ini (Windows)
# For demonstration, we'll create a test file in a temporary directory.

# Linux example:
echo "test content" > /tmp/test.txt
python3 vulnerable.py "http://example.com?file=../../../tmp/test.txt"

# Attempt to read /etc/passwd (if you have permission):
python3 vulnerable.py "http://example.com?file=../../../etc/passwd"
```

The vulnerable script will happily read and display the contents of any file the process can access.

## Fixed Code (`fixed.py`)

The fixed code introduces a base directory (`BASE_DIR`) and ensures that the resolved path stays within that directory.
It uses `os.path.realpath` to resolve symlinks and relative paths, then checks that the resolved path starts with the base directory.

### How to test the fix

1. Create a base directory and a test file inside it:

```bash
mkdir -p ./safe_files
echo "safe content" > ./safe_files/test.txt
```

2. Run the fixed script with a legitimate request:

```bash
python3 fixed.py "http://example.com?file=test.txt"
```

   This should succeed and display the content of `./safe_files/test.txt`.

3. Attempt a directory traversal:

```bash
python3 fixed.py "http://example.com?file=../../../etc/passwd"
```

   The script will reject the request with an error message.

## Running the example

Make sure you are in the `examples/performing-directory-traversal-testing` directory.

```bash
# Test the vulnerable version (use with caution!)
python3 vulnerable.py "http://example.com?file=../../../etc/passwd"

# Test the fixed version
python3 fixed.py "http://example.com?file=test.txt"
```

## Notes

- This example is for educational purposes only.
- Always validate and sanitize user input when dealing with file paths.
- Consider using an allowlist of permitted files or a mapping from user input to safe file paths.