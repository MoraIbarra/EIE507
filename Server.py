import socket
import threading

HEADER = 64
PORT = 3074
SERVER = '169.254.116.33'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            encrypted_msg = conn.recv(msg_length)
            decrypted_msg = decrypt_message(encrypted_msg)
            if decrypted_msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {decrypted_msg}")
            conn.send(encrypt_message(str(decrypted_msg)))

    conn.close()

def start():
    server.listen()
    print(f"[LISTEN] Server is listening on address {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) + 97)
        encrypted_message += encrypted_char
    return encrypted_message.encode(FORMAT)

def decrypt_message(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message.decode(FORMAT):
        decrypted_char = chr(ord(char) - 97)
        decrypted_message += decrypted_char
    return decrypted_message

print("[STARTING] server is running.....")
start()
