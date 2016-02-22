import config
import socket
import re
import conn_handle
import urllib.request
import urllib.error
import json
import main
import points

modsOnline = ""

def retrieve_mods(channel):
	try:
		j_obj = json.loads(urllib.request.urlopen('http://tmi.twitch.tv/group/user/'+channel+'/chatters', timeout = 15).read().decode('utf-8'))
		modsOnline = j_obj['chatters']['moderators']
		return(modsOnline)
	except urllib.error.URLError as e:
		print(e.reason)
		main.chat("Twitch messed up KappaGee", channel)
		return

def add_channel(user):
	channelFile = open("Authorised_Channels.txt","a+")
	if user in channelFile:
		main.chat("Come on, you can't adopt me again OpieOP", config.NICK)
	else:
		channelFile.write(user+"\n");
		#s.send("JOIN {}\r\n".format("#"+user).encode("utf-8"))
		main.chat("Thanks fam", user)
	channelFile.close()

def remove_channel(channel):
	main.chat("Bye fam", channel)

def perform_command(user, channel, message, command, response):
	messageList = message.split()
	if messageList[0] == "!mods":
		modsOnline = retrieve_mods(channel)
		if modsOnline is not None:
			print(modsOnline)
			if len(modsOnline) > 0:
				modList = ""
				for curMod in modsOnline:
					modList = modList+curMod+", "
				main.chat("Mods currently in chat: "+modList[0:(len(modList)-2)], channel)
			else:
				main.chat("mods are offline, post FrankerZ", channel)
	elif messageList[0] == "!points":
		points.points_command(user, channel, messageList, response)
	elif messageList[0] == "!adopt" and channel == config.NICK:
		add_channel(user)
	else:
		main.chat("'"+command.group(0)+"' is not a valid command GeeFaceNoSpace", channel)