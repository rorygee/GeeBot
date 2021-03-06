import config
import re
import conn_handle
import command_list
import time

'''
def cooldown(lastTime):
	thisTime = int(round(time.time() * 1000))
	if lastTime > thisTime:
		time.sleep(1) # need to work out calculation for this
'''
def chat(msg, channel):
	conn_handle.s.send(bytes('PRIVMSG %s :%s\r\n' % ("#"+channel, msg), 'UTF-8'))

def ban(user, channel):
	chat(".ban {}".format(user),channel)

def timeout(user, channel, secs=60):
	chat(".timeout {}".format(user, secs),channel)

def valid_command(user, channel, messageList, response):
	command = re.search("(?<=\{0})\w+".format(config.CMDP), messageList[0])
	if command:
		command_list.perform_command(user, channel, messageList, response)
	else:
		chat("Blank is not a valid command", channel)