from __future__ import print_function

import urllib2
from BeautifulSoup import BeautifulSoup


# Ref: https://github.com/leandrotoledo/gae-devops-reaction-telegram-bot/blob/master/devops_reactions.py
class DevOpsReactions():
    URL = 'http://devopsreactions.tumblr.com/%s'

    @classmethod
    def _getRSS(cls):
        url = cls.URL % 'rss'
        data = urllib2.urlopen(url).read()
        return [i.find('guid').text for i in BeautifulSoup(data).findAll('item')]

    @classmethod
    def _getPost(cls, url):
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)
        try:
            title = soup.find('div', attrs={'class': 'post_title'}).text.encode('utf-8')
            image_url = soup.find('div', attrs={'class': 'item text'}).p.img['src']
        except TypeError:
            title = ''
            image_url = soup.find('div', attrs={'class': 'item text'}).img['src']
        return {'title': title, 'image_url': image_url}

    @classmethod
    def latest(cls):
        return cls._getPost(url=cls._getRSS()[0])

    @classmethod
    def random(cls):
        return cls._getPost(url=cls.URL%'random')


if __name__ == "__main__":
    print(DevOpsReactions.random())
    print(DevOpsReactions.latest())