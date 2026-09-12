#!/usr/bin/env python3
"""
Fixed: Directory traversal prevented by validating the file path.
Uses a safe base directory and ensures the resolved path stays within it.
"""
import os
import sys
from urllib.parse import urlparse, parse_qs

BASE_DIR = os.path.abspath("./safe_files")

def is_safe_path(path: str, base: str) -> bool:
    """Return True if path is within base directory."""
    # Resolve relative paths and symlinks
    real_path = os.path.realpath(path)
    real_base = os.path.realpath(base)
    # Check that real_path starts with real_base
    return os.path.commonpath([real_path, real_base]) == real_base

def load_file_from_url(url: str):
    """SECURE: validates the 'file' parameter against directory traversal."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    filename = params.get("file", [None])[0]
    if not filename:
        print("Usage: python fixed.py 'http://example.com?file=../../../etc/passwd'")
        sys.exit(1)

    # Construct the full path by joining with base directory
    # Note: We assume the application intends to serve files from BASE_DIR.
    # The user provides a relative path (or filename) that is appended to BASE_DIR.
    requested_path = os.path.join(BASE_DIR, filename)

    # SECURITY CHECK: ensure the resolved path is still inside BASE_DIR
    if not is_safe_path(requested_path, BASE_DIR):
        print(f"Error: Attempted directory traversal detected: {filename}")
        sys.exit(1)

    try:
        with open(requested_path, "r") as f:
            content = f.read()
        print(f"--- Content of {requested_path} ---")
        print(content)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fixed.py 'http://example.com?file=../../../etc/passwd'")
        sys.exit(1)
    load_file_from_url(sys.argv[1])