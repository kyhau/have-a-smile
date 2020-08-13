#!/bin/bash
set -eo pipefail

rm -rf package
pushd smile
pip install --target ../package -r requirements.txt
cp *.py ../package
cp bootstrap ../package
popd
