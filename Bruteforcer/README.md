# HTTP Login Bruteforce Script

This repository contains a Python script to perform brute-force attacks on HTTP login forms. It systematically tests a list of potential passwords for a given username, attempting to authenticate against a specified target URL. 

⚠️ **Disclaimer:** This script is for educational and ethical use only. Unauthorized access to systems is illegal. Use this tool only on systems you own or have explicit permission to test.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup and Usage](#setup-and-usage)
    - [Script Overview](#script-overview)
    - [Input Parameters](#input-parameters)
    - [Execution](#execution)
5. [How It Works](#how-it-works)
6. [Security and Limitations](#security-and-limitations)
7. [Disclaimer](#disclaimer)

---

## Introduction

This script attempts to brute-force HTTP login forms by trying a list of passwords against a specified username. It supports custom cookies for authentication and identifies login success by the absence of a user-defined "login failed" string in the server's response.

---

## Features

- **Customizable Parameters:** Accepts user-defined URL, username, password file, and failed login string.
- **Cookie Support:** Allows the use of cookies for authenticated requests.
- **Visual Feedback:** Displays password attempts in red and successful credentials in green.
- **Efficient Processing:** Reads and processes passwords line by line from a file.

---

## Requirements

- **Python:** Python 3.x
- **Python Libraries:**
  - `requests` (HTTP requests library)
  - `termcolor` (Colored output)

Install the required libraries using:
```bash
pip install requests termcolor
```

---

## Setup and Usage

### Script Overview

The script performs the following steps:
1. Accepts user input for target URL, username, password file, login failed string, and optional cookie value.
2. Reads passwords from the specified file line by line.
3. Sends HTTP POST or GET requests to the target URL with the username and password.
4. Checks the server's response for the login failed string to determine success or failure.

### Input Parameters

1. **URL:** The full URL of the target login page (e.g., `http://example.com/login`).
2. **Username:** The username for the account being brute-forced.
3. **Password File:** A text file containing a list of potential passwords (one per line).
4. **Login Failed String:** A string from the server's response indicating a failed login (e.g., `"Invalid credentials"`).
5. **Cookie Value (Optional):** A cookie value to include in the request for session-based authentication.

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. Run the script:
   ```bash
   python3 bruteforce.py
   ```

3. Provide the required inputs when prompted:
   ```
   [+] Enter Page URL: http://example.com/login
   [+] Enter Username For The Account To Bruteforce: admin
   [+] Enter Password File To Use: passwords.txt
   [+] Enter String That Occurs When Login Fails: Invalid login
   Enter Cookie Value(Optional): <your_cookie_value_here>
   ```

4. View the output:
   - If a password is found:
     ```
     [+] Found Username: ==> admin
     [+] Found Password: ==> password123
     ```
   - If no password is found in the file:
     ```
     [!!] Password Not In List
     ```

---

## How It Works

1. **Password Loading:**
   The script reads the password file line by line to avoid memory overload with large files.

2. **HTTP Requests:**
   - If a cookie value is provided, the script uses an HTTP `GET` request with cookies.
   - Otherwise, it sends an HTTP `POST` request with form data.

3. **Response Validation:**
   The server's response is checked for the presence of the login failed string. If it is absent, the script assumes the credentials are valid.

4. **Output:**
   - Password attempts are printed in red.
   - Successful credentials are printed in green.

---

## Security and Limitations

1. **Ethical Use Only:** Use the script only on systems you own or have explicit permission to test.
2. **Rate Limiting and Detection:** Targets may have rate-limiting or intrusion detection systems that block repeated login attempts.
3. **Encrypted Forms:** The script does not support forms protected by CAPTCHA, 2FA, or JavaScript-based encryption.
4. **Legal Implications:** Unauthorized use of this tool can result in legal consequences.

---

## Disclaimer

This script is intended for educational purposes and ethical penetration testing only. The author is not responsible for any misuse or illegal activities conducted with this tool. Always ensure you have proper authorization before testing any system.

--- 

Happy Testing! 🎉  
Made with ❤️ by [JEET🫰🏻](https://github.com/JEETB03). 