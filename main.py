# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} se conectó a Discord!')

print(TOKEN)
client.run(TOKEN)