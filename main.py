from import discord
from discord.ext import commands, tasks

TOKEN = open('token.txt')
bot = commands.Bot(command_prefix='')


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


bot.run(TOKEN)