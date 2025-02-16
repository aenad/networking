import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
    S.connect((HOST, PORT))

    S.sendall(b"hello, world")
    data = S.recv(1024)


print(f"Received {data}")