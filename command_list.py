import config
import re
import conn_handle
import db_handle
import urllib.request
import urllib.error
import json
import main

def points_add(user, channel, messageList, response):
	isMod = re.search(r"(mod=)(.*?);",response).group(2) # grabs for mod status from raw message
	if isMod == "1":
		main.chat("Points were added... somehow", channel)
	else:
		main.chat("You don't have the permission to send points OpieOP", channel)

def points_remove(user, channel, messageList, response):
	isMod = re.search(r"(mod=)(.*?);",response).group(2) # grabs for mod status from raw message
	if isMod == "1":
		main.chat("Points were removed... somehow", channel)
	else:
		main.chat("You don't have the permission to remove points OpieOP", channel)

def points_send(user, channel, messageList):
	main.chat("Send points pls", channel)

def points_help():
	main.chat("Syntax: !points [send/add] [user] [amount]", channel)

def retrieve_mods(channel):
	try:
		j_obj = json.loads(urllib.request.urlopen('http://tmi.twitch.tv/group/user/'+channel+'/chatters', timeout = 15).read().decode('utf-8'))
		modsOnline = j_obj['chatters']['moderators']
		if modsOnline is not None:
			print(modsOnline)
			if len(modsOnline) > 0:
				modList = ""
				for curMod in modsOnline:
					modList = modList+curMod+", "
				main.chat("Mods currently in chat: "+modList[0:(len(modList)-2)], channel)
			else:
				main.chat("mods are offline, post FrankerZ", channel)
	except urllib.error.URLError as e:
		print(e.reason)
		main.chat("Twitch messed up KappaGee", channel)
		return

def points_command(user, channel, messageList, response):
	if len(messageList) > 1:
		if messageList[1] == "send":
			points_send(user, channel, messageList)
		elif messageList[1] == "add":
			points_add(user, channel, messageList, response)
		elif messageList[1] == "remove":
			points_remove(user, channel, messageList, response)
		elif messageList[1] == "help":
			points_help()
	else:
		main.chat(user+": 0 4Head", channel)

def perform_command(user, channel, messageList, response):
	if messageList[0] == "!mods":
		retrieve_mods(channel)
	elif messageList[0] == "!points":
		points_command(user, channel, messageList, response)
	elif messageList[0] == "!adopt" and channel == config.NICK:
		db_handle.add_channel(user)
	elif messageList[0] == "!abandon" and channel == config.NICK:
		conn_handle.remove_channel(user)
	else:
		main.chat("'"+messageList[0][1:len(messageList[0])]+"' is not a valid command GeeFaceNoSpace", channel)