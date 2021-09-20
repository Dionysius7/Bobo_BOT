import discord
from dotenv import load_dotenv 
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print('Hi My Name is {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$author'):
        await message.channel.send('Hi there! Dio and Sunny are my favorite creator')

client.run(DISCORD_TOKEN)
