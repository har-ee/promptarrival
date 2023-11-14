import asyncio
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import re
import time

# Load .env file
load_dotenv()
bot_token = os.getenv("DISCORD_TOKEN")

# Set up bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def extract_time_from_message(message):
    time_pattern = re.compile(r'(?:in|be|brb)\s*(\d+|\d+\s*-\s*\d+)\s*(sec|secs|second|seconds|min|mins|minute|minutes|h|hour|hours)\s*(\d+)?', re.IGNORECASE)

    match = time_pattern.search(message)

    if match:
        whole_str = match.group(0)
        time_str = match.group(1).replace(' ', '')
        time_units = match.group(2).lower()
        time_str_extra = match.group(3)

        if '-' in time_str:
            time_value = time_str.split('-')[1]
            time_seconds = int(time_value)
        else:
            time_seconds = int(time_str)

        if 'min' in time_units or 'minute' in time_units:
            time_seconds *= 60
        elif 'h' in time_units or 'hour' in time_units:
            time_seconds *= 3600
            if time_str_extra is not None:
                extra_mins = int(time_str_extra)
                time_seconds += (extra_mins * 60)

        print(time_str, time_units, time_seconds)

        return time_seconds, whole_str.strip()

    return None, None

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
        await channel.send(f"{message.author.mention}, {time_str} has passed. Have you arrived?")
    except ValueError:
        print("Invalid time format")

# Run bot
bot.run(bot_token)
