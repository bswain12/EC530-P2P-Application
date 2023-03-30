import socket
import threading
import time


HOST = 'localhost'
PORT = int(input("Enter port number: "))
PORT_TO = int(input("Enter port number: "))

addresses = []

""" init_udp: initialize udp network communication
    @return socket and status
"""


def init_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    return sock, 0


""" listener: function for listening thread
    @param sock - socket to listen to
"""


def listener(sock):
    print("Listener started.")
    while True:
        data, addr = sock.recvfrom(1024)
        print(f'Recieved: {data.decode()} from {addr}')

        if addr not in addresses:
            print(f'{addr} added to addresses.')
            addresses.append(addr)
        time.sleep(1)


""" sender: function for sending thread
    @param sock - socket to send on
"""


def sender(sock):
    while True:
        data = "TEST_MESSAGE"
        sock.sendto(data.encode(), (HOST, PORT_TO))
        print(f'Sent: {data} to {HOST}')
        time.sleep(1)


def main():
    sock, status = init_udp()
    if status != 0:
        print("ERROR: Couldn't start UDP communications.")
        exit()

    # Start a listening thread
    listener_thread = threading.Thread(
        target = listener, 
        args = [sock]
    )
    listener_thread.start()

    # Start a sending thread
    sender_thread = threading.Thread(
        target = sender,
        args = [sock]
    )
    sender_thread.start()




if __name__ == "__main__":
    main()
