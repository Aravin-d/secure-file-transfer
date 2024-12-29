import socket
import ssl

#configuration
HOST = 'localhost'
PORT = 9999
CERTFILE =  '../cert/sever.crt'
KEYFILE = '../cert/sever.key'

#create socket and use ssl for encryption

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = ssl.wrap(
    server_socket,
    server_side=True,
    certfile=CERTFILE,
    keyfile=KEYFILE
)

#starting the server
secure_socket.bind((HOST, PORT))
secure_socket.listen(5)
print(f'Sever listening on {HOST}:{PORT}...')