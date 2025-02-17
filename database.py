"""
File: database.py
Author: Andrew Silkwood
Date Created: 2025-02-17
Description:
    A bridge to connect the bot code to a database.
    Currently configured for PostgreSQL 17.
"""

from dotenv import load_dotenv
import os
import asyncpg

import asyncio

# Global Variables
# .env vars
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# this main is not intended for actual use; used to test functionality
def main():
    asyncio.run(connect())


# connect to the database
async def connect():
    db = await asyncpg.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
    )
    return db


if __name__ == "__main__":
    main()
