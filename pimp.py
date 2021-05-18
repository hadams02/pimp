from discord import channel, client
from discord.flags import Intents
import requests
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = '$')
bot = client

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_message_join(member):
    channel = client.get_channel(820511759155855362)
    embed=discord.Embed(title=f"Waddup G {member.name}", description=f"Welcome playa {member.guild.name}!") 
    embed.set_thumbnail(url=member.avatar_url) 

    await channel.send(embed=embed)

@bot.event
async def on_member_leave(ctx):
    await ctx.send('{member} hates the game and not the playa')

@bot.event
async def on_member_kick(ctx):
    bot.get_channel(820511759155855362)
    await ctx.send('{member} got the fookin boot')

@bot.command()
async def passtheblunt(ctx):
    await ctx.send("help yaself g")

##Random biggie lyric command
my_list = ["i love it when they call me big poppa", "throw ya hands in the air if u a true playa", "super nintendo sega genesis when i was dead broke man i couldnt picture this"]
@bot.command()
async def biggie(ctx):
    await ctx.send(random.choice(my_list))

## Coinflip command
heads = "Heads"
tails = "Tails"

@bot.command()
async def coinflip(ctx):
    await ctx.send(random.choice([heads, tails]))

## Runs bot
bot.run('ODQzNjg5ODY0ODk2ODM5Njkx.YKHhag.GGZlzHfOfSJI523u0x7HthurNKE')

