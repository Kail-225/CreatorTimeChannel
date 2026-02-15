import discord
from discord.ext import commands
from command import coms
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
t=access["ctc"]
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.change_presence(activity=discord.Game(name="!help"))
    return
    print("Started without errors!")
@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    guild=member.guild
    print(guild)
    #print(f"Участник: {member}\nПеред обновлением: {before}\nПосле обновления: {after}")
    if str(after.channel)=="Основной":
        name_channel=str("Канал")
        time_channel=await guild.create_voice_channel(name=name_channel)
        await member.move_to(time_channel)
coms(bot)
bot.run(t)