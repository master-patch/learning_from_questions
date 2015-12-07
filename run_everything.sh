#!/bin/sh
./run_cache.sh &
./run_client.sh &
./run_ir.sh &
sleep 3 &&
./run_learner.sh
