from dotenv import load_dotenv
import discord
import os
from myutils.data import Bot

load_dotenv()
print("Logging in...")

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    command_prefix='!',
    prefix='!',
    command_attrs=dict(hidden=True)
)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(BOT_TOKEN)