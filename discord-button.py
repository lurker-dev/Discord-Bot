#A Simple Code for Discord buttons. This code asks a question on sending the command "!question"


import discord
from discord.ext import commands
from discord.ui import Button, View
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

class MyButtonView(discord.ui.View):  # New class for button logic
  
    @discord.ui.button(label="Uniswap", style=discord.ButtonStyle.green, custom_id="test_button_id")
    async def test_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Yup it's correct! Uniswap it is!", ephemeral=True)
      
    @discord.ui.button(label="PancakeSwap", style=discord.ButtonStyle.green, custom_id="me_button_id")
    async def me_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Pancakeswap is used to swap bsc tokens... It's wrong...", ephemeral=True)

@bot.command(name='question')
async def test_button(ctx):
    #Sends a message with two test buttons.
    embed = discord.Embed(title="Where can SBEE swapped", description="Select one answer")
    # Use the MyButtonView class for button creation
    action_row = MyButtonView()
    await ctx.send(embed=embed, view=action_row)
  
bot.run('TOKEN')  # Replace with your actual bot token
