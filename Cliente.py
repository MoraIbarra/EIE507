import socket

HEADER = 64
PORT = 3074
SERVER = '169.254.116.33'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) + 97)
        encrypted_message += encrypted_char
    return encrypted_message.encode(FORMAT)

def send(msg):
    encrypted_message = encrypt_message(msg)
    message_length = len(encrypted_message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(encrypted_message)
    print(client.recv(2048).decode(FORMAT))

while True:
    message = input("Enter a message (or 'quit' to exit): ")
    if message == 'quit':
        break
    send(message)

send(DISCONNECT_MESSAGE)
