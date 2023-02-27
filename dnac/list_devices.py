#!/usr/bin/env python

"""
Prints a table of network devices from the DNAC always-on sandbox.
"""

from pprint import pprint

import env_lab
import requests
from dnac_token import get_auth_token
from tabulate import tabulate

requests.packages.urllib3.disable_warnings()


def list_dnac_devices(host: str, token: str):
    url = f"https://{host}/dna/intent/api/v1/network-device"
    headers = {"X-Auth-Token": token, "Accept": "application/json"}
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()["response"]


if __name__ == "__main__":
    token = get_auth_token(**env_lab.dnac)
    devices = list_dnac_devices(env_lab.dnac["host"], token)
    columns = ("hostname", "family", "type", "managementIpAddress", "id")
    table = [{c: d[c] for c in columns} for d in devices]
    print(tabulate(table, headers="keys"))
