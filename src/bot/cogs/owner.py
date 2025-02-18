"""
File: owner.py
Author: Andrew Silkwood
Date Created: 2025-02-18
Description:
    Discord bot cog that handles owner only commands. This includes cog
    loading/unloading and graceful shutdown of the bot.
"""

from discord.ext import commands


class Owner(commands.Cog):
    # on cog load
    def __init__(self, bot):
        self.bot = bot

    # on cog unload
    def cog_unload(self):
        return super().cog_unload()

    # Commands

    # shutdown bot
    @commands.command(aliases=["sd"])
    @commands.is_owner()
    async def shutdown(self, ctx):
        print(f"Shutting down bot...")
        await ctx.send("Shutting down...")

        # unload cogs
        print("Unloading cogs...")
        for ext in list(self.bot.extensions.keys()):
            if ext.lower().endswith("owner"):
                continue
            try:
                await self.bot.unload_extension(ext)
                print(f"\tUnloaded [{ext.split('.')[-1]}]")
            except:
                print(f"\tFailed to unload [{ext.split('.')[-1]}]")
                await ctx.send(f"Failed to unload [{ext.split('.')[-1]}]")
        print("Cogs have been unloaded")
        await self.cog_unload()

        # close bot connection
        print("Shutdown bot")
        await self.bot.close()

    # loads a single file in the cogs folder
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, arg):
        if arg.lower() == "owner":
            return
        try:
            await self.bot.load_extension(f"src.bot.cogs.{arg}")
            print(f"Loaded [{arg}]")
            await ctx.send(f"Loaded [{arg}]")
        except:
            print(f"Failed to load [{arg}]")
            await ctx.send(f"Failed to load [{arg}]")

    # unloads a single file in the cogs folder
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, arg):
        if arg.lower() == "owner":
            return
        try:
            await self.bot.unload_extension(f"src.bot.cogs.{arg}")
            print(f"Unloaded [{arg}]")
            await ctx.send(f"Unoaded [{arg}]")
        except:
            print(f"Failed to unload [{arg}]")
            await ctx.send(f"Failed to unload [{arg}]")

    # reloads all files in the cogs folder
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        print("Reloading cogs...")
        for ext in list(self.bot.extensions.keys()):
            if ext.lower().endswith("owner"):
                continue
            try:
                await self.bot.reload_extension(ext)
                print(f"\tReloaded [{ext.split('.')[-1]}]")
            except:
                print(f"\tFailed to reload [{ext.split('.')[-1]}]")
                await ctx.send(f"Failed to reload [{ext.split('.')[-1]}]")

        print("Cogs have been reloaded")
        await ctx.send(f"Reload complete")


async def setup(bot):
    await bot.add_cog(Owner(bot))
