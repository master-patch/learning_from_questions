#!/bin/sh
docker build -t questionbot .
docker run -i -t questionbot sh ./run_test.sh
