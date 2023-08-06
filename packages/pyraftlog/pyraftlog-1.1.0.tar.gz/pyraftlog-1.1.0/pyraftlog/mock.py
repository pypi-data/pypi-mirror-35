import argparse
import logging
import os
import signal
import ssl
import sys

import pyraftlog
from pyraftlog.httpd import RaftHTTPServer
from pyraftlog.nodes import Node
from pyraftlog.storage import FileStorage
from pyraftlog.transports import SslSocketTransport

directory = os.path.dirname(__file__)
key_file = os.path.join(directory, 'certs/localhost.key')
crt_file = os.path.join(directory, 'certs/localhost.crt')
ca_file = os.path.join(directory, 'certs/ca.pem')


def mock_run():
    parser = argparse.ArgumentParser(description='Run a mock localhost pyraftlog server')
    parser.add_argument('-t', '--type', default="active", help='Type of the node',
                        choices=['active', 'reluctant', 'passive'])
    parser.add_argument('-n', '--node', required=True, help='(host:)?port of this node. e.g. 7001 or node:7001')
    parser.add_argument('-b', '--neighbours', required=True, nargs='+', help='Port(s) of neighbour')
    parser.add_argument('-c', '--command', default=7500, type=int, help='Port for receiving commands')
    parser.add_argument('-l', '--log-level', default="INFO", help='Logging level', choices=['DEBUG', 'INFO', 'WARNING'])
    parser.add_argument('-f', '--file', default=None, help='Storage filename')
    args = parser.parse_args()

    # Get the node name and neighbourhood
    node_name = args.node if ':' in args.node else ('localhost:' + str(args.node))
    node_host, node_port = node_name.split(':', 1)
    neighbourhood = [node_name]
    for neighbour in args.neighbours:
        neighbourhood.append(neighbour if ':' in neighbour else ('localhost:' + neighbour))

    # Create the logger
    log_level = logging.getLevelName(args.log_level)
    logging.basicConfig(stream=sys.stderr, level=log_level,
                        format='%(asctime)s [%(filename)-15s:%(lineno)-4s] %(levelname)-8s %(message)s')
    logger = logging.getLogger(node_name)

    # Create the storage
    storage = FileStorage(args.file or node_name + '.pickle')

    httpd = None
    if args.type == "active":
        node = Node(pyraftlog.NODE_MODE_ACTIVE, node_name, neighbourhood, storage,
                    election_timeout=5000, heartbeat_timeout=1000, vote_timeout=1500, logger=logger)
        node.request_address = 'https://%s:%d' % (node_host, args.command)

        httpd = RaftHTTPServer(('', args.command), pyraftlog.httpd.RaftHTTPLocalApplyRequestHandler)
        httpd.raft = node
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=key_file, certfile=crt_file,
                                       server_side=True, cert_reqs=ssl.CERT_NONE,
                                       ssl_version=ssl.PROTOCOL_TLSv1_2, ca_certs=ca_file,
                                       ciphers=SslSocketTransport.CIPHERS)
    elif args.type == "reluctant":
        node = Node(pyraftlog.NODE_MODE_RELUCTANT, node_name, neighbourhood, storage,
                    election_timeout=5000, heartbeat_timeout=1000, vote_timeout=1500, logger=logger)

    else:
        node = Node(pyraftlog.NODE_MODE_PASSIVE, node_name, neighbourhood, storage,
                    election_timeout=5000, heartbeat_timeout=1000, vote_timeout=1500, logger=logger)

    # Create and start the transport
    transport = SslSocketTransport(node_port, key_file, crt_file, ca_file, response_timeout=None, logger=logger)
    transport.activate(node)
    while True:
        if httpd:
            httpd.transport = transport
            httpd.handle_request()
        else:
            pass


def handle_signal(signum, frame):
    logging.getLogger().info('SIGINT received, stopping mock server...')
    sys.exit(signum)


def main():
    signal.signal(signal.SIGINT, handle_signal)
    mock_run()


if __name__ == '__main__':
    sys.exit(main())
