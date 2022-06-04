import discord
from ranked_finder import get_rank
from valorant_stats import val_stats
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('O4Ls')
client = discord.Client() #gets connect to Discord

@client.event #is used to register an event
async def on_ready(): #is called when the bot is ready to start being used
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message): #event triggers each time a message is received
    if message.author == client.user:
        return
    if message.content.startswith(':)league'): #sees if the beginning of the message starts with '$league' to trigger the command
        username = message.content[8:] #concatenates the beginning of the message to only get the username
        league_stats = get_rank(username) #uses the get_rank function to get the data about the user
        await message.channel.send(league_stats) #prints the users data into discord
    if message.content.startswith(':)val'):
        username = message.content[5:]
        valorant_stats = val_stats(username)
        await message.channel.send(valorant_stats)
client.run(TOKEN)
