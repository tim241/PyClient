from client.irc import IRC

# TODO Add a config and read it from here

def init():
	IRC.Connect("irc.freenode.net", 6697, True, "TimsPyBot")