"""
Fortune and cowsay
"""
from __future__ import print_function
import subprocess


def fortune_cow(logger):
    """
    Run: fortune | cowsay -f $(ls /usr/share/cowsay/cows/ | shuf -n1)
    """
    try:
        logger.debug('Running fortune_cow ...')

        ps = subprocess.Popen(('ls', '/usr/share/cowsay/cows/'), stdout=subprocess.PIPE)
        ret1 = subprocess.check_output(('/usr/bin/shuf', '-n1'), stdin=ps.stdout).strip()

        ps2 = subprocess.Popen(('/usr/games/fortune'), stdout=subprocess.PIPE)
        ret2 = subprocess.check_output(('/usr/games/cowsay', '-f', ret1), stdin=ps2.stdout)

        ret = '\n'.join(['    {}'.format(line) for line in ret2.split('\n')])
        return ret

    except Exception as e:
        logger.error(e)

    return None


if __name__ == '__main__':
    # debug-only
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    print(fortune_cow(logger))
