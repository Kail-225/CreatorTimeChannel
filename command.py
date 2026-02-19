import discord
from boot import *
from discord.ext import commands
def coms(bot):
    @bot.slash_command(name="settings",description="Вызов меню настроек бота")
    async def test(ctx):
        return