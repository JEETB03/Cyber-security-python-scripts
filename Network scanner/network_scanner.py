#! /usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    """
    Parses and returns the command-line arguments for the script.
    
    Returns:
        options (argparse.Namespace): The parsed command-line arguments containing the target IP/IP range.
    """
    parser = argparse.ArgumentParser(description="Network scanner to detect IP and MAC addresses on a local network.")
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP or IP range to scan.")
    options = parser.parse_args()
    return options


def scan(ip):
    """
    Scans the network for devices using ARP requests and returns a list of IP and MAC addresses.

    Args:
        ip (str): The target IP or IP range to scan.
    
    Returns:
        clients_list (list): A list of dictionaries containing IP and MAC addresses of devices found on the network.
    """
    # Create an ARP request for the specified IP range
    arp_request = scapy.ARP(pdst=ip)
    
    # Create an Ethernet frame with the broadcast MAC address (ff:ff:ff:ff:ff:ff)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combine the ARP request and Ethernet frame to create the final packet
    arp_request_broadcast = broadcast/arp_request
    
    # Send the packet and capture responses (timeout is set to 1 second)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # List to store details of detected clients
    clients_list = []

    # Extract and store the IP and MAC address from each response
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_result(results_list):
    """
    Prints the scanned IP and MAC addresses in a structured format.

    Args:
        results_list (list): List of dictionaries containing IP and MAC addresses of devices found on the network.
    """
    print("IP\t\t\tMAC Address\n-------------------------------------------")

    # Loop through the results and print each client's IP and MAC address
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Get command-line arguments
options = get_arguments()

# Perform the network scan
scan_result = scan(options.target)

# Display the results
print_result(scan_result)
