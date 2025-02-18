"""
File: bot.py
Author: Andrew Silkwood
Date Created: 2025-02-13
Description:
    Initializes a Discord bot. The bot is intended to let Discord users to take
    part in a simulated stock market using real-time data from the actual stock
    market.
"""

from os import listdir
from re import match

from discord.ext import commands

from src.config.settings import SRC_PTH


class SM_Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # on bot initialized
    async def on_ready(self):
        print(f"We have logged in as [{self.user}]")

        # load all files in the cogs folder
        print("Loading cogs...")
        for f in listdir(f"{SRC_PTH}/bot/cogs/"):
            if match(r"\w+\.py", f):
                try:
                    await self.load_extension(f"src.bot.cogs.{f[:-3]}")
                    print(f"\tLoaded [{f[:-3]}]")
                except:
                    print(f"\tFailed to load [{f[:-3]}]")
        print("Cogs have been loaded")
