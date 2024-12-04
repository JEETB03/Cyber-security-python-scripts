

# Directory Discovery Script

This repository contains a Python script for discovering directories on a target website through brute-forcing. The script reads a list of potential directory names from a file and checks whether each directory exists on the specified target URL.

⚠️ **Disclaimer:** This tool is intended for educational and ethical use only. Unauthorized use of this script on systems without permission is illegal.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup and Usage](#setup-and-usage)
5. [How It Works](#how-it-works)
6. [Security and Limitations](#security-and-limitations)
7. [Disclaimer](#disclaimer)

---

## Introduction

The **Directory Discovery Script** automates the process of testing whether specific directories exist on a target website. This can be useful in penetration testing for identifying hidden admin panels, configuration directories, or other sensitive locations.

---

## Features

- **Directory Brute-Forcing:** Uses a user-specified file containing potential directory names to test against a target URL.
- **HTTP GET Requests:** Sends requests to check the existence of directories.
- **Error Handling:** Handles connection errors gracefully.
- **Flexible Input:** Supports custom target URLs and directory wordlists.

---

## Requirements

- **Python:** Python 3.x
- **Python Libraries:**
  - `requests`: For sending HTTP requests.

Install the required library with:
```bash
pip install requests
```

---

## Setup and Usage

### 1. Clone the Repository
Clone the repository and navigate to the project directory:


### 2. Prepare the Directory Wordlist
Create or download a text file containing a list of potential directories (one directory per line). For example:
```
admin
login
config
uploads
```

### 3. Run the Script
Execute the script by running:
```bash
python3 directory_discovery.py
```

Provide the required inputs when prompted:
- **Target URL:** The base URL of the website (e.g., `example.com`).
- **File Name:** The name of the file containing the directory names (e.g., `directories.txt`).

### Example Input
```
[*] Enter Target URL: example.com
[*] Enter Name Of The File Containing Directories: directories.txt
```

### Example Output
```
[*] Discovered Directory At This Path: http://example.com/admin
[*] Discovered Directory At This Path: http://example.com/login
```

---

## How It Works

1. **User Input:**
   - The script prompts the user for the target URL and the file containing directory names.

2. **File Processing:**
   - Reads directory names from the specified file, stripping any whitespace.

3. **HTTP Requests:**
   - For each directory, sends an HTTP `GET` request to the constructed URL (`http://<target_url>/<directory>`).

4. **Response Handling:**
   - If a response is received (i.e., the directory exists), the script prints the discovered directory path.

---

## Security and Limitations

1. **Ethical Use Only:** Use this tool only on systems you own or have explicit permission to test.
2. **Rate Limiting and Detection:** The target server may block or throttle requests if too many are sent in a short period.
3. **HTTPS URLs:** The script currently assumes `http://` as the default protocol. For `https://`, modify the URL construction in the script.
4. **Large Wordlists:** For large directory wordlists, the script may take significant time to complete.

---

## Disclaimer

This script is intended for educational and ethical purposes only. The author is not responsible for any misuse or illegal activities conducted with this tool. Always ensure you have proper authorization before testing any system.

---

Happy Testing! 🎉  
Made with ❤️ by [JEET🫰🏻](https://github.com/JEETB03) 