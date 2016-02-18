import config
import socket
import time
import re
import conn_handle

def chat(msg):
	conn_handle.s.send(bytes('PRIVMSG %s :%s\r\n' % (config.CHAN, msg), 'UTF-8'))

def ban(sock, user):
	chat(".ban {}".format(user))

def timeout(sock, user, secs=60):
	chat(".timeout {}".format(user, secs))

def check_command(user, message):
	command = re.search("(?<=\{0})\w+".format(config.CMDP), message)
	if command:
		chat("'"+command.group(0)+"' is not a valid command GeeFaceNoSpace")
	else:
		chat("Put in a command dummy KappaGee")