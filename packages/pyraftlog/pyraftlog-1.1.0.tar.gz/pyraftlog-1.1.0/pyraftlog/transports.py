import logging
import socket
import ssl
import struct
import threading
import time

from messages import Message
from states import Follower


class Transport(object):
    def __init__(self):
        self.connected = {}
        self.responded = {}

    """
    Transport classes MUST listen to the node's message board and publish any new message ASAP. They must also
    listen to incoming messages from neighbours and call `node.on_message` when a new message is received.
    """
    def activate(self, node):
        """
        :param pyraftlog.nodes.Node node:
        """
        raise NotImplementedError()


class SocketTransport(Transport):
    def __init__(self, port, response_timeout=100, logger=None):
        super(SocketTransport, self).__init__()
        self.port = port
        self.response_timeout = response_timeout
        self.logger = logger or logging.getLogger(__name__)

        self.node = None

    def activate(self, node):
        self.node = node

        # Start separate publishing threads for each client
        for neighbour in self.node.neighbours:
            self.connected[neighbour] = False
            self.responded[neighbour] = 0
            thread = threading.Thread(target=self.publish, args=[neighbour])
            thread.daemon = True
            thread.start()

        # Start a single subscription thread
        thread = threading.Thread(target=self.subscribe)
        thread.daemon = True
        thread.start()

    def _socket(self, server_hostname=None):
        """ Get an instance of socket. """
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @staticmethod
    def _set_sock_options(sock):
        """ Set socket options. """
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.setsockopt(socket.IPPROTO_TCP, socket.SO_KEEPALIVE, 3)
        sock.settimeout(None)

    def _node_receive(self, sock):
        """
        Receive a message from another node. We first expect the message length, then the message itself.
        :param socket.socket sock:
        :return: Message from another node
        :rtype: str
        """
        data = b''
        try:
            sock.settimeout(self.response_timeout)
            # Get the message length
            bs = sock.recv(8)
            if len(bs) > 0:
                (length,) = struct.unpack('>Q', bs)
                # Read data in chunks
                while len(data) < length:
                    to_read = length - len(data)
                    data += sock.recv(1024 if to_read > 1024 else to_read)

        finally:
            sock.settimeout(None)

        return data

    def _node_send(self, sock, data):
        """
        Send a message to another node. We first send the message length, then the message itself.
        :param socket.socket sock: Socket to send the data through
        :param str data: Data to be sent
        :return:
        """
        try:
            sock.settimeout(self.response_timeout)
            length = struct.pack('>Q', len(data))

            sock.sendall(length)
            sock.sendall(data)

        finally:
            sock.settimeout(None)

    def publish(self, recipient):
        """
        Establish a keep-alive connection to the recipient, then wait for new messages to arrive and send them.
        Continually try to reconnect to the recipient node.
        """
        while True:
            self.connected[recipient] = False
            # Only try to connect if not a follower
            if type(self.node.state) == Follower:
                continue

            # Attempt to open a keep alive connection to the recipient
            sock = None
            try:
                host, port = recipient.split(":")
                sock = self._socket(host)
                self._set_sock_options(sock)
                sock.connect((host, int(port)))
                self.logger.info("[%s] Established connection" % recipient)
                self.connected[recipient] = True

                # Check for new messages and send if available
                while type(self.node.state) != Follower:
                    # Wait for messages on the board
                    if self.node.message_board.empty(recipient):
                        continue

                    # Get and send the message
                    message = self.node.message_board.get(recipient)
                    self._node_send(sock, message.serialise())
                    self.logger.debug("-> %s" % str(message))

                    # Wait and handle response
                    response = Message.unserialise(self._node_receive(sock))
                    self.responded[recipient] = time.time()
                    self.logger.debug("<- %s" % str(response))
                    message = self.node.on_message(response)
                    if message:
                        self.node.message_board.put(message)

                self.logger.info("[%s] Closing connection" % recipient)

            except socket.error:
                pass
            except ValueError as e:
                self.logger.critical("[%s][%s] %s" % (recipient, type(e), e))
                return
            except Exception as e:
                self.logger.critical("[%s][%s] %s" % (recipient, type(e), e))
            finally:
                if sock:
                    sock.close()

    def subscribe(self):
        """
        Listen for incoming connections and converse with them.
        """
        sock = None
        try:
            sock = self._socket()
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            sock.bind(('0.0.0.0', int(self.port)))
            sock.listen(len(self.node.neighbours))
            while True:
                try:
                    client_sock, address = sock.accept()
                    self._set_sock_options(client_sock)
                    self.logger.debug("Accepted connection (%s:%d)" % (address[0], address[1]))

                    # Move the conversation to a new thread
                    thread = threading.Thread(target=self.converse, args=[client_sock])
                    thread.daemon = True
                    thread.start()

                except Exception as e:
                    self.logger.critical("[%s] %s" % (type(e), e))
                    pass
        except ValueError as e:
            self.logger.critical("[%s] %s" % (type(e), e))
            return
        finally:
            self.logger.critical("Stopped subscribing")
            if sock:
                sock.close()

    def converse(self, client_sock):
        """
        Given a open connection `client_sock` receive messages and send appropriate responses.
        :param client_sock:
        """
        try:
            while True:
                message = self._node_receive(client_sock)
                if not message:
                    break
                response = self.node.on_message(Message.unserialise(message))
                if not response:
                    break

                self._node_send(client_sock, response.serialise())
        finally:
            client_sock.close()


class SslSocketTransport(SocketTransport):
    CIPHERS = 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH'

    def __init__(self, port, key_file, cert_file, ca_cert, response_timeout=100, ciphers=None, logger=None):
        super(SslSocketTransport, self).__init__(port, response_timeout, logger)
        self.node = None

        self.ciphers = ciphers or self.CIPHERS
        self.key_file = key_file
        self.cert_file = cert_file
        self.ca_cert = ca_cert

    def _socket(self, server_hostname=None):
        sock = super(SslSocketTransport, self)._socket()
        if server_hostname:
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=self.ca_cert)
        else:
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cafile=self.ca_cert)

        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3
        context.load_cert_chain(self.cert_file, self.key_file)
        context.verify_mode = ssl.CERT_REQUIRED

        if self.ciphers:
            context.set_ciphers(self.ciphers)

        if server_hostname:
            context.check_hostname = True
            sock = context.wrap_socket(sock, server_side=False, server_hostname=server_hostname)
        else:
            sock = context.wrap_socket(sock, server_side=True)

        return sock
