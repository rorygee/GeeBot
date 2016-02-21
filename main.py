import config
import socket
import time
import re
import conn_handle
import command_list
import urllib.request
import urllib.error
import json

def CAP_REQ():
#	conn_handle.s.send(bytes('CAP REQ :twitch.tv/membership\n', 'UTF-8')) borks connection, will fix later
	conn_handle.s.send(bytes('CAP REQ :twitch.tv/commands\n', 'UTF-8'))
	conn_handle.s.send(bytes('CAP REQ :twitch.tv/tags\n', 'UTF-8'))

def chat(msg):
	conn_handle.s.send(bytes('PRIVMSG %s :%s\r\n' % ("#"+config.CHAN, msg), 'UTF-8'))

def ban(sock, user):
	chat(".ban {}".format(user))

def timeout(sock, user, secs=60):
	chat(".timeout {}".format(user, secs))

def valid_command(user, message, response):
	command = re.search("(?<=\{0})\w+".format(config.CMDP), message)
	if command:
		command_list.perform_command(user, message, command, response)
	else:
		chat("Put in a command dummy KappaGee")