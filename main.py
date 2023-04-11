from client import Client


def main():
    client = Client(debug=False)
    while client.running:
        client.prompt()


if __name__ == "__main__":
    main()
