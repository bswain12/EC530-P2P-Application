from communicator import Communicator

# Chat color variables
TITLE_FG = '\033[96m'
CHR_RST = '\033[0m'
USER_FG = '\033[34m'
OTHER_FG = '\033[32m'


class Client:
    def __init__(self, ip='localhost', port=6000, debug=False):
        self.comm = Communicator(ip, port, debug)
        self.running = True
        self.debug = debug
        self.comm.discover()
        self.messages = []

    def prompt(self):
        self.clear()
        prompt_message = f'''\
{TITLE_FG}What would you like to do? {CHR_RST}
SHORTCUT    |   COMMAND             |   RESULT
[o]         |   online              |   - See online friends
[m] [user]  |   message [username]  |   - Message a friend
[q]         |   quit                |   - Quit the app
[h]         |   help                |   - Print help results
    > '''
        query = input(prompt_message)
        query = query.lower()
        self.clear()
        if not query:
            return  # do nothing if query is empty
        if query == 'online' or query == 'o':
            users = self.comm.get_online()
            print(f"{TITLE_FG}ONLINE USERS{CHR_RST}:")
            for user in users:
                print(f'    - {user[0]}')
            input("Press return to continue:")
        elif 'message' in query or query.split()[0] == 'm':
            words = query.split()
            if len(words) < 2:
                print("No user inputted")
                input("Press return to continue:")
                return
            username = query.split()[1]
            address = self.comm.get_address(username)
            if not address:
                print("User not found")
                input("Press return to continue:")
                return
            self.chat(username, address)
        elif 'quit' in query or query == 'q':
            self.__del__()
        elif 'help' in query or query == 'h':
            print("The command 'o' will return all of the users who are currently online.\n"
                  "The command 'm [username]' will send a message to the specified user.\n"
                  "The command 'q' will quit the application.\n"
                  "The command 'h' or 'help' will display this help message.")
            input("Press return to continue:")
        else:
            print("Command not found. Try again.")
            input("Press return to continue:")

    def chat(self, username, address: tuple):
        while True:
            self.clear()
            self.load_chat(username)
            chat_prompt = f'''\
==== Chatting with {OTHER_FG}{username.upper()}{CHR_RST} ====
Send a message or 'q' to exit the chat
    > '''
            message = input(chat_prompt)
            if message == 'q':
                self.clear()
                return
            self.comm.send_message(message, address)
            self.messages.append(message)

    def load_chat(self, username):
        # TODO
        for message in self.messages:
            print(message)
        pass

    def clear(self):
        if not self.debug:
            print("\033c", end="")

    def __del__(self):
        self.running = False
        self.comm.exit()
