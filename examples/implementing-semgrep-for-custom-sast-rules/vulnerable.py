#!/usr/bin/env python3
"""
Example vulnerable code with hardcoded secret for Semgrep testing.
"""

import os

# Vulnerable: hardcoded secret
API_KEY = "sk-live-1234567890abcdef"
DB_PASSWORD = "super_secret_password_123"
SECRET_TOKEN = "ghp_abcdef1234567890"

def connect_to_database():
    """Connect to database using hardcoded credentials."""
    # This is bad practice - credentials should come from environment variables or secret manager
    connection_string = f"postgresql://user:{DB_PASSWORD}@localhost:5432/mydb"
    return connection_string

def make_api_call():
    """Make API call with hardcoded key."""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    # In real code, this would make an HTTP request
    return headers

if __name__ == "__main__":
    print("Database connection:", connect_to_database())
    print("API headers:", make_api_call())
