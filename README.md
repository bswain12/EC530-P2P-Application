# EC530-P2P-Application

[Google doc describing architecture](https://docs.google.com/document/d/1kVgk00fAzenLcZiCFu41l1q4Ih7ZU_AyObCae7Ok-So/edit?usp=sharing)

This is a simple chat application built with Python and SQLite3. The application allows users to send and receive messages with other users who are connected to the same server.

## Requirements

* Python 3.x
* SQLite3

## Installation

* Clone the repository: git clone https://github.com/bswain12/EC530-P2P-Application.git
* Create a new SQLite3 database: python3 database.py

# Usage

* To start the code as a User, run the following command: python3 main.py
This will start the Client and listen for incoming connections on port 6000.


python main.py <server_ip_address> <server_port>
This will start the client and connect to the specified server. If no server IP address or port is provided, the client will connect to the local server running on port 6000.

Once the client is running, you will be prompted to enter commands. You can send a message to another user by entering the send command and following the prompts. You can view your messages by entering the message command. You can view who is online by entering the online command. You can exit the application by entering the quit command.

Help
To view a list of available commands, enter the help command.

License
This project is licensed under the MIT License. See the LICENSE file for details.