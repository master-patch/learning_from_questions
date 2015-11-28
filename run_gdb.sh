#!/bin/sh
./run_cache.sh &
./run_client.sh &
gdb bin/text_guided_planner
