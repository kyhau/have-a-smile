"""
xkcd
"""
import xkcd


def random_xkcd(logger):
    """
    Retrieve url of a random xkcd
    """
    logger.debug('Running random_xkcd ...')

    try:
        comic = xkcd.getRandomComic()
        return '{}:\n{}\n{}'.format(
            comic.getAsciiTitle(),
            comic.getAsciiAltText(),
            comic.getAsciiImageLink()
        )

    except Exception as e:
        logger.error(e)
    return None


if __name__ == "__main__":
    # debug-only
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    random_xkcd(logger)
