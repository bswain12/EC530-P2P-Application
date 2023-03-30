# Defines methods and class for client

import socket as s
import sys
import os


class p2p_client:
    def __init__(host = "127.0.0.1", port = 8000):
        self.host = host
        self.port = port
        self.connections = []
        self.socket = []

    def listening_thread():
        # Constantly listen for packets
        # When a handshake package is recieved, send back an "I'm online" message
        # When a message packet is recieved, send back a "recieved" message and handle chat message
        raise None

    def send_message():
        # Build a message object, add it to self.outgoing_buffer database
        # Try to send it to the recipient
        raise None

    def acknowledge_recieved():
        # Build a packet that says that this client has recieved a message, send
        raise None