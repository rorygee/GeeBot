import config
import socket
import time
import re
import main
import os

if os.path.exists("Authorised_Channels.txt"):
	pass
else:
	channelFile = open("Authorised_Channels.txt","w+")
	channelFile.close()

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

try:
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8")) #Bot channel connect, replace with for loop with list
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8")) #Bot host connect
	main.CAP_REQ()
	s.send("JOIN {}\r\n".format("#"+config.NICK).encode("utf-8"))
	channelFile = open("Authorised_Channels.txt","r")# implement for loop for joining channels
	for line in channelFile:
		s.send("JOIN {}\r\n".format("#"+line).encode("utf-8"))
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
			reName = str(re.search(r"(display-name=(.*?;))", response).group(2))
			user = reName[0:len(reName)-1].lower()
			message = reMessage.group(3)
			messageList = message.split()
			channel = reMessage.group(2)
			print(user+": "+message)
			if re.match(config.CMDP, message[0]): # Checks for specified command character
				main.valid_command(user, channel, messageList, response)
			time.sleep(1 / config.RATE)
		else:
			print(response)

active_loop()