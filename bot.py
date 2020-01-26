import requests
from pprint import pprint
import discord
from discord.ext import commands
import random
import os
import asyncio

bot = commands.Bot(command_prefix = ".")

bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Keeping up with the World!'))
    print('Bot is running')

r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=')
##Put ur api key from newsapi.org after =
print(r)

first_article = r.json()["articles"][0]

@bot.command()
async def support(ctx):
    await ctx.send('Primitive Technology keeps you up with the news by typing .news it also has moderation command like .ban (reason) and .kick (reason)')
    print(ctx.author, "Ran support command")
@bot.command()
async def invite(ctx):
  await ctx.send('You can invite me to your discord by using https://discordapp.com/api/oauth2/authorize?client_id=670476763754790944&permissions=8&scope=bot')
  print(ctx.author, "Ran Invite command")
@bot.command()
async def kick(ctx, member : discord.Member, *,  reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"""User has been Kicked {member.mention}""")
  print(ctx.author, "Ran Kick command")
@bot.command()
async def ban(ctx, member : discord.Member, *,   reason=None):
  await member.ban(reason=reason)
  await ctx.send(f"""User has been Banned {member.mention}""")
  print(ctx.author, "Ran Ban command")

@bot.command()
async def news(ctx):
  await ctx.send(first_article)
  print(ctx.author, "Ran news command")

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send(f"""Welcome to {member.guild.name} {member.mention}""")


bot.run('Bot token here')
