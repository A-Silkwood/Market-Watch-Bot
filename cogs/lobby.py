"""
File: lobby.py
Author: Andrew Silkwood
Date Created: 2025-02-13
Description:
    Discord bot cog that handles game lobbies.
"""

import discord
from discord.ext import commands


class Lobby(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("received")


async def setup(bot):
    await bot.add_cog(Lobby(bot))
