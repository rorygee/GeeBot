import config
import socket
import time
import re
import conn_handle
import command_list
import urllib.request
import urllib.error
import json

channel = config.CHAN

def CAP_REQ():
#	conn_handle.s.send(bytes('CAP REQ :twitch.tv/membership\n', 'UTF-8')) borks connection, will fix later
	conn_handle.s.send(bytes('CAP REQ :twitch.tv/commands\n', 'UTF-8'))
	conn_handle.s.send(bytes('CAP REQ :twitch.tv/tags\n', 'UTF-8'))

def chat(msg, channel):
	conn_handle.s.send(bytes('PRIVMSG %s :%s\r\n' % ("#"+channel, msg), 'UTF-8'))

def ban(user, channel):
	chat(".ban {}".format(user),channel)

def timeout(user, channel, secs=60):
	chat(".timeout {}".format(user, secs),channel)

def valid_command(user, channel, messageList, response):
	command = re.search("(?<=\{0})\w+".format(config.CMDP), messageList[0])
	if command:
		command_list.perform_command(user, channel, messageList, response)
	else:
		chat("Put in a command dummy KappaGee", channel)