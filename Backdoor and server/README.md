# Remote Command Execution Framework

This repository contains two Python scripts that facilitate remote command execution between a server and a target client. These scripts implement reliable data transfer, file upload/download functionality, and command execution using sockets and JSON for structured communication.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
    - [Setup](#setup)
    - [Server Script](#server-script)
    - [Client Script](#client-script)
5. [How It Works](#how-it-works)
6. [Security Considerations](#security-considerations)
7. [Disclaimer](#disclaimer)

---

## Introduction

This framework allows for secure communication between a "server" and a "target client" using a socket-based architecture. The server sends commands to the client, which executes them and sends back results. Additionally, files can be uploaded to or downloaded from the target system.

---

## Features

- **Remote Command Execution:** Execute shell commands on the target machine and receive output.
- **File Upload:** Upload files from the server to the client system.
- **File Download:** Download files from the client system to the server.
- **Reliable Data Transfer:** Ensures data integrity using JSON encoding/decoding.
- **Persistent Connection:** The client attempts to reconnect to the server in case of a connection failure.

---

## Requirements

- **Python:** Python 3.x
- **Network Configuration:** Ensure both server and client can communicate over a network (adjust firewalls or NAT settings as necessary).

---

## Usage

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/JEETB03/Cyber-security-python-scripts/Backdoor%20and%20server.git
   cd to the repo cloned in terminal
   ```

2. Update the IP and port in both scripts:
   - Replace `'192.168.1.12'` with the actual IP address of the server.
   - Ensure the port (`5555` by default) is open and not blocked by firewalls.

---

### Server Script

The `server.py` script is responsible for:
- Listening for incoming connections.
- Sending commands and receiving output.
- Facilitating file upload/download.

#### Running the Server

1. Start the server script:
   ```bash
   python3 server.py
   ```

2. Once a client connects, you can interact with it via the shell prompt:
   ```
   * Shell~<client_ip>: 
   ```

3. Available commands:
   - `quit`: Close the connection.
   - `clear`: Clear the terminal (server-side).
   - `cd <directory>`: Change directory on the target machine.
   - `download <file_name>`: Download a file from the target.
   - `upload <file_name>`: Upload a file to the target.

---

### Client Script

The `client.py` script is executed on the target machine. It:
- Connects to the server.
- Executes received commands and sends results back.
- Handles file uploads and downloads.

#### Running the Client

1. Start the client script:
   ```bash
   python3 client.py
   ```

2. The client will attempt to connect to the server at regular intervals (20 seconds by default) until a connection is established.

---

## How It Works

1. **Connection Establishment:**
   - The server listens on a specified IP and port for incoming connections.
   - The client continuously attempts to connect to the server.

2. **Data Transmission:**
   - Commands are sent from the server to the client in JSON format.
   - Results are returned from the client to the server in the same format.

3. **File Transfer:**
   - Files are read in binary mode and sent in chunks to ensure efficient transfer.

4. **Command Execution:**
   - The client executes shell commands using `subprocess` and sends back the output.

---

## Security Considerations

- **Authorization:** These scripts do not implement authentication, so ensure they are only run in secure, private networks.
- **Encryption:** All data is sent in plaintext. Use tools like SSL/TLS to secure communication for production use.
- **Use Responsibly:** Unauthorized use of these scripts on any system other than your own is illegal.

---

## Disclaimer

This project is for **educational purposes only**. The author is not responsible for any misuse of this framework. Always ensure you have permission to execute commands on the target system.

---

Feel free to contribute or raise issues! 🎉  
Made with ❤️ by [JEET](https://github.com/JEETB03).
