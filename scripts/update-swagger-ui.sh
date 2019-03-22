#!/bin/bash

set -e
set -x

git clone https://github.com/swagger-api/swagger-ui

rm -rf static/apidoc

mv swagger-ui/dist static/apidoc

rm -rf swagger-ui
