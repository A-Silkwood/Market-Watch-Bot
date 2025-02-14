from dotenv import load_dotenv
import os
import discord
import logging

# Global Variables
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def main():
    # load in .env variables
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # initialize bot
    handler = logging.FileHandler(filename='marketwatch.log', encoding='utf-8', mode='w')
    client.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)


# General Bot Events

# on bot initialized
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# on user message received
@client.event
async def on_message(message):
    # ignore bot's own messages
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


if __name__ == "__main__":
    main()
