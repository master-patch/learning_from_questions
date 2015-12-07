#!/bin/sh
docker build -t questionbot .
docker run -ti questionbot sh ./run_everything.sh -v tmp:/tmp
