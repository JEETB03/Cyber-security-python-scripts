import socket
import termcolor

def scan(target, ports):
    """
    Scan the specified number of ports on a given target.

    Args:
        target (str): The IP address or hostname to scan.
        ports (int): The number of ports to scan.
    """
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    """
    Scan a specific port on a given IP address.

    Args:
        ipaddress (str): The IP address to scan.
        port (int): The port number to scan.
    """
    try:
        # Create a socket object
        sock = socket.socket()
        # Attempt to connect to the IP address and port
        sock.connect((ipaddress, port))
        # If successful, print that the port is open
        print("[+] Port Opened " + str(port))
        # Close the socket connection
        sock.close()
    except:
        # If connection fails, do nothing
        pass

# Get user input for targets and number of ports
targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

# Check if multiple targets are specified
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    # Split the targets and scan each one
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    # Scan the single target
    scan(targets, ports)
