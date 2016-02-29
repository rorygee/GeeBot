import sqlite3
import os

if os.path.exists("Channel_Database.db"):
	conn = sqlite3.connect('Channel_Database.db')
	cur = conn.cursor()
else:
	conn = sqlite3.connect('Channel_Database.db')
	cur = conn.cursor()
	cur.executescript(
	"""
	CREATE TABLE channels
	(channelName VARCHAR(25), Enabled BOOLEAN); 
	CREATE TABLE sessions
	(username VARCHAR(25), channelName VARCHAR(25), points INTEGER);
	""")