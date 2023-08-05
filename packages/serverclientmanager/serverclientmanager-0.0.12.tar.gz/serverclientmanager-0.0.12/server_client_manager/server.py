from queue import Queue
from multiprocessing import Process
from threading import Thread
from socketserver import TCPServer, BaseRequestHandler
import socket

from .data import Data

from werkzeug.security import check_password_hash


queue_conns = Queue()
data = Data()


def authenticate(conn: socket.socket, password_hash: str):
    if check_password_hash(password_hash, conn.recv().decode()):
        conn.send(data.SYNC)
        queue_conns.put(conn)
    else:
        conn.close()


# 0: multiprocessing
# 1: multithreading
# 2: none
def serve_client(handling_state: int) -> None:
    assert 0 <= handling_state <= 2
    assert type(handling_state).__name__ == "int"
    while True:
        conn = queue_conns.get()
        if handling_state == 0:
            Process(target=_serve_client, daemon=True, args=[conn]).start()
        elif handling_state == 1:
            Thread(target=_serve_client, daemon=True, args=[conn]).start()
        else:
            _serve_client(conn)


def _serve_client(conn: socket.socket) -> None:
    request = conn.recv().decode()
    conn.send(data.SYNC)
    print(f"Got request: {request}")
    if request == data.SEND_FILE:
        print("SEND FILE")
    else:
        pass


class Server:
    def __init__(self, host: str, port: int, password_hash: str = None) -> None:
        self.password_hash = password_hash
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

    def run(self) -> None:
        self.socket.listen()
        while True:
            conn, addr = self.socket.accept()
            print(f"Connected: {addr}")
            if self.password_hash is None:
                print("PUT IN QUEUE")
                queue_conns.put(conn)
            else:
                thread = Thread(target=authenticate, args=[conn, self.password_hash])
                thread.run()
