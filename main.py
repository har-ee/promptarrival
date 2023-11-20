import asyncio
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import re
import time

from extraction import extract_time_from_message

# Load .env file
load_dotenv()
bot_token = os.getenv("DISCORD_TOKEN")

# Set up bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    print(message)
    print(f'Received message `{message.content}`')
    channel = message.channel

    time_num, time_str = extract_time_from_message(message.content)

    if time_num is None:
        return

    try:
        arrival_time = int(time_num)

        await asyncio.sleep(arrival_time)  # Convert minutes to seconds
        await channel.send(f"{message.author.mention} you said `{time_str}`. Are you here?")
    except ValueError:
        print("Invalid time format")

# Run bot
bot.run(bot_token)
