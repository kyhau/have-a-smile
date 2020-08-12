import json
import logging
from devopsreaction import random_dev_ops_reactions
from dilbert import random_dilbert
from fortune_cow import fortune_cow
from xkcd import random_xkcd

logging.getLogger().setLevel(logging.INFO)


def main(event, context):
    logging.info(f"Event: {json.dumps(event)}")

    message = None

    topic = event.get("body", {}).get("topic")
    if topic is not None:
        if topic == "devopsreaction":
            message = random_dev_ops_reactions()
        elif topic == "dilbert":
            message = random_dilbert()
        elif topic == "fortunecow":
            message = fortune_cow()
        elif topic == "xkcd":
            message = random_xkcd()

    logging.info(message)

    return {
        "body": "usage: [devopsreaction|dilbert|fortunecow|xkcd]" if message is None else message,
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
    }
