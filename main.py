import config
import socket
import time
import re
import conn_handle
import urllib.request
import urllib.error
import json

def chat(msg):
	conn_handle.s.send(bytes('PRIVMSG %s :%s\r\n' % (config.CHAN, msg), 'UTF-8'))

def ban(sock, user):
	chat(".ban {}".format(user))

def timeout(sock, user, secs=60):
	chat(".timeout {}".format(user, secs))

def valid_command(user, message):
	command = re.search("(?<=\{0})\w+".format(config.CMDP), message)
	if command:
		if command.group(0) == "mods":
			try:
				j_obj = json.loads(urllib.request.urlopen('http://tmi.twitch.tv/group/user/rory_gee/chatters', timeout = 15).read().decode('utf-8'))
				modsOnline = j_obj['chatters']['moderators']
				modList = ""
				for curMod in modsOnline:
					modList = modList+curMod+", "
				chat("Mods currently in chat: "+modList[0:(len(modList)-2)])
			except urllib.error.URLError as e:
				print(e.reason) 
		else:
			chat("'"+command.group(0)+"' is not a valid command GeeFaceNoSpace")
	else:
		chat("Put in a command dummy KappaGee")