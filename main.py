from communicator import Communicator
import time


HOST = 'localhost'
PORT = 6000


def main():
    comm = Communicator(HOST, PORT, debug=True)
    comm.discover()
    time.sleep(4)
    comm.exit()


if __name__ == "__main__":
    main()
