#!/usr/bin/env python

from pprint import pprint

import requests
from dnac_token import get_auth_token

requests.packages.urllib3.disable_warnings()


def list_dnac_devices(host: str, token: str):
    url = f"https://{host}/dna/intent/api/v1/network-device"
    headers = {"X-Auth-Token": token, "Accept": "application/json"}
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    dnac = {
        "host": "sandboxdnac.cisco.com",
        "username": "devnetuser",
        "password": "Cisco123!",
    }
    token = get_auth_token(**dnac)
    pprint(list_dnac_devices(dnac["host"], token))
