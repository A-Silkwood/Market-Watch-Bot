"""
File: main.py
Author: Andrew Silkwood
Date Created: 2025-02-17
Description:
    Running this file will start up the Discord bot.
"""

import logging

import discord

from src.config.settings import SRC_PTH, BOT
from src.bot.bot import SM_Bot


def main():
    _intents = discord.Intents.default()
    _intents.message_content = True
    bot = SM_Bot(command_prefix=BOT.get("prefix"), intents=_intents)

    handler = logging.FileHandler(
        filename=f"{SRC_PTH}/../logs/bot.log", encoding="utf-8", mode="w"
    )

    bot.run(BOT.get("token"), log_handler=handler, log_level=logging.DEBUG)


if __name__ == "__main__":
    main()
