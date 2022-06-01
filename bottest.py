import discord
from ranked_finder import get_rank
import asyncio
from discord.ext import commands

client = discord.Client() #gets connect to Discord
bot = commands.Bot(command_prefix = '.')

@client.event #is used to register an event
async def on_ready(): #is called when the bot is ready to start being used
    print('bot is running') #

async def prompt(ctx, message: str, timeout: float) -> str:
    await ctx.send(message)
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=timeout)
    return message.content

@bot.command
async def league(ctx):
    try:
        user = await prompt(ctx, "What is your username?", timeout=10)
    except asyncio.TimeoutError:
        await ctx.send("You are too slow.")
    else:
        rank_stats = get_rank(user)
        for i in range(len(rank_stats)):
            await ctx.send(rank_stats[i])

client.run('OTgwNjc5MjcyOTUzOTU0MzU1.Gwmkje.tpGgNF5NzPlDZNGlAFXOie317d9Hyhf5DC0tHo')