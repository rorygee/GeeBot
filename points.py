import config
import socket
import time
import re
import conn_handle
import command_list
import urllib.request
import urllib.error
import json
import main

def points_command(user, messageList):
	if len(messageList) > 1:
		if messageList[1] == "send":
			main.chat("Send points pls")
		elif messageList[1] == "add":
			modsOnline = command_list.retrieve_mods()
			if modsOnline is not None:
				if user in modsOnline: # Sufficient permissions
					main.chat("Points were added... somehow")
				else:
					main.chat("You don't have the permission to send points OpieOP")
		elif messageList[1] == "help":
			main.chat("Syntax: !points [send] [user] [amount]")
	else:
		main.chat(user+": 0 4Head")