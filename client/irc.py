import socket as so;
class IRC():
# TODO Add connection loop
    class attributes():
        socket = so.socket()
    def Connect(ip, port, ssl_enabled, nick):
        if ssl_enabled == True:
            import ssl
            context = ssl.create_default_context()
            IRC.attributes.socket = context.wrap_socket(so.socket(so.AF_INET), server_hostname=ip)
        IRC.attributes.socket.connect((ip, port))
        IRC.send("NICK " + nick)
        IRC.send("USER " + nick + " 0 * :" + nick)
        IRC.send("CAP LS")
    def send(msg):
        print(msg)
        IRC.attributes.socket.sendall((msg + "\r\n").encode())
    def msg(msg, rec):
        IRC.send("PRIVMSG " + rec + " :" + msg)
