import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='+')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Cicerone, at your sevice")
    await client.change_status(game=discord.Game(name='Trivia Route Patrol'))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I know.", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="No. of Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="No. of Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: {}. He didn't deserve his stay!".format(user.name))
    await bot.kick(user)

#@bot.command(pass_context=True)
#async def embed(ctx):
#    embed = discord.Embed(title="test", description="my name jeff", color=0x00ff00)
#    embed.set_footer(text="this is a footer")
#    embed.set_author(name="Will Ryan of DAGames")
#    embed.add_field(name="This is a field", value="no it isn't", inline=True)
#    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def clr(ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.event
async def on_message(message):
    await bot.delete_message(message)

bot.run("NDQzMjkwNDAwMjkyMjA4NjQy.DdapEw.FrCnxvOX-fyntfNgdOnfs28kXsg")
