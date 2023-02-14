#! /usr/bin/env python3

"""
Use the BeautifulSoup and requests Python packages to print out a list of all 
the article titles on the New York Times homepage.

https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.nytimes.com/"
    resp = requests.get(url)
    bs = BeautifulSoup(resp.text, "html.parser")
    article_titles = set(
        h3.text for h3 in bs.find_all("h3", "indicate-hover", string=True)
    )
    print(*article_titles, sep="\n")


if __name__ == "__main__":
    main()
