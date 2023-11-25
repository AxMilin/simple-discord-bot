import discord
from discord.ext import commands

token = ""

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send(f"pong!🏓 {round(bot.latency * 1000)}ms")

bot.run(token)
