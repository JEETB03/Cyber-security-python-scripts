#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    """
    Parse command-line arguments for the interface and the new MAC address.

    Returns:
        options (object): Parsed arguments which include:
            - interface (str): The network interface to change the MAC address of.
            - new_MAC (str): The new MAC address to assign to the interface.
    """
    parser = optparse.OptionParser()
    
    # Add options for interface and MAC address
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC Address to assign")
    
    # Parse the options and arguments
    (options, arguments) = parser.parse_args()

    # Validate that both interface and MAC address are provided
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_MAC:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    
    return options

def change_MAC(interface, new_MAC):
    """
    Change the MAC address of the specified network interface.

    Args:
        interface (str): The network interface to modify.
        new_MAC (str): The new MAC address to set for the interface.

    This function performs the following steps:
    1. Brings the interface down.
    2. Changes the MAC address.
    3. Brings the interface back up.
    """
    print(f"[-] Changing MAC Address for {interface} to {new_MAC}")
    
    # Bring the interface down
    subprocess.call(["ifconfig", interface, "down"])
    
    # Change the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
    
    # Bring the interface back up
    subprocess.call(["ifconfig", interface, "up"])

# Get command-line arguments from the user
options = get_arguments()

# Change the MAC address using the provided options
change_MAC(options.interface, options.new_MAC)
