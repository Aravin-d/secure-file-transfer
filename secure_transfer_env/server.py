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

#connecting client and receiving file
while True:
    client_socket, addr = secure_socket.accept()
    print(f'connected to {addr}')

    #Receiving file
    with open('received_file.txt', 'wb') as f:
        while True:
            data = client_socket.recv(1024) #Receive data in chunks of 1024 b
            if not data:
                break
            f.write(data)

    print("File received")
    client_socket.close()