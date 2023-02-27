#!/usr/bin/env python

"""
Deletes a device from DNA Center.
"""

import env_lab
import requests
from dnac_token import get_auth_token

requests.packages.urllib3.disable_warnings()


def delete_device(host: str, id: str):
    url = f"https://{host}/dna/intent/api/v1/network-device/{id}"
    response = requests.delete(url, verify=False)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    host = env_lab.dnac["host"]
    token = get_auth_token(**env_lab.dnac)
    id = "6b741b27-f7e7-4470-b6fc-d5168cc59502"
    print(delete_device(host, id))
