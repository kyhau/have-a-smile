#!/usr/bin/env python3
import json
import os
from aws_cdk.core import App
from cdk_deploy_stack import SmileStack


env_file = os.environ.get("ENV_FILE", "env_dev.json")
with open(env_file) as json_file:
    stage_env = json.load(json_file)


app = App()

SmileStack(app, "cdk-smile")

app.synth()
