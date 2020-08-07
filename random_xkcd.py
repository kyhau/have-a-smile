"""
Retrieve random/latest xkcd image
"""
import logging
import xkcd_wrapper

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('urllib3.connectionpool').setLevel(logging.CRITICAL)


def random_xkcd(latest=False):
    """Retrieve url of a random or the latest xkcd"""
    logging.debug('Running random xkcd...')

    try:
        client = xkcd_wrapper.Client()
        comic = client.get_latest() if latest is True else client.get_random()

        return f'{comic.title}:\n{comic.description}\n{comic.image}'
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    print(random_xkcd(latest=True))
    print(random_xkcd(latest=False))
