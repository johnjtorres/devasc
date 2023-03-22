"""Listing rooms using requests."""

import json
import os

import requests


def webex_request(method, token, uri, json=None, version=1, timeout=10, **kwargs):
    """Perform API requests to WebEx."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://webexapis.com/v{version}{uri}"
    response = requests.request(
        method, url, json=json, headers=headers, timeout=timeout, **kwargs
    )
    response.raise_for_status()
    return response.json()


def list_rooms(token, sortBy=None, max=None):
    """List WebEx rooms."""
    params = {"sortBy": sortBy, "max": max}
    json_response = webex_request("GET", token, "/rooms", params=params)
    print(json.dumps(json_response, indent=2, sort_keys=True))


def send_message(token, roomId, message, markdown=False):
    body = {"roomId": roomId, f"{'markdown' if markdown else 'text'}": message}
    json_response = webex_request("POST", token, "/messages", json=body)
    print(json.dumps(json_response, indent=2, sort_keys=True))


if __name__ == "__main__":
    token = os.getenv("WEBEX_TOKEN")

    print("Listing all rooms")
    list_rooms(token)

    print("\n", "=" * 100, "\n", sep="")

    print("Show room that last had any activity")
    list_rooms(token, sortBy="lastactivity", max=1)

    print("\n", "=" * 100, "\n", sep="")

    print("Sending a message!")
    roomId = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOWYzNmY5MjAtYzgxMi0xMWVkLWEwMjktOGRhZjZlZWY0OTI5"
    message = "Hello, from Python!"
    # send_message(token, roomId, message)

    print("\n", "=" * 100, "\n", sep="")

    print("Sending a markdown message!")
    message = "**Warning!!!** _Warning!!!_ [Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)"
    send_message(token, roomId, message, markdown=True)
