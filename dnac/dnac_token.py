#!/usr/bin/env python3

"""DevNet LL - Retrieve a token from DNA Center."""

import env_lab
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


def get_auth_token(host: str, username: str, password: str) -> str:
    """Return an authentication token from DNA Center."""
    url = f"https://{host}/dna/system/api/v1/auth/token"
    auth = (username, password)
    headers = {"Accept": "application/json"}
    response = requests.post(
        url, auth=auth, headers=headers, verify=False, timeout=30
    )
    response.raise_for_status()
    return response.json()["Token"]


if __name__ == "__main__":
    print(get_auth_token(**env_lab.dnac))
