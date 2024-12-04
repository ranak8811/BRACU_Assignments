import socket

port = 5040
buffer = 16
format = 'utf-8'

hostname = socket.gethostname()
server_ip_addr=socket.gethostbyname(hostname)
client_ip_addr=socket.gethostbyname(hostname)

server_sock_addr = (server_ip_addr, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_sock_addr)

def send_encoded_message(msg):
    message = msg.encode(format)
    msg_len = len(message)
    send_len = str(msg_len).encode(format)
    send_len += b" "*(buffer - len(send_len))

    client.send(send_len)
    client.send(message)

    sent_from_server = client.recv(2024).decode(format)
    print("Sent from the server: ", sent_from_server)

while True:
    inp = input("Enter something that needs to be sent to the server: ")
    send_encoded_message(inp)

    if inp == 'Terminate':
        break
