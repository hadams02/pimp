import asyncio
from discord import channel, client
import requests
import discord
import random
import requests
import youtube_dl
import asyncio
from discord import FFmpegPCMAudio
from bs4 import  BeautifulSoup
from discord.ext import commands
from list1 import kanyequotes

intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix = '$', intents=intents)
bot = client

@bot.event
async def on_ready():
    print('Bot is ready.')

## Action messages, work in progress 
@bot.event
async def on_member_join(member):
    channel = client.get_channel(820511759155855362)
    embed=discord.Embed(title=f"Waddup G {member.name}", description=f"Welcome playa to {member.guild.name}!") 
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = client.get_channel(820511759155855362)
    embed=discord.Embed(title=f"Leave and take ya homeboys with ya {member.name}", description=f"And dont ask for no handouts from {member.guild.name}!") 
    embed.set_thumbnail(url=member.avatar_url) 

    await channel.send(embed=embed)

@bot.event
async def on_member_kick(ctx):
    bot.get_channel(820511759155855362)
    await ctx.send('{member} got the fookin boot')

@bot.command()
async def passtheblunt(channel):
    channel = client.get_channel(820511759155855362)
    await channel.send("help yaself g", file=discord.File('/Users/hunter/Desktop/pimp/pass.png'))
    

## discord.Sticker

##Random biggie lyric command
my_list = ["i love it when they call me big poppa", "throw ya hands in the air if u a true playa", "super nintendo sega genesis when i was dead broke man i couldnt picture this"]
@bot.command()
async def biggie(ctx):
    await ctx.send(random.choice(my_list))

##Random Kanye quote
@bot.command()
async def kanye(ctx):
    await ctx.send(random.choice(kanyequotes) + " -Kanye West")

#crypto
@bot.command()
async def crypto(ctx, arg):
    s = requests.session()
    if (arg=='btc'):
        r = s.get("https://www.coindesk.com/price/bitcoin")
        soup = BeautifulSoup(r.content, 'html.parser')
        price = soup.find('div', class_ ="price-large")
        getText = price.getText()
        em = discord.Embed(title=getText, colour=0xff9900)
        em.set_author(name='Bitcoin', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/BTC_Logo.svg/1200px-BTC_Logo.svg.png')
        await ctx.send('', embed=em)
    elif (arg=='ada'):
        r = s.get("https://www.coindesk.com/price/cardano")
        soup = BeautifulSoup(r.content, 'html.parser')
        price = soup.find('div', class_ ="price-large")
        getText = price.getText()
        em = discord.Embed(title=getText, colour=0x2a71d0)
        em.set_author(name='Cardano', icon_url='https://cryptologos.cc/logos/cardano-ada-logo.png')
        await ctx.send('', embed=em)
    elif (arg=='eth'):
        r = s.get("https://www.coindesk.com/price/ethereum")
        soup = BeautifulSoup(r.content, 'html.parser')
        price = soup.find('div', class_ ="price-large")
        getText = price.getText()
        em = discord.Embed(title=getText, colour=0xecf0f1)
        em.set_author(name='Ethereum', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png')
        await ctx.send('', embed=em)
    elif (arg=='doge'):
        r = s.get("https://www.coindesk.com/price/dogecoin")
        soup = BeautifulSoup(r.content, 'html.parser')
        price = soup.find('div', class_ ="price-large")
        getText = price.getText()
        em = discord.Embed(title=getText, colour=0xba9f34)
        em.set_author(name='Dogecoin', icon_url='https://static.wikia.nocookie.net/dogecoin/images/c/c9/Logo.png/revision/latest?cb=20180917222934')
        await ctx.send('', embed=em)
    elif (arg=='ltc'):
        r = s.get("https://www.coindesk.com/price/litecoin")
        soup = BeautifulSoup(r.content, 'html.parser')
        price = soup.find('div', class_ ="price-large")
        getText = price.getText()
        em = discord.Embed(title=getText, colour=0xba9f34)
        em.set_author(name='Litecoin', icon_url='https://upload.wikimedia.org/wikipedia/commons/f/f8/LTC-400.png')
        await ctx.send('', embed=em)
    elif (arg=='list'):
        await ctx.send('')
    
## Coinflip command
heads = "Heads"
tails = "Tails"

@bot.command()
async def coinflip(ctx):
    await ctx.send(random.choice([heads, tails]))

bot.run('ODQzNjg5ODY0ODk2ODM5Njkx.YKHhag.GGZlzHfOfSJI523u0x7HthurNKE')
