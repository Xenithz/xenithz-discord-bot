import discord
import random

from discord.ext import commands

class Fun_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def roll(self, ctx, sides):
        r = random.randint(1, int(sides))
        embed = discord.Embed(colour=0xFFFFCC, title=":game_die: Rolling Dice!")
        embed.add_field(name="Result", value=r)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def convertToCelcius(self, ctx, fahrenheit):
        r = (int(fahrenheit) - 32) / 1.8
        rounded = round(r, 4)
        embed = discord.Embed(colour=0x000099, title=":thermometer: Converting to Celcius!")
        embed.add_field(name="Result", value=rounded)
        
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def convertToCentimeters(self, ctx, inches):
        r = int(inches) * 2.54
        embed = discord.Embed(colour=0xffb8c6, title=":straight_ruler: Converting to Centimeters!")
        embed.add_field(name="Result", value=r)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun_Commands(bot))