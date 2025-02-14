from dotenv import load_dotenv
import os
import discord
import logging
from discord.ext import commands

# Load .env
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CMD_PREFIX = os.getenv('CMD_PREFIX')

# Global Variables
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=intents)

def main():
    # load in .env variables
    BOT_TOKEN = os.getenv('BOT_TOKEN')

    # initialize bot
    handler = logging.FileHandler(filename='marketwatch.log', encoding='utf-8', mode='w')
    bot.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)


# General Bot Events

# on bot initialized
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await bot.close()


if __name__ == '__main__':
    main()
