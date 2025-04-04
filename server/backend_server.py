import socket
import threading
import sys
import os
import json

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import encryption_script

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
                # Receive data from the client
                data = client_socket.recv(4096).decode()
                if not data:
                    break
                
                # Deserialize the JSON data
                data = json.loads(data)
                algorithm = data["algorithm"]

                if algorithm == "AES":
                    iv = bytes.fromhex(data["iv"])  # Convert IV from hex to bytes
                    ciphertext = bytes.fromhex(data["ciphertext"])
                    aes_cipher = encryption_script.AesEncryption()
                    aes_cipher.iv = iv  # Set the IV for decryption
                    plaintext = aes_cipher.decrypt(ciphertext)
                elif algorithm == "Caesar":
                    shift = 5  # Pre-shared shift value
                    caesar_cipher = encryption_script.CeasarCipher(shift)
                    ciphertext = data["ciphertext"]
                    plaintext = caesar_cipher.decrypt(ciphertext)
                elif algorithm == "DES3":
                    key = b'12345678abcdefgh'  # Pre-shared key
                    des3_cipher = encryption_script.Des3Encryption(key)
                    ciphertext = bytes.fromhex(data["ciphertext"])
                    plaintext = des3_cipher.decrypt(ciphertext)
                else:
                    plaintext = "Unknown encryption algorithm"

                # Display the decrypted message in the server GUI
                if self.ui:
                    self.ui.display_message(f"Decrypted message: {plaintext}")
        finally:
            client_socket.close()
    def process_request(self, request):
        """Process the request from the client."""
        # Placeholder for request processing logic
        response = f"Processed request: {request}"
        return response.encode()
