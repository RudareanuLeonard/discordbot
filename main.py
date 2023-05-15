from datetime import datetime
import random
import discord
from discord.ext import commands
import logging

#####################################
JENKINS_TEST = "INAINTE DE MODIFICARE"
#####################################

# its set to INFO and its annoying
logging.getLogger('discord.client').setLevel(logging.WARNING)
logging.getLogger('discord.gateway').setLevel(logging.WARNING)

# random setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# haha hihi
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
    "Why did the programmer quit his job? Because he didn't get arrays!"
]

# logs some stuff
@bot.event
async def on_ready():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(f'{current_time} - Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

@bot.command()
async def joke(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    random_index = random.randint(0, 2)
    print(f'{current_time} - {jokes[random_index]}')
    await ctx.send(jokes[random_index])

@bot.command()
async def jenkins_test(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    random_index = random.randint(0, 2)
    print(f'{current_time} - {JENKINS_TEST}')
    await ctx.send(JENKINS_TEST)

bot.run("OTE4MTA2NDQ1Nzk3NTU2MjQ1.Guioyc.ezor-HUpNQZ37Gm5Nh4Ql8BEXOHv6yL7gKonD4")