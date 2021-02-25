import discord, Commands, LoadJson

client = discord.Client()
prefix = '+'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith(prefix + "Slope"):
        await Commands.Slope(message, prefix, client)

client.run(LoadJson.JsonToken()[0]["TOKEN"])