import socket
import sys
import os
import json
from datetime import datetime

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import encryption_script

# from CN_PROJECT import encryption_script


class BackendClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """Establish a connection to the backend server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_request(self, request, encryption_algorithm):
        """Send a request to the backend server and receive a response."""
        if not self.socket:
            raise Exception("Socket is not connected. Call connect() first.")
        if encryption_algorithm == "AES":
            cipher = encryption_script.AesEncryption()
            start_time = datetime.now()
            encrypted_request = cipher.encrypt(request)
            end_time = datetime.now()
            encrypted_time = end_time - start_time
            data = {
                "ciphertext": encrypted_request.hex(),  # Convert bytes to hex for transmission
                "iv": cipher.iv.hex(),  # Send IV for decryption
                "algorithm": "AES",
                "time_for_encryption": encrypted_time.total_seconds(),  # Send the time taken for encryption
            }
            self.socket.sendall(json.dumps(data).encode())
        elif encryption_algorithm == "Caesar":
            cipher = encryption_script.CeasarCipher(5)
            start_time = datetime.now()
            encrypted_request = cipher.encrypt(request)
            end_time = datetime.now()
            encrypted_time = end_time - start_time
            data = {
                "ciphertext": encrypted_request,
                "algorithm": "Caesar",
                "time_for_encryption": encrypted_time.total_seconds()  # Send the time taken for encryption
            }
            self.socket.sendall(json.dumps(data).encode())
        elif encryption_algorithm == "DES3":
            cipher = encryption_script.Des3Encryption(b'12345678abcdefgh')  # Pre-shared key
            start_time = datetime.now()
            encrypted_request = cipher.encrypt(request)
            end_time = datetime.now()
            encrypted_time = end_time - start_time
            data = {
                "ciphertext": encrypted_request.hex(),  # Convert bytes to hex for transmission
                "algorithm": "DES3",
                "time_for_encryption": encrypted_time.total_seconds(),  # Send the time taken for encryption
            }
            self.socket.sendall(json.dumps(data).encode())

    def close(self):
        """Close the connection to the backend server."""
        if self.socket:
            self.socket.close()
            self.socket = None
