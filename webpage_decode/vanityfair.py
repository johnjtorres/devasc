#! /usr/bin/env python3

"""
Using the requests and BeautifulSoup Python libraries, print to the screen the 
full text of the article on this website: 
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = (
        "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    )
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    paragraphs = soup.find_all("p", string=True)
    for paragraph in paragraphs:
        print(paragraph.text)


if __name__ == "__main__":
    main()
