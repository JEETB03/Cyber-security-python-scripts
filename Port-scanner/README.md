# Port Scanner

## Description
This script performs a basic port scan on specified targets. It uses the Python `socket` library to attempt connections to a range of ports and prints out the open ports. The `termcolor` library is used to colorize terminal output.

## Features
- Scans specified number of ports on one or multiple targets
- Identifies and prints open ports
- Uses haptic feedback for multiple targets
- Simple command-line interface

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/JEETB03/Cyber-security-python-scripts/Port-scanner.git
    ```
2. Navigate to the project directory:
    ```sh
    cd port-scanner
    ```
3. Install the required dependencies:
    ```sh
    pip install termcolor
    ```

## Usage
1. Run the script:
    ```sh
    python scanner.py
    ```
2. Enter the targets you wish to scan (comma-separated if multiple):
    ```
    [*] Enter Targets To Scan (split them by ,): 192.168.1.1, 192.168.1.2
    ```
3. Enter the number of ports you want to scan:
    ```
    [*] Enter How Many Ports You Want To Scan: 100
    ```
4. The script will scan the specified ports and print out the open ports.

## Example Output
```sh
Enter Targets To Scan (split them by ,): 192.168.1.1 
[] Enter How Many Ports You Want To Scan: 100
 Starting Scan For 192.168.1.1 
 [+] Port Opened 22 
 [+] Port Opened 80
```

## Acknowledgements - This script uses the `termcolor` library for colored terminal output.
