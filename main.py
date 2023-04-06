from communicator import Communicator
import time


HOST = 'localhost'
PORT = 6000


def main():
    comm = Communicator(HOST, PORT, True)
    while True:
        comm.send(str(input("Enter a message to send: ")), (HOST, PORT))
        time.sleep(2)