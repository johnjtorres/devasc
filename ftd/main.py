"""
A couple basic FDM API calls.

  - Logging in to FDM
  - Get hostname
  - Get SRU Version
"""

import json
import os

import requests
from crayons import green, yellow
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def fdm_login(ipaddr, username, password, version):
    """Log in to FDM and get an access token."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer",
    }
    payload = {"grant_type": "password", "username": username, "password": password}

    request = requests.post(
        "https://{}:{}/api/fdm/v{}/fdm/token".format(ipaddr, FDM_PORT, version),
        json=payload,
        verify=False,
        headers=headers,
        timeout=10,
    )
    if request.status_code == 400:
        raise Exception("Error logging in: {}".format(request.content))
    try:
        access_token = request.json()["access_token"]
        print(green("Token = " + access_token))
        return access_token
    except Exception:
        raise


def fdm_get_hostname(ipaddr, token, version):
    """Get the FDM hostname."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(token),
    }
    try:
        request = requests.get(
            "https://{}:{}/api/fdm/v{}/devicesettings/default/devicehostnames".format(
                ipaddr, FDM_PORT, version
            ),
            verify=False,
            headers=headers,
            timeout=10,
        )
        return request.json()
    except Exception:
        raise


def get_ftd_sruversion(ipaddr, token, version):
    """Get the SRU Version on FTD."""
    url = f"https://{ipaddr}/api/fdm/v{version}/operational/systeminfo/default"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(url, headers=headers, verify=False, timeout=10)
    return response.json()["sruVersion"]


if __name__ == "__main__":
    FDM_USER = os.getenv("FTD_USERNAME")
    FDM_PASSWORD = os.getenv("FTD_PASSWORD")
    FDM_IP_ADDR = "ftdsandbox"
    FDM_PORT = "443"
    FDM_VERSION = "6"

    token = fdm_login(FDM_IP_ADDR, FDM_USER, FDM_PASSWORD, FDM_VERSION)

    print(yellow("BINGO ! You got a token ! :", bold=True))

    hostname = fdm_get_hostname(FDM_IP_ADDR, token, FDM_VERSION)
    print("JSON HOSTNAME IS =")
    print(json.dumps(hostname, indent=4, sort_keys=True))
    print(green("  ===>  ALL GOOD !", bold=True))
    sruVersion = get_ftd_sruversion(FDM_IP_ADDR, token, FDM_VERSION)
    print("JSON SRU Version IS =")
    print(json.dumps(sruVersion, indent=4))
