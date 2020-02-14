import discord
import aiohttp
import json

from discord.ext import commands
from myutils import http

class Stats_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def corona(self, ctx):
        try:
            r = await http.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22confirmed%22%7D%2C%20%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22deaths%22%7D%2C%20%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22recovered%22%7D%5D", res_method="text", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        data = json.loads(r)
        attr = data["features"][0]["attributes"]

        embed = discord.Embed(colour=0xFF0000, title="Corona statistics")
        embed.add_field(name="Confirmed", value=attr['confirmed'], inline=True)
        embed.add_field(name="Deaths", value=attr['deaths'], inline=True)
        embed.add_field(name="Recovered", value=attr['recovered'], inline=True)

        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Stats_Commands(bot))