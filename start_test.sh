#!/bin/sh
docker build -t questionyala .
docker run -i -t questionyala sh ./run_test.sh
