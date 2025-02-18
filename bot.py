"""
File: bot.py
Author: Andrew Silkwood
Date Created: 2025-02-13
Description:
    Initializes a Discord bot. The bot is intended to let Discord users to take
    part in a simulated stock market using real-time data from the actual stock
    market.
"""

import logging
import os
import re

import discord
from discord.ext import commands
from dotenv import load_dotenv

import database

# Global Variables

# .env vars
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CMD_PREFIX = os.getenv("CMD_PREFIX")

# database vars
# db is declared in on_ready()

# bot vars
_intents = discord.Intents.default()
_intents.message_content = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=_intents)


# initialize and start bot
def main():
    handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
    bot.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)


# Bot Events


# on bot initialized
@bot.event
async def on_ready():
    print(f"We have logged in as [{bot.user}]")

    # initialize connection to database
    global db
    db = await database.connect()

    # load all files in the cogs folder
    print("Loading cogs...")
    for f in os.listdir("./cogs/"):
        if re.match(r"\w+\.py", f):
            try:
                await bot.load_extension(f"cogs.{f[:-3]}")
                print(f"\tLoaded [{f[:-3]}]")
            except:
                print(f"\tFailed to load [{f[:-3]}]")

    print("Cogs have been loaded")


# Bot Control Commands


# shutdown bot gracefully
@bot.command(aliases=["sd", "quit", "close"])
@commands.is_owner()
async def shutdown(ctx):
    print(f"Shutting down bot...")
    await ctx.send("Shutting down...")

    # unload cogs
    print("Unloading cogs...")
    for ext in list(bot.extensions.keys()):
        try:
            await bot.unload_extension(ext)
            print(f"\tUnloaded [{ext[5:]}]")
        except:
            print(f"\tFailed to unload [{ext[5:]}]")
    print("Cogs have been unloaded")

    # close database connection
    try:
        await db.close()
        print("Closed database connection")
    except Exception as e:
        print("Database connection could not close!")
        print(e)

    await bot.close()
    print("Shutdown bot")


# loads a single file in the cogs folder
@bot.command()
@commands.is_owner()
async def load(ctx, arg):
    try:
        await bot.load_extension(f"cogs.{arg}")
        print(f"Reloaded [{arg}]")
        await ctx.send(f"Loaded [{arg}]")
    except:
        print(f"Failed to reload [{arg}]")
        await ctx.send(f"Failed to load [{arg}]")


# reloads all files in the cogs folder
@bot.command()
@commands.is_owner()
async def reload(ctx):
    print("Reloading cogs...")
    for ext in list(bot.extensions.keys()):
        try:
            await bot.reload_extension(ext)
            print(f"\tReloaded [{ext[5:]}]")
        except:
            print(f"\tFailed to reload [{ext[5:]}]")
            await ctx.send(f"Failed to reload [{ext[5:]}]")

    print("Cogs have been reloaded")
    await ctx.send(f"Reload complete")


if __name__ == "__main__":
    main()
