"""
Dilbert
"""
from __future__ import print_function
import random
import urllib
import re


def random_dilbert(logger):
    """
    Retrieve url of a random dilbert
    """
    logger.debug('Running random_dilbert ...')

    year = random.choice(['2014', '2015', '2016'])
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))

    try:
        url_to_dilbert_page = 'http://www.dilbert.com/%s-%s-%s/' % (year, month, day)
        page_contents = urllib.urlopen(url_to_dilbert_page).read()
        image_url = re.search('<meta name="twitter:image" content="(.*)">', page_contents).group(1) + '.png'
        return image_url

    except Exception as e:
        logger.error(e)
    return None


if __name__ == "__main__":
    # debug-only
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    print(random_dilbert(logger))
