# Work with Python 3.6
import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!ayo'):
        msg = 'ayo {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!fuckyou'):
        msg = 'Fuck you, {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!philwall'):
        msg = '<:cursedPhil:614184742522454024><:bluephil:614217661781508148><:pinkphil:614217661714268161><:redphil:614217661639032832><:philred:614184742111412236> \n<:cursedPhil:614184742522454024><:bluephil:614217661781508148><:pinkphil:614217661714268161><:redphil:614217661639032832><:philred:614184742111412236> \n<:cursedPhil:614184742522454024><:bluephil:614217661781508148><:pinkphil:614217661714268161><:redphil:614217661639032832><:philred:614184742111412236> \n<:cursedPhil:614184742522454024><:bluephil:614217661781508148><:pinkphil:614217661714268161><:redphil:614217661639032832><:philred:614184742111412236> \n<:cursedPhil:614184742522454024><:bluephil:614217661781508148><:pinkphil:614217661714268161><:redphil:614217661639032832><:philred:614184742111412236> \n'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!dabchain'):
        msg = '<:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n <:zzdab:614185041194647612> \n <:zzdab2:614185041203036160> \n '.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!pogwall'):
        msg = '<a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974>\n<a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974>\n<a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974>\n<a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974>\n<a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974><a:pogwall:642146937490898974>'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!dekudancers'):
        msg = '<a:DekuDance1:642150739472416811><a:DekuDance1:642150739472416811><a:DekuDance1:642150739472416811><a:DekuDance1:642150739472416811>\n<a:DekuDance2:642150726042386432><a:DekuDance2:642150726042386432><a:DekuDance2:642150726042386432><a:DekuDance2:642150726042386432>'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
