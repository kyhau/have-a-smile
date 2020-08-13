# Smile

A lambda function get random message/image from
1. [DevOps Reactions](http://devopsreactions.tumblr.com/)
1. [Dilbert](https://dilbert.com)
1. fortune | cowsay
1. [xkcd](https://xkcd.com/)

- Support deployment as AWS Lambda Function with CDK.
- Can be run separatedly as a Python function.

## Steps
```bash
# Create and activate a virtual env

# Update env_dev.json

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
