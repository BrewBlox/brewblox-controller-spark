#!/usr/bin/env bash
# Automatically executed by CI
set -e
pushd "$(dirname "$0")/.." > /dev/null

rm -rf dist docker/dist docker/firmware-bin

poetry install
poetry build --format sdist
poetry export --without-hashes -f requirements.txt -o docker/requirements.txt

cp -rf dist/ docker/
cp -rf firmware-bin/ docker/
