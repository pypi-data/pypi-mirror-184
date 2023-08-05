from socket import socket
from pathlib import Path

from .data import Data


data = Data()


def close_connection(socket: socket) -> None:
    socket.send(data.CLOSE_CONNECTION)
    socket.recv(data.SYNC_LENGTH)
    socket.close()


def send_authentication(socket: socket, password=str) -> None:
    socket.send(data.SEND_AUTHENTICATION.encode())
    socket.recv(data.SYNC_LENGTH)
    socket.send(password.encode())
    socket.recv(data.SYNC_LENGTH)


def recv_authentication(socket: socket) -> str:
    password = socket.recv()
    socket.send(data.SYNC)
    return password


def send_file(socket: socket, path: Path) -> None:
    socket.send(data.SEND_FILE)
    socket.recv(data.SYNC_LENGTH)
    socket.send(str(path).encode())
    socket.recv(data.SYNC_LENGTH)
    socket.send(path.stat().st_size)
    socket.recv(data.SYNC_LENGTH)
    with open(path, "rb") as f:
        for _ in range(0, path.stat().st_size, data.BUFFER_SIZE):
            socket.send(f.read(data.BUFFER_SIZE))
            socket.recv(data.SYNC_LENGTH)
    socket.recv(data.SYNC_LENGTH)


def recv_file(socket: socket) -> None:
    path = socket.recv()
    socket.send(data.SYNC_LENGTH)
    size = socket.recv()
    socket.send(data.SYNC_LENGTH)
    with open(path, "wb") as f:
        for _ in range(0, size, data.BUFFER_SIZE):
            f.write(socket.recv())
            socket.send(data.SYNC)


# def handle_request(
#     socket: socket,
#     need_authorization: bool = True,
#     pre_handle: function = empty,
#     post_handle: function = empty,
# ):
#     authorized = False
#     while True:
#         request = socket.recv().encode()
#         socket.send(data.SYNC_LENGTH)
#         pre_handle(request)
#         if request == data.CLOSE_CONNECTION:
#             socket.close()
#         elif request == data.SEND_AUTHENTICATION:
#             recv_authentication(socket)
#         elif request == data.SEND_FILE:
#             recv_file(socket)
#         post_handle(request)
