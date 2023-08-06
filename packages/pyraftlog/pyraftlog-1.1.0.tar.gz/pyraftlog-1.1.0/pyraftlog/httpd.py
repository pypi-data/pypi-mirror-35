import BaseHTTPServer
import SocketServer
import json
import time


class RaftHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    raft = None
    transport = None
    consensus_timeout = 3000.0


class RaftHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = 'RaftHTTP/1.0'
    sys_version = ''
    error_message_format = '{"code":%(code)d}'
    error_content_type = 'application/json'
    protocol_version = 'HTTP/1.1'

    def redirect_location(self):
        return self.server.raft.get_request_address() + self.path

    def _send_leader_redirect(self):
        self.send_response(307)
        self.send_header('Connection', 'Close')
        self.send_header('Location', self.redirect_location())
        self.end_headers()

    def _send_headers_and_response(self, code, response=None):
        self.send_response(code)
        self.send_header('Connection', 'Keep-Alive')
        self.send_header('Keep-Alive', 'timeout=5, max=100')
        if response is not None:
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', len(response))
        if self.server.raft.get_leader():
            self.send_header('Leader-Location', self.server.raft.get_request_address())
        self.end_headers()

        self.wfile.write(response)

    def do_HEAD(self):
        # If not leader redirect request
        if not self.server.raft.is_leader():
            self._send_leader_redirect()

        elif self.path == '/' or self.path == '':
            self.send_response(204)
            self.end_headers()

        else:
            self.send_error(404, 'Not found')

    def do_GET(self):
        raft = self.server.raft

        if self.path == '/' or self.path == '':
            neighbours = []
            for neighbour in raft.neighbours:
                neighbours.append({
                    "name": neighbour,
                    "connected": self.server.transport.connected[neighbour] if raft.is_leader() else None,
                    "responded": self.server.transport.responded[neighbour] if raft.is_leader() else None,
                })
            response = json.dumps({
                "term": raft.state.current_term,
                "committed": {
                    "term": raft.state.log.get(raft.state.commit_index).term,
                    "index": raft.state.log.get(raft.state.commit_index).index,
                },
                "leader": raft.get_leader(),
                "neighbours": neighbours,
                "request_address": raft.get_request_address(),
            })

            self._send_headers_and_response(200, response)

        elif self.path == '/log':
            response = json.dumps(raft.state.log.values(0, raft.state.last_applied))

            self._send_headers_and_response(200, response)

        else:
            self.send_error(404, 'Not found')


class RaftHTTPLocalApplyRequestHandler(RaftHTTPRequestHandler):
    def do_POST(self):
        raft = self.server.raft
        # If there isn't a leader
        if not raft.get_leader():
            self._send_headers_and_response(503, '')

        # If not leader redirect request
        elif not raft.is_leader():
            self._send_leader_redirect()

        elif self.path == '/log':
            # If not enough connected nodes to make a majority
            if not raft.has_majority(self.server.transport.connected.values().count(True) + 1):
                self._send_headers_and_response(503, '')
            # Validate request
            elif self.headers['Content-Type'] == 'application/json':
                # Read and parse request data
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                parsed_data = json.loads(post_data)

                # Attempt to write to log and wait for consensus
                raft.logger.debug("[%-9s] Command received: %s" % (raft.state.__class__.__name__, post_data))
                index = raft.state.append_log_entry(parsed_data)
                timeout = time.time() + (self.server.consensus_timeout / 1000.0)
                while raft.state.last_applied < index and timeout > time.time():
                    time.sleep(0.01)

                if raft.state.last_applied >= index:
                    raft.logger.debug("[%-9s] Command applied" % raft.state.__class__.__name__)
                    self._send_headers_and_response(201, '')
                else:
                    self._send_headers_and_response(500, '')

        else:
            self.send_error(404, 'Not found')


class RaftHTTPRemoteApplyRequestHandler(RaftHTTPRequestHandler):
    def do_PUT(self):
        """ PUT a new entry into the log. """
        raft = self.server.raft
        # If there isn't a leader
        if not raft.get_leader():
            self._send_headers_and_response(503, '')

        # If not leader redirect request
        elif not raft.is_leader():
            self._send_leader_redirect()

        # If not enough connected nodes to make a majority
        elif not raft.has_majority(self.server.transport.connected.values().count(True) + 1):
            self._send_headers_and_response(503, '')

        # Validate request
        elif self.headers['Content-Type'] == 'application/json':
            # Read and parse request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = json.loads(post_data)

            # Attempt to write to log and wait for consensus
            raft.logger.debug("[%-9s] Command received: %s" % (raft.state.__class__.__name__, post_data))
            index = raft.state.append_log_entry(parsed_data)
            timeout = time.time() + (self.server.consensus_timeout / 1000.0)
            while raft.state.commit_index < index and timeout > time.time():
                time.sleep(0.01)

            if raft.state.commit_index >= index:
                self._send_headers_and_response(201, json.dumps({'index': index}))
            else:
                self._send_headers_and_response(500, '')

    def do_PATCH(self):
        """ PATCH an existing log entry to mark it as applied. """
        raft = self.server.raft
        # If there isn't a leader
        if not raft.get_leader():
            self._send_headers_and_response(503, '')

        # Validate request
        elif self.headers['Content-Type'] == 'application/json':
            # Read and parse request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = json.loads(post_data)

            # If not the next index to be applied
            if parsed_data['index'] != raft.state.last_applied - 1:
                self._send_headers_and_response(409, '')
            else:
                # Update the last applied
                raft.logger.debug("[%-9s] Command applied: %s" % (raft.state.__class__.__name__, post_data))
                raft.apply_entry(raft.state)
                self._send_headers_and_response(204, '')
