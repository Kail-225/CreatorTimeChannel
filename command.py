import discord
from boot import *
from discord.ext import commands
def coms(bot):
    @bot.slash_command(name="test",description="тестовая функция")
    async def test(ctx):
        return