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
	chat("Commands to be implemented in the near future")