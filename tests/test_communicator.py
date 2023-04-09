from communicator import Communicator # noqa


class Test_Communicator:

    comm = Communicator(
        host='localhost',
        port=8080,
        debug=True
    )

    def test_send_ping(self):
        comm = self.__class__.comm
        recipient = comm.host, comm.port

        comm.send_ping(recipient)
        comm.exit()

    def test_send_message(self):
        comm = self.__class__.comm
        recipient = comm.host, comm.port

        comm.send_message("Test message", recipient)
        comm.exit()
    
    def test_discover(self):
        comm = self.__class__.comm
        comm.discover()
        comm.exit()
