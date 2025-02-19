"""
File: queries.py
Author: Andrew Silkwood
Date Created: 2025-02-17
Description:
    Handles database queries. If project scale becomes too large, this will
    become a folder of query files.
"""

from src.db.connection import get_db


async def add_guild(guild_id: int):
    db = await get_db()
    async with db.acquire() as conn:
        await conn.execute("CALL insert_guild($1)", guild_id)


async def get_guild_ids():
    db = await get_db()
    async with db.acquire() as conn:
        return await conn.fetch("SELECT * FROM get_guild_ids()")
