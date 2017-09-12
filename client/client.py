from client.irc import IRC
import configparser as ConfigParser
import string, os, sys
# TODO Add a config and read it from here
ip = 'none'
port = 0000
ssl = 'none'
nick = 'none'
def ReadConf():
	config = ConfigParser.ConfigParser()
	config.read("irc.conf")
	ip = config.get('Server', 'ip')
	port = config.getint('Server', 'port')
	ssl = config.get('Server', 'ssl')
	nick = config.get('User', 'nick')
def GenExampleConf():
	config = ConfigParser.RawConfigParser()
	config.add_section('Server')
	config.add_section('User')
	config.set('Server', 'ip', 'localhost')
	config.set('Server', 'port', '6667')
	config.set('Server', 'ssl', 'False')
	config.set('User', 'nick', "ExampleUser")
	with open('irc.conf', 'w') as configfile: 
		config.write(configfile)
	print("Created a template config file!")
def init():
	if os.path.isfile('irc.conf'):
		print("Config found!")
		ReadConf()
	else:
		print("Config not found!")
		GenExampleConf()
		sys.exit(1)
	IRC.Connect(ip, port, ssl, nick)
