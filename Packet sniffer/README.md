# Packet Sniffer Using Scapy

## Overview
This project is a basic packet sniffer using Python and the Scapy library. It listens to network traffic on a specified interface and detects HTTP requests. Additionally, it attempts to extract login credentials such as usernames and passwords from the packet data (if available).

### Features:
- Sniffs HTTP traffic on a specified network interface.
- Extracts and prints the URL of any HTTP requests.
- Searches for login credentials such as usernames and passwords in the HTTP request body.

## Requirements
- Python 3.x
- Scapy library (install using `pip install scapy`)

## How to Run
1. Install the required dependencies:
    ```bash
    pip install scapy
    ```

2. Run the script with the appropriate permissions:
    ```bash
    sudo python3 packet_sniffer.py
    ```

3. Specify your network interface (default in the script is `eth0`):
    ```bash
    sniff("your_network_interface")
    ```

## How Packet Sniffing Works
Packet sniffing is the process of capturing network traffic as it flows across a network. A packet sniffer captures all data being transmitted, including the sender's IP, receiver's IP, and the packet's content. This can include HTTP requests, files, emails, and login credentials (in unsecured HTTP traffic). 

### How this Sniffer Works:
1. **Sniffing Packets:** The script uses Scapy to listen to packets on a specific interface.
2. **Identifying HTTP Requests:** It looks for HTTP request packets to capture the URL and request path.
3. **Extracting Login Information:** It inspects the raw packet data for keywords commonly associated with login credentials, such as "username" and "password."

### Important Note on HTTPS:
This packet sniffer only works for **HTTP** traffic. HTTPS traffic is encrypted, meaning the content (such as URLs or login credentials) cannot be easily accessed without decryption, which would require breaking SSL/TLS encryption.

## Legal Disclaimer
This script is for educational purposes only. Use of this tool to monitor or tamper with network traffic without permission is illegal and unethical. Make sure to only use this tool in environments where you have explicit permission (e.g., your own network or a test network).

## Example Output
```bash
[+] HTTP Request >> www.example.com/login
[+] Possible Username / Password >> user=admin&password=secret
