"""
File: lobby.py
Author: Andrew Silkwood
Date Created: 2025-02-13
Description:
    Discord bot cog that handles game lobbies.
"""

from discord.ext import commands


class League(commands.Cog):
    # on cog load
    def __init__(self, bot):
        self.bot = bot

        # needs to catch up
        # catch up needs to carry over to stock market calculations as well
        # ensure all guilds are in the database

    # on cog unload
    def cog_unload(self):
        return super().cog_unload()

    # events

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(guild.id)
        print(type(guild.id))
        # try:
        #     await db.execute("CALL insert_guild($1)", guild.id)
        # except Exception as e:
        #     print(f"Could not add guild!: {e}")

    # creation

    @commands.command()
    async def create(self, ctx):
        pass

    @commands.command()
    async def delete(self, ctx):
        pass

    @commands.command()
    async def overview(self, ctx):
        pass

    @commands.command()
    async def setting(self, ctx):
        pass

    # player joining

    @commands.command()
    async def invite(self, ctx):
        pass

    @commands.command()
    async def join(self, ctx):
        pass

    @commands.command()
    async def accept(self, ctx):
        pass

    @commands.command()
    async def reject(self, ctx):
        pass

    @commands.command()
    async def leave(self, ctx):
        pass

    # game control

    @commands.command()
    async def start(self, ctx):
        pass

    @commands.command()
    async def end(self, ctx):
        pass

    @commands.command()
    async def list(self, ctx):
        pass


async def setup(bot):
    await bot.add_cog(League(bot))
