from dotenv import load_dotenv
import discord
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$zamir'):
        await message.channel.send('is a furry!')

client.run(BOT_TOKEN)