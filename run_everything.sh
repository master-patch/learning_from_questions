#!/bin/sh
./run_cache.sh &
./run_client.sh &
./run_learner.sh
