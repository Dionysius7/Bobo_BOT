# discord_token = "ODg5NTE4NjY1MzEyMTEyNjUw.YUia0A.cWUWSVnJY9CF8-XxqXJR07LuyAo"

import discord

token = "ODg5NTE4NjY1MzEyMTEyNjUw.YUia0A.anKdY9jX3P6tQkNdu4mt5aiEVlk"

from discord.ext import commands



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

client.run(token)

# print("ehe")