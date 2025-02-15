from dotenv import load_dotenv
import os
import re

import discord
import logging
from discord.ext import commands

# Global Variables
# .env vars
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CMD_PREFIX = os.getenv("CMD_PREFIX")
# bot vars
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=intents)


def main():
    # load in .env variables
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # initialize bot
    handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
    bot.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)


# Bot Events


# on bot initialized
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

    # load all files in the cogs folder
    print("Loading cogs")
    for f in os.listdir("./cogs/"):
        if re.match(r"\w+\.py", f):
            try:
                await bot.load_extension(f"cogs.{f[:-3]}")
                print(f"Loaded {f[:-3]}")
            except:
                print(f"Failed to load {f[:-3]}")

    print("Cogs have been loaded")


# Bot Control Commands


# shutdown bot gracefully
@bot.command(aliases=["sd", "quit", "close"])
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    await bot.close()


# loads a single file in the cogs folder
@bot.command()
@commands.is_owner()
async def load(ctx, arg):
    try:
        await bot.load_extension(f"cogs.{arg}")
        print(f"Reloaded {arg}")
        await ctx.send(f"Loaded {arg}")
    except:
        print(f"Failed to reload {arg}")
        await ctx.send(f"Failed to load '{arg}'")


# reloads all files in the cogs folder
@bot.command()
@commands.is_owner()
async def reload(ctx):
    print("Reloading cogs")
    for ext in list(bot.extensions.keys()):
        try:
            await bot.reload_extension(ext)
            print(f"Reloaded {ext[5:]}")
        except:
            print(f"Failed to reload {ext[5:]}")
            await ctx.send(f"Failed to load '{ext[5:]}'")

    print("Cogs have been reloaded")
    await ctx.send(f"Reload complete")


if __name__ == "__main__":
    main()
