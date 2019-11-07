# Work with Python 3.6
import discord

TOKEN = 'NjQwOTg5OTI2Nzc0NjY5Mzcz.XcSYHg.ZPJoz966A8fnYGQvqtASF9nQCRE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
