import discord
from discord.ext import commands

Token = open("token.txt", "r").readline()

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name}이(가) 성공적으로 로그인했습니다!')

@bot.command()
async def c(ctx,*,text):
    await ctx.send(text)

bot.run(Token)