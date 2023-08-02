# import discord
# from discord.ext import commands
# from discord import app_commands

# class cog1(commands.Cog):
#     def __init__(self, client: commands.Bot):
#         self.clilent = client
    
#     @app_commands.command(name="cog1", description='Says hello!')
#     async def cog1(self, interaction: discord.Interaction):
#         await interaction.response.send_message(content="Hello")

#     async def setup(client:commands.Bot) -> None:
#         await client.add_cog1(cog1(client))