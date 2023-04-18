from client import Client
from sys import argv


def main():
    if len(argv) > 1:
        client = Client(
            ip=argv[1],
            port=int(argv[2]),
            debug=False
        )
    else:
        client = Client(debug=False)
    while client.running:
        try:
            client.prompt()
        except KeyboardInterrupt:
            client.clear()
            client.running = False


if __name__ == "__main__":
    main()
