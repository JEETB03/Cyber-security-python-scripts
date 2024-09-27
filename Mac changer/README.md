
# MAC Address Changer

This Python script allows you to change the MAC address of a specified network interface. It's useful for network troubleshooting, improving anonymity, or bypassing MAC address filters.

## Features

- Change the MAC address of any network interface on Linux-based systems.
- Simple command-line interface.
- Automatically brings the interface down, changes the MAC, and brings it back up.

## Requirements

- Python 3.x
- A Linux-based operating system (the script uses the `ifconfig` command, which is available on Linux)
- Administrative privileges (sudo/root access) to change MAC addresses

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/mac-address-changer.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd mac-address-changer
    ```

3. **Make the script executable (optional)**:
    ```bash
    chmod +x mac_changer.py
    ```

## Usage

Run the script with the required options:

```bash
sudo python mac_changer.py -i <interface> -m <new MAC address>
```

### Example:

To change the MAC address of the `eth0` interface to `00:11:22:33:44:55`, use:

```bash
sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

### Command-Line Options:

- `-i`, `--interface`: Specifies the network interface whose MAC address you want to change.
- `-m`, `--mac`: Specifies the new MAC address.

Use `--help` for more information:

```bash
python mac_changer.py --help
```

## How it Works

1. The script first brings the specified network interface down.
2. It then uses the `ifconfig` command to set a new MAC address.
3. Finally, the network interface is brought back up.

### Code Overview:

- **get_arguments()**: Parses the command-line arguments (interface and new MAC address).
- **change_MAC(interface, new_MAC)**: Changes the MAC address for the specified network interface.

## Important Notes

- **Root Access**: Changing a MAC address requires administrative (root) privileges. Ensure you run the script with `sudo` or as root.
- **Linux Only**: This script works on Linux systems since it uses the `ifconfig` command, which is not available on Windows.

## Troubleshooting

- **Command Not Found**: If `ifconfig` is not installed on your system, install it using:
  ```bash
  sudo apt install net-tools
  ```

- **Permission Denied**: Ensure you are running the script with `sudo` or root privileges.


## Contributions

Feel free to contribute to this project by submitting issues or pull requests. Any improvements or suggestions are welcome!

---



