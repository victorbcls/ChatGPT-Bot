import asyncio
import os
import sys
from curses.ascii import isspace

import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

import automation
import read

TOKEN = "your discord bot token"
automation.login()  # Login on ChatGPT
bot = Bot("!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command(aliases=["ask"])
async def play(ctx):
    try:
        channel = ctx.author.voice.channel
        message = ctx.message.content.replace("!ask", "").replace("\n", " ")
        talk = True
        if len(message) < 1 or message.isspace():
            talk = False
        if talk == True:
            filename = automation.ask(message)
            await channel.connect()
            guild = ctx.guild
            voice_client: discord.VoiceClient = discord.utils.get(
                bot.voice_clients, guild=guild
            )
            audio_source = discord.FFmpegPCMAudio(filename)
            voice_client.play(
                audio_source,
                after=lambda _: asyncio.run_coroutine_threadsafe(
                    coro=disconnectAndClear(voice_client), loop=voice_client.loop
                ).result(),
            )
        else:
            await ctx.message.channel.send("Não rolou, foi mal")
    except Exception as e:
        await disconnectAndClear(voice_client),


async def disconnectAndClear(voice_client):
    await voice_client.disconnect(),
    dir = "./mp3"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


while True:
    bot.run(token=TOKEN)
