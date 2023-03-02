#!/usr/bin/env python

"""
Deletes a device from DNA Center.
"""

from typing import Any

import env_lab
import requests
import urllib3
from dnac_token import get_auth_token

urllib3.disable_warnings()


def delete_device(hostname: str, id_: str) -> Any:
    """Delete a device from DNA Center"""
    url = f"https://{hostname}/dna/intent/api/v1/network-device/{id_}"
    response = requests.delete(url, verify=False, timeout=60)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    HOST = env_lab.dnac["host"]
    DEVICE_ID = "6b741b27-f7e7-4470-b6fc-d5168cc59502"
    token = get_auth_token(**env_lab.dnac)
    print(delete_device(HOST, DEVICE_ID))
