import pickle
from CheckServer import Server

servers = pickle.load(open("servers.pickle", "rb"))
print("Example to add server")

servername = input("enter server name")
port = int(input("Enter a port number as an integer"))
connection = input("Enter a connection type i.e ping/plain/ssl")
priority = input("Enter priority i.e high/low")

new_server = Server(servername, port, connection, priority)
servers.append(new_server)

pickle.dump(servers, open("servers.pickle", "wb"))