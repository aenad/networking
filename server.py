import socket
import threading
from celery import Celery

HOST = "127.0.0.1"
PORT = 65432
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        try:
            msg = conn.recv(SIZE).decode(FORMAT)
            if not msg:
                break
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            msg = f"Msg received: {msg}"
            conn.send(msg.encode(FORMAT))
        except ConnectionResetError:
            print(f"[ERROR] Connection reset by {addr}")
            break
    conn.close()


def main():
    print("[Starting] Server is starting...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

        while True:  # accept multiple connection
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[Active Connections] {threading.active_count()}")


if __name__ == "__main__":
    main()
