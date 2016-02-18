import config
import socket
import time
import re

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

try:
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
	s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))
	connected = True	# Socket is connected

except Exception as e:
	print(str(e))
	connected = False	# Socket connection failed

def chat(msg):
	s.send(bytes('PRIVMSG %s :%s\r\n' % (config.CHAN, msg), 'UTF-8'))

def ban(sock, user):
	chat(".ban {}".format(user))

def timeout(sock, user, secs=60):
	chat(".timeout {}".format(user, secs))

def active_loop():
	while connected:
		response = s.recv(1024).decode("utf-8")
		if response == "PING :tmi.twitch.tv\r\n":	# Detecting ping
			s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))	# Sending pong
			print(config.NICK + ": Pong")	# Showing pong in console
		else:
			username = re.search(r"\w+", response).group(0)
			message = CHAT_MSG.sub("", response)
			print(username + ": " + message)
			time.sleep(1 / config.RATE)

active_loop()