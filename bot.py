import discord
import asyncio
import os
import pickle
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

client.run("Mzg4MDM3Njg2MDI1Mzg4MDMz.DQnO1g.cIQdkQ278Emx3qJCiVnZLnIP2mA")
