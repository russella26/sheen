from dotenv import load_dotenv
import discord
import os
import requests

load_dotenv()
token = os.getenv("TOKEN")
guild = [os.getenv("GUILD")]
dockerstate = os.getenv("DOCKER")

if dockerstate:
    url = "http://server:5000"
else:
    url = "http://localhost:5000"

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=guild)
async def generate(ctx):
    response = requests.get(url + "/generate")
    aistring = response.content.decode("utf-8")
    await ctx.respond(aistring)

bot.run(token)
