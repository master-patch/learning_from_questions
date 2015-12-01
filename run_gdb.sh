#!/bin/sh
./run_cache.sh &
./run_client.sh &
./run_ir.sh &
cgdb bin/text_guided_planner -x gdb-learner
