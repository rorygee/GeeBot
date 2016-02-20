import config
import socket
import time
import re
import conn_handle
import urllib.request
import urllib.error
import json
import main
import points

modsOnline = ""

def retrieve_mods():
	try:
		j_obj = json.loads(urllib.request.urlopen('http://tmi.twitch.tv/group/user/'+config.CHAN+'/chatters', timeout = 15).read().decode('utf-8'))
		modsOnline = j_obj['chatters']['moderators']
		return(modsOnline)
	except urllib.error.URLError as e:
		print(e.reason)
		main.chat("Twitch messed up KappaGee")
		return

def perform_command(user, message, command, response):
	messageList = message.split()
	if messageList[0] == "!mods":
		modsOnline = retrieve_mods()
		if modsOnline is not None:
			print(modsOnline)
			if len(modsOnline) > 0:
				modList = ""
				for curMod in modsOnline:
					modList = modList+curMod+", "
				main.chat("Mods currently in chat: "+modList[0:(len(modList)-2)])
			else:
				main.chat("mods are offline, post FrankerZ")
	elif messageList[0] == "!points":
		points.points_command(user, messageList, response)
	else:
		main.chat("'"+command.group(0)+"' is not a valid command GeeFaceNoSpace")