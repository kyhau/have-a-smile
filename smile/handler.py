import json
import logging

from devopsreaction import random_dev_ops_reactions
from dilbert import random_dilbert
from xkcd import random_xkcd

logging.getLogger().setLevel(logging.INFO)


def main(event, context):
    logging.info(f"Event: {json.dumps(event)}")

    message = None

    topic = event.get("topic")
    latest = event.get("latest", False)

    if topic is not None:
        if topic == "devopsreaction":
            message = random_dev_ops_reactions(latest=latest)
        elif topic == "dilbert":
            message = random_dilbert(lookup_days=1 if latest else 400)
        elif topic == "xkcd":
            message = random_xkcd(latest=latest)

    logging.info(message)

    return {
        "body": "usage: [devopsreaction|dilbert|xkcd]" if message is None else message,
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
    }
