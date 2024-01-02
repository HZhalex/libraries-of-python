import socket
import threading
IP = socket.gethostbyname(socket.gethostname())
PORT = 9998
def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP, PORT)) 
    server.listen() 
    print(f'[*] Listening on {IP}:{PORT}')
    while True:
        client, address = server.accept() 
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler =threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        server.close() 
        break
def handle_client(client_socket): 
    with client_socket :
        request = client_socket.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        client_socket.send(b'ACK')
if __name__ == '__main__':
    main()