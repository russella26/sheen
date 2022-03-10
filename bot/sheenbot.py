from dotenv import load_dotenv
import discord
import os
import requests

load_dotenv()
token = os.getenv("TOKEN")
guild = int(os.getenv("GUILD"))
dockerstate = os.getenv("DOCKER")
togglestate = False
togglechannel = ''

if dockerstate:
    url = "http://server:5000"
else:
    url = "http://localhost:5000"

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[guild])
async def context(ctx, context):
    context += '\n'
    response = requests.post(url + "/generate", json={"context": context})
    aistring = response.content.decode("utf-8").split("\n")[1]
    await ctx.respond(aistring)

@bot.slash_command(guild_ids=[guild])
async def generate(ctx):
    response = requests.get(url + "/generate")
    aistring = response.content.decode("utf-8")
    await ctx.respond(aistring)

@bot.slash_command(guild_ids=[guild])
async def toggle(ctx):
    global togglestate
    global togglechannel
    togglestate = not togglestate
    if togglestate:
        togglechannel = ctx.channel
        await ctx.respond("replymode enabled :)")
    else:
        togglechannel = ''
        await ctx.respond("replymode disabled :(")

@bot.event
async def on_message(message):
    global togglestate
    global togglechannel
    if message.author.bot:
        return
    if togglestate and message.channel == togglechannel:
        context = message.content + '\n'
        response = requests.post(url + "/generate", json={"context": context})
        aistring = response.content.decode("utf-8").split("\n")[1]
        await message.reply(aistring)

bot.run(token)
