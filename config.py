HOST = "irc.twitch.tv"              # Twitch IRC server address
PORT = 6667                         # Port number, for Twitch/IRC use 6667 ~ONLY~
NICK = "username"                   # Host Twitch username, lowercase
PASS = "oauth:xxxxxxxxxxxxxxxxxxxx" # Host Twitch OAuth token
CHAN = "#channel"                   # Connecting channel name
RATE = (100/30)                     # Rate at which messages can be sent, TwitchAPI's limit for mod is 100 every 30 seconds
CMDP = "!"                          # Single character prefix for commands