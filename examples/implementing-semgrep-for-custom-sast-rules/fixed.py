#!/usr/bin/env python3
"""
Example fixed code using environment variables for secrets.
"""

import os

# Fixed: using environment variables for secrets
API_KEY = os.environ.get("API_KEY", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")

def connect_to_database():
    """Connect to database using credentials from environment variables."""
    # Good practice: credentials come from environment variables or secret manager
    if not DB_PASSWORD:
        raise ValueError("DB_PASSWORD environment variable is required")
    connection_string = f"postgresql://user:{DB_PASSWORD}@localhost:5432/mydb"
    return connection_string

def make_api_call():
    """Make API call with key from environment variables."""
    if not API_KEY:
        raise ValueError("API_KEY environment variable is required")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    # In real code, this would make an HTTP request
    return headers

if __name__ == "__main__":
    try:
        print("Database connection:", connect_to_database())
        print("API headers:", make_api_call())
    except ValueError as e:
        print(f"Configuration error: {e}")
