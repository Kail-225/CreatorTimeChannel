import discord,asyncio
from boot import *
from discord.ext import commands
from command import coms
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
t=access()["ctc"]
async def autoreg(guild):
    mems=guild.members
    for i in mems:
        if str(i).find("(")!=-1:
            idu=guild.get_member_named(str(i).split("(")[1][0:-1]).id
            name=str(i).split("(")[0][0:-1]
            add_user(idu,name,guild.id)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.change_presence(activity=discord.Game(name="!help"))
    return
    print("Started without errors!")
@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    print(f"member: {member}\nbefore:{before}\nafter:{after}")
    guild=member.guild
    try:
        #channel=check_channel(member.id,guild.id)
        match after.channel:
            case None:
                if before.channel.id==925311871848947775:
                        list=discord.VoiceChannel(925311871848947775).members
                        print(list)
            case _:
                if before.channel!=None:
                    if before.channel.id==925311871848947775:
                        list=discord.VoiceChannel(925311871848947775).members
                        print(list)
                time_channel=guild.create_voice_channel(name=f"Канал {member.global_name}")
                member.move_to(time_channel)
    except Exception as e:
        print(f"Ошибка: {e}")
@bot.event
async def on_guild_join(guild):
    server=check_server(guild.id)
    if server==None:
        add_server(guild.id,guild.name)
        await autoreg(guild)
    else:
        return
@bot.event
async def on_member_join(member: discord.Member):
    guild=member.guild
    user=check_user(member.id,guild.id)
    if user==None:
        add_user(member.id,guild.id)
    else:
        return
con()
coms(bot)
bot.run(t)