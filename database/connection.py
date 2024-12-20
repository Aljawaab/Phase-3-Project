import sqlite3

# Database connection module (database/connection.py)
def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect("cars_ownership.db")
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn
