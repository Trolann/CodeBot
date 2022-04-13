"""
CodeBot bot developed by Trolan (Trevor Mathisen). 
"""
import discord
import os

# Configuration variables requested for the rest of the program
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)
guild = ''
DISCORD_TOKEN = os.environ['DISCORD_TOKEN'] # Stored in secrets
GUILD_ID = int(os.environ['GUILD_ID']) # Stored in secrets

#voice_channel_id = int(902294184994693224)

#*****************************************************#
#                      On ready:                      #
#                    Basic actions                    #
#                      Process:                       #
#      - Prints to console when ready                 #
#*****************************************************#
@client.event
async def on_ready(): # When ready
	print('We have logged in as {0.user}'.format(client))

#*****************************************************#
#                 Message Processing:                 #
#     Channel and Private messages processed here     #
#                      Process:                       #
#     - Return formatted message                      #
#     - Don't process the bot's own message           #
#     - Process ping/pong checks                      #
#*****************************************************#
@client.event
async def on_message(message): # On every message

	if message.author == client.user: # Cancel own message
		return

	if message.content.lower().startswith('ping'): # Simple test the bot is working
		print('ping?/pong! processed from {}'.format(message.author))
		await message.channel.send('pong!')

	if not message.content.startswith("```") and message.content.find(';') != -1:
		formatted_msg = "```cpp\n {} \n```".format(message.content)
		await message.channel.send('{} here\'s your formatted code'.format(message.author.mention))
		await message.channel.send(formatted_msg)
		

	if message.content.startswith('!kill'):
		os.system('kill 1')
		return

client.run(DISCORD_TOKEN)