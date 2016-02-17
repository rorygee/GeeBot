import config
import socket
import time
import re

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

def chat(sock, msg):
	sock.send("PRIVMSG #{} :{}".format(config.CHAN, msg))
def ban(sock, user):
	chat(sock, ".ban {}".format(user))
def timeout(sock, user, secs=60):
	chat(sock, ".timeout {}".format(user, secs))

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

def active_loop():
	while connected:
		response = s.recv(1024).decode("utf-8")
		if response == "PING :tmi.twitch.tv\r\n":
			s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
			print("Pong")
		else:
			username = re.search(r"\w+", line).group(0)  # Return the entire match
			message = CHAT_MSG.sub("", line)
			print(username + ": " + message)
			time.sleep(1 / config.RATE)