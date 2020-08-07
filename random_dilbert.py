"""
Retrieve random/latest Dilbert image
"""
import logging
import re
import urllib3
from datetime import datetime, timedelta
from random import randrange

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('urllib3.connectionpool').setLevel(logging.CRITICAL)


def random_dilbert(lookup_days=400):
    """Retrieve url of a random dilbert"""
    logging.debug('Running random dilbert...')

    http = urllib3.PoolManager()

    dt = datetime.now() - timedelta(days=randrange(lookup_days))
    dt_str = dt.strftime('%Y-%m-%d')
    logging.debug(f'Random date: {dt_str}')

    try:
        url_to_dilbert_page = f'https://dilbert.com/strip/{dt_str}/'
        page_contents = http.request('GET', url_to_dilbert_page).data.decode('utf-8')
        return re.search('<meta name="twitter:image" content="(.*)">', page_contents).group(1) + '.png'

    except Exception as e:
        logging.error(e)
    return None


if __name__ == "__main__":
    print(random_dilbert())
