import discord
from discord.ext import commands
from datetime import datetime
from datetime import date
import pytz

TOKEN = "NzU0MDU1MDg0MDYwNzA0ODA4.X1vKhQ.UKrOEhb0Dsd5whL_ygj3CwQqi3w"
client = commands.Bot(command_prefix='?')

tz_br = pytz.timezone("America/Sao_Paulo")
datetime_br = datetime.now(tz_br)
timeformat = datetime_br.strftime("%H:%M")
today = date.today()
vdate = today.strftime("%d")
alertdate = int(vdate) % 2


@client.event
async def on_ready():
    print("BOT ONLINE - Hello World")
    print(client.user.name)
    print(client.user.id)


@client.command()
async def routeRhotano(ctx):
    embedR = discord.Embed(
        title="Rhotano Sea Route",
        description="This route is composed by: Galadion Bay, Southern Strait, Rhotano Sea",
        colour=discord.Colour.blue()
    )
    embedR.set_footer(text="Rhotano Sea Route Map")
    embedR.set_image(url="https://i.imgur.com/HJHkBAP.png")
    embedR.add_field(name="1st Stop\nGaladion Bay", value="Bait to use\nPlump Worm", inline=True)
    embedR.add_field(name="2nd Stop\nThe Southern Strait", value="Bait to use\nKrill", inline=True)
    embedR.add_field(name="3rd Stop\nRhotano Sea", value="Bait to use\nPlump Worm", inline=True)

    await ctx.send(embed=embedR)


@client.command()
async def routeNorthern(ctx):
    embedN = discord.Embed(
        title="The Northern Strait of Merlthor Route",
        description="This route is composed by: Southern Strait, Galadion Bay, Nothern Strait",
        colour=discord.Colour.blue()
    )
    embedN.set_footer(text="The Northern Strait of Merlthor Route Map")
    embedN.set_image(url="https://i.imgur.com/NJCpKgC.png")
    embedN.add_field(name="1st Stop\nThe Southern Strait", value="Bait to use\nKrill", inline=True)
    embedN.add_field(name="2nd Stop\nGaladion Bay", value="Bait to use\nPlump Worm", inline=True)
    embedN.add_field(name="3rd Stop\nNothern Strait", value="Bait to use\nRagworm", inline=True)
    await ctx.send(embed=embedN)


client.run(TOKEN)
