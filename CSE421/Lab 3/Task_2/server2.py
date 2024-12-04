import socket

port = 5050
buffer = 16
format = 'utf-8'

hostname = socket.gethostname()
server_ip_addr = socket.gethostbyname(hostname)

server_sock_addr = (server_ip_addr, port)
print("Server's socket address is: ", server_sock_addr)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_sock_addr)

server.listen()
print("I am listening to requests...")

while True:
    conn, client_sock_addr = server.accept()
    print("Connected to client: ", client_sock_addr)

    connected = True
    while connected:
        next_msg_len = conn.recv(16).decode(format)
        print("Upcoming message length is: ", next_msg_len)

        if next_msg_len:
            message = conn.recv(int(next_msg_len)).decode(format)
            print('Sent from the client: ', message)

            if message == "Terminate":
                print("Terminating connection with: ", client_sock_addr)
                conn.send('Connection terminated as you have wished'.encode(format))
                connected = False
            else:
                count = 0
                for ch in message:
                    if ch in "aeiouAEIOU":
                        count += 1
                conn.send(f"The message you sent has {count} numbers of vowels in it".encode(format))

                
    conn.close()