import discord, asyncio, io, os, Commands
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

TOKEN = ('ODE0MjMzNzgzNTkwMTkxMTA0.YDa4TQ.IYTJKsLLg3SOLGF-c4rgspe_fWU')
client = discord.Client()
prefix = '+'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith(prefix + "Slope"):
        await Commands.Slope(message, prefix, client)
        




client.run(TOKEN)