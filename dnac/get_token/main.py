#!/usr/bin/env python
from pprint import pprint

import env_lab
import requests

requests.packages.urllib3.disable_warnings()


def get_token():
    url = env_lab.DNA_CENTER["URL"]
    url += "dna/system/api/v1/auth/token"
    username = env_lab.DNA_CENTER["Username"]
    password = env_lab.DNA_CENTER["Password"]
    response = requests.post(url, auth=(username, password), verify=False)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    token = get_token()
    pprint(token)
