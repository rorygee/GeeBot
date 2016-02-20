import config
import time
import re
import conn_handle
import command_list
import main

def points_command(user, messageList,response):
	if len(messageList) > 1:
		if messageList[1] == "send":
			main.chat("Send points pls")
		elif messageList[1] == "add":
			isMod = re.search(r"(mod=)(.*?);",response).group(2)
			if isMod == "1":
				main.chat("Points were added... somehow")
			else:
				main.chat("You don't have the permission to send points OpieOP")
		elif messageList[1] == "help":
			main.chat("Syntax: !points [send/add] [user] [amount]")
	else:
		main.chat(user+": 0 4Head")