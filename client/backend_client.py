import socket

class BackendClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """Establish a connection to the backend server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_request(self, request):
        """Send a request to the backend server and receive a response."""
        if not self.socket:
            raise Exception("Socket is not connected. Call connect() first.")
        
        self.socket.sendall(request.encode())

    def close(self):
        """Close the connection to the backend server."""
        if self.socket:
            self.socket.close()
            self.socket = None
