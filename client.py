from communicator import Communicator


class Client:

    def __init__(self, ip='localhost', port=6000, debug=False):
        self.comm = Communicator(ip, port, debug)
        self.running = True
        self.debug = debug
        self.comm.discover()

    def prompt(self):
        self.clear()
        prompt_message = '''
        What would you like to do?
            COMMAND                                 RESULT
            "online | o"                            - See online friends
            "message / msg [username] [message]"    - Message a friend
            "quit | q"                              - Quit the app
        > '''
        query = input(prompt_message)
        query = query.lower()
        self.clear()

        if query == 'online' or query == 'o':
            users = self.comm.get_online()
            print("ONLINE USERS:")
            for user in users:
                print(f'    - {user[0]}')
            input("Press return to continue:")
        elif 'message' in query or 'msg' in query:
            username = query.split()[1]
            address = self.comm.get_address(username)
            message = ' '.join(query.split()[2:])
            self.comm.send_message(message, address)
            print(message)
            input("Press return to continue:")
        elif 'quit' in query or query == 'q':
            self.__del__()
        else:
            print("Command not found. Try again.")
            input("Press return to continue:")

    def clear(self):
        if not self.debug:
            print("\n" * 100)

    def __del__(self):
        self.running = False
        self.comm.exit()
