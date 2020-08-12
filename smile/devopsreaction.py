"""
Retrieve random/latest DevOps Reactions image
"""
import logging
import urllib3
from bs4 import BeautifulSoup

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("urllib3.connectionpool").setLevel(logging.CRITICAL)


def random_dev_ops_reactions(latest=False):
    URL = "http://devopsreactions.tumblr.com/%s"

    http = urllib3.PoolManager()

    def get_latest(http):
        url = URL % "rss"
        data = http.request("GET", url).data
        return [i.find("guid").text for i in BeautifulSoup(data, "html.parser").find_all("item")][0]

    url = get_latest(http) if latest is True else URL % "random"

    html = http.request("GET", url).data
    soup = BeautifulSoup(html, "html.parser")

    try:
        title = soup.find("div", attrs={"class": "post_title"}).text
        image_url = soup.find("div", attrs={"class": "item text"}).p.img["src"]

    except TypeError:
        title = ""
        image_url = soup.find("div", attrs={"class": "item text"}).img["src"]

    return {"title": title, "image_url": image_url}


if __name__ == "__main__":
    print(random_dev_ops_reactions(latest=False))
    print(random_dev_ops_reactions(latest=True))
