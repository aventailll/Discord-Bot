import discord
from ranked_finder import get_rank

client = discord.Client() #gets connect to Discord

@client.event #is used to register an event
async def on_ready(): #is called when the bot is ready to start being used
    print('We have logged in as {0.user}'.format(client)) #

@client.event
async def on_message(message): #event triggers each time a message is received
    if message.author == client.user:
        return
    if message.content.startswith('$league GigaBlue'):
        rank_stats = get_rank('GigaBlue')
        for i in range(len(rank_stats)):
            await message.channel.send(rank_stats[i])

client.run('OTgwNjc5MjcyOTUzOTU0MzU1.Gwmkje.tpGgNF5NzPlDZNGlAFXOie317d9Hyhf5DC0tHo')