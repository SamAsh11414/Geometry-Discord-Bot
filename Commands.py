import discord, asyncio, io, os, Commands, MathFuntions
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

async def Slope(message, prefix, client):
    await message.channel.send('What is your X1?')
    try:
        X1 = await client.wait_for("message", timeout=30)
    except asyncio.TimeoutError:
        await message.channel.send("Please type faster")
    await asyncio.sleep(1)
    await message.channel.send('What is your Y1?')
    try:
        Y1 = await client.wait_for("message", timeout=30)
    except asyncio.TimeoutError:
        await message.channel.send("Please type faster")
    await asyncio.sleep(1)
    await message.channel.send('What is your X2?')
    try:
        X2 = await client.wait_for("message", timeout=30)
    except asyncio.TimeoutError:
        await message.channel.send("Please type faster")
    await asyncio.sleep(1)
    await message.channel.send('What is your Y2?')
    try:
        Y2 = await client.wait_for("message", timeout=30)
    except asyncio.TimeoutError:
        await message.channel.send("Please type faster")
    print(X1.content + X2.content + Y2.content + Y1.content)
    plt.style.use('dark_background')
    plt.plot([X1.content,Y1.content,X2.content,Y2.content])
    MF = await MathFuntions.Intconversion(X1, X2, Y1, Y2)
    plt.savefig('images/graph.png')
    with open('images/graph.png', 'rb') as f:
        image = discord.File(f, filename='graph.png')
    await message.channel.send(file=discord.File('images/graph.png'))
    plt.clf()
    answer = linregress(MF[0]["X"], MF[0]["Y"])
    print(answer.slope)
    await message.channel.send("The Slope is:" )
    await message.channel.send(answer.slope)
