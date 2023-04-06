import socket
import threading
import time
from uuid import uuid4
from datetime import datetime
import json


class Communicator:

    def __init__(self, host: str, port: int, debug=False):
        self.host = host
        self.port = port
        self.debug = debug
        self.exit_flag = False
        self.send_buf = []
        self.online_conns = []

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
            
            # Decode json data into a python dictionary 
            data = json.loads(data.decode())
            if self.debug:
                print(f'Recieved msg with type {data["type"]} and message {data["msg"]} from {addr}')
            # Do things based on message type
            if data["type"] == -1: # recieved a ping that that address is online
                self.online_conns.append(addr)
            elif data["type"] == 0: # recieved a message
                # call something to store the message
                print(f'New message: {data["msg"]}')
            elif data["type"] == 1: # recieved delivery confirmation
                # call something to remove that message from the sending buffer
                ##TODO 
                print("Message confirmations not implemented yet")
            else:
                raise ValueError("Unexpected message format")
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

    def send_ping(self, recipient_address):
        # Build an "I'm online" message and send it
        id = uuid4()
        timestamp = datetime.now()
        data = {"type": -1, "id": id.int, "timestamp": timestamp.isoformat('m'), "msg": None}
        json_data = json.dumps(data)
        self.sock.sendto(json_data.encode(), recipient_address)

    def send_message(self, message: str, recipient_address: tuple):
        # Build a message, add it to self.outgoing_buffer database 
        id = uuid4()
        timestamp = datetime.now()
        data = {"type": 0, "id": id.int, "timestamp": timestamp.isoformat('m'), "msg": message}
        json_data = json.dumps(data)
        self.send_buf.append((json_data, recipient_address))

    def send_recieved(self, message_id, recipient_address: tuple):
        # Build a packet that says that this client has recieved a message, send
        timestamp = datetime.now()
        data = {"type": 1, "id": message_id, "timestamp": timestamp.isoformat('m'), "msg": None}
        json_data = json.dumps(data)
        self.send_buf.append((json_data, recipient_address))

    def __del__(self):
        if self.debug:
            print("Cleaning up Communicator.")
        self.sender_thread.join()
        self.listener_thread.join()
        self.sock.close()


HOST = 'localhost'
PORT = 6000

comm = Communicator(HOST, PORT, debug=True)
while True:
    comm.send(str(input("Enter a message to send: ")), (HOST, PORT))
    time.sleep(2)
    comm.send_ping((HOST, PORT))
    comm.send_recieved("12039123114", (HOST, PORT))
