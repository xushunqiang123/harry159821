from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import socket

def main():
    # ip = socket.gethostbyname(socket.gethostname())

    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user("admin", "123456", ".", perm="elradfmwM")
    authorizer.add_anonymous(".", perm="elradfmwM")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    # handler.banner = "pyftpdlib based ftpd ready."
    handler.permit_foreign_addresses = True

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    server = FTPServer(("0.0.0.0", 8443), handler)
    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
