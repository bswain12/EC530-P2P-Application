from communicator import Communicator
import time


HOST = 'localhost'
PORT = 6000


def main():
    comm = Communicator(HOST, PORT, debug=True)
    for i in range(5):
        time.sleep(2)
        comm.send_ping((HOST, PORT))
        comm.send_recieved(f'Message #{i}', (HOST, PORT))
    comm.exit()


if __name__ == "__main__":
    main()
