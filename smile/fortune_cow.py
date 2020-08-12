"""
Fortune and cowsay
Install: sudo apt-get install cowsay fortune
"""
import subprocess
import logging

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("urllib3.connectionpool").setLevel(logging.CRITICAL)


def fortune_cow():
    """
    Run: fortune | cowsay -f $(ls /usr/share/cowsay/cows/ | shuf -n1)
    """
    try:
        logging.debug("Running fortune_cow ...")

        ps = subprocess.Popen(("ls", "/usr/share/cowsay/cows/"), stdout=subprocess.PIPE)
        ret1 = subprocess.check_output(("/usr/bin/shuf", "-n1"), stdin=ps.stdout).strip()

        ps2 = subprocess.Popen(("/usr/games/fortune"), stdout=subprocess.PIPE)
        ret2 = subprocess.check_output(("/usr/games/cowsay", "-f", ret1), stdin=ps2.stdout)

        ret = "\n".join(["    {}".format(line) for line in ret2.decode().split("\n")])
        return ret

    except Exception as e:
        logging.error(e)

    return None


if __name__ == "__main__":
    print(fortune_cow())
