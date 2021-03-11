import discord
import os
from awake import awake
from itertools import cycle
from discord.ext import commands, tasks

client = discord.Client()
status = cycle(['prefix=(#) | #help', 'Developed with ❤️ & 🧠 by https://mr-a0101.github.io/ '])

#status
@client.event

async def on_ready():
  change_status.start()
  print('{0.user} is Online!'.format(client))

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

#commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#hello'):
      await message.channel.send('Yo Boi, How you doin!')

#end-to-end
awake()
client.run(os.getenv('TOKEN'))
