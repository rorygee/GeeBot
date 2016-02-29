import sqlite3
import os
import main
import conn_handle

if os.path.exists("Channel_Database.db"):
	conn = sqlite3.connect('Channel_Database.db')
	cur = conn.cursor()
else:
	conn = sqlite3.connect('Channel_Database.db')
	cur = conn.cursor()
	cur.executescript(
	"""
	CREATE TABLE channels
	(Channelname VARCHAR(25), Enabled BIT); 
	CREATE TABLE sessions
	(Username VARCHAR(25), ChannelName VARCHAR(25), Points INTEGER);
	""")

def add_channel(user):

		cur.execute("""INSERT INTO channels VALUES(?, 1)""", (user,))
		conn_handle.join_channel(user)
		main.chat("Hey, I'm here now 4Head", user)