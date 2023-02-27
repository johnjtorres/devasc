#!/usr/bin/env python

"""
An example script that retrieves an authentication token from DNA Center. This
token can be used in future API requests.
"""

import requests

requests.packages.urllib3.disable_warnings()


def get_auth_token(host: str, username: str, password: str) -> str:
    """Returns an authentication token from DNA Center."""
    url = f"https://{host}/dna/system/api/v1/auth/token"
    auth = (username, password)
    headers = {"Accept": "application/json"}
    response = requests.post(url, auth=auth, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()["Token"]


if __name__ == "__main__":
    dnac = {
        "host": "sandboxdnac.cisco.com",
        "username": "devnetuser",
        "password": "Cisco123!",
    }
    print(get_auth_token(**dnac))
