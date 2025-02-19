"""
File: league.py
Author: Andrew Silkwood
Date Created: 2025-02-13
Description:
    Discord bot cog that handles game leagues. Scope will be restricted to
    control of leagues such as players and game settings. Actual game behavior
    will be handled elsewhere.
"""

from discord.ext import commands

from src.db.queries import add_guild, get_guild_ids


class League(commands.Cog):
    # on cog load
    def __init__(self, bot):
        self.bot = bot

        # call on ready
        self.bot.loop.create_task(self.cog_ready())

    # cog is ready; catch up logic to update database to current discord state
    async def cog_ready(self):
        # add guilds while cog was offline to database
        # TODO implement datetime variable of last unload to pass fetch_guild's 'after' param
        guilds = await get_guild_ids()
        async for guild in self.bot.fetch_guilds(limit=None):
            if guild.id not in guilds:
                await add_guild(guild.id)

    # on cog unload
    def cog_unload(self):
        return super().cog_unload()

    # events

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await add_guild(guild.id)

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
