import discord
from discord.ext import commands

# Client
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    # DO STUFF....
    general_channel = client.get_channel(547544688819961870)

    await general_channel.send('sup dog!')


    

@client.command()
async def editingmusicsmm2(ctx):
    await ctx.send('https://mariomakingmods.github.io/#editing-music-2')
@client.command()
async def tutorials(ctx):
    await ctx.send('https://mariomakingmods.github.io/')
@client.command()
async def gamebanana(ctx):
    await ctx.send('https://gamebanana.com/games/7348')



# Run the client on the server
client.run('ODMxOTg3MzA2MzM2MzU0MzM0.YHdOjw.vwtG7wPbEhXnW11GSMilr_Ssn14')
