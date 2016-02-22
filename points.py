import config
import re
import conn_handle
import command_list
import main

def points_command(user, channel, messageList,response):
	if len(messageList) > 1:
		if messageList[1] == "send":
			main.chat("Send points pls", channel)
		elif messageList[1] == "add":
			isMod = re.search(r"(mod=)(.*?);",response).group(2)
			if isMod == "1":
				main.chat("Points were added... somehow", channel)
			else:
				main.chat("You don't have the permission to send points OpieOP", channel)
		elif messageList[1] == "help":
			main.chat("Syntax: !points [send/add] [user] [amount]", channel)
	else:
		main.chat(user+": 0 4Head", channel)