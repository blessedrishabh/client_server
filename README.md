# Client-Server Communication Project

This project demonstrates a simple client-server communication system using Python. The client and server applications are built with a graphical user interface (GUI) using the `customtkinter` library. The server listens for incoming connections and processes requests from the client, while the client sends messages to the server and displays responses.

---

## Features

1. **Client-Side GUI**:
   - A user-friendly interface for sending messages to the server.
   - Displays a text entry field and a "Send" button for user interaction.

2. **Server-Side GUI**:
   - A graphical interface for monitoring incoming messages from the client.
   - Displays received messages in a scrollable text box.

3. **Backend Communication**:
   - The client communicates with the server using sockets.
   - The server processes client requests and sends responses back.

4. **Threading**:
   - The server handles multiple client connections concurrently using threads.
   - The GUI remains responsive during communication.

---

## Methodologies Used

### 1. **Socket Programming**
   - The project uses Python's `socket` module to establish communication between the client and server.
   - The server listens on a specified port for incoming connections, while the client connects to the server using the same port.

### 2. **CustomTkinter for GUI**
   - The `customtkinter` library is used to create modern and customizable GUIs for both the client and server applications.
   - The client GUI includes:
     - A text entry field for typing messages.
     - A "Send" button to send messages to the server.
   - The server GUI includes:
     - A scrollable text box to display received messages.

### 3. **Threading**
   - The server uses Python's `threading` module to handle multiple client connections simultaneously.
   - Each client connection is processed in a separate thread to ensure the server remains responsive.

### 4. **Message Handling**
   - The client sends messages to the server using the `sendall` method of the socket.
   - The server receives messages, processes them, and sends responses back to the client.
   - The server GUI updates dynamically to display received messages.

### 5. **Error Handling**
   - The client ensures that the socket is connected before sending messages.
   - The server gracefully handles client disconnections and ensures that resources are released.

---

## File Structure
CN_PROJECT/ │ ├── client/ │ ├── user_interface_client.py # Client-side GUI implementation │ ├── backend_client.py # Client-side backend logic │ ├── server/ │ ├── user_interface_server.py # Server-side GUI implementation │ ├── backend_server.py # Server-side backend logic │ └── README.md # Project


---

## How It Works

### 1. **Server-Side Workflow**
   - The server starts and listens for incoming connections on a specified port.
   - When a client connects, the server spawns a new thread to handle the client.
   - The server receives messages from the client, processes them, and sends responses back.
   - The server GUI dynamically updates to display received messages.

### 2. **Client-Side Workflow**
   - The client connects to the server using the specified host and port.
   - The user types a message in the text entry field and clicks the "Send" button.
   - The client sends the message to the server and waits for a response.
   - The client GUI remains responsive during communication.

---

# Encrypted Client-Server Communication Project

This project demonstrates a secure client-server communication system using Python. The system implements multiple encryption algorithms (AES, DES3, and Caesar cipher) and measures encryption/decryption performance. The applications feature graphical user interfaces built with the `customtkinter` library.

## Features

1. **Encryption Support**:
   - AES (Advanced Encryption Standard)
   - Triple DES (DES3)
   - Caesar Cipher
   - Performance measurements for encryption/decryption operations

2. **Client-Side GUI**:
   - Text entry field for message input
   - Encryption algorithm selection dropdown
   - Send button for encrypted message transmission
   - Modern and user-friendly interface

3. **Server-Side GUI**:
   - Real-time display of received encrypted messages
   - Automatic decryption and display of plaintext
   - Performance metrics display (encryption/decryption times)
   - Scrollable message history

4. **Security Features**:
   - Secure message encryption using industry-standard algorithms
   - IV (Initialization Vector) generation for AES
   - Pre-shared keys for symmetric encryption
   - Secure message transmission using JSON serialization

## Technical Implementation

### 1. **Encryption Algorithms**
```python
- AES: CBC mode with 128-bit key and random IV
- DES3: ECB mode with 16/24-byte key
- Caesar: Classic substitution cipher with configurable shift
```

### 2. **Performance Measurement**
- Encryption time measurement on client side
- Decryption time measurement on server side
- Total processing time calculation
- Results displayed in nanoseconds

### 3. **Data Transmission**
- JSON-formatted encrypted messages
- Hexadecimal encoding for binary data
- Metadata inclusion (algorithm type, IV, timing data)

## Project Structure

```
CN_PROJECT/
│
├── client/
│   ├── user_interface_client.py    # Client GUI implementation
│   └── backend_client.py           # Client encryption and networking
│
├── server/
│   ├── user_interface_server.py    # Server GUI implementation
│   └── backend_server.py           # Server decryption and request handling
│
├── encryption_script.py            # Encryption algorithm implementations
└── README.md                       # Project documentation
```

## Requirements

- Python 3.8 or higher
- Required packages:
  ```bash
  pip install customtkinter
  pip install pycryptodome
  ```

## How to Run

1. **Start the Server**:
   ```bash
   cd server
   python user_interface_server.py
   ```

2. **Start the Client**:
   ```bash
   cd client
   python user_interface_client.py
   ```

## Usage Instructions

1. Launch the server application
2. Start the client application
3. In the client window:
   - Type your message in the text field
   - Select an encryption algorithm (AES, DES3, or Caesar)
   - Click "Send" to transmit the encrypted message
4. The server window will display:
   - The received encrypted message
   - The decrypted plaintext
   - Performance metrics for the encryption/decryption process

## Security Considerations

- Keys are pre-shared between client and server
- AES and DES3 use secure key sizes
- IV is randomly generated for each AES encryption
- Caesar cipher is included for educational purposes only

## Performance Analysis

The system measures and displays:
- Encryption time on the client side
- Decryption time on the server side
- Total processing time for the complete operation
- All timing measurements are in nanoseconds for precision

## Future Improvements

- Implementation of asymmetric encryption
- Key exchange protocols
- Support for file encryption
- Enhanced security features
- Additional encryption algorithms
- Performance optimization

## Author

Created as part of a Computer Networks course project, demonstrating practical implementation of:
- Network programming
- Cryptography
- GUI development
- Performance measurement
- Client-server architecture

---

**Note**: This project is for educational purposes and demonstrates basic principles of encrypted communication. For production use, additional security measures would be necessary.