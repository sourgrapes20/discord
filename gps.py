import discord
from discord.ext import commands
from geopy.geocoders import Nominatim
from maps import locate
from ebay import watch

TOKEN = 'NTM4NDI3NTg5OTI1MjczNjAx.D2s8hQ.cKyBN_21-ge73vTPYODeQhXlgso'

#client = discord.Client()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("We are up and ready to go")

@client.command()
async def view(ctx, ctx2):
    #await client.say("How many views would you like?(or type in cancel to cancel the command): ")
    #await client.say(str(ctx2))
    await client.say("```" + str(ctx2)  + " views scheduled for the link: " + str(ctx) +  "```")
    watch(ctx, int(ctx2))
    await client.say('```views completed ```')
    '''
    views = message.content()
    if views == 'cancel':
        await client.say("Views cancelled")
    elif is_int(views) == True:
        await client.say("Views Queued, please be patient")
        watch(ctx, views)
        await client.say("Views completed :smile:")
    '''

@client.command()
async def stop():
    await client.say("Shutting down.")
    await client.logout()

@client.command()
async def ping():
    await client.say("!pong")

@client.command()
async def find(*args):
    output = ' '
    for word in args:
        output += word
    coords = locate(output)
    await client.say("``` The gps coordinates for" + str(output) + " are " + str(coords) + "```")







client.run(TOKEN)
