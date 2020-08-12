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
pip install -r requirements.txt

cdk ls

cdk synth

./install_lambda_dependencies.sh
cdk deploy

./test_lambda.sh

rm -rf package
```
