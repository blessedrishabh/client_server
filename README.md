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

## Requirements

- Python 3.8 or higher
- `customtkinter` library

To install `customtkinter`, run:
```bash
pip install customtkinter

How to Run
1. Start the Server
Navigate to the server directory and run:
python user_interface_client.py

2. Start the Client
Navigate to the client directory and run:
python user_interface_client.py


THis is
