import discord
import os
#import request
#import json

client = discord.Client()

#def get_quote():
 # response = request.get("")
  #json_data = json.loads(response.text)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.endsWith('hi elon'):
    await message.channel.send('hello {0.author}'.format(message))

client.run(os.getenv('TOKEN'))
