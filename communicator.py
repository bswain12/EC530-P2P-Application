import socket
import threading
import time


class Communicator:

    def __init__(self, host: str, port: int, debug=False):
        self.host = host
        self.port = port
        self.debug = debug
        self.exit_flag = False
        self.send_buf = []

        self.init_udp()
        try:
            self.init_udp()
        except socket.error:
            print("ERROR: Couldn't start UDP communications")
            self.__del__()
            raise socket.error

        self.listener_thread = threading.Thread(
            target=self.listener,
            args=[self.exit_flag]
        )
        self.listener_thread.start()

        self.sender_thread = threading.Thread(
            target=self.sender,
            args=[self.exit_flag]
        )
        self.sender_thread.start()

    def init_udp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.sock.bind((self.host, self.port))
        except socket.error:
            raise socket.error

    def listener(self, exit_flag: bool):
        if self.debug:
            print("Listener started.")
        while True:
            if exit_flag:
                break
            data, addr = self.sock.recvfrom(1024)
            if self.debug:
                print(f'Recieved: {data.decode()} from {addr}')
            time.sleep(1)

    def sender(self, exit_flag: bool):
        while True:
            if exit_flag:
                break
            for message in self.send_buf:
                data, target = message
                self.sock.sendto(data.encode(), target)
                if self.debug:
                    print(f'Sent: \"{data}\" to {target[0]}')
                self.send_buf.remove(message)
            time.sleep(1)

    def send(self, message: str, target: tuple):
        self.send_buf.append((message, target))

    def __del__(self):
        if self.debug:
            print("Cleaning up Communicator.")
        self.sender_thread.join()
        self.listener_thread.join()
        self.sock.close()


HOST = 'localhost'
PORT = 6000

comm = Communicator(HOST, PORT, True)
while True:
    comm.send(str(input("Enter a message to send: ")), (HOST, PORT))
    time.sleep(2)
