# Smile

Some simple scripts to get random message/image from
1. [DevOps Reactions](http://devopsreactions.tumblr.com/)
1. [Dilbert](https://dilbert.com)
1. fortune | cowsay
1. [xkcd](https://xkcd.com/)


- Support deployment as AWS Lambda Function with CDK v2 for DevOps Reactions, Dilbert and xkcd.
- Can be run separatedly as a Python function.

## Prerequisites
1. Install CDK v2: `npm install -g aws-cdk@next`
2. Update env_dev.json

## Build and Deploy
```bash
# Create and activate a virtual env

pip install -r requirements.txt

./build_lambda.sh

cdk ls

cdk synth

cdk deploy

./test_lambda.sh

rm -rf package/
rm -rf cdk_smile/__pycache__
rm -rf cdk.out/
```
