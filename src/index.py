import discord
from discord import embeds
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>',description="This is a helper bot")

@bot.command()
async def sum(ctx,num1: int, num2: int):
    await ctx.send(num1+num2)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem impsum asdasd",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png")
    await ctx.send(embed=embed)
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
 
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('/watch\?v=(.{11})',html_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v='+ search_results[0])
    
   
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/anyname"))
    print('My Bot is Ready')   
    
    
bot.run('discord bot number')    