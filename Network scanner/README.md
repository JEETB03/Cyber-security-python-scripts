# Network Scanner using Scapy

This Python script scans a local network to detect devices and retrieves their IP and MAC addresses using ARP requests. The script utilizes the `scapy` library for network-related operations and is run through the command line with the option to specify a target IP or IP range.

## Features

- Scans a specified IP range for devices on the network.
- Displays the IP address and MAC address of all devices that respond to the ARP request.
- Easy to use with command-line arguments.
- Timeout to avoid long wait times during scanning.

## Requirements

Before running the script, ensure that the following dependencies are installed:

- Python 3.x
- `scapy` library: You can install it using the command:
    ```bash
    pip install scapy
    ```

## Usage

1. Clone the repository or download the script.
2. Run the script with the target IP or IP range you want to scan.

Example command to scan a specific IP range:

```bash
python network_scanner.py -t 192.168.1.0/24
The -t or --target argument specifies the target IP range. The script will output the IP and MAC addresses of the devices found on the network.

Sample Output

IP              MAC Address
-------------------------------------------
192.168.1.1     aa:bb:cc:dd:ee:ff
192.168.1.2     11:22:33:44:55:66
192.168.1.3     77:88:99:aa:bb:cc

How It Works
The script creates an ARP (Address Resolution Protocol) request for the given IP range and sends it as a broadcast to all devices on the network. Devices that receive the request will respond with their MAC address, which the script collects and displays in a formatted table.