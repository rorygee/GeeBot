import config
import socket
import time
import re
import main

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

try:
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
	s.send("JOIN {}\r\n".format("#"+config.CHAN).encode("utf-8"))
	connected = True	# Socket is connected

except Exception as e:
	print(str(e))
	connected = False	# Socket connection failed

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
			if re.match(config.CMDP, message[0]): # Checks for specified command character
				main.valid_command(username, message)
			time.sleep(1 / config.RATE)

active_loop()