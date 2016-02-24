import config
import re
import conn_handle
import command_list
import main

def points_add_command(user, channel, messageList, response):
	isMod = re.search(r"(mod=)(.*?);",response).group(2)
	if isMod == "1":
		main.chat("Points were added... somehow", channel)
	else:
		main.chat("You don't have the permission to send points OpieOP", channel)

def points_remove_command(user, channel, messageList, response):
	isMod = re.search(r"(mod=)(.*?);",response).group(2)
	if isMod == "1":
		main.chat("Points were removed... somehow", channel)
	else:
		main.chat("You don't have the permission to remove points OpieOP", channel)

def points_send_command(user, channel, messageList):
	main.chat("Send points pls", channel)

def points_help_command():
	main.chat("Syntax: !points [send/add] [user] [amount]", channel)

def points_command(user, channel, messageList, response):
	if len(messageList) > 1:
		if messageList[1] == "send":
			points_send_command(user, channel, messageList)
		elif messageList[1] == "add":
			points_add_command(user, channel, messageList, response)
		elif messageList[1] == "remove":
			points_remove_command(user, channel, messageList, response)
		elif messageList[1] == "help":
			points_help_command()
	else:
		main.chat(user+": 0 4Head", channel)