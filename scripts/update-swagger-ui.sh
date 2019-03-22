#!/bin/bash

git clone https://github.com/swagger-api/swagger-ui

mv swagger-ui/dist bd/static/doc

rm -rf swagger-ui
