import discord
from ranked_finder import get_rank
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client() #gets connect to Discord

@client.event #is used to register an event
async def on_ready(): #is called when the bot is ready to start being used
    print('We have logged in as {0.user}'.format(client)) #

@client.event
async def on_message(message): #event triggers each time a message is received
    if message.author == client.user:
        return
    if message.content.startswith('$league'):
        username = message.content[8:]
        rank_stats = get_rank(username)
        await message.channel.send(rank_stats)
    
client.run(TOKEN)