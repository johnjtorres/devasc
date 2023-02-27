#!/usr/bin/env python

"""
Adds a new device to DNA Center.
"""

import env_lab
import requests
from dnac_token import get_auth_token

requests.packages.urllib3.disable_warnings()


def add_dnac_device(host: str, token: str, device: dict):
    url = f"https://{host}/dna/intent/api/v1/network-device"
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=device, verify=False)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    host = env_lab.dnac["host"]
    token = get_auth_token(**env_lab.dnac)
    device = {
        "cliTransport": "ssh",
        "enablePassword": "Cisco123!",
        "ipAddress": ["10.0.0.1"],
        "password": "Cisco123!",
        "snmpAuthPassphrase": "Cisco123!",
        "snmpAuthProtocol": "SHA",
        "snmpMode": "AuthPriv",
        "snmpPrivPassphrase": "string",
        "snmpPrivProtocol": "AES128",
        "snmpROCommunity": "cisco",
        "snmpRWCommunity": "cisco",
        "snmpRetry": "5",
        "snmpTimeout": "10",
        "snmpUserName": "devnet",
        "snmpVersion": "v3",
        "userName": "devnet",
    }
    print(add_dnac_device(host, token, device))
