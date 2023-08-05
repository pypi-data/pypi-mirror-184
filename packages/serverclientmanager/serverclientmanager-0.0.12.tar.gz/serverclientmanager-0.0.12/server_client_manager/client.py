import socket
from pathlib import Path
from json import load

from .data import Data


class Client:
    def __init__(self, host: str, port: int, password: str = None) -> None:
        self.password = password
        self.data = Data()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        if password is not None:
            self.authenticate()
        print("Connected")

    def authenticate(self):
        self.socket.send(self.password.encode())
        self.socket.recv(1)

    def send_file(self, path: Path | str):
        self.socket.send(self.data.SEND_FILE.encode())
        self.socket.recv(1)

        self.socket.close()
