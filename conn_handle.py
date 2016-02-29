import config
import db_handle
import main
import socket
import time
import re
import os

if os.path.exists("Authorised_Channels.txt"):
	pass
else:
	channelFile = open("Authorised_Channels.txt","w+")
	channelFile.close()

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

def CAP_REQ():
	s.send(bytes('CAP REQ :twitch.tv/commands\n', 'UTF-8'))
	s.send(bytes('CAP REQ :twitch.tv/tags\n', 'UTF-8'))

def join_channel(channel):
	s.send("JOIN {}\r\n".format("#"+channel).encode("utf-8"))
	time.sleep(0.3) # Ensures that the bot joins within Twitch's limit (50 connections per 15 seconds)

def leave_channel(channel):
	s.send("PART {}\r\n".format("#"+channel).encode("utf-8"))

def add_channel(user):
	users = open('Authorised_Channels.txt', 'r').read()
	userExists = re.search(r"(\{0}\n)|(^{0}\n)".format(user), users)
	if userExists:
		main.chat("Come on, you can't adopt me again OpieOP", config.NICK)
	else:
		conn_handle.join_channel(user)
		main.chat("Hey, I'm here now 4Head", user)
		channelFile = open("Authorised_Channels.txt","a+")
		channelFile.write(user+"\n");
		channelFile.close()

def remove_channel(user):
	users = open('Authorised_Channels.txt', 'r').read()
	userExists = re.search(r"(\{0}\n)|(^{0}\n)".format(user), users)
	if userExists:
		channelFile = open("Authorised_Channels.txt","r")
		lines = channelFile.readlines()
		channelFile.close()
		channelFile = open("Authorised_Channels.txt","w")
		for line in lines:
			if line!=user+"\n":
				channelFile.write(line)
			channelFile.close()
		main.chat("I'm gone now BibleThump",config.NICK)
		conn_handle.leave_channel(user)
	else:
		main.chat("You can't remove me if I wasn't there to begin with 4Head", config.NICK)

try:
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
	CAP_REQ()
	join_channel(config.NICK)
	channelFile = open("Authorised_Channels.txt","r") # implement for loop for joining channels
	for line in channelFile:
		join_channel(line)
	connected = True # Socket is connected

except Exception as e:
	print(str(e))
	connected = False # Socket connection failed

def active_loop():
	while connected:
		response = s.recv(1024).decode("utf-8")
		if response == "PING :tmi.twitch.tv\r\n": # Detecting ping
			s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8")) # Sending pong
			print(config.NICK + ": Pong") # Showing pong in console
		elif "PRIVMSG" in response:
			reMessage = re.search(r"(PRIVMSG #(.*?) :(.*))", response)
			reName = str(re.search(r"(display-name=(.*?;))", response).group(2))
			user = reName[0:len(reName)-1].lower()
			message = reMessage.group(3)
			messageList = message.split()
			channel = reMessage.group(2)
			print(channel+";"+user+": "+message)
			if re.match(config.CMDP, message[0]): # Checks for specified command character
				main.valid_command(user, channel, messageList, response)
			time.sleep(1 / config.RATE)
		else:
			print(response)

active_loop()