import config
import socket
import time
import re
import conn_handle
import urllib.request
import urllib.error
import json
import main

def perform_command(user, message, command):
	if command.group(0) == "mods":
		try:
			j_obj = json.loads(urllib.request.urlopen('http://tmi.twitch.tv/group/user/rory_gee/chatters', timeout = 15).read().decode('utf-8'))
			modsOnline = j_obj['chatters']['moderators']
			modList = ""
			for curMod in modsOnline:
				modList = modList+curMod+", "
			main.chat("Mods currently in chat: "+modList[0:(len(modList)-2)])
		except urllib.error.URLError as e:
			print(e.reason)
			main.chat("Twitch messed up KappaGee") # !mods
	else:
		main.chat("'"+command.group(0)+"' is not a valid command GeeFaceNoSpace")
