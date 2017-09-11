import socket as so;
from client.irc import IRC
class IRC():
# TODO Add connection loop
    def Connect(ip, port, ssl, nick):
        if ssl:
            import ssl
            c = ssl.create_default_context()
            s = c.wrap_socket(so.socket(so.AF_INET), server_hostname=ip)
        else:
            s = so.socket()
        s.connect((ip, port))
        IRC.send("NICK " + nick)
        IRC.send("USER " + nick + " 0 * :" + nick)
        IRC.send("CAP LS")
    def send(msg):
        print(msg)
        IRC.s.sendall((msg + "\r\n").encode())
    def msg(msg, rec):
        IRC.send("PRIVMSG " + rec + " :" + msg)