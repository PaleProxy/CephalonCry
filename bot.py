import discord 
import os
from discord import app_commands
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import datetime
import platform



bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

TOKEN =  os.environ.get('BOT_TOKEN')

#Syncs slash commands
@bot.event
async def on_ready():
    info = (Back.BLACK + Fore.GREEN + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z GMT+2 ", time.localtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(info + "Logged in as " + Fore.YELLOW + bot.user.name)
    print(info + "BOT ID " + Fore.YELLOW + str(bot.user.id))
    print(info + "Discord VVersion " + Fore.YELLOW + discord.__version__)
    print(info + "Python Version " + Fore.YELLOW + str(platform.python_version()))
    print(f'Bot is running')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


#help.................
@bot.tree.command(name='help', description='list of commands')
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(f"Here is a list of interactions: {interaction.user.mention}: ``")



#simple slash boilerplate
@bot.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Ahoy {interaction.user.mention}! This is a slash command", ephemeral=True)

#Userinfo
@bot.tree.command(name='userinfo', description="userinfo")
async def userinfo(interaction: discord.Interaction, member:discord.Member=None):
    if member == None:
        member = interaction.user
    roles = [role for role in member.roles]
    embed = discord.Embed(title=" User Info", description=f"Here is the info on the user {member.mention}", color= discord.Color.green(), timestamp= datetime.datetime.utcnow())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Nickname", value=f"{member.name}")
    embed.add_field(name="Status", value=member.status)
    embed.add_field(name="Created at", value=member.created_at.strftime("%a, %B, %#d, %Y, %I:%M %p "))
    embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %B, %#d, %Y, %I:%M %p "))
    embed.add_field(name=f"Roles {len(roles)}", value= " ".join([role.mention for role in roles]))
    embed.add_field(name="Top Role", value=member.top_role.mention)
    embed.add_field(name="Messages", value="0")
    embed.add_field(name="Bot?", value=member.bot)
    await interaction.response.send_message(embed=embed)

#status



bot.run(TOKEN)