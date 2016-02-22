import config
import socket
import time
import re
import main

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

try:
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8")) #Bot channel connect, replace with for loop with list
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8")) #Bot host connect
	main.CAP_REQ()
	s.send("JOIN {}\r\n".format("#"+config.CHAN).encode("utf-8"))
	s.send("JOIN {}\r\n".format("#"+config.NICK).encode("utf-8"))
	main.chat("I'm here 4Head")
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
		elif "PRIVMSG" in response:
			print(response)
			reMessage = re.search(r"(PRIVMSG #(.*?) :(.*))", response)
			reName = str(re.search(r"(display-name=(.*?;))", response).group(0))
			username = reName[0:len(reName)-1]
			message = reMessage.group(3)
			channel = reMessage.group(2)
			print(username+": "+message)
			if re.match(config.CMDP, message[0]): # Checks for specified command character
				main.valid_command(username, message,response)
			time.sleep(1 / config.RATE)
		else:
			print(response)

active_loop()