#!/usr/bin/env python3
import json
import os
from aws_cdk import App, Environment
from cdk_smile.lambda_smile import SmileStack


env_file = os.environ.get("ENV_FILE", "env_dev.json")
with open(env_file) as json_file:
    stage_env = json.load(json_file)


app = App()

SmileStack(app, "cdk-smile", env=Environment(**stage_env))

app.synth()
