#!/bin/bash
set -eo pipefail

rm -rf package
cd smile
pip install --target ../package -r requirements.txt
cp *.py ../package
cd -
