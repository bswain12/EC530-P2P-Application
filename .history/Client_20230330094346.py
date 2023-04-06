import socket
import os
import sys


class p2p_client:
    def __init__(self, port):
        self.ip = assign_ip(self)
        self.port = port
        

    def assign_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        #print(s.getsockname()[0])
        s_return = s.getsockname()[0]
        s.close()
        return s_return
    



# Main funtion where I can run the client and thread functions etc.
def main():
    print("HI")


if __name__ == "__main__":
    main()