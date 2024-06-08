import discord
from discord.ext import commands

Token = 'MTIzMTU3Nzk3OTQ1MzE3NzkzNg.GnAWc5.pFeBnM3vEa_Oe6gTLCq8kxt8mLl2BjN9cOMeTs'

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name}이(가) 성공적으로 로그인했습니다!')

@bot.command()
async def JingJing(ctx):
    await ctx.send("나는 뀽뀽이다.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    user_text = message.content
    
    await message.channel.send(user_text)

    await bot.process_commands(message)

bot.run(Token)