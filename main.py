import config
import socket
import time
import re
import conn_handle
import command_list
import urllib.request
import urllib.error
import json

def chat(msg):
	conn_handle.s.send(bytes('PRIVMSG %s :%s\r\n' % ("#"+config.CHAN, msg), 'UTF-8'))

def ban(sock, user):
	chat(".ban {}".format(user))

def timeout(sock, user, secs=60):
	chat(".timeout {}".format(user, secs))

def valid_command(user, message):
	command = re.search("(?<=\{0})\w+".format(config.CMDP), message)
	if command:
		command_list.perform_command(user, message, command)
	else:
		chat("Put in a command dummy KappaGee")