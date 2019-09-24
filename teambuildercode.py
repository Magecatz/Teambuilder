import discord
from discord.ext import commands
import random
import operator

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

channeldict = {}

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('Use this link to invite {}:'.format(bot.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
	print('--------')

@bot.command()
async def ping(message):

	await message.channel.send(":ping_pong: Pong!")

@bot.command()
async def maketeams(message):
	team_captions = message.content.split(",")
	for x in team_captions:
		await message.channel.send(x)

@bot.event
async def on_message(message):
	if message.content.startswith('?') != True:
		channel = message.channel
		if channel.name in channeldict:
			msgs = int(channeldict[channel.name]) + 1
			channeldict[channel.name] = msgs
			print(channel.name, msgs)
		else:
			channeldict[channel.name] = 1
	
	await bot.process_commands(message)



bot.run('NjI1ODc0NTg5MTg4MjI3MjAx.XYl5Tw.iYD2MR2CL1Mgif-dJ8s2aH8cAa8')