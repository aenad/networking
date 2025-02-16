import socket

HOST = "127.0.0.1"
PORT = 65432
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Client connected to server {HOST}:{PORT}")

        connected = True
        while connected:
            msg = input("> ")
            client.send(msg.encode(FORMAT))

            if msg == DISCONNECT_MSG:
                connected = False
            else:
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")


if __name__ == "__main__":
    main()
