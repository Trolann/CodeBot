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
pb = ''
REQUEST_PREFIX = "@" # Prefix for users to interact with bot
COMMAND_PREFIX = "!" # Prefix for managers to command the bot
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
	global guild
	global voice_channel
	global pb
	guild = client.get_guild(GUILD_ID)
	print(guild)
	print('We have logged in as {0.user}'.format(client))

#*****************************************************#
#                 Message Processing:                 #
#     Channel and Private messages processed here     #
#                      Process:                       #
#     - Count every message                           #
#     - Don't process the bot's own message           #
#     - Tell DM senders DM's aren't supported         #
#     - Process ping/pong checks                      #
#     - Check if the user is a BotManager             #
#     - Run message through bad word detector         #
#                       (if not a bot manager         #
#     - Then the message is processed                 #
#           - Requests: Require @IrieArmy role        #
#           - Commands: Require @BotManager role      #
#*****************************************************#
@client.event
async def on_message(message): # On every message
	global pb
	if message.author == client.user: # Cancel own message
		return

	if message.content.lower().startswith('ping'): # Simple test the bot is working
		print('ping?/pong! processed from {}'.format(message.author))
		await message.channel.send('pong!')

	if str(message.channel.type) == 'private':
		member = guild.get_member(message.author.id)
		channel = member
		print('DM from: {}'.format(member))
		print('Message: {}'.format(message.clean_content))
	else:
		member = message.author
		channel = message.channel

	if not message.content.startswith("```") and message.content.find(';') != -1:
		formatted_msg = "```cpp\n {} \n```".format(message.content)
		await message.channel.send('{} here\'s your formatted code'.format(message.author.mention))
		await message.channel.send(formatted_msg)
		

	if message.content.startswith('{}kill'.format(COMMAND_PREFIX)):
		os.system('kill 1')
		return

client.run(DISCORD_TOKEN)