

# DNS Spoofing Script

## Overview

This project demonstrates **DNS spoofing**, a technique where an attacker intercepts DNS queries and responds with false DNS records, redirecting users to a malicious server. The Python script in this repository is an educational example that shows how DNS spoofing can be performed to redirect DNS queries for `www.google.com` to any IP address provided by the user.

### What is DNS Spoofing?

DNS (Domain Name System) resolves human-readable domain names (like `www.google.com`) into machine-readable IP addresses. DNS spoofing is a type of attack where an attacker provides a forged DNS response to a victim, redirecting them to a fake website. The victim is unaware that they are not connecting to the intended server, which could lead to data theft or further exploitation.

---

### How DNS Spoofing Works

#### 1. **Normal DNS Resolution Flow**

In a typical DNS query:

1. A user types `www.google.com` into their browser.
2. The browser sends a DNS query to the network's DNS server to resolve the domain to an IP address.
3. The DNS server responds with the legitimate IP address for `www.google.com`.
4. The browser uses the IP address to connect to the real Google server.

**Diagram:**

```plaintext
+------------+       DNS Query       +------------+       DNS Response        +--------------+
|  User's    |  www.google.com?   -> | DNS Server |   www.google.com -> IP    |  Legitimate  |
|  Browser   |                       |            |                           |  Google Server|
+------------+                       +------------+                           +--------------+
        |                                                                        |
        +------------------------------------------------------------------------+
                                User Browses Google
```

---

#### 2. **DNS Spoofing Attack Flow**

In a DNS spoofing attack:

1. The user sends a DNS query for `www.google.com`.
2. The attacker intercepts this DNS request.
3. Instead of allowing the legitimate DNS response, the attacker sends a forged response with a fake IP address.
4. The user’s browser is tricked into connecting to the attacker's server instead of the legitimate server.

**Diagram:**

```plaintext
+------------+       DNS Query       +------------+      Forged DNS Response      +--------------+
|  User's    |  www.google.com?   -> |  Attacker   |  www.google.com -> Fake IP   |  Attacker's   |
|  Browser   |                       | Intercepts  |                             |  Fake Server  |
+------------+                       +------------+                             +--------------+
        |                                                                        |
        +------------------------------------------------------------------------+
                              User Browses Fake Website
```

---

## How the Script Works

This Python script performs DNS spoofing by intercepting DNS queries for `www.google.com` and responding with a forged DNS response containing a user-provided IP address. Below is an in-depth look at the script's operation.

### Script Flow

1. **Packet Interception**: The script uses `netfilterqueue` to capture DNS requests sent from a victim machine.
2. **DNS Query Detection**: The script examines each packet to determine if it's a DNS request for `www.google.com`.
3. **Forging DNS Response**: If a DNS query for `www.google.com` is detected, the script creates a forged DNS response that redirects the victim to a fake IP address provided by the user.
4. **Packet Modification**: The forged DNS response is reinjected into the network so that the victim’s browser receives the fake DNS response and redirects to the attacker's server.

**Diagram of the Script Flow:**

```plaintext
+------------+   DNS Query: www.google.com   +--------------------+   Forged DNS Response   +--------------+
|  User's    | ---------------------------> |   Python Script     | ----------------------> |  Attacker's   |
|  Browser   |                               |  (Intercepts Query) |                         |  Fake Server  |
+------------+                               +--------------------+                         +--------------+
                                                  |
                                      +-----------v------------+
                                      |  Modifies DNS Response  |
                                      |   (Redirect to Fake IP) |
                                      +-------------------------+
```

---

## Installation and Usage

### Prerequisites

- **Python 3** is required to run the script.
- You need **root access** to execute the script since it interacts with network traffic.
- Install the required Python modules using:
  ```bash
  pip install netfilterqueue scapy
  ```

### Setup

1. **Configure iptables** to forward DNS packets to the `netfilterqueue`:
   ```bash
   sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
   ```
   This command ensures that all packets in the network are passed to the script.

2. **Run the script**:
   ```bash
   sudo python3 dns_spoof.py
   ```
   When prompted, enter the IP address you want to redirect DNS queries for `www.google.com` to:
   ```bash
   Enter the IP address to redirect www.google.com to: 192.168.1.100
   ```

3. **Spoofing in action**: The script will start intercepting DNS requests and spoofing responses for `www.google.com`. Any client on the network that requests this domain will be redirected to the specified IP address.

---

### Script Details

#### **Step 1: Packet Interception**

The script captures packets using the `netfilterqueue` Python module, which hooks into Linux’s Netfilter system, enabling the interception of network traffic.

#### **Step 2: DNS Query Detection**

When the script detects a DNS query for `www.google.com`, it proceeds to spoof the DNS response. The code checks the `qname` (DNS query name) to ensure the target domain is `www.google.com`:

```python
qname = scapy_packet[scapy.DNSQR].qname.decode()
if "www.google.com" in qname:
    print("[+] Spoofing target")
```

#### **Step 3: Packet Modification**

Once the DNS query is detected, the script forges a new DNS response that contains the spoofed IP address entered by the user. The code creates a new DNS resource record (DNSRR) with the user-defined IP address:

```python
answer = scapy.DNSRR(rrname=qname, rdata=spoofed_ip)
scapy_packet[scapy.DNS].an = answer
scapy_packet[scapy.DNS].ancount = 1
```

#### **Step 4: Reinjecting the Packet**

The modified DNS response is then reinjected into the network, so that the victim receives the spoofed response:

```python
packet.set_payload(bytes(scapy_packet))
packet.accept()
```

---

### Cleanup

After you're done testing, you should restore the network's packet forwarding rules by flushing the `iptables` rule:

```bash
sudo iptables --flush
```

This will prevent further interception of DNS traffic by the script.

---

## Security and Ethical Considerations

This tool is created for **educational purposes** and **authorized penetration testing** only. DNS spoofing is a serious attack and can lead to the theft of sensitive data or other malicious outcomes. Ensure that you only use this tool in environments where you have explicit permission to test.

### Legal Disclaimer

Unauthorized use of this tool to intercept or manipulate network traffic is illegal. Use it responsibly and ensure you have proper authorization before running it on any network. Misuse of this tool can result in legal action.

---

## Conclusion

This script demonstrates how DNS spoofing can be performed to redirect a user’s traffic from legitimate websites to malicious ones. While this attack is powerful, it should only be used in ethical hacking scenarios for testing the security of a network or system.

--- 

Feel free to enhance this script for educational purposes, but always ensure you are conducting ethical hacking in environments where you have permission to test.