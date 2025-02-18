"""
File: connection.py
Author: Andrew Silkwood
Date Created: 2025-02-17
Description:
    Handles the connection to the database.
    Currently configured for PostgreSQL 17.
"""

import asyncpg
from src.config.settings import DB

_db = None


# initialize database connection
async def init_db():
    global _db
    if _db is None:
        print(
            f"Connecting to [{DB.get('name')}] on [{DB.get('host')}:{DB.get('port')}] as [{DB.get('user')}]..."
        )
        _db = await asyncpg.create_pool(
            user=DB.get("user"),
            password=DB.get("password"),
            database=DB.get("name"),
            host=DB.get("host"),
            port=DB.get("port"),
        )
        print(f"Connected to [{DB.get('name')}]")


# getter for connection
async def get_db():
    return _db
