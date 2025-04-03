import socket
import threading

class BackendServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.ui = None
    def set_ui(self, ui):
        self.ui = ui
    
    def start(self):
        """Start the backend server."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
    
    def accept_connections(self):
        """Accept incoming connections and handle requests."""
        while True:
            client_socket, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()
    def handle_client(self, client_socket):
        """Handle a client connection."""
        try:
            while True:
                request = client_socket.recv(4096).decode()
                if not request:
                    break
                if self.ui:
                    self.ui.display_message(f"Received request: {request}")
        finally:
            client_socket.close()
    def process_request(self, request):
        """Process the request from the client."""
        # Placeholder for request processing logic
        response = f"Processed request: {request}"
        return response.encode()
