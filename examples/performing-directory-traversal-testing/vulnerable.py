#!/usr/bin/env python3
"""
Vulnerable: Directory traversal via file parameter.
Accepts 'file' query param and directly uses it to open files — classic path traversal.
"""
import sys
from urllib.parse import urlparse, parse_qs

def load_file_from_url(url: str):
    """INSECURE: directly uses the 'file' parameter to open files."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    filename = params.get("file", [None])[0]
    if not filename:
        print("Usage: python vulnerable.py 'http://example.com?file=../../../etc/passwd'")
        sys.exit(1)

    # VULNERABLE: no sanitization, direct path usage
    with open(filename, "r") as f:
        content = f.read()
    print(f"--- Content of {filename} ---")
    print(content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vulnerable.py 'http://example.com?file=../../../etc/passwd'")
        sys.exit(1)
    load_file_from_url(sys.argv[1])