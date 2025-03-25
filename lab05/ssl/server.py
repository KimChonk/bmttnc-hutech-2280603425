import socket
import ssl
import threading

server_address = ('localhost', 12345)
clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    print("Connected with", client_socket.getpeername())
    try:
        while True:  # Fixed 'true' to 'True'
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received data:", data.decode("utf-8"))
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
    except:
        clients.remove(client_socket)
    finally:
        print("Connection closed")
        client_socket.close()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server is listening...")
while True:
    client_socket, client_address = server_socket.accept()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile="C:/CODING/BMTT_NANG_CAO/bmttnc-hutech-2280603425/lab05/ssl/certificates/server-cert.crt", 
                            keyfile="C:/CODING/BMTT_NANG_CAO/bmttnc-hutech-2280603425/lab05/ssl/certificates/server-key.key")
    ssl_socket = context.wrap_socket(client_socket, server_side=True)
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()